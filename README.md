<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# fix-protocol

FIX Latest, the FIX application layer standard (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/fix-protocol](https://lmodel.github.io/fix-protocol)

## What it models

The schema renders FIX Latest at extension pack 312, of 8 September 2026: the FIX Trading Community's FIX application layer, from its Orchestra file in [orchestrations](https://github.com/FIXTradingCommunity/orchestrations). Every section, category, datatype, code set, code, field, component, repeating group and message is a record that keeps FIX's names, numbers and codes and leaves FIX's descriptions out.

`src/fix_protocol/data/` holds the records, `upstream/` holds FIX's file, pinned by hash, and `scripts/fix_latest_to_records.py` writes the first from the second. [docs/about.md](docs/about.md) says how a record reads and what it leaves out.

## Mappings

* **Orchestra 1.0**, the edition FIX Latest's file follows: each class and slot maps to its type or attribute under `fixr:`. `tests/test_mappings.py` holds each to Orchestra 1.0's names.
* **[lmodel/fix-orchestra](https://github.com/lmodel/fix-orchestra)**: each record class maps to its class in that model of Orchestra 1.0. The test holds them to its released copy once there is one.

The six SSSOM sets are gone: a matching tool wrote their rows, and most named classes that no longer exist.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the converter from FIX's file and the upstream watch
* [src/fix_protocol/schema/](src/fix_protocol/schema): the LinkML schema
* [src/fix_protocol/data/](src/fix_protocol/data): every element of FIX Latest, which the converter writes
* [src/fix_protocol/datamodel/](src/fix_protocol/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): FIX Latest's Orchestra file and its repository's licence, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes. `just refresh-fix-latest <commit>` moves the catalogue to the extension pack at that commit.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/fix-protocol.yaml`, is the copy `just lokf-adapt` writes from `src/fix_protocol/schema/fix_protocol.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-fix-protocol.yaml`.

The copy roots `FixElement` on `Concept`, so a concept names one of its record classes as its type. In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
FixCategory, FixCode, FixCodeSet, FixComponent, FixDatatype, FixField, FixGroup, FixMessage, FixSection
```

The copy drops `id` for LOKF's `id` and folds FIX's `name` into LOKF's `title`. Every other key is this schema's own, so it shares none with LOKF or with another released copy. `tests/test_schema_rules.py` checks this.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

FIX's file in `upstream/` comes from a repository under the Apache License 2.0, while the file's own metadata says all rights are reserved. [NOTICE](NOTICE) says how this project reads that and why the records hold no text of FIX's. The FIX Trading Community has not endorsed this project.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
