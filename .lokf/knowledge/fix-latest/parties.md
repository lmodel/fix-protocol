---
type: FixGroup
id: https://w3id.org/lmodel/fix-protocol/knowledge/fix-latest/parties
genre: reference
title: Parties
description: The Parties repeating group, record `fix_group:1012`, counted by field 453 and holding five members, written as a concept of type `FixGroup`.
resource: src/fix_protocol/data/groups.yaml
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
abbr_name: Pty
in_category: fix_category:Common
added_in: FIX.4.3
num_in_group:
  count_field: fix_field:453
  added_in: FIX.4.3
fix_members:
  - member_field: fix_field:448
    added_in: FIX.4.3
    updated_in: FIX.5.0SP2
    updated_in_ep: 204
  - member_field: fix_field:447
    added_in: FIX.4.3
    updated_in: FIX.5.0SP2
    updated_in_ep: 204
  - member_field: fix_field:452
    added_in: FIX.4.3
    updated_in: FIX.5.0SP2
    updated_in_ep: 204
  - member_field: fix_field:2376
    added_in: FIX.5.0SP2
    added_in_ep: 179
  - member_group: fix_group:2077
    added_in: FIX.4.4
sources:
  - id: src-fix_protocol-data-groups.yaml
    resource: src/fix_protocol/data/groups.yaml
    title: the record fix_group:1012
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Parties

Parties belongs to the Common category. Field 453 counts its repeats, and it holds five members.[^src-fix_protocol-data-groups.yaml]

The keys beside LOKF's are the catalogue's own for `fix_group:1012`, which `lokf validate` checks against `.lokf/fix-protocol.yaml`.[^readme.md]

[^src-fix_protocol-data-groups.yaml]: src/fix_protocol/data/groups.yaml, the record fix_group:1012
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
