# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Added

- **Every element of FIX Latest at extension pack 312 as a record** in `src/fix_protocol/data/`: 5 sections, 34 categories, 38 datatypes, 694 code sets with 5,745 codes, 6,203 fields, 167 components, 580 repeating groups and 181 messages. `scripts/fix_latest_to_records.py` writes them from `upstream/`.
- **`upstream/`**, holding FIX Latest's Orchestra file and its repository's licence at commit `cd24169` of FIXTradingCommunity/orchestrations, pinned by git object hash, with a weekly watch and `just refresh-fix-latest`.
- **Rules a validator cannot state** in `tests/fix_rules.py`, among them that each message's MsgType is a code of the MsgType code set, and the two places FIX Latest breaks one in `tests/upstream_departures.yaml`.
- **Tests** that check the catalogue against the Orchestra file, keep FIX's descriptions out of every file the project writes, and hold an example per class and a counter-example per constraint.
- **`.lokf/fix-protocol.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-fix-protocol.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, the CONTRIBUTING checklist, and a NOTICE that states the licence position.

### Changed

- **The schema models what FIX Latest is, not how its web pages are laid out.** Each kind of element in FIX's Orchestra file is a class with the `Fix` prefix, and each record keeps FIX's identifiers under an `id` such as `fix_field:55`.
- **The schema names the extension pack it renders**, `FIX.Latest_EP312`, where it named EP284 with nothing pinned.
- **Every title and description is this project's own**, and no file carries FIX's descriptive text.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `fix-protocol-linkml`.

### Removed

- **The six SSSOM sets a matching tool wrote**, with the script that overlaid them on the schema.
- **The modules that described fixtrading.org's chapter pages**: business areas, page layout rows, footnotes, committees and the tables the pages hold.
- **The patched generator scripts**, which linkml 1.12.1 no longer needs, and the mentions of a private prose overlay.
