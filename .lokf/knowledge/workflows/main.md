---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: The workflow that installs the locked environment and runs `just test` on Python 3.10 to 3.14, with `just lint` and `just lokf-adapt-check` on 3.13, on every pull request and push to `main`.
resource: .github/workflows/main.yaml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
sources:
  - id: github-workflows-main.yaml
    resource: .github/workflows/main.yaml
    title: the workflow
  - resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Build and test (main.yaml)

The job lints the schema and checks the adapt copy on Python 3.13 only.[^github-workflows-main.yaml]

[^github-workflows-main.yaml]: .github/workflows/main.yaml, the workflow
