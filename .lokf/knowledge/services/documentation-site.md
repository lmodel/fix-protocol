---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, a Hugo site that the knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/fix-protocol`, built from the README, `docs/`, the schema's pages and this bundle.
resource: website
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/workflows/knowledge-website
sources:
  - id: website-readme.md
    resource: website/README.md
    title: the overview and What the site shows
  - id: website-site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - resource: docs/index.md
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:04:04Z"
status: draft
---

# Documentation site

Every page comes from a file the repository already holds, so a change to the site is a change to that file.[^website-readme.md]

`site.toml` sends the old mkdocs address `/about` to `docs/about.md`.[^website-site.toml] Each page of the schema is also at `elements/<Name>/`, where the schema's w3id rules point.[^website-readme.md]

[^website-readme.md]: website/README.md, the overview and What the site shows
[^website-site.toml]: website/site.toml, the site's address, title and redirects
