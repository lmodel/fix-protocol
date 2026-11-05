---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
genre: reference
title: The catalogue
description: "`src/fix_protocol/data/`: every element of FIX Latest at extension pack 312 as a record, in seven files: 5 sections, 34 categories, 38 datatypes, 694 code sets with 5,745 codes, 6,203 fields, 167 components, 580 repeating groups and 181 messages."
resource: src/fix_protocol/data
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/upstream-copy
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
  - https://w3id.org/lmodel/fix-protocol/knowledge/services/converter
sources:
  - id: docs-index.md
    resource: docs/index.md
    title: What the catalogue holds
  - id: tests-test_catalogue.py
    resource: tests/test_catalogue.py
    title: the module's tests
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The catalogue

The converter writes each file from `upstream/`. Each file is a `FixRepository` that names the edition and holds one or more kinds of element.[^docs-index.md]

| File | Records |
| --- | --- |
| `repository.yaml` | The edition, its metadata, 5 sections and 34 categories |
| `datatypes.yaml` | 38 datatypes |
| `code-sets.yaml` | 694 code sets with 5,745 codes |
| `fields.yaml` | 6,203 fields |
| `components.yaml` | 167 components |
| `groups.yaml` | 580 repeating groups |
| `messages.yaml` | 181 messages |

Every file passes the committed JSON Schema and the rules in `tests/fix_rules.py`, except the two departures that the departures file names.[^tests-test_catalogue.py]

[^docs-index.md]: docs/index.md, What the catalogue holds
[^tests-test_catalogue.py]: tests/test_catalogue.py, the module's tests
