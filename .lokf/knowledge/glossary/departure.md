---
type: GlossaryTerm
id: https://w3id.org/lmodel/fix-protocol/knowledge/glossary/departure
title: Departure
description: "A departure: a place where FIX Latest's own data breaks a rule it otherwise keeps; the catalogue keeps it as FIX wrote it and `tests/upstream_departures.yaml` names it."
resource: tests/upstream_departures.yaml
sources:
  - id: tests-upstream_departures.yaml
    resource: tests/upstream_departures.yaml
    title: the list
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Departure

Each departure names the record, the rule it breaks, and why.[^tests-upstream_departures.yaml]

[^tests-upstream_departures.yaml]: tests/upstream_departures.yaml, the list
