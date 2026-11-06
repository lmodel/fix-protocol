## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Rewrite the catalogue in src/fix_protocol/data/ from upstream/, and the edition in the
# schema's headers.
[group('model development')]
gen-schema:
  uv run --quiet scripts/fix_latest_to_records.py

# Move to the FIX Latest file of another commit of FIXTradingCommunity/orchestrations, as
# the upstream watch names it, and rebuild the catalogue from it. Then run gen-project,
# gen-doc and the tests, and commit everything they change together.
[group('model development')]
refresh-fix-latest COMMIT:
  python3 scripts/check_upstream_release.py --refresh {{COMMIT}}
  uv run --quiet scripts/fix_latest_to_records.py

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/schema/fix-protocol.yaml` is the copy `lokf adapt` writes from the schema so that it can
# sit beside `.lokf/schema/lokf.yaml` (`lokf adapt --help` lists the moves). The root is
# FixElement, the abstract base of every record with an identifier, so a concept names
# FixSection, FixCategory, FixDatatype, FixCodeSet, FixCode, FixField, FixComponent,
# FixGroup or FixMessage as its `type`, and LOKF's `id` stands for the record's. The fold
# puts FIX's name into the concept's `title`. The metadata's source stays this schema's
# own, since it holds one value where LOKF's source holds a list. The recipes run the
# `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs another, such as a
# checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root FixElement --prefix fix_protocol --fold name=title --keep FixRepository.metadata_source"

# Rewrite .lokf/schema/fix-protocol.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/fix-protocol.yaml

# Fail when .lokf/schema/fix-protocol.yaml is stale against the schema or .lokf/schema/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/schema/lokf.yaml -o .lokf/schema/fix-protocol.yaml --check
