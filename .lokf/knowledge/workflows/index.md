# Workflows

* [Build and test (main.yaml)](main.md) - The workflow that installs the locked environment and runs `just test` on Python 3.10 to 3.14, with `just lint` and `just lokf-adapt-check` on 3.13, on every pull request and push to `main`.
* [Lint and docs (lint-and-docs.yaml)](lint-and-docs.md) - The workflow that runs ShellCheck, actionlint, markdownlint, lychee and codespell, and holds CONTRIBUTING.md and SECURITY.md to their word budgets.
* [Upstream watch (upstream-watch.yaml)](upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: a new FIX Latest extension pack, a rewritten pinned commit or a changed licence opens or updates an issue.
* [Semantic release (semantic-release.yml)](semantic-release.md) - The workflow that, on a push to `main` behind the `release` Environment, promotes the changelog, tags the release and dispatches the knowledge release.
* [Knowledge librarian (knowledge-librarian.yaml)](knowledge-librarian.md) - The scheduled workflow that runs the KTL librarian on the bundle and opens a pull request with its patch, inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](knowledge-registrar.md) - The gate on every pull request that touches `.lokf/`: `lokf validate --check-refs` against the adapt copy, and the conventions script.
* [Knowledge release (knowledge-release.yaml)](knowledge-release.md) - The workflow that attaches the adapt copy, the bundle and a Copilot skill to a release, each with its `.sha256` and an attestation.
* [Knowledge sync (knowledge-sync.yaml)](knowledge-sync.md) - The weekly workflow that keeps the sidecar's copied workflows and scripts at the newest KTL release, by pull request.
* [Knowledge website (knowledge-website.yaml)](knowledge-website.md) - The workflow that builds the documentation site and publishes it to GitHub Pages from `main`, once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
