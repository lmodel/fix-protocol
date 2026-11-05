---
type: Reference
id: https://w3id.org/lmodel/fix-protocol/knowledge/references/orchestra-1-0
genre: reference
title: FIX Orchestra 1.0
description: Orchestra 1.0, the FIX Trading Community's format for machine-readable rules of engagement, which FIX Latest's file follows and whose names the `fixr:` mappings use.
resource: tests/upstream/orchestra-1.0-names.txt
source:
  - https://github.com/FIXTradingCommunity/fix-orchestra-spec
sources:
  - id: docs-about.md
    resource: docs/about.md
    title: Mappings
  - id: tests-test_mappings.py
    resource: tests/test_mappings.py
    title: the module's header
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# FIX Orchestra 1.0

FIX Latest's file states that it conforms to Orchestra v1.0, under the namespace `http://fixprotocol.io/2020/orchestra/repository`.[^docs-about.md]

lmodel/fix-orchestra models Orchestra itself. This schema's record classes map to its Orchestra 1.0 classes.[^tests-test_mappings.py]

[^docs-about.md]: docs/about.md, Mappings
[^tests-test_mappings.py]: tests/test_mappings.py, the module's header
