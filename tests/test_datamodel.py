"""Checks what the generated models do with real data.

The Pydantic models load each file of the catalogue, the dataclasses load the smaller ones,
and the catalogue's JSON-LD, written with the generated context, gives each record an IRI
under its kind's namespace.
"""

import json

import pytest
from linkml_runtime.loaders import json_loader
from rdflib import Graph, URIRef

from fix_protocol.datamodel import fix_protocol as dataclasses_module
from fix_protocol.datamodel import fix_protocol_pydantic
from tests import conversion

CONTEXT = conversion.ROOT / "project" / "jsonld" / "fix_protocol.context.jsonld"
BASE = "https://w3id.org/lmodel/fix-protocol/"


@pytest.mark.parametrize("stem", conversion.FILES)
def test_each_file_loads_into_the_pydantic_models(stem):
    document = conversion.documents()[stem]
    model = fix_protocol_pydantic.FixRepository(**document)
    for key in conversion.LISTS:
        assert len(getattr(model, key) or []) == len(document.get(key, []))


@pytest.mark.parametrize("stem", ["repository", "datatypes", "messages"])
def test_the_smaller_files_load_into_the_dataclasses(stem):
    """The fields and the code sets load the same way and take longer, so these three
    stand for them, and between them hold every slot's form."""
    document = conversion.documents()[stem]
    model = json_loader.loads(
        json.dumps(document), target_class=dataclasses_module.FixRepository
    )
    for key in conversion.LISTS:
        assert len(getattr(model, key) or []) == len(document.get(key, []))


def test_the_pydantic_models_refuse_a_wrong_reference():
    with pytest.raises(ValueError):
        fix_protocol_pydantic.FixField(
            id="fix_field:55", name="Symbol", field_datatype="String"
        )


def test_the_json_ld_gives_each_record_its_kinds_iri():
    """A message and a field that share a number are two resources, and a reference is
    an IRI, not text."""
    document = {
        "@context": json.loads(CONTEXT.read_text(encoding="utf-8"))["@context"],
        "fix_messages": [conversion.records()["fix_message:1"]],
        "fix_fields": [conversion.records()["fix_field:1"]],
    }
    graph = Graph().parse(data=json.dumps(document), format="json-ld")
    subjects = {str(s) for s in graph.subjects() if isinstance(s, URIRef)}
    assert f"{BASE}message/1" in subjects
    assert f"{BASE}field/1" in subjects
    category = URIRef(f"{BASE}in_category")
    assert URIRef(f"{BASE}category/Session") in set(graph.objects(None, category))
