---
type: Playbook
id: https://w3id.org/lmodel/fix-protocol/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons."
resource: .
references:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/fix-protocol-linkml-schema
  - https://w3id.org/lmodel/fix-protocol/knowledge/references/fix-latest
exclusions:
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sidecar sync's pull request template.
  - resource: .github/dependabot.yml
    reason: "Tooling: the dependency update schedule."
  - resource: .github/scripts/report-issue.sh
    reason: "Tooling: the upstream watch's issue writer."
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .pre-commit-config.yaml
    reason: "Tooling: the hooks and the files they leave alone."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: .linkmllint.yaml
    reason: "Tooling: the schema linter's settings."
  - resource: .linkml
    reason: "Tooling: the generators' settings."
  - resource: config.public.mk
    reason: "Tooling: the variables the justfile loads."
  - resource: justfile
    reason: The template's recipes, which `just update` replaces.
  - resource: pyproject.toml
    reason: "Tooling: the package's metadata and the linters' settings."
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: src/fix_protocol/schema/README.md
    reason: Text from the project template.
  - resource: examples/README.md
    reason: Text from the project template.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: docs/elements
    reason: Generated pages that git ignores, apart from a placeholder.
  - resource: src/fix_protocol/__init__.py
    reason: Package plumbing.
  - resource: src/fix_protocol/_version.py
    reason: Package plumbing.
  - resource: tests/__init__.py
    reason: Package plumbing.
  - resource: tests/conversion.py
    reason: "Test plumbing: the tests' shared loader."
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The sidecar's link to the bundle.
  - resource: .lokf/schema/lokf.yaml
    reason: LOKF's schema, pinned by the sidecar.
  - resource: .lokf/scripts
    reason: The sidecar's scripts, which the weekly sync replaces.
  - resource: .lokf/m365
    reason: The sidecar's Copilot skill builder and its instructions.
  - resource: .lokf/README.md
    reason: The sidecar's own README.
  - resource: .lokf/queries.http
    reason: The sidecar's sample queries.
  - resource: .lokf/ingest.yaml.sample
    reason: The sidecar's unused example; this host has no outside sources.
  - resource: .lokf/uv.lock
    reason: The sidecar's lock file, tooling that pins versions.
  - resource: .lokf/.gitignore
    reason: "Tooling: what the sidecar keeps out of git."
  - resource: .lokf/.gitattributes
    reason: "Tooling: line endings in the bundle."
  - resource: .lokf/justfile
    reason: The sidecar's recipes, which the weekly sync rewrites but for its schema line.
  - resource: .lokf/pyproject.toml
    reason: The sidecar's toolkit floor and the domain schema it reads.
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: src/fix_protocol/schema
  - resource: src/fix_protocol/data
  - resource: src/fix_protocol/datamodel
  - resource: scripts
  - resource: upstream
  - resource: tests
  - resource: project
  - resource: project.justfile
  - resource: website
  - resource: .github/workflows
  - resource: .lokf/schema/fix-protocol.yaml
  - resource: NOTICE
  - resource: AI_COVENANT.md
  - resource: SECURITY.md
  - resource: CONTRIBUTING.md
  - resource: CHANGELOG.md
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:20:28Z"
status: draft
---

# Knowledge sources map

| Source | Yields | Re-check |
| --- | --- | --- |
| `src/fix_protocol/schema/` | the schema and its modules (`Dataset`) | read the module headers and classes |
| `src/fix_protocol/data/` | the catalogue, and the FIX elements typed by the domain classes | `just gen-schema --check` and the record each concept names |
| `upstream/`, `scripts/upstream_pins.tsv` | the copy of FIX Latest and its references (`Dataset`, `Reference`) | `tests/test_upstream.py` and the watch |
| `scripts/` | the converter and the upstream check (`Service`) | each module's description |
| `tests/` | the example data, the departures, the neighbours and Orchestra's names (`Dataset`) | each test module's header |
| `project/`, `src/fix_protocol/datamodel/`, `docs/schema/` | the generated artefacts (`Dataset`) | `just gen-project` and `just gen-doc` |
| `.github/workflows/` | one `Service` per workflow | each workflow's header comment |
| `docs/`, `README.md` | the explanations and the how-to pages | the section each concept cites |
| `NOTICE`, `AI_COVENANT.md`, `SECURITY.md`, `CONTRIBUTING.md` | the policies (`Policy`) and the release playbook | the section each concept cites |
| `.lokf/schema/fix-protocol.yaml`, `project.justfile` | the adapt copy (`Dataset`) | `just lokf-adapt-check` |
| `website/` | the documentation site (`Service`) | `website/README.md` |
