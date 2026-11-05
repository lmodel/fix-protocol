---
type: FixCategory
id: https://w3id.org/lmodel/fix-protocol/knowledge/fix-latest/single-general-order-handling
genre: reference
title: SingleGeneralOrderHandling
description: The category of single orders, record `fix_category:SingleGeneralOrderHandling`, in the Trade section, written as a concept of type `FixCategory`.
resource: src/fix_protocol/data/repository.yaml
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
fixml_file_name: order
in_section: fix_section:Trade
category_kind: Message
include_file: components
sources:
  - id: src-fix_protocol-data-repository.yaml
    resource: src/fix_protocol/data/repository.yaml
    title: the record fix_category:SingleGeneralOrderHandling
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# SingleGeneralOrderHandling

SingleGeneralOrderHandling groups the messages for one order, such as NewOrderSingle. The Trade section holds it, and its FIXML schema file is `order`.[^src-fix_protocol-data-repository.yaml]

The keys beside LOKF's are the catalogue's own for `fix_category:SingleGeneralOrderHandling`. `lokf validate` checks them against `.lokf/fix-protocol.yaml`.[^readme.md]

[^src-fix_protocol-data-repository.yaml]: src/fix_protocol/data/repository.yaml, the record fix_category:SingleGeneralOrderHandling
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
