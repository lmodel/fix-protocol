---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/services/upstream-check
genre: reference
title: The upstream check
description: "`scripts/check_upstream_release.py`: compares the pinned FIX Latest file and licence with GitHub, names a new extension pack, and with `--refresh` copies the file at another commit into `upstream/`."
resource: scripts/check_upstream_release.py
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/upstream-copy
  - https://w3id.org/lmodel/fix-protocol/knowledge/playbooks/refresh-fix-latest
sources:
  - id: scripts-check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the module's description
  - resource: scripts/upstream_pins.tsv
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# The upstream check

The check lists trees through GitHub's API and compares git object hashes. For a new file it reads only the first kilobyte, to name the extension pack.[^scripts-check_upstream_release.py]

It sends its token to api.github.com alone, and follows a redirect only to an https address on GitHub's API or raw host.[^scripts-check_upstream_release.py]

[^scripts-check_upstream_release.py]: scripts/check_upstream_release.py, the module's description
