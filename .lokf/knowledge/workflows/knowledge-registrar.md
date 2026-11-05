---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/workflows/knowledge-registrar
genre: reference
title: Knowledge registrar (knowledge-registrar.yaml)
description: "The gate on every pull request that touches `.lokf/`: `lokf validate --check-refs` against the adapt copy, and the conventions script."
resource: .github/workflows/knowledge-registrar.yaml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
sources:
  - id: github-workflows-knowledge-registrar.yaml
    resource: .github/workflows/knowledge-registrar.yaml
    title: the workflow
  - resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Knowledge registrar (knowledge-registrar.yaml)

It validates the bundle against the domain schema the justfile names.[^github-workflows-knowledge-registrar.yaml]

[^github-workflows-knowledge-registrar.yaml]: .github/workflows/knowledge-registrar.yaml, the workflow
