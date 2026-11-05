"""Checks the numbers the docs give against the catalogue and FIX's file."""

import xml.etree.ElementTree as ET

from tests import conversion

ROOT = conversion.ROOT


def _text(path):
    return " ".join((ROOT / path).read_text(encoding="utf-8").split())


def test_the_index_gives_the_catalogues_counts():
    catalogue = conversion.catalogue()
    index = _text("docs/index.md")
    codes = sum(len(s["fix_codes"]) for s in catalogue["fix_code_sets"])
    for key, label in (
        ("fix_sections", "sections"),
        ("fix_categories", "categories"),
        ("fix_datatypes", "datatypes"),
        ("fix_code_sets", "code sets"),
        ("fix_fields", "fields"),
        ("fix_components", "components"),
        ("fix_groups", "repeating groups"),
        ("fix_messages", "messages"),
    ):
        assert f"{len(catalogue[key]):,} {label}" in index, label
    assert f"{codes:,} codes" in index


def test_the_about_page_gives_the_files_counts():
    about = _text("docs/about.md")
    root = ET.parse(conversion.UPSTREAM_FILE).getroot()
    docs = sum(1 for e in root.iter() if e.tag.endswith("}documentation"))
    assert f"{docs:,} documentation elements" in about
    catalogue = conversion.catalogue()
    messages = {r["id"].partition(":")[2] for r in catalogue["fix_messages"]}
    fields = {r["id"].partition(":")[2] for r in catalogue["fix_fields"]}
    assert f"{len(messages & fields)} message numbers are also field tags" in about


def test_the_readme_and_changelog_name_the_edition():
    edition = conversion.documents()["repository"]
    pack = edition["repository_version"].rpartition("_EP")[2]
    readme = _text("README.md")
    assert f"extension pack {pack}, of 8 September 2026" in readme
    assert edition["metadata_created"] == "2026-09-08"
    changelog = _text("CHANGELOG.md")
    assert f"extension pack {pack} as a record" in changelog
    assert edition["repository_version"] in changelog
