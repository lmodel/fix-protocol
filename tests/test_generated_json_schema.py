"""Checks the JSON Schema this project commits, as a user of it would read it.

project/jsonschema/fix_protocol.schema.json is what a consumer without LinkML validates
with. It is read here under the draft it declares, and held to the generator's settings in
.linkml/generators.yaml.
"""

import json
from functools import cache
from pathlib import Path

import jsonschema
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent
COMMITTED = ROOT / "project" / "jsonschema" / "fix_protocol.schema.json"
SCHEMA = ROOT / "src" / "fix_protocol" / "schema" / "fix_protocol.yaml"


@cache
def schema():
    return json.loads(COMMITTED.read_text(encoding="utf-8"))


def _validator():
    return jsonschema.validators.validator_for(schema())(schema())


def test_the_schema_is_valid_under_the_draft_it_declares():
    jsonschema.validators.validator_for(schema()).check_schema(schema())


def test_the_committed_file_is_the_generators_output():
    """A schema edit without `just gen-project` fails here."""
    settings = yaml.safe_load((ROOT / ".linkml" / "generators.yaml").read_text())
    args = settings["generator_args"]["jsonschema"]
    generated = JsonSchemaGenerator(str(SCHEMA), **args).serialize()
    assert json.loads(generated) == schema()


def test_the_top_of_the_schema_is_a_file_of_the_catalogue():
    """The file's root names the edition, and refuses another repository or key."""
    assert schema()["title"] == "fix_protocol"
    assert schema()["version"] == "FIX.Latest_EP312"
    top = {"repository_name": "FIX.Latest", "repository_version": "FIX.Latest_EP312"}
    assert _validator().is_valid(top)
    assert not _validator().is_valid({**top, "repository_name": "FIX.4.4"})
    assert not _validator().is_valid({**top, "x": 1})


def test_a_reference_must_look_like_one():
    """LinkML renders a reference as a string with no format, so each slot carries a pattern
    of its own, and a name in one fails."""
    props = schema()["$defs"]["FixField"]["properties"]
    for key in ("field_datatype", "field_code_set", "length_field", "base_category"):
        assert "pattern" in props[key], key
    member = schema()["$defs"]["FixMember"]["properties"]
    assert all("pattern" in member[k] for k in ("member_field", "member_group"))


def test_a_field_takes_a_datatype_or_a_code_set_and_not_both():
    field = {
        "id": "fix_field:55",
        "name": "Symbol",
        "field_datatype": "fix_datatype:String",
    }
    defs = schema()["$defs"]
    check = jsonschema.validators.validator_for(schema())(
        {"$ref": "#/$defs/FixField", "$defs": defs}
    )
    assert check.is_valid(field)
    assert not check.is_valid({**field, "field_code_set": "fix_code_set:55"})
    field.pop("field_datatype")
    assert not check.is_valid(field)
