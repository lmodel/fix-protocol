#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml>=6"]
# ///
"""Write the catalogue of FIX Latest from the Orchestra file in upstream/.

FIX Latest's Orchestra file holds each element of the standard as an XML element whose
attributes are its names, numbers, codes and pedigree, and whose annotations hold FIX's
descriptive text. This script writes each element as a record of this project's schema,
keeping every attribute and leaving every annotation's text out. NOTICE says why.

It stops on an element or attribute that no table below names, so a new kind of content in
a later extension pack is read and modelled, never dropped. It also writes the extension
pack and the pinned commit into the schema's headers, so ``--check`` fails when either is
stale. Usage::

    python scripts/fix_latest_to_records.py [--check]
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "upstream" / "OrchestraFIXLatest.xml"
PINS = ROOT / "scripts" / "upstream_pins.tsv"
DATA = ROOT / "src" / "fix_protocol" / "data"
SCHEMA_DIR = ROOT / "src" / "fix_protocol" / "schema"

FIXR = "{http://fixprotocol.io/2020/orchestra/repository}"
FIXML = "{http://fixprotocol.io/2022/orchestra/appinfo/fixml}"
DCTERMS = "{http://purl.org/dc/terms/}"

# The six pedigree attributes, which every kind of element may carry.
PEDIGREE = {
    "added": ("added_in", str),
    "addedEP": ("added_in_ep", int),
    "updated": ("updated_in", str),
    "updatedEP": ("updated_in_ep", int),
    "deprecated": ("deprecated_in", str),
    "deprecatedEP": ("deprecated_in_ep", int),
}

# Each kind's own attributes: the record's key and how the value is read. "id" and "name"
# come first in every record; the rest follow in this order, then the pedigree.
ATTRIBUTES = {
    "section": {
        "name": ("name", str),
        "FIXMLFileName": ("fixml_file_name", str),
        "displayOrder": ("section_order", int),
    },
    "category": {
        "name": ("name", str),
        "FIXMLFileName": ("fixml_file_name", str),
        "section": ("in_section", "section"),
        "componentType": ("category_kind", str),
        "includeFile": ("include_file", str),
    },
    "datatype": {
        "name": ("name", str),
        "baseType": ("base_type", "datatype"),
    },
    "mappedDatatype": {
        "standard": ("mapped_standard", str),
        "base": ("mapped_base", str),
        "builtin": ("mapped_builtin", "boolean"),
        "minInclusive": ("mapped_min_inclusive", str),
        "pattern": ("mapped_pattern", str),
    },
    "codeSet": {
        "id": ("id", "code_set"),
        "name": ("name", str),
        "type": ("code_set_datatype", "datatype"),
    },
    "code": {
        "id": ("id", "code"),
        "name": ("name", str),
        "value": ("code_value", str),
        "sort": ("sort_order", int),
        "group": ("code_group", str),
    },
    "field": {
        "id": ("id", "field"),
        "name": ("name", str),
        "abbrName": ("abbr_name", str),
        "type": (None, "field_type"),
        "unionDataType": ("union_datatype", "datatype"),
        "lengthId": ("length_field", "field"),
        "discriminatorId": ("discriminator_field", "field"),
        "baseCategory": ("base_category", "category"),
        "baseCategoryAbbrName": ("base_category_abbr_name", str),
    },
    "component": {
        "id": ("id", "component"),
        "name": ("name", str),
        "abbrName": ("abbr_name", str),
        "category": ("in_category", "category"),
    },
    "group": {
        "id": ("id", "group"),
        "name": ("name", str),
        "abbrName": ("abbr_name", str),
        "category": ("in_category", "category"),
    },
    "message": {
        "id": ("id", "message"),
        "name": ("name", str),
        "abbrName": ("abbr_name", str),
        "msgType": ("msg_type", str),
        "category": ("in_category", "category"),
    },
    "numInGroup": {"id": ("count_field", "field")},
    "fieldRef": {"id": ("member_field", "field"), "presence": ("presence", str)},
    "componentRef": {
        "id": ("member_component", "component"),
        "presence": ("presence", str),
    },
    "groupRef": {"id": ("member_group", "group"), "presence": ("presence", str)},
}

# The kinds whose identifier is FIX's name rather than a number.
NAMED = {"section", "category", "datatype"}

# The repository's lists: the element that holds each, its items' tag and the file and key
# each is written to.
LISTS = (
    ("sections", "section", "repository", "fix_sections"),
    ("categories", "category", "repository", "fix_categories"),
    ("datatypes", "datatype", "datatypes", "fix_datatypes"),
    ("codeSets", "codeSet", "code-sets", "fix_code_sets"),
    ("fields", "field", "fields", "fix_fields"),
    ("components", "component", "components", "fix_components"),
    ("groups", "group", "groups", "fix_groups"),
    ("messages", "message", "messages", "fix_messages"),
)

# The repository's metadata, by its Dublin Core element.
METADATA = {
    "title": "metadata_title",
    "description": "metadata_description",
    "creator": "metadata_creator",
    "publisher": "metadata_publisher",
    "rights": "metadata_rights",
    "format": "metadata_format",
    "conformsTo": "metadata_conforms_to",
    "created": "metadata_created",
    "source": "metadata_source",
}

# The children each kind may hold besides its annotation.
CHILDREN = {
    "codeSet": {"code"},
    "datatype": {"mappedDatatype"},
    "component": {"fieldRef", "componentRef", "groupRef"},
    "group": {"numInGroup", "fieldRef", "componentRef", "groupRef"},
    "message": {"structure"},
    "structure": {"fieldRef", "componentRef", "groupRef"},
}
MEMBERS = {"fieldRef", "componentRef", "groupRef"}

# The one piece of application information FIX Latest carries, and the key each of its
# attributes becomes.
APPINFO = {"notReqXML": "fixml_not_required", "inlined": "fixml_inlined"}


class Unknown(ValueError):
    """The file holds something the tables above do not name."""


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


class Converter:
    def __init__(self, root: ET.Element):
        self.root = root
        self.datatypes = {e.get("name") for e in self._list("datatypes")}
        self.code_sets = {e.get("name"): e.get("id") for e in self._list("codeSets")}

    def _list(self, name: str) -> list[ET.Element]:
        found = self.root.find(FIXR + name)
        return [] if found is None else list(found)

    def reference(self, kind: str, value: str) -> str:
        return f"fix_{kind}:{value}"

    def value(self, how, raw: str, record: dict, kind: str):
        if how is str:
            return raw
        if how is int:
            return int(raw)
        if how == "boolean":
            if raw not in ("true", "false", "1", "0"):
                raise Unknown(f"{kind} holds {raw!r} where a boolean belongs")
            return raw in ("true", "1")
        if how == "field_type":
            if raw in self.datatypes:
                record["field_datatype"] = self.reference("datatype", raw)
            elif raw in self.code_sets:
                record["field_code_set"] = self.reference(
                    "code_set", self.code_sets[raw]
                )
            else:
                raise Unknown(f"field type {raw!r} names no datatype or code set")
            return None
        return self.reference(how, raw)

    def annotation(self, element: ET.Element, kind: str) -> dict:
        """The application information an element's annotation holds. Its documentation
        is FIX's text, which the catalogue leaves out."""
        found = {}
        note = element.find(FIXR + "annotation")
        if note is None:
            return found
        for child in note:
            tag = local(child.tag)
            if tag == "documentation":
                continue
            if tag != "appinfo" or child.get("purpose") != "FIXML":
                raise Unknown(f"{kind} holds an annotation child {tag}")
            for encoding in child:
                if encoding.tag != FIXML + "FIXMLencodingType":
                    raise Unknown(f"{kind} holds appinfo {encoding.tag}")
                for name, raw in encoding.attrib.items():
                    if name not in APPINFO:
                        raise Unknown(f"{kind} holds FIXML attribute {name}")
                    found[APPINFO[name]] = self.value("boolean", raw, found, kind)
        return found

    def record(self, element: ET.Element) -> dict:
        kind = local(element.tag)
        table = ATTRIBUTES[kind]
        record = {}
        if kind in NAMED:
            record["id"] = self.reference(kind, element.get("name"))
        for name in element.attrib:
            if name not in table and name not in PEDIGREE:
                raise Unknown(f"{kind} holds attribute {name}")
        for name, (key, how) in table.items():
            raw = element.get(name)
            if raw is None:
                continue
            value = self.value(how, raw, record, kind)
            if key is not None:
                record[key] = value
        for name, (key, how) in PEDIGREE.items():
            if element.get(name) is not None:
                record[key] = how(element.get(name))
        record.update(self.annotation(element, kind))
        allowed = CHILDREN.get(kind, set()) | {"annotation"}
        for child in element:
            if local(child.tag) not in allowed:
                raise Unknown(f"{kind} holds element {local(child.tag)}")
        if kind == "datatype":
            mapped = [
                self.record(c) for c in element if local(c.tag) == "mappedDatatype"
            ]
            if mapped:
                record["mapped_datatypes"] = mapped
        if kind == "codeSet":
            record["fix_codes"] = [
                self.record(c) for c in element if local(c.tag) == "code"
            ]
        if kind == "group":
            count = element.find(FIXR + "numInGroup")
            record["num_in_group"] = self.record(count)
        if kind in ("component", "group", "message"):
            holder = element.find(FIXR + "structure") if kind == "message" else element
            members = [self.record(c) for c in holder if local(c.tag) in MEMBERS]
            if members:
                record["fix_members"] = members
        return self.ordered(record, kind)

    def ordered(self, record: dict, kind: str) -> dict:
        """The record's keys in a fixed order: identity, the kind's own, pedigree, the
        FIXML information, then the nested lists."""
        order = ["id", "name"]
        order += [key for key, _ in ATTRIBUTES[kind].values() if key]
        if kind == "field":
            order[order.index("abbr_name") + 1 : order.index("abbr_name") + 1] = [
                "field_datatype",
                "field_code_set",
            ]
        order += [key for key, _ in PEDIGREE.values()]
        order += list(APPINFO.values())
        order += ["mapped_datatypes", "fix_codes", "num_in_group", "fix_members"]
        missing = set(record) - set(order)
        if missing:
            raise Unknown(f"{kind} record has keys no order names: {missing}")
        return {key: record[key] for key in order if key in record}

    def metadata(self) -> dict:
        found = {}
        meta = self.root.find(FIXR + "metadata")
        for child in meta:
            name = local(child.tag)
            if not child.tag.startswith(DCTERMS) or name not in METADATA:
                raise Unknown(f"metadata holds {child.tag}")
            found[METADATA[name]] = (child.text or "").strip()
        return found

    def files(self) -> dict[str, dict]:
        """Each data file's content, by file stem."""
        top = {
            "repository_name": self.root.get("name"),
            "repository_version": self.root.get("version"),
        }
        names = {local(child.tag) for child in self.root}
        known = {"metadata"} | {holder for holder, _, _, _ in LISTS}
        if names - known:
            raise Unknown(f"the repository holds {sorted(names - known)}")
        files = {"repository": {**top, **self.metadata()}}
        for holder, item, stem, key in LISTS:
            elements = self._list(holder)
            for element in elements:
                if local(element.tag) != item:
                    raise Unknown(f"{holder} holds {local(element.tag)}")
            files.setdefault(stem, dict(top))[key] = [self.record(e) for e in elements]
        return files


def header(stem: str, version: str, commit: str) -> str:
    return (
        f"# FIX Latest at {version}: {stem.replace('-', ' ')}. "
        "scripts/fix_latest_to_records.py writes this\n"
        "# file from upstream/OrchestraFIXLatest.xml, so regenerate it, never edit it.\n"
        "#\n"
        "# Copyright (c) FIX Protocol Ltd. The file is copied from\n"
        f"# FIXTradingCommunity/orchestrations at {commit},\n"
        "# which is licensed under the Apache License, Version 2.0. This file restates its\n"
        "# names, numbers and codes as records and leaves its descriptive text out, as\n"
        "# NOTICE says.\n"
    )


class _Dumper(yaml.SafeDumper):
    """A dumper that indents a list under its key, as the repository's YAML style asks."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def dump(data: dict) -> str:
    return yaml.dump(
        data,
        Dumper=_Dumper,
        sort_keys=False,
        allow_unicode=True,
        width=100,
        default_flow_style=False,
    )


def pins() -> dict[str, str]:
    found = {}
    for line in PINS.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and ":" in line:
            key, _, value = line[2:].partition(":")
            found[key.strip()] = value.strip()
    return found


def stamp(text: str, version: str, commit: str, created: str) -> str:
    """A schema file with the pinned edition, commit and date in its header."""
    text = re.sub(r"(?m)^version: .*$", f"version: {version}", text)
    text = re.sub(
        r"(?m)^(source: https://github\.com/FIXTradingCommunity/orchestrations/blob/)"
        r"[0-9a-f]{40}",
        rf"\g<1>{commit}",
        text,
    )
    text = re.sub(r"(?m)^(  upstream_commit: )[0-9a-f]{40}$", rf"\g<1>{commit}", text)
    return re.sub(r'(?m)^(  upstream_created: )"[0-9-]+"$', rf'\g<1>"{created}"', text)


def outputs() -> dict[Path, str]:
    """Every file the script writes, with its content."""
    root = ET.parse(SOURCE).getroot()
    pinned = pins()
    version = root.get("version")
    if version != pinned["version"]:
        raise Unknown(
            f"upstream/ holds {version}, and the pins name {pinned['version']}"
        )
    written = {}
    for stem, data in Converter(root).files().items():
        written[DATA / f"{stem}.yaml"] = header(stem, version, pinned["commit"]) + dump(
            data
        )
    for path in sorted(SCHEMA_DIR.glob("fix_protocol*.yaml")):
        text = path.read_text(encoding="utf-8")
        written[path] = stamp(text, version, pinned["commit"], pinned["created"])
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="Fail if a file differs, writing nothing"
    )
    args = parser.parse_args(argv)
    try:
        written = outputs()
    except Unknown as err:
        print(
            f"Stopped: {err}. Model it before writing the catalogue.", file=sys.stderr
        )
        return 1
    stale = [
        path
        for path, text in written.items()
        if not path.exists() or path.read_text(encoding="utf-8") != text
    ]
    if args.check:
        for path in stale:
            print(f"stale: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1 if stale else 0
    DATA.mkdir(parents=True, exist_ok=True)
    for path in stale:
        path.write_text(written[path], encoding="utf-8")
    print(f"Wrote {len(stale)} of {len(written)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
