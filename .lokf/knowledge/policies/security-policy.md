---
type: Policy
id: https://w3id.org/lmodel/fix-protocol/knowledge/policies/security-policy
title: Security policy
description: "SECURITY.md: report a vulnerability by private vulnerability reporting; it says what executes here, from the tests to the scheduled librarian, and what holds each."
resource: SECURITY.md
sources:
  - id: security.md
    resource: SECURITY.md
    title: What this repository releases
  - resource: CONTRIBUTING.md
  - resource: CODE_OF_CONDUCT.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Security policy

Only the latest release receives fixes.[^security.md]

The upstream check sends its token to api.github.com alone, and the converter reads `upstream/` with the standard library's XML parser.[^security.md]

[^security.md]: SECURITY.md, What this repository releases
