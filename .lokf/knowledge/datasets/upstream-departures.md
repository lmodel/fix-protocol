---
type: Dataset
id: https://w3id.org/lmodel/fix-protocol/knowledge/datasets/upstream-departures
genre: reference
title: Where FIX Latest breaks its own rules
description: "`tests/upstream_departures.yaml`: the two places FIX Latest at extension pack 312 breaks a rule its data otherwise keeps, which the catalogue keeps as FIX wrote them."
resource: tests/upstream_departures.yaml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/explanations/rules-and-departures
sources:
  - id: tests-upstream_departures.yaml
    resource: tests/upstream_departures.yaml
    title: the list
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Where FIX Latest breaks its own rules

- The code BQ of the MsgType code set states no `added`.
- The raw-data field EncodedMDEntryStatusText names no length field.

The whole-catalogue test fails when a departure goes away, so the list stays current.[^tests-upstream_departures.yaml]

[^tests-upstream_departures.yaml]: tests/upstream_departures.yaml, the list
