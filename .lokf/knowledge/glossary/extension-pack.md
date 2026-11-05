---
type: GlossaryTerm
id: https://w3id.org/lmodel/fix-protocol/knowledge/glossary/extension-pack
title: Extension pack
description: "An extension pack: the numbered unit in which FIX Latest changes; each record names the packs that added, last changed and deprecated it."
resource: src/fix_protocol/schema/fix_protocol_core.yaml
sources:
  - id: src-fix_protocol-schema-fix_protocol_core.yaml
    resource: src/fix_protocol/schema/fix_protocol_core.yaml
    title: fix_extension_pack
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Extension pack

FIX Latest changes one extension pack at a time. The schema's version names the pack it renders, `FIX.Latest_EP312`, and each record's `added_in_ep`, `updated_in_ep` and `deprecated_in_ep` name the packs that changed it.[^src-fix_protocol-schema-fix_protocol_core.yaml]

FIX Latest writes -1 on some elements that FIX 4.4 and FIX 5.0 added, and states nothing about what the value means.[^src-fix_protocol-schema-fix_protocol_core.yaml]

[^src-fix_protocol-schema-fix_protocol_core.yaml]: src/fix_protocol/schema/fix_protocol_core.yaml, fix_extension_pack
