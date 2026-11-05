---
type: Playbook
id: https://w3id.org/lmodel/fix-protocol/knowledge/playbooks/release
genre: how-to
title: Release
description: "How a release happens: a releasing commit type merged to `main` promotes the changelog, tags the version and attaches the adapt copy and the bundle, starting from the `v0.0.0` baseline."
resource: CONTRIBUTING.md
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/workflows/semantic-release
  - https://w3id.org/lmodel/fix-protocol/knowledge/workflows/knowledge-release
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - resource: .releaserc.json
  - resource: CHANGELOG.md
  - resource: .github/scripts/changelog-release.mjs
  - resource: .github/release
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Release

- Write the change under `## [Unreleased]` in CHANGELOG.md.
- Only `feat:`, `fix:`, `security:` and a breaking change start a release.
- Push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0.[^contributing.md]

[^contributing.md]: CONTRIBUTING.md, Releasing (maintainers)
