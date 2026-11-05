"""Checks the catalogue as a whole: against the committed JSON Schema, against the
converter, and against the rules of tests/fix_rules.py."""

import json
from functools import cache

import jsonschema
import pytest
import yaml

from tests import conversion
from tests.fix_rules import rule_errors

COMMITTED = conversion.ROOT / "project" / "jsonschema" / "fix_protocol.schema.json"
DEPARTURES = conversion.ROOT / "tests" / "upstream_departures.yaml"


@cache
def validator():
    schema = json.loads(COMMITTED.read_text(encoding="utf-8"))
    return jsonschema.validators.validator_for(schema)(schema)


@pytest.mark.parametrize("stem", conversion.FILES)
def test_each_file_validates_against_the_committed_json_schema(stem):
    """The file a user without LinkML validates with accepts every file of the catalogue."""
    found = list(validator().iter_errors(conversion.documents()[stem]))
    assert not found, [f"{list(e.absolute_path)}: {e.message[:200]}" for e in found[:5]]


def test_the_catalogue_is_the_converters_output():
    """A change to upstream/ or the converter without `just gen-schema` fails here. The
    files are compared by digest, since a diff of files this size takes minutes."""
    stale = [
        path.relative_to(conversion.ROOT)
        for path, text in conversion.CONVERTER.outputs().items()
        if not path.exists() or path.read_text(encoding="utf-8") != text
    ]
    assert not stale


def test_each_file_names_the_edition():
    for document in conversion.documents().values():
        assert document["repository_name"] == "FIX.Latest"
        assert document["repository_version"] == "FIX.Latest_EP312"


def test_the_whole_edition_keeps_the_rules_but_for_its_departures():
    """FIX Latest keeps every rule, but where tests/upstream_departures.yaml says it does
    not. A departure FIX has mended fails here too, so the list stays current."""
    departures = {
        (row["id"], row["rule"])
        for row in yaml.safe_load(DEPARTURES.read_text(encoding="utf-8"))
    }
    found = {
        (owner, rule)
        for _, rule, owner, _ in rule_errors(conversion.catalogue(), whole=True)
    }
    assert found == departures, (sorted(found - departures), sorted(departures - found))


def test_every_record_has_a_kind_of_its_own():
    """An identifier's prefix names its kind, so the projection's IRIs never collide,
    though a message and a field can share a number."""
    prefixes = {
        "fix_sections": "fix_section",
        "fix_categories": "fix_category",
        "fix_datatypes": "fix_datatype",
        "fix_code_sets": "fix_code_set",
        "fix_fields": "fix_field",
        "fix_components": "fix_component",
        "fix_groups": "fix_group",
        "fix_messages": "fix_message",
    }
    for key, prefix in prefixes.items():
        for record in conversion.catalogue()[key]:
            assert record["id"].partition(":")[0] == prefix, record["id"]
    numbers = {
        prefix: {r["id"].partition(":")[2] for r in conversion.catalogue()[key]}
        for key, prefix in prefixes.items()
    }
    assert numbers["fix_message"] & numbers["fix_field"]
