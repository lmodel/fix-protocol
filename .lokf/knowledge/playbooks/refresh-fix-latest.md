---
type: Playbook
id: https://w3id.org/lmodel/fix-protocol/knowledge/playbooks/refresh-fix-latest
genre: how-to
title: Move to a new extension pack
description: How to move the catalogue to the FIX Latest file of another commit, as the upstream watch's issue names it, with `just refresh-fix-latest <commit>`, then regenerate and test.
resource: project.justfile
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/services/upstream-check
  - https://w3id.org/lmodel/fix-protocol/knowledge/workflows/upstream-watch
sources:
  - id: docs-about.md
    resource: docs/about.md
    title: Keeping current
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Move to a new extension pack

1. Run `just refresh-fix-latest <commit>` with the commit the watch named. It copies the file and the licence into `upstream/`, rewrites the pins and rebuilds the catalogue.
2. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, then the tests, and read what they report.
3. Commit `upstream/`, the pins, the catalogue and the regenerated files together.[^docs-about.md]

[^docs-about.md]: docs/about.md, Keeping current
