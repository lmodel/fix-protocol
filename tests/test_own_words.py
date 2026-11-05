"""Checks that FIX's descriptive text stays out of the repository's own files.

FIX Latest's Orchestra file carries FIX's descriptions of its elements in documentation
elements. NOTICE says why the catalogue and everything written from it leave them out, and
why the schema, the docs and the bundle describe FIX in the project's own words. These tests
hold both: no run of six words of FIX's text reaches a generated file or the catalogue, and
no run of four words reaches what the project writes by hand. Runs that are only FIX's own
names and values, which the records keep, do not count.
"""

import re
import xml.etree.ElementTree as ET
from functools import cache
from pathlib import Path

import pytest
import yaml

from tests import conversion

ROOT = conversion.ROOT
FIXR = "{http://fixprotocol.io/2020/orchestra/repository}"
WORD = re.compile(r"[a-z0-9]+")

# What the project writes by hand, in its own words.
OWN = [
    *sorted((ROOT / "src" / "fix_protocol" / "schema").glob("*.yaml")),
    *sorted((ROOT / "docs").glob("*.md")),
    ROOT / "README.md",
    *sorted((ROOT / ".lokf" / "knowledge").rglob("*.md")),
]

# What the converter writes. The generators write only what the schema holds, which the
# check of the project's own words covers.
WRITTEN = sorted((ROOT / "src" / "fix_protocol" / "data").glob("*.yaml"))


def words(text):
    return WORD.findall(text.lower())


def runs(text, size):
    found = words(text)
    return {tuple(found[i : i + size]) for i in range(len(found) - size + 1)}


@cache
def root():
    return ET.parse(conversion.UPSTREAM_FILE).getroot()


@cache
def documentation():
    """The text of every documentation element, as FIX wrote it."""
    return [e.text or "" for e in root().iter(FIXR + "documentation")]


@cache
def fix_runs(size):
    found = set()
    for text in documentation():
        found |= runs(text, size)
    return found


@cache
def name_runs(size):
    """Runs made only of what the records keep: FIX's names, codes and attribute values,
    and the metadata's text."""
    found = set()
    for element in root().iter():
        for value in element.attrib.values():
            found |= runs(value, size)
        if element.tag.startswith("{http://purl.org/dc/terms/}") and element.text:
            found |= runs(element.text, size)
    return found


def test_the_file_holds_the_text_these_tests_look_for():
    assert len(documentation()) == 29430
    assert len(fix_runs(4)) > 80_000


def _strings(node):
    """Every text value of a parsed data file."""
    if isinstance(node, dict):
        for value in node.values():
            yield from _strings(value)
    elif isinstance(node, list):
        for value in node:
            yield from _strings(value)
    elif isinstance(node, str):
        yield node


@pytest.mark.parametrize("stem", conversion.FILES)
def test_no_record_carries_fixs_text(stem):
    """Each text value of the catalogue is checked on its own, so a run cannot span two
    keys by chance."""
    shared = set()
    for value in _strings(conversion.documents()[stem]):
        shared |= runs(value, 6) & fix_runs(6)
    shared -= name_runs(6)
    assert not shared, sorted(" ".join(run) for run in shared)[:10]


def _prose(path):
    """The descriptive text of a file: each title, description, comment and note of a
    schema, or a Markdown file's text."""
    text = path.read_text(encoding="utf-8")
    if path.suffix != ".yaml":
        return [text]
    found = []

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key in ("title", "description", "comments", "notes"):
                    found.extend(value if isinstance(value, list) else [value])
                else:
                    walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(yaml.safe_load(text))
    return found


@pytest.mark.parametrize("path", OWN, ids=lambda p: str(p.relative_to(ROOT)))
def test_own_words_share_no_run_of_four(path):
    shared = set()
    for text in _prose(path):
        shared |= _shared_runs(text)
    assert not shared, sorted(" ".join(run) for run in shared)


def _shared_runs(text):
    # A code span or a block is a name, a value or a command, not a description.
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    return (runs(text, 4) & fix_runs(4)) - name_runs(4)


def test_the_check_would_catch_a_copied_sentence(tmp_path):
    """A description pasted from FIX's file shares runs of both lengths."""
    pasted = max(documentation(), key=len)
    assert runs(pasted, 4) & fix_runs(4)
    assert runs(pasted, 6) - name_runs(6)
