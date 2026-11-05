---
type: Service
id: https://w3id.org/lmodel/fix-protocol/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website in `website/`, an Astro Starlight site that the knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/fix-protocol`, built from the README, `docs/`, the schema's pages and this bundle.
resource: website
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/workflows/knowledge-website
sources:
  - id: website-readme.md
    resource: website/README.md
    title: the overview
  - id: website-site.config.mjs
    resource: website/site.config.mjs
    title: REDIRECTS
  - resource: docs/index.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Documentation site

Every page comes from a file the repository already holds, so a change to the site is a change to that file.[^website-readme.md]

`site.config.mjs` sends the old mkdocs addresses `/about` and `/elements` to their new pages.[^website-site.config.mjs]

[^website-readme.md]: website/README.md, the overview
[^website-site.config.mjs]: website/site.config.mjs, REDIRECTS
