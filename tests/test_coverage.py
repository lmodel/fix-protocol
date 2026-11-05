"""Walks the Orchestra file and the catalogue side by side, sharing no code with the
converter.

Each XML element maps to the class the schema gives it, and each of its attributes to the
slot whose aliases name that attribute. The expected record is built from those alone, so a
converter that drops, renames, adds or misreads a value fails here, and so does a slot
whose alias does not name an attribute FIX writes.
"""

import re
import xml.etree.ElementTree as ET
from functools import cache

from linkml_runtime import SchemaView

from tests import conversion

FIXR = "{http://fixprotocol.io/2020/orchestra/repository}"
DCTERMS = "{http://purl.org/dc/terms/}"

# Which class each element of the file is a record of.
CLASSES = {
    "section": "FixSection",
    "category": "FixCategory",
    "datatype": "FixDatatype",
    "mappedDatatype": "FixMappedDatatype",
    "codeSet": "FixCodeSet",
    "code": "FixCode",
    "field": "FixField",
    "component": "FixComponent",
    "group": "FixGroup",
    "message": "FixMessage",
    "numInGroup": "FixNumInGroup",
    "fieldRef": "FixMember",
    "componentRef": "FixMember",
    "groupRef": "FixMember",
}
MEMBER_TAGS = ("fieldRef", "componentRef", "groupRef")
# The repository's lists, by the element that holds each.
HOLDERS = {
    "sections": "fix_sections",
    "categories": "fix_categories",
    "datatypes": "fix_datatypes",
    "codeSets": "fix_code_sets",
    "fields": "fix_fields",
    "components": "fix_components",
    "groups": "fix_groups",
    "messages": "fix_messages",
}


def local(tag):
    return tag.rsplit("}", 1)[-1]


@cache
def view():
    return SchemaView(str(conversion.SCHEMA))


@cache
def root():
    return ET.parse(conversion.UPSTREAM_FILE).getroot()


@cache
def slots_of(class_name):
    """Each slot of a class by the XML attribute its aliases name."""
    found = {}
    for slot in view().class_induced_slots(class_name):
        for alias in slot.aliases or ():
            found.setdefault(alias, []).append(slot)
    return found


@cache
def id_prefix(class_name):
    """The CURIE prefix of a class's identifiers, from the pattern the schema holds it to."""
    pattern = view().induced_slot("id", class_name).pattern
    return re.match(r"\^([a-z_]+):", pattern).group(1)


@cache
def by_id_or_name(class_name):
    """Each element of a class in the file, by its id and by its name, as an identifier."""
    tag = next(t for t, c in CLASSES.items() if c == class_name)
    found = {}
    for element in root().iter(FIXR + tag):
        key = element.get("id") or element.get("name")
        identifier = f"{id_prefix(class_name)}:{key}"
        found[key] = identifier
        if element.get("name"):
            found.setdefault(element.get("name"), identifier)
    return found


def expected_value(slot, raw):
    """What a record holds for an attribute's text, by the slot's range."""
    if slot.range in view().all_classes():
        return by_id_or_name(slot.range).get(raw)
    ancestry = (
        view().type_ancestors(slot.range) if slot.range in view().all_types() else []
    )
    if "integer" in ancestry or slot.range == "integer":
        return int(raw)
    if slot.range == "boolean":
        return raw in ("1", "true")
    return raw


def expected(element):
    """The record an element should be, built from its attributes and the schema's aliases."""
    tag = local(element.tag)
    class_name = CLASSES[tag]
    slots = slots_of(class_name)
    record = {}
    if tag in ("section", "category", "datatype", "codeSet", "code", "field",
               "component", "group", "message"):  # fmt: skip
        record["id"] = (
            f"{id_prefix(class_name)}:{element.get('id') or element.get('name')}"
        )
    for attribute, raw in element.attrib.items():
        if attribute == "id" and "id" in record:
            continue
        if tag in MEMBER_TAGS and attribute == "id":
            candidates = slots[tag]
        else:
            candidates = slots.get(attribute, [])
        assert candidates, f"{tag} attribute {attribute} has no slot"
        values = {
            slot.name: expected_value(slot, raw)
            for slot in candidates
            if slot.name != "id"
        }
        values = {name: value for name, value in values.items() if value is not None}
        assert len(values) == 1 or (attribute == "id" and not values), (tag, attribute)
        record.update(values)
    note = element.find(FIXR + "annotation")
    for appinfo in [] if note is None else note.findall(FIXR + "appinfo"):
        for encoding in appinfo:
            for attribute, raw in encoding.attrib.items():
                (slot,) = slots[attribute]
                record[slot.name] = expected_value(slot, raw)
    children = [c for c in element if local(c.tag) != "annotation"]
    if tag == "message":
        (structure,) = children
        children = list(structure)
    nested = {}
    for child in children:
        child_tag = local(child.tag)
        if child_tag in MEMBER_TAGS:
            nested.setdefault("fix_members", []).append(expected(child))
            continue
        (slot,) = slots[child_tag]
        value = expected(child)
        if slot.multivalued:
            nested.setdefault(slot.name, []).append(value)
        else:
            nested[slot.name] = value
    record.update(nested)
    return record


def test_every_element_is_its_record_and_nothing_more():
    """Each list of the file equals the catalogue's list, record by record and in order."""
    catalogue = conversion.catalogue()
    compared = 0
    for holder in root():
        name = local(holder.tag)
        if name == "metadata":
            continue
        key = HOLDERS[name]
        records = catalogue[key]
        assert len(records) == len(holder), key
        for element, record in zip(holder, records):
            assert record == expected(element), record["id"]
            compared += 1
    assert compared == 5 + 34 + 38 + 694 + 6203 + 167 + 580 + 181


def test_the_repositories_name_version_and_metadata():
    slots = slots_of("FixRepository")
    for document in conversion.documents().values():
        for attribute, raw in root().attrib.items():
            (slot,) = slots[attribute]
            assert document[slot.name] == raw
    repository = conversion.documents()["repository"]
    for child in root().find(FIXR + "metadata"):
        assert child.tag.startswith(DCTERMS)
        (slot,) = slots[local(child.tag)]
        assert repository[slot.name] == child.text.strip()


def test_the_counts_of_each_kind():
    """The numbers the docs give for this edition."""
    counts = {key: len(value) for key, value in conversion.catalogue().items()
              if isinstance(value, list)}  # fmt: skip
    assert counts == {
        "fix_sections": 5,
        "fix_categories": 34,
        "fix_datatypes": 38,
        "fix_code_sets": 694,
        "fix_fields": 6203,
        "fix_components": 167,
        "fix_groups": 580,
        "fix_messages": 181,
    }
    codes = sum(len(s["fix_codes"]) for s in conversion.catalogue()["fix_code_sets"])
    assert codes == 5745


def test_every_alias_is_a_name_fix_writes():
    """Each alias names an attribute or an element of the file, so an alias with a typo
    cannot leave its slot empty unnoticed."""
    written = set()
    for element in root().iter():
        written.add(local(element.tag))
        written.update(local(name) for name in element.attrib)
    aliases = {
        alias for slot in view().all_slots().values() for alias in slot.aliases or ()
    }
    for cls in view().all_classes().values():
        for attribute in (cls.attributes or {}).values():
            aliases.update(attribute.aliases or ())
    assert aliases <= written, sorted(aliases - written)
