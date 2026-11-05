---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/generated-artefacts
genre: reference
title: The generated artefacts
description: "What the LinkML generators write from the schema: `project/` (JSON Schema, JSON-LD, OWL, SHACL, ShEx, SQL, GraphQL, protobuf, TypeScript, Java, Excel), the Python datamodel in `src/fix_protocol/datamodel/`, and `docs/schema/`."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: tests-test_generated_json_schema.py
    resource: tests/test_generated_json_schema.py
    title: the module's tests
  - resource: src/fix_protocol/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The generated artefacts

`just gen-project` writes `project/` and the Python datamodel, and `just gen-doc` writes `docs/schema/` and the schema's pages. None of them is edited by hand.[^contributing.md]

`project/jsonschema/fix_protocol.schema.json` is the schema for anyone without LinkML. A test compares it with the generator's output.[^tests-test_generated_json_schema.py]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^tests-test_generated_json_schema.py]: tests/test_generated_json_schema.py, the module's tests
