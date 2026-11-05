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
