---
type: FixDatatype
id: https://w3id.org/lmodel/fix-protocol/knowledge/fix-latest/price
genre: reference
title: Price
description: The Price datatype, record `fix_datatype:Price`, which narrows float and maps to xs:decimal, written as a concept of type `FixDatatype`.
resource: src/fix_protocol/data/datatypes.yaml
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
base_type: fix_datatype:float
added_in: FIX.4.2
mapped_datatypes:
  - mapped_standard: XML
    mapped_base: xs:decimal
    mapped_builtin: false
sources:
  - id: src-fix_protocol-data-datatypes.yaml
    resource: src/fix_protocol/data/datatypes.yaml
    title: the record fix_datatype:Price
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:20:28Z"
status: draft
---

# Price

Price narrows FIX's float datatype, and FIX gives xs:decimal as its XML Schema form. FIX 4.2 added it.[^src-fix_protocol-data-datatypes.yaml]

The keys beside LOKF's are the catalogue's own for `fix_datatype:Price`. `lokf validate` checks them against `.lokf/schema/fix-protocol.yaml`.[^readme.md]

[^src-fix_protocol-data-datatypes.yaml]: src/fix_protocol/data/datatypes.yaml, the record fix_datatype:Price
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
