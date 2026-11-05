---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
genre: reference
title: The FIX Latest LinkML schema
description: "The LinkML schema in `src/fix_protocol/schema/`: an umbrella over three modules that models each kind of element in FIX Latest, at extension pack 312, as a class with the `Fix` prefix."
resource: src/fix_protocol/schema
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/references/fix-latest
sources:
  - id: src-fix_protocol-schema-fix_protocol.yaml
    resource: src/fix_protocol/schema/fix_protocol.yaml
    title: the header
  - id: docs-about.md
    resource: docs/about.md
    title: What the schema models
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The FIX Latest LinkML schema

`fix_protocol.yaml` is the umbrella. It imports the core, the data dictionary and the message structure modules, and holds only `FixRepository`, the root of a catalogue file.[^src-fix_protocol-schema-fix_protocol.yaml]

Its `version` is `FIX.Latest_EP312`, the extension pack the pinned Orchestra file states, and its `source` is that file at the pinned commit.[^src-fix_protocol-schema-fix_protocol.yaml]

The records keep FIX's names, numbers and codes. The schema's titles and descriptions are this project's own.[^docs-about.md]

[^src-fix_protocol-schema-fix_protocol.yaml]: src/fix_protocol/schema/fix_protocol.yaml, the header
[^docs-about.md]: docs/about.md, What the schema models
