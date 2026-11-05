---
type: Explanation
id: https://w3id.org/lmodel/fix-protocol/knowledge/explanations/what-the-records-leave-out
genre: explanation
title: What the records leave out
description: Why the catalogue holds none of the 29,430 documentation elements of FIX's file, and how a test keeps FIX's descriptive text out of every file the project writes.
resource: NOTICE
about:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/policies/license-and-attribution
sources:
  - id: notice
    resource: NOTICE
    title: FIX Latest
  - id: tests-test_own_words.py
    resource: tests/test_own_words.py
    title: the module's header
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# What the records leave out

The file's repository is licensed under the Apache License 2.0, while the file's own rights line says all rights are reserved. The project keeps the file whole, and takes the narrower course with what it derives: the records hold identifiers, names, numbers, codes, structure and pedigree, and no description.[^notice]

`tests/test_own_words.py` refuses a run of six words of FIX's text in a record, and a run of four in the schema, the docs or this bundle.[^tests-test_own_words.py]

[^notice]: NOTICE, FIX Latest
[^tests-test_own_words.py]: tests/test_own_words.py, the module's header
