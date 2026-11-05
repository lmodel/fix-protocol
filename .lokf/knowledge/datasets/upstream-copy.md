---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/upstream-copy
genre: reference
title: The copy of FIX Latest
description: "`upstream/`: FIX Latest's Orchestra file and the Apache-2.0 licence of the repository it comes from, unchanged, at commit `cd24169` of FIXTradingCommunity/orchestrations, pinned by git object hash."
resource: upstream
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/references/orchestrations-repository
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/license-and-attribution
sources:
  - id: scripts-upstream_pins.tsv
    resource: scripts/upstream_pins.tsv
    title: the header
  - id: notice
    resource: NOTICE
    title: FIX Latest
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The copy of FIX Latest

`scripts/upstream_pins.tsv` names the commit, the extension pack the file states and the file's creation date, then each file's path in the upstream repository and its git object hash.[^scripts-upstream_pins.tsv]

The file's metadata carries the rights line "Copyright (c) FIX Protocol Ltd. All Rights Reserved.", while its repository is licensed under the Apache License 2.0. NOTICE says how this project reads that.[^notice]

[^scripts-upstream_pins.tsv]: scripts/upstream_pins.tsv, the header
[^notice]: NOTICE, FIX Latest
