"""The catalogue, the schema and the converter, for the tests that read them.

scripts/fix_latest_to_records.py is not a package, so it is loaded by its path. Each test
module shares one copy of what is read here and must not change it.
"""

import importlib.util
import sys
from functools import cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "fix_latest_to_records.py"
SCHEMA_DIR = ROOT / "src" / "fix_protocol" / "schema"
SCHEMA = SCHEMA_DIR / "fix_protocol.yaml"
DATA_DIR = ROOT / "src" / "fix_protocol" / "data"
UPSTREAM_FILE = ROOT / "upstream" / "OrchestraFIXLatest.xml"
FILES = (
    "repository",
    "datatypes",
    "code-sets",
    "fields",
    "components",
    "groups",
    "messages",
)
# The catalogue's lists, by the key that holds each.
LISTS = (
    "fix_sections",
    "fix_categories",
    "fix_datatypes",
    "fix_code_sets",
    "fix_fields",
    "fix_components",
    "fix_groups",
    "fix_messages",
)

# The C loader reads the catalogue in a fifth of the time, where the build has it.
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def _load():
    spec = importlib.util.spec_from_file_location("fix_latest_to_records", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


CONVERTER = _load()


@cache
def documents():
    """Each committed data file, by stem, read once."""
    return {
        stem: yaml.load(
            (DATA_DIR / f"{stem}.yaml").read_text(encoding="utf-8"), Loader=LOADER
        )
        for stem in FILES
    }


@cache
def catalogue():
    """The whole catalogue as one document, as the rules read it."""
    merged = {}
    for document in documents().values():
        for key, value in document.items():
            if key in LISTS:
                merged.setdefault(key, []).extend(value)
            else:
                merged.setdefault(key, value)
    return merged


@cache
def records():
    """Every record that has an identifier, codes included, by id."""
    found = {}
    for key in LISTS:
        for record in catalogue().get(key, ()):
            found[record["id"]] = record
            for code in record.get("fix_codes", ()):
                found[code["id"]] = code
    return found


@cache
def modules():
    """Each committed module of the schema, by file stem."""
    return {
        path.stem: yaml.load(path.read_text(encoding="utf-8"), Loader=LOADER)
        for path in sorted(SCHEMA_DIR.glob("fix_protocol*.yaml"))
    }


@cache
def all_classes():
    """Each class of the schema, by name."""
    return {
        name: cls
        for module in modules().values()
        for name, cls in (module.get("classes") or {}).items()
    }
