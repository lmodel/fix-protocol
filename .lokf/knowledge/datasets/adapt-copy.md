---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/adapt-copy
genre: reference
title: The adapt copy
description: "`.lokf/fix-protocol.yaml`: the copy of the schema that `lokf adapt` writes for the knowledge bundle, with `FixElement` re-rooted on LOKF's `Concept`; a release carries it as `schema-<tag>-fix-protocol.yaml`."
resource: .lokf/fix-protocol.yaml
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/neighbour-copies
sources:
  - id: project.justfile
    resource: project.justfile
    title: "Knowledge bundle: the adapted domain schema"
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The adapt copy

`just lokf-adapt` writes the copy from the schema, and `just lokf-adapt-check` fails when it is stale.[^project.justfile]

The copy drops `id` for LOKF's `id` and folds FIX's `name` into LOKF's `title`. It keeps the metadata's source apart from LOKF's, since it holds one value where LOKF's holds a list.[^project.justfile]

No other key is renamed, and the copy shares no name with LOKF or with a released neighbour copy.[^readme.md]

[^project.justfile]: project.justfile, Knowledge bundle: the adapted domain schema
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
