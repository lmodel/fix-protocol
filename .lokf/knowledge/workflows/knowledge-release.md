---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge release (knowledge-release.yaml)
description: The workflow that attaches the adapt copy, the bundle and a Copilot skill to a release, each with its `.sha256` and an attestation.
resource: .github/workflows/knowledge-release.yaml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
sources:
  - id: github-workflows-knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
    title: the workflow
  - resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Knowledge release (knowledge-release.yaml)

It skips a release whose bundle and schema match the last one released.[^github-workflows-knowledge-release.yaml]

[^github-workflows-knowledge-release.yaml]: .github/workflows/knowledge-release.yaml, the workflow
