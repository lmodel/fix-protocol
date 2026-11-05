"""Data tests: every example against the JSON Schema the validator generates, and the rules
on FIX Latest's data that no generator carries."""

import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.validator import validate
from linkml_runtime import SchemaView

from tests import conversion
from tests.fix_rules import rule_errors

SCHEMA = conversion.SCHEMA
DATA = Path(__file__).parent / "data"
VALID = sorted((DATA / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "invalid").glob("*.yaml"))
PROBLEM_INVALID = sorted((DATA / "problem" / "invalid").glob("*.yaml"))


@cache
def definitions():
    """The class definitions of the JSON Schema that linkml-validate generates. Generating
    it once keeps the run short; test_validator_agrees checks that linkml-validate gives the
    same answers."""
    return json.loads(JsonSchemaGenerator(str(SCHEMA), mergeimports=True).serialize())[
        "$defs"
    ]


def errors(instance, class_name):
    schema = {"$ref": f"#/$defs/{class_name}", "$defs": definitions()}
    validator = jsonschema.validators.validator_for(schema)(schema)
    return list(validator.iter_errors(instance))


def pointer(error):
    return "/" + "/".join(str(part) for part in error.absolute_path)


def class_of(path):
    return path.stem.split("-")[0]


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def fails_at(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[1].startswith("# Fails at: "), (
        f"{path.name}: the second line says where"
    )
    return lines[1].removeprefix("# Fails at: ").strip()


def places(error):
    """Where an error points: its own place, or, for an anyOf that no branch met, the place
    inside the branch that could have been meant. An optional value's branches are the value
    and null, so its error points inside the value."""
    if error.validator != "anyOf" or not error.context:
        return {pointer(error)}
    branches = {}
    for sub in error.context:
        branches.setdefault(sub.relative_schema_path[0], []).append(sub)
    real = [
        subs
        for subs in branches.values()
        if not any(s.validator == "type" and s.validator_value == "null" for s in subs)
    ]
    if len(real) != 1:
        return {pointer(error)}
    found = set()
    for sub in real[0]:
        found |= places(sub)
    return found or {pointer(error)}


def test_the_example_folders_hold_examples():
    """The parametrized tests below pass on an empty folder, so this one does not."""
    assert len(VALID) >= 16, len(VALID)
    assert len(INVALID) >= 29, len(INVALID)
    assert len(PROBLEM_INVALID) >= 13, len(PROBLEM_INVALID)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_examples_validate(path):
    found = errors(load(path), class_of(path))
    assert not found, [f"{pointer(e)}: {e.message[:200]}" for e in found]


def test_the_small_catalogue_keeps_the_rules():
    """The valid tree root breaks none of the rules, resolving only against itself."""
    found = rule_errors(load(DATA / "valid" / "FixRepository-small.yaml"))
    assert not found, found


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_examples_fail_where_they_say(path):
    """Every counter-example fails at the place its first comment names, and nowhere else but
    on the way to it, so a file that starts failing for another reason fails this test."""
    where = fails_at(path)
    found = errors(load(path), class_of(path))
    assert found, "it validates"
    reached = set().union(*(places(e) for e in found))
    report = [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert where in reached, (sorted(reached), report)
    on_the_way = {
        p for p in reached if where == p or where.startswith(p.rstrip("/") + "/")
    }
    assert reached == on_the_way, (sorted(reached - on_the_way), report)


@pytest.mark.parametrize("path", PROBLEM_INVALID, ids=lambda p: p.stem)
def test_rule_counter_examples_fail_where_they_say(path):
    """A counter-example under problem/invalid/ passes the JSON Schema, which cannot state
    its rule, and fails only the rule its first comment points to."""
    where = fails_at(path)
    instance = load(path)
    found = errors(instance, class_of(path))
    assert not found, [f"{pointer(e)}: {e.message[:200]}" for e in found]
    assert [found[0] for found in rule_errors(instance)] == [where]


def test_each_rule_has_a_counter_example():
    """Every rule of tests/fix_rules.py refuses one of the counter-examples."""
    from tests.fix_rules import RULES

    caught = {rule for path in PROBLEM_INVALID for _, rule, _, _ in rule_errors(load(path))}
    assert caught == {rule.__name__ for rule in RULES}


def test_validator_agrees():
    """linkml-validate, which the docs tell a user to run, accepts a valid example and
    rejects a counter-example at the same place."""
    good = DATA / "valid" / "FixRepository-small.yaml"
    report = validate(load(good), str(SCHEMA), "FixRepository")
    assert not report.results, [r.message for r in report.results]
    bad = DATA / "invalid" / "FixMessage-msg-type-of-three-characters.yaml"
    report = validate(load(bad), str(SCHEMA), "FixMessage")
    assert any("ABC" in r.message for r in report.results), [
        r.message for r in report.results
    ]


def test_every_concrete_class_has_an_example():
    """Each class a record can take has a valid example, and so does the root."""
    view = SchemaView(str(SCHEMA))
    concrete = {
        name
        for name, cls in view.all_classes().items()
        if not cls.abstract and not cls.mixin
    }
    examples = {class_of(path) for path in VALID}
    assert concrete == examples, sorted(concrete ^ examples)


def _nested(record):
    """A record and every record, member and value it holds."""
    yield record
    for key in ("fix_codes", "mapped_datatypes", "fix_members"):
        for value in record.get(key) or ():
            yield value
    if "num_in_group" in record:
        yield record["num_in_group"]


def test_each_example_is_a_real_record():
    """Each valid example but the small catalogue is a copy of the catalogue's own, so
    nothing in them is made up."""
    real = [
        value
        for key in conversion.LISTS
        for record in conversion.catalogue()[key]
        for value in _nested(record)
    ]
    for path in VALID:
        if path.stem == "FixRepository-small":
            continue
        assert load(path) in real, path.name
