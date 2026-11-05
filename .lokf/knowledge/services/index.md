# Services

* [The converter](converter.md) - `scripts/fix_latest_to_records.py`: reads FIX Latest's Orchestra file in `upstream/` and writes the catalogue and the edition in the schema's headers. `just gen-schema` runs it, and it stops on an element or attribute no table names.
* [The upstream check](upstream-check.md) - `scripts/check_upstream_release.py`: compares the pinned FIX Latest file and licence with GitHub, names a new extension pack, and with `--refresh` copies the file at another commit into `upstream/`.
* [Documentation site](documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/fix-protocol`, built from the README, `docs/`, the schema's pages and this bundle.
