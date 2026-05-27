# About fix-protocol

LinkML metamodel for the structural elements of the FIX Latest
specification. The schema describes the **shape** of the FIX
specification documents (business areas, message categories, message
and component listings, datatypes, extension packs, footnotes,
workflow scenarios, status tables) — not market data or session
traffic.

## Design

### Modular layout

The umbrella schema [`fix_protocol.yaml`](../src/fix_protocol/schema/fix_protocol.yaml)
imports one module per FIX Latest chapter:

| Module | Source chapter | Classes | Enums | Slots |
|---|---|---:|---:|---:|
| [`fix_base`](../src/fix_protocol/schema/fix_base.yaml) | Introduction | 14 | 20 | 83 |
| [`fix_pre_trade`](../src/fix_protocol/schema/fix_pre_trade.yaml) | Business Area: Pre-Trade | 10 | 5 | 27 |
| [`fix_trade`](../src/fix_protocol/schema/fix_trade.yaml) | Business Area: Trade | 14 | 4 | 38 |
| [`fix_post_trade`](../src/fix_protocol/schema/fix_post_trade.yaml) | Business Area: Post-Trade | 16 | 21 | 35 |
| [`fix_infrastructure`](../src/fix_protocol/schema/fix_infrastructure.yaml) | Business Area: Infrastructure | 12 | 11 | 36 |
| [`fix_global_components`](../src/fix_protocol/schema/fix_global_components.yaml) | Global Components (cross-area) | 0 | 0 | 1 |

The `fix_global_components` module is a thin horizontal overlay: it
defines the `referenced_global_components` slot that each business-area
tree-root uses to record which entries from the FIX Latest "Global
Components" page its messages embed. The component catalog itself
(name, numeric ID, repeating-vs-block flag) is published as instances
of the `GlobalComponent` class declared in `fix_base`.

### Authoring conventions

- Apache-2.0 licensed; only shape-level structure lives in the public
  repository. FIX prose enrichments (descriptions, examples drawn from the
  published specification) live in a private `fix-protocol-private/` overlay
  repository split into a schema-side overlay (`fix-content/<module>.content.yaml`),
  and a fixture-side overlay (`test-fixtures-content/{valid,invalid}/<fixture>.yaml`).
  Both overlays carry CC BY-ND 4.0 prose from FIX Latest and can be deep-merged
  over the public artifacts at load time, never redistributed.
- Enums use body-less permissible values; descriptive prose is added
  in the private overlay.
- Names follow LinkML conventions: PascalCase for classes/enums,
  snake_case for slots, UPPER_SNAKE_CASE for permissible values.
- Per-module slots that would collide across business areas are
  disambiguated with a module prefix (e.g. `post_common_components`,
  `post_sole_category`).
- Line length ≤ 80 chars; indented lists; lint clean under
  `linkml-lint` and `yamllint`.

### Source provenance

Each module's `source:` field points at the canonical FIX Latest
chapter URL on fixtrading.org.

## Status

### Coverage

- **Introduction** — complete; covers FIX Family Standards, datatypes,
  field tag ranges (UDF / Reserved / GTC), extension packs,
  publisher / FPL metadata, footnotes, common components.
- **Pre-Trade business area** — complete for all eight pre-trade
  message categories with per-category sections, quote models,
  message and component listings.
- **Post-Trade business area** — complete; all twelve message
  categories, 47 messages, ~55 components (16 common), 14 footnotes
  with `introduced_in` extension packs, Allocation / Registration
  status tables, Trade Capture report usages and identifier rules,
  Allocation fragmentation field map, four communication scenarios,
  post-trade allocation pricing methods, Collateral Management usages
  and CollateralAssignment purposes, Position Management clearing
  functions, six clearing-service message-format families with
  per-format action lists, INITIATOR / RESPONDENT role labelling.
- **Infrastructure business area** — complete; four categories
  (Business Rejects, Network Status Communication, User Management,
  Application Sequencing), messages and components per category,
  BusinessRejectReason value table, standard request/response
  mappings, and Global-Components cross-references (the
  ApplicationSequenceControl global component referenced by the
  Application Sequencing category, with its tag set captured via
  `InfrastructureGlobalComponentReference`).
- **Trade business area** — complete; 18 classes covering the
  Trade categories (Single General Order Handling, Cross Order
  Handling, Multileg Order Handling, List Order Handling, Order
  Mass Handling, Indication of Interest, Order Status, Trade
  Capture), message and component listings, common-component
  catalog, OrdStatus precedence table, fragmentation entries, and
  Trade Appendix sections.

The full FIX Latest specification (EP284) has been audited against
the schemas; all enums and class catalogs match the upstream TOC
verbatim.

### Test fixtures

Executable instance data lives under
[`tests/data/`](../tests/data/) and is validated both with the
pytest harness (against the generated Python dataclasses) and with
`linkml-run-examples` (against the umbrella schema).

- **56 valid fixtures** (`tests/data/valid/`) — at least one per
  concrete class, plus rich tree-root fixtures for each business area
  populated from the corresponding source chapter.
- **26 invalid fixtures** (`tests/data/invalid/`) — each exercises a
  distinct constraint that LinkML actually enforces (enum
  membership, required-slot omission, pattern violation, numeric
  range). Four earlier fixtures that asserted constraints LinkML
  cannot express on enum-ranged slots (`equals_string` on
  `*BusinessArea.area`; conditional `high_tag` on `UDFTagRange`)
  have been retired — see [Known issues](#known-issues).
- Filename convention: `<ClassName>-<desc>.yaml`; the stem prefix
  must match the LinkML class name so the test driver can dispatch.

### Tooling

| Goal | Command |
|---|---|
| Lint the schema | `just lint` |
| Validate one fixture | `uv run linkml-validate -s src/fix_protocol/schema/fix_protocol.yaml -C <Class> <file>` |
| Regenerate artifacts | `just gen-project` |
| Regenerate pandera schema | `just gen-pandera-artifact` |
| Run full test suite | `just test` |
| Build docs | `just gen-doc` |

`just lint`, `just gen-project`, `just gen-pandera-artifact`, and
`just test` (schema lint + 56 pytest cases + counter-example
validation via `linkml-run-examples`) are all clean.

### Known issues

A growing set of upstream `linkml` / `linkml-runtime` defects
surfaced while building this schema. Every effort was made
to isolate the issues and report upstream with fix-PRs.

Meanwhile we done local workarounds:

| Upstream defect | Workaround in this repo |
|---|---|
| A. `gen-python` / `gen-yaml` drop prefixes declared on imported sub-schemas | Duplicate every ISO prefix into the umbrella `fix_protocol.yaml` |
| B. `linkml-runtime` is missing a PyYAML representer for `JsonObj` | [`scripts/gen_yaml_patched.py`](../scripts/gen_yaml_patched.py) registers it |
| C. `EnumDefinitionImpl` instances are unhashable | [`scripts/patch_pythongen.py`](../scripts/patch_pythongen.py) injects a `__hash__` |
| D. `EnumDefinitionMeta.__contains__` / `__getitem__` ignore the MRO | Same script rewrites empty enum-wrapper subclasses as module-level aliases |
| E. `EnumDefinitionImpl.__eq__` is not text-comparable to strings | Same script also injects a text-aware `__eq__` |
| F. `panderagen.map_type` crashes on a type whose `uri` is not in its built-in `TYPE_MAP` and that has no `typeof:` | Custom types (e.g. `TagNumber`) declare `uri: xsd:integer` and record the tighter XSD type via `exact_mappings:` |
| G. `pythongen` raises `Cyclic wrapper inheritance` when `camelcase(class)+camelcase(slot) == range-type-name` | Avoided by not declaring `typeof:` on the affected custom types (see F) |
| [linkml/linkml#3572](https://github.com/linkml/linkml/issues/3572) — `pythongen` emits class-reference wrappers before referenced enum bodies | `scripts/patch_pythongen.py` reorders the sections; [`scripts/run_examples_patched.py`](../scripts/run_examples_patched.py) applies the same patch in-process so `linkml-run-examples` can compile the module |
| H. `gen-rdf` embeds relative `./<module>.context.jsonld` refs in the merged `@context` array; rdflib resolves them against the schema's `@base` URI and 404s because the files are not published there | [`scripts/gen_rdf_patched.py`](../scripts/gen_rdf_patched.py) subclasses `RDFGenerator` and strips the unresolvable relative refs (plus the redundant `w3id.org/linkml/types.context.jsonld` remote ref) from the JSON-LD before handing it to rdflib |
| I. `gen-pandera` doesn't actually merge imports — `DataframeGenerator` builds its `SchemaView` without calling `merge_imports()`, so classes/enums in imported sub-modules are invisible and the emitted Pandera code only covers the umbrella schema's local entities | [`scripts/gen_pandera_patched.py`](../scripts/gen_pandera_patched.py) monkey-patches `DataframeGenerator.__post_init__` to call `self.schemaview.merge_imports()` after super setup |
| J. `gen-pandera`'s `DependencySorter._visit` raises `ValueError: Cyclic dependency detected` on any back-edge, aborting generation for schemas with legitimate cycles (self-referential slots, mutual references) | Same script replaces `_visit` with a cycle-tolerant variant that skips back-edges silently |
| K. `gen-markdown-datadict._generate_class_diagram` constructs a fresh `ERDiagramGenerator` (re-parsing the whole schema from disk) for every class, making the generator O(n²) and effectively hanging on large schemas | [`scripts/gen_markdown_datadict_patched.py`](../scripts/gen_markdown_datadict_patched.py) subclasses `MarkdownDataDictGen`, lazily creates a single `ERDiagramGenerator` on `self._erd_gen` and reuses it across all per-class diagrams |

In addition to the upstream defects above, two FIX-Latest invariants
cannot be expressed in LinkML and are therefore enforced only by
convention and documented inline on the affected slots:

- `*BusinessArea.area` is enum-typed and so cannot be pinned with
  `equals_string` (which accepts string-ranged slots only).
- `UDFTagRange.high_tag` is required for every `usage` except
  `GTC_RESERVED`; LinkML rules cannot make slot presence depend on
  the value of another enum-typed slot.

