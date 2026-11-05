---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/neighbour-copies
genre: reference
title: The neighbour copies
description: "`tests/neighbours/`: the adapt copies that 30 other lmodel repositories release, each pinned by checksum, which the tests hold this copy apart from."
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/adapt-copy
sources:
  - id: tests-test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the module's header
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The neighbour copies

Each file is a release's schema asset, downloaded and checked against the release's `.sha256` and its attestation, and pinned in the test by that checksum.[^tests-test_schema_rules.py]

When lmodel/fix-orchestra releases, its asset joins them, and the mapping test then checks this schema's `fix_orchestra:` mappings against it.[^tests-test_schema_rules.py]

[^tests-test_schema_rules.py]: tests/test_schema_rules.py, the module's header
