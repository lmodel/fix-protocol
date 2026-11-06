---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/fix-protocol/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: fix-protocol Knowledge Bundle
description: FIX Latest, the FIX application layer standard (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/fix-protocol/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# fix-protocol Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for fix-protocol. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [The converter](services/converter.md) - `scripts/fix_latest_to_records.py`: reads FIX Latest's Orchestra file in `upstream/` and writes the catalogue and the edition in the schema's headers. `just gen-schema` runs it, and it stops on an element or attribute no table names.
* [The upstream check](services/upstream-check.md) - `scripts/check_upstream_release.py`: compares the pinned FIX Latest file and licence with GitHub, names a new extension pack, and with `--refresh` copies the file at another commit into `upstream/`.
* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/fix-protocol`, built from the README, `docs/`, the schema's pages and this bundle.

# Datasets

* [The FIX Latest LinkML schema](datasets/fix-protocol-linkml-schema.md) - The LinkML schema in `src/fix_protocol/schema/`: an umbrella over three modules that models each kind of element in FIX Latest, at extension pack 312, as a class with the `Fix` prefix.
* [The core module](datasets/core-module.md) - `fix_protocol_core.yaml`: the types for a FIX version, an extension pack number and a FIX name, the pedigree every element records, the `FixElement` base, and the section and category classes.
* [The data dictionary module](datasets/dictionary-module.md) - `fix_protocol_dictionary.yaml`: the classes for FIX's datatypes, the XML Schema types they map to, code sets, codes and fields.
* [The message structure module](datasets/structure-module.md) - `fix_protocol_structure.yaml`: the classes for FIX's components, repeating groups and messages, with the ordered members each holds and the field that counts a group's repeats.
* [The catalogue](datasets/catalogue.md) - `src/fix_protocol/data/`: every element of FIX Latest at extension pack 312 as a record, in seven files: 5 sections, 34 categories, 38 datatypes, 694 code sets with 5,745 codes, 6,203 fields, 167 components, 580 repeating groups and 181 messages.
* [The copy of FIX Latest](datasets/upstream-copy.md) - `upstream/`: FIX Latest's Orchestra file and the Apache-2.0 licence of the repository it comes from, unchanged, at commit `cd24169` of FIXTradingCommunity/orchestrations, pinned by git object hash.
* [The adapt copy](datasets/adapt-copy.md) - `.lokf/schema/fix-protocol.yaml`: the copy of the schema that `lokf adapt` writes for the knowledge bundle, with `FixElement` re-rooted on LOKF's `Concept`; a release carries it as `schema-<tag>-fix-protocol.yaml`.
* [The neighbour copies](datasets/neighbour-copies.md) - `tests/neighbours/`: the adapt copies that 30 other lmodel repositories release, each pinned by checksum, which the tests hold this copy apart from.
* [The example data](datasets/example-data.md) - `tests/data/`: a valid example of every class, a counter-example for each constraint the JSON Schema states, and one for each rule of `tests/fix_rules.py`, all copied from real records.
* [Where FIX Latest breaks its own rules](datasets/upstream-departures.md) - `tests/upstream_departures.yaml`: the two places FIX Latest at extension pack 312 breaks a rule its data otherwise keeps, which the catalogue keeps as FIX wrote them.
* [Orchestra 1.0's names](datasets/orchestra-names.md) - `tests/upstream/orchestra-1.0-names.txt`: the names Orchestra 1.0 gives its types, elements and attributes, which the mapping test holds every `fixr:` mapping to.
* [The generated artefacts](datasets/generated-artefacts.md) - What the LinkML generators write from the schema: `project/` (JSON Schema, JSON-LD, OWL, SHACL, ShEx, SQL, GraphQL, protobuf, TypeScript, Java, Excel), the Python datamodel in `src/fix_protocol/datamodel/`, and `docs/schema/`.

# Fix-latest

* [PreTrade](fix-latest/pre-trade.md) - The PreTrade section of FIX Latest, record `fix_section:PreTrade`, written as a concept of type `FixSection`. FIX lists it second of its five sections.
* [SingleGeneralOrderHandling](fix-latest/single-general-order-handling.md) - The category of single orders, record `fix_category:SingleGeneralOrderHandling`, in the Trade section, written as a concept of type `FixCategory`.
* [Price](fix-latest/price.md) - The Price datatype, record `fix_datatype:Price`, which narrows float and maps to xs:decimal, written as a concept of type `FixDatatype`.
* [SideCodeSet](fix-latest/side-code-set.md) - The code set of field 54, Side, record `fix_code_set:54`, whose values are single characters, written as a concept of type `FixCodeSet` without its codes.
* [Buy](fix-latest/buy.md) - The code 1, Buy, of the Side code set, record `fix_code:54001`, written as a concept of type `FixCode`.
* [Symbol](fix-latest/symbol.md) - Field 55, Symbol, record `fix_field:55`, a String with the FIXML short name Sym, written as a concept of type `FixField`.
* [Instrument](fix-latest/instrument.md) - The Instrument component, record `fix_component:1003`, in the Common category, written as a concept of type `FixComponent` without its members.
* [Parties](fix-latest/parties.md) - The Parties repeating group, record `fix_group:1012`, counted by field 453 and holding five members, written as a concept of type `FixGroup`.
* [Heartbeat](fix-latest/heartbeat.md) - The Heartbeat message, MsgType 0, record `fix_message:1`, with its three members, written as a concept of type `FixMessage`.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The workflow that installs the locked environment and runs `just test` on Python 3.10 to 3.14, with `just lint` and `just lokf-adapt-check` on 3.13, on every pull request and push to `main`.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The workflow that runs ShellCheck, actionlint, markdownlint, lychee and codespell, and holds CONTRIBUTING.md and SECURITY.md to their word budgets.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: a new FIX Latest extension pack, a rewritten pinned commit or a changed licence opens or updates an issue.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that, on a push to `main` behind the `release` Environment, promotes the changelog, tags the release and dispatches the knowledge release.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The scheduled workflow that runs the KTL librarian on the bundle and opens a pull request with its patch, inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on every pull request that touches `.lokf/`: `lokf validate --check-refs` against the adapt copy, and the conventions script.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the adapt copy, the bundle and a Copilot skill to a release, each with its `.sha256` and an attestation.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copied workflows and scripts at the newest KTL release, by pull request.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds the documentation site and publishes it to GitHub Pages from `main`, once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

# References

* [FIX Latest](references/fix-latest.md) - FIX Latest, the FIX Trading Community's current FIX application layer, which changes by extension packs and which the schema models at extension pack 312 from its Orchestra file.
* [The orchestrations repository](references/orchestrations-repository.md) - FIXTradingCommunity/orchestrations on GitHub, licensed under the Apache License 2.0, which publishes FIX Latest as `FIX Standard/OrchestraFIXLatest.xml` and which the upstream watch compares each week.
* [FIX Orchestra 1.0](references/orchestra-1-0.md) - Orchestra 1.0, the FIX Trading Community's format for machine-readable rules of engagement, which FIX Latest's file follows and whose names the `fixr:` mappings use.

# Explanations

* [Why the schema holds FIX as records](explanations/elements-as-records.md) - Why the schema models each kind of FIX Latest element as a class and every element as a record, rather than describing the online specification's chapters as the earlier schema did.
* [What the records leave out](explanations/what-the-records-leave-out.md) - Why the catalogue holds none of the 29,430 documentation elements of FIX's file, and how a test keeps FIX's descriptive text out of every file the project writes.
* [Rules beside the schema](explanations/rules-and-departures.md) - What `tests/fix_rules.py` checks that no JSON Schema can state, such as that each reference resolves and each message opens with the standard header, and where FIX Latest breaks a rule.
* [Mappings](explanations/mappings.md) - How the schema maps to Orchestra 1.0's names under `fixr:` and to lmodel/fix-orchestra's classes, why it keeps no SSSOM set, and which test holds each mapping.

# Glossary

* [Extension pack](glossary/extension-pack.md) - An extension pack: the numbered unit in which FIX Latest changes; each record names the packs that added, last changed and deprecated it.
* [Record identifier](glossary/record-identifier.md) - A record's `id`: a prefix for its kind and FIX's own number or name, such as `fix_field:55` or `fix_category:Allocation`, since FIX numbers each kind on its own.
* [Departure](glossary/departure.md) - A departure: a place where FIX Latest's own data breaks a rule it otherwise keeps; the catalogue keeps it as FIX wrote it and `tests/upstream_departures.yaml` names it.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - How to regenerate the catalogue, the project files, the docs and the adapt copy after a change, and run the tests, with `just gen-schema`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`.
* [Move to a new extension pack](playbooks/refresh-fix-latest.md) - How to move the catalogue to the FIX Latest file of another commit, as the upstream watch's issue names it, with `just refresh-fix-latest <commit>`, then regenerate and test.
* [Validate a catalogue file](playbooks/validate-a-file.md) - How to validate a file of the catalogue, or a file of one's own, against the schema with `linkml-validate`, or against the committed JSON Schema without LinkML.
* [Release](playbooks/release.md) - How a release happens: a releasing commit type merged to `main` promotes the changelog, tags the version and attaches the adapt copy and the bundle, starting from the `v0.0.0` baseline.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work in this repository: the contributor owns every contribution, a record says what FIX's file says, and FIX's words stay out.
* [License and attribution](policies/license-and-attribution.md) - NOTICE: the project is under the Apache License 2.0, FIX's file stays under the FIX Trading Community's terms, and the records hold no text of FIX's; nothing comes from fixtrading.org.
* [Security policy](policies/security-policy.md) - SECURITY.md: report a vulnerability by private vulnerability reporting; it says what executes here, from the tests to the scheduled librarian, and what holds each.
