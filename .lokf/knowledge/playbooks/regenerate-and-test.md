---
type: Playbook
id: https://w3id.org/lmodel/fix-protocol/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: How to regenerate the catalogue, the project files, the docs and the adapt copy after a change, and run the tests, with `just gen-schema`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`.
resource: CONTRIBUTING.md
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/services/converter
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/generated-artefacts
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Regenerate and test

1. Edit the schema or the converter.
2. Run `just gen-schema`, `just gen-project`, `just gen-doc` and `just lokf-adapt`.
3. Run `just lint` and `just test`.
4. Commit what they changed with the edit.[^contributing.md]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
