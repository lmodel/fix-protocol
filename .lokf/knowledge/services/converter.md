---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/services/converter
genre: reference
title: The converter
description: "`scripts/fix_latest_to_records.py`: reads FIX Latest's Orchestra file in `upstream/` and writes the catalogue and the edition in the schema's headers. `just gen-schema` runs it, and it stops on an element or attribute no table names."
resource: scripts/fix_latest_to_records.py
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/upstream-copy
sources:
  - id: scripts-fix_latest_to_records.py
    resource: scripts/fix_latest_to_records.py
    title: the module's description
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The converter

The converter keeps every attribute of each element and leaves every annotation's text out.[^scripts-fix_latest_to_records.py]

It stops on an element or attribute that no table names, so new content in a later extension pack is modelled before it is written. `--check` fails when a file differs and writes nothing.[^scripts-fix_latest_to_records.py]

[^scripts-fix_latest_to_records.py]: scripts/fix_latest_to_records.py, the module's description
