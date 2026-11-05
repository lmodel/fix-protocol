---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/dictionary-module
genre: reference
title: The data dictionary module
description: "`fix_protocol_dictionary.yaml`: the classes for FIX's datatypes, the XML Schema types they map to, code sets, codes and fields."
resource: src/fix_protocol/schema/fix_protocol_dictionary.yaml
isPartOf:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
dependsOn:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/core-module
sources:
  - id: src-fix_protocol-schema-fix_protocol_dictionary.yaml
    resource: src/fix_protocol/schema/fix_protocol_dictionary.yaml
    title: the module
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The data dictionary module

The module holds `FixDatatype`, `FixMappedDatatype`, `FixCodeSet`, `FixCode` and `FixField`.[^src-fix_protocol-schema-fix_protocol_dictionary.yaml]

A field names its datatype in `field_datatype` or its code set in `field_code_set`, never both. FIX's file names either one in a single attribute, `type`. The record splits it, so each reference has one range.[^src-fix_protocol-schema-fix_protocol_dictionary.yaml]

[^src-fix_protocol-schema-fix_protocol_dictionary.yaml]: src/fix_protocol/schema/fix_protocol_dictionary.yaml, the module
