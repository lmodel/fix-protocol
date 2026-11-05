---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge librarian (knowledge-librarian.yaml)
description: The scheduled workflow that runs the KTL librarian on the bundle and opens a pull request with its patch, inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
resource: .github/workflows/knowledge-librarian.yaml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
sources:
  - id: github-workflows-knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
    title: the workflow
  - resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Knowledge librarian (knowledge-librarian.yaml)

The agent's job holds no write token, and a separate job applies its patch.[^github-workflows-knowledge-librarian.yaml]

[^github-workflows-knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml, the workflow
