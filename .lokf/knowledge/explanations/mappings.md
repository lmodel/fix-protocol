---
type: Explanation
id: https://w3id.org/lmodel/fix-protocol/knowledge/explanations/mappings
genre: explanation
title: Mappings
description: How the schema maps to Orchestra 1.0's names under `fixr:` and to lmodel/fix-orchestra's classes, why it keeps no SSSOM set, and which test holds each mapping.
resource: tests/test_mappings.py
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/references/orchestra-1-0
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/orchestra-names
sources:
  - id: docs-about.md
    resource: docs/about.md
    title: Mappings
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Mappings

Each class maps to Orchestra 1.0's type for it, and to its class in lmodel/fix-orchestra's Orchestra 1.0 module. Each slot maps to the attribute it holds.[^docs-about.md]

The six SSSOM sets of the earlier schema were a matching tool's guesses, and most named classes that no longer exist, so they are gone. FIX's own datatype mappings are on each datatype's record.[^docs-about.md]

[^docs-about.md]: docs/about.md, Mappings
