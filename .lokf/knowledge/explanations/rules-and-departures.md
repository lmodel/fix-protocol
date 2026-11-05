---
type: Explanation
id: https://w3id.org/lmodel/fix-protocol/knowledge/explanations/rules-and-departures
genre: explanation
title: Rules beside the schema
description: What `tests/fix_rules.py` checks that no JSON Schema can state, such as that each reference resolves and each message opens with the standard header, and where FIX Latest breaks a rule.
resource: tests/fix_rules.py
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/upstream-departures
sources:
  - id: tests-fix_rules.py
    resource: tests/fix_rules.py
    title: the module's description
  - id: docs-about.md
    resource: docs/about.md
    title: Rules beside the schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Rules beside the schema

The rules hold what FIX's data keeps: references resolve; names, tags and MsgTypes are unique; an extension pack comes with its version; a raw-data field names its length field; and a code set's number is the tag of a field that takes it.[^tests-fix_rules.py]

FIX Latest breaks two of them, and the departures file names both.[^docs-about.md]

[^tests-fix_rules.py]: tests/fix_rules.py, the module's description
[^docs-about.md]: docs/about.md, Rules beside the schema
