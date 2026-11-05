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
  at: "2026-11-05T19:50:21Z"
status: draft
---

# Rules beside the schema

The rules check what FIX's data keeps and no JSON Schema can state.[^tests-fix_rules.py] Among them:

- each reference names a record that exists;
- names, MsgTypes and the codes of a set are unique;
- each message's MsgType is a code of the MsgType code set, and each code of that set names a message;
- each code set, code, field, component, group and message states the FIX version that added it;
- each message opens with the standard header and closes with the standard trailer;
- a raw-data field names the field that gives its length.

FIX Latest breaks two of them, the third and the last, and the departures file names both.[^docs-about.md]

[^tests-fix_rules.py]: tests/fix_rules.py, the module's description
[^docs-about.md]: docs/about.md, Rules beside the schema
