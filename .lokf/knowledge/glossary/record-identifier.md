---
type: GlossaryTerm
id: https://w3id.org/lmodel/fix-protocol/knowledge/glossary/record-identifier
title: Record identifier
description: "A record's `id`: a prefix for its kind and FIX's own number or name, such as `fix_field:55` or `fix_category:Allocation`, since FIX numbers each kind on its own."
resource: docs/about.md
sources:
  - id: docs-about.md
    resource: docs/about.md
    title: How a record reads
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Record identifier

Datatypes, categories and sections have no number in FIX, so their name stands in. The prefix matters because 159 message numbers are also field tags.[^docs-about.md]

[^docs-about.md]: docs/about.md, How a record reads
