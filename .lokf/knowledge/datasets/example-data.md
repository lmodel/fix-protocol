---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/example-data
genre: reference
title: The example data
description: "`tests/data/`: a valid example of every class, a counter-example for each constraint the JSON Schema states, and one for each rule of `tests/fix_rules.py`, all copied from real records."
resource: tests/data
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
  - https://w3id.org/lmodel/fix-protocol/knowledge/explanations/rules-and-departures
sources:
  - id: tests-test_data.py
    resource: tests/test_data.py
    title: the module's tests
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The example data

- `valid/` holds an example of every concrete class. Each one except the small catalogue is a real record from the catalogue.
- `invalid/` holds the counter-examples the JSON Schema refuses. Each file's second line names where it fails.
- `problem/invalid/` holds a counter-example for each rule, which passes the JSON Schema and breaks only that rule.

`tests/test_data.py` checks all three.[^tests-test_data.py]

[^tests-test_data.py]: tests/test_data.py, the module's tests
