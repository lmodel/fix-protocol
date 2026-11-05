---
type: FixComponent
id: https://w3id.org/lmodel/fix-protocol/knowledge/fix-latest/instrument
genre: reference
title: Instrument
description: The Instrument component, record `fix_component:1003`, in the Common category, written as a concept of type `FixComponent` without its members.
resource: src/fix_protocol/data/components.yaml
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
abbr_name: Instrmt
in_category: fix_category:Common
added_in: FIX.4.3
sources:
  - id: src-fix_protocol-data-components.yaml
    resource: src/fix_protocol/data/components.yaml
    title: the record fix_component:1003
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Instrument

Instrument belongs to the Common category, which holds the components messages share. The catalogue lists its 174 members. This concept leaves them out, which the schema allows for a component.[^src-fix_protocol-data-components.yaml]

The keys beside LOKF's are the catalogue's own for `fix_component:1003`. `lokf validate` checks them against `.lokf/fix-protocol.yaml`.[^readme.md]

[^src-fix_protocol-data-components.yaml]: src/fix_protocol/data/components.yaml, the record fix_component:1003
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
