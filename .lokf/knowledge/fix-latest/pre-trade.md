---
type: FixSection
id: https://w3id.org/lmodel/fix-protocol/knowledge/fix-latest/pre-trade
genre: reference
title: PreTrade
description: The PreTrade section of FIX Latest, record `fix_section:PreTrade`, written as a concept of type `FixSection`. FIX lists it second of its five sections.
resource: src/fix_protocol/data/repository.yaml
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
fixml_file_name: pretrade
section_order: 1
updated_in: FIX.Latest
updated_in_ep: 271
sources:
  - id: src-fix_protocol-data-repository.yaml
    resource: src/fix_protocol/data/repository.yaml
    title: the record fix_section:PreTrade
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# PreTrade

PreTrade is FIX Latest's section of messages exchanged before a trade. Its FIXML schema file is `pretrade`, and FIX Latest last changed it in extension pack 271.[^src-fix_protocol-data-repository.yaml]

The keys beside LOKF's are the catalogue's own for `fix_section:PreTrade`. `lokf validate` checks them against `.lokf/fix-protocol.yaml`.[^readme.md]

[^src-fix_protocol-data-repository.yaml]: src/fix_protocol/data/repository.yaml, the record fix_section:PreTrade
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
