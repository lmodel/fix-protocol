---
type: FixField
id: https://w3id.org/lmodel/fix-protocol/knowledge/fix-latest/symbol
genre: reference
title: Symbol
description: Field 55, Symbol, record `fix_field:55`, a String with the FIXML short name Sym, written as a concept of type `FixField`.
resource: src/fix_protocol/data/fields.yaml
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
abbr_name: Sym
field_datatype: fix_datatype:String
added_in: FIX.2.7
sources:
  - id: src-fix_protocol-data-fields.yaml
    resource: src/fix_protocol/data/fields.yaml
    title: the record fix_field:55
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:20:28Z"
status: draft
---

# Symbol

Symbol is field 55. It holds values of datatype String. Its FIXML short name is Sym, and FIX 2.7 added it.[^src-fix_protocol-data-fields.yaml]

The keys beside LOKF's are the catalogue's own for `fix_field:55`. `lokf validate` checks them against `.lokf/schema/fix-protocol.yaml`.[^readme.md]

[^src-fix_protocol-data-fields.yaml]: src/fix_protocol/data/fields.yaml, the record fix_field:55
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
