---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/workflows/lint-and-docs
genre: reference
title: Lint and docs (lint-and-docs.yaml)
description: The workflow that runs ShellCheck, actionlint, markdownlint, lychee and codespell, and holds CONTRIBUTING.md and SECURITY.md to their word budgets.
resource: .github/workflows/lint-and-docs.yaml
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
sources:
  - id: github-workflows-lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
    title: the workflow
  - resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Lint and docs (lint-and-docs.yaml)

CONTRIBUTING.md has a budget of 1,000 words and SECURITY.md of 900.[^github-workflows-lint-and-docs.yaml]

[^github-workflows-lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml, the workflow
