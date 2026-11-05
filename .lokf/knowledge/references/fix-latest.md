---
type: Reference
id: https://w3id.org/lmodel/fix-protocol/knowledge/references/fix-latest
genre: reference
title: FIX Latest
description: FIX Latest, the FIX Trading Community's current FIX application layer, which changes by extension packs and which the schema models at extension pack 312 from its Orchestra file.
resource: upstream/OrchestraFIXLatest.xml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/references/orchestra-1-0
source:
  - https://github.com/FIXTradingCommunity/orchestrations
sources:
  - id: src-fix_protocol-data-repository.yaml
    resource: src/fix_protocol/data/repository.yaml
    title: the metadata
  - id: docs-about.md
    resource: docs/about.md
    title: What the schema models
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# FIX Latest

FIX Latest is published as one Orchestra file in the orchestrations repository. The file's metadata names the edition "FIX Latest as of Extension Pack 312", created on 2026-09-08 and following Orchestra v1.0.[^src-fix_protocol-data-repository.yaml]

The schema renders that edition, and the upstream watch reports the next.[^docs-about.md]

[^src-fix_protocol-data-repository.yaml]: src/fix_protocol/data/repository.yaml, the metadata
[^docs-about.md]: docs/about.md, What the schema models
