"""Checks each mapping the schema states against the source it names.

A fixr: mapping names a type, an element or an attribute of Orchestra 1.0, the edition FIX
Latest's file conforms to, and tests/upstream/orchestra-1.0-names.txt lists them. A
fix_orchestra: mapping names a class of lmodel/fix-orchestra's model of Orchestra 1.0,
which this test reads from that repository's released adapt copy in tests/neighbours/.
"""

from functools import cache
from pathlib import Path

import yaml

from tests import conversion

ROOT = Path(__file__).parent.parent
NAMES = ROOT / "tests" / "upstream" / "orchestra-1.0-names.txt"
FIX_ORCHESTRA = ROOT / "tests" / "neighbours" / "fix-orchestra.yaml"


def _mappings(node, where=""):
    """Each mapping CURIE of a schema, with the element that states it."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key.endswith("_mappings"):
                for curie in value:
                    yield where, curie
            else:
                yield from _mappings(value, key if isinstance(value, dict) else where)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item, where)


@cache
def mappings():
    return [
        (stem, where, curie)
        for stem, module in conversion.modules().items()
        for where, curie in _mappings(module)
    ]


def test_every_mapping_prefix_is_bound_where_it_is_stated():
    for stem, where, curie in mappings():
        prefixes = conversion.modules()[stem].get("prefixes") or {}
        assert curie.partition(":")[0] in prefixes, (stem, where, curie)


def test_the_umbrella_binds_every_prefix_a_module_uses():
    """The JSON-LD context takes its prefixes from the umbrella alone."""
    umbrella = conversion.modules()["fix_protocol"]["prefixes"]
    for module in conversion.modules().values():
        for prefix, iri in (module.get("prefixes") or {}).items():
            assert umbrella.get(prefix) == iri, prefix


def test_every_fixr_mapping_names_an_orchestra_1_0_name():
    names = {
        line.strip()
        for line in NAMES.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }
    targets = [curie for _, _, curie in mappings() if curie.startswith("fixr:")]
    assert len(targets) > 40
    assert {t.partition(":")[2] for t in targets} <= names


def test_each_record_class_maps_to_its_orchestra_type():
    """Each kind of record names Orchestra 1.0's type for it and fix-orchestra's class."""
    expected = {
        "FixRepository": "OrchestraRepositoryV10",
        "FixSection": "OrchestraSectionV10",
        "FixCategory": "OrchestraCategoryV10",
        "FixDatatype": "OrchestraDatatypeV10",
        "FixCodeSet": "OrchestraCodeSetV10",
        "FixCode": "OrchestraCodeV10",
        "FixField": "OrchestraFieldV10",
        "FixComponent": "OrchestraComponentV10",
        "FixGroup": "OrchestraGroupV10",
        "FixMessage": "OrchestraMessageV10",
    }
    classes = conversion.all_classes()
    for name, target in expected.items():
        assert f"fix_orchestra:{target}" in classes[name]["exact_mappings"], name
        assert any(c.startswith("fixr:") for c in classes[name]["exact_mappings"]), name


def test_every_fix_orchestra_mapping_names_a_released_class():
    classes = set(yaml.safe_load(FIX_ORCHESTRA.read_text(encoding="utf-8"))["classes"])
    targets = {
        curie.partition(":")[2]
        for _, _, curie in mappings()
        if curie.startswith("fix_orchestra:")
    }
    assert targets <= classes, sorted(targets - classes)
