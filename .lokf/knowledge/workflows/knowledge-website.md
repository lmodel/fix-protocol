---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: The workflow that builds the documentation site and publishes it to GitHub Pages from `main`, once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
resource: .github/workflows/knowledge-website.yaml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
sources:
  - id: github-workflows-knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the workflow
  - resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

Only its deploy job holds a write scope.[^github-workflows-knowledge-website.yaml]

[^github-workflows-knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the workflow
