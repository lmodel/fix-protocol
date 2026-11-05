---
type: Explanation
id: https://w3id.org/lmodel/fix-protocol/knowledge/explanations/elements-as-records
genre: explanation
title: Why the schema holds FIX as records
description: Why the schema models each kind of FIX Latest element as a class and every element as a record, rather than describing the online specification's chapters as the earlier schema did.
resource: docs/about.md
about:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
sources:
  - id: docs-about.md
    resource: docs/about.md
    title: What the catalogue leaves out
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Why the schema holds FIX as records

FIX Latest is published as an Orchestra file that holds every element with its names, numbers, codes and pedigree. A record per element keeps what the file says, can be checked against it, and moves with each extension pack.[^docs-about.md]

The earlier schema described fixtrading.org's chapters: business areas, footnotes, page layouts and committees. Those pages are under a licence that allows no adapted copy, and the file states what they said about messages and fields.[^docs-about.md]

[^docs-about.md]: docs/about.md, What the catalogue leaves out
