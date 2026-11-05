---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: The weekly workflow that keeps the sidecar's copied workflows and scripts at the newest KTL release, by pull request.
resource: .github/workflows/knowledge-sync.yaml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
sources:
  - id: github-workflows-knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the workflow
  - resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

It reads the skills pin from the librarian workflow.[^github-workflows-knowledge-sync.yaml]

[^github-workflows-knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the workflow
