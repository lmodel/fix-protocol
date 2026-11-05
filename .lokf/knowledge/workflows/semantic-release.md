---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: The workflow that, on a push to `main` behind the `release` Environment, promotes the changelog, tags the release and dispatches the knowledge release.
resource: .github/workflows/semantic-release.yml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
sources:
  - id: github-workflows-semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the workflow
  - resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Semantic release (semantic-release.yml)

It refuses to run without a `v*` tag, so the first releasing merge needs the `v0.0.0` baseline.[^github-workflows-semantic-release.yml]

[^github-workflows-semantic-release.yml]: .github/workflows/semantic-release.yml, the workflow
