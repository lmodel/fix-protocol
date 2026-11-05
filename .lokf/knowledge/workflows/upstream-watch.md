---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: a new FIX Latest extension pack, a rewritten pinned commit or a changed licence opens or updates an issue."
resource: .github/workflows/upstream-watch.yaml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
sources:
  - id: github-workflows-upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the workflow
  - resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

A failing check fails the run and opens an issue, or comments on the one already open.[^github-workflows-upstream-watch.yaml]

[^github-workflows-upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the workflow
