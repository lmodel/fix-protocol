# Playbooks

* [Regenerate and test](regenerate-and-test.md) - How to regenerate the catalogue, the project files, the docs and the adapt copy after a change, and run the tests, with `just gen-schema`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`.
* [Move to a new extension pack](refresh-fix-latest.md) - How to move the catalogue to the FIX Latest file of another commit, as the upstream watch's issue names it, with `just refresh-fix-latest <commit>`, then regenerate and test.
* [Validate a catalogue file](validate-a-file.md) - How to validate a file of the catalogue, or a file of one's own, against the schema with `linkml-validate`, or against the committed JSON Schema without LinkML.
* [Release](release.md) - How a release happens: a releasing commit type merged to `main` promotes the changelog, tags the version and attaches the adapt copy and the bundle, starting from the `v0.0.0` baseline.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
