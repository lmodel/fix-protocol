---
type: Playbook
id: https://w3id.org/lmodel/fix-protocol/knowledge/playbooks/validate-a-file
genre: how-to
title: Validate a catalogue file
description: How to validate a file of the catalogue, or a file of one's own, against the schema with `linkml-validate`, or against the committed JSON Schema without LinkML.
resource: docs/index.md
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
sources:
  - id: docs-index.md
    resource: docs/index.md
    title: Validating a file of the catalogue
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Validate a catalogue file

```bash
uv run linkml-validate -s src/fix_protocol/schema/fix_protocol.yaml -C FixRepository src/fix_protocol/data/fields.yaml
```

`project/jsonschema/fix_protocol.schema.json` is the same schema for anyone without LinkML.[^docs-index.md]

[^docs-index.md]: docs/index.md, Validating a file of the catalogue
