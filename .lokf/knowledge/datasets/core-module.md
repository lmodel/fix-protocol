---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/core-module
genre: reference
title: The core module
description: "`fix_protocol_core.yaml`: the types for a FIX version, an extension pack number and a FIX name, the pedigree every element records, the `FixElement` base, and the section and category classes."
resource: src/fix_protocol/schema/fix_protocol_core.yaml
isPartOf:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
sources:
  - id: src-fix_protocol-schema-fix_protocol_core.yaml
    resource: src/fix_protocol/schema/fix_protocol_core.yaml
    title: the module
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The core module

The module imports only the LinkML types.[^src-fix_protocol-schema-fix_protocol_core.yaml]

- `FixPedigreeMixin` holds the six pedigree slots: the version and the extension pack that added, last changed and deprecated an element.
- `FixElement` is the abstract base of every record with an identifier, and gives each an `id` and a `name`.
- `FixSection` and `FixCategory` say how FIX groups its messages.

The `fix_version` type carries Orchestra 1.0's pattern for a version, anchored at both ends.[^src-fix_protocol-schema-fix_protocol_core.yaml]

[^src-fix_protocol-schema-fix_protocol_core.yaml]: src/fix_protocol/schema/fix_protocol_core.yaml, the module
