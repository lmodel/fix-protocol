---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/structure-module
genre: reference
title: The message structure module
description: "`fix_protocol_structure.yaml`: the classes for FIX's components, repeating groups and messages, with the ordered members each holds and the field that counts a group's repeats."
resource: src/fix_protocol/schema/fix_protocol_structure.yaml
isPartOf:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
dependsOn:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/core-module
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/dictionary-module
sources:
  - id: src-fix_protocol-schema-fix_protocol_structure.yaml
    resource: src/fix_protocol/schema/fix_protocol_structure.yaml
    title: the module
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The message structure module

The module holds `FixComponent`, `FixGroup`, `FixMessage`, `FixMember` and `FixNumInGroup`.[^src-fix_protocol-schema-fix_protocol_structure.yaml]

A member is one field, one component or one group, and holds exactly one of them. A message, a component and a group list their members in `fix_members`, in FIX's order.[^src-fix_protocol-schema-fix_protocol_structure.yaml]

[^src-fix_protocol-schema-fix_protocol_structure.yaml]: src/fix_protocol/schema/fix_protocol_structure.yaml, the module
