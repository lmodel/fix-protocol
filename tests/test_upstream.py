"""Checks that upstream/ holds the edition the schema and the catalogue render.

upstream/ holds FIX Latest's Orchestra file and the licence of the repository it comes from,
as the FIX Trading Community publishes them. scripts/check_upstream_release.py compares them
with GitHub. These tests make the same comparison offline.
"""

import hashlib
import importlib.util
import re
from functools import cache

import pytest
import yaml

from tests.conversion import ROOT, SCHEMA_DIR, UPSTREAM_FILE

UPSTREAM = ROOT / "upstream"
WATCH = ROOT / "scripts" / "check_upstream_release.py"


@cache
def _watch():
    spec = importlib.util.spec_from_file_location("watch_pins", WATCH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _blob(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_upstream_holds_only_the_pinned_files():
    found = {path.name for path in UPSTREAM.iterdir() if path.is_file()}
    assert found == set(_watch().FILES.values())
    assert set(_watch().pins()) == set(_watch().FILES)


def test_copies_match_the_pinned_blobs():
    """Each file has the git object hash the watch pins."""
    watch = _watch()
    for path, sha in watch.pins().items():
        assert _blob((UPSTREAM / watch.FILES[path]).read_bytes()) == sha, path


def test_the_file_names_the_pinned_edition_and_date():
    head = UPSTREAM_FILE.read_bytes()[:2048]
    pinned = _watch().header()
    assert re.search(rb'version="([^"]+)"', head).group(1).decode() == pinned["version"]
    created = re.search(rb"<dcterms:created>([^<]+)<", head).group(1).decode()
    assert created == pinned["created"]
    assert re.fullmatch(r"[0-9a-f]{40}", pinned["commit"])


@pytest.mark.parametrize(
    "path", sorted(SCHEMA_DIR.glob("fix_protocol*.yaml")), ids=lambda p: p.stem
)
def test_each_module_names_the_pinned_edition(path):
    header = yaml.safe_load(path.read_text(encoding="utf-8"))
    pinned = _watch().header()
    assert header["version"] == pinned["version"]
    assert pinned["commit"] in header["source"]
    assert header["license"] == "Apache-2.0"


def test_the_umbrella_names_the_pinned_commit():
    header = yaml.safe_load((SCHEMA_DIR / "fix_protocol.yaml").read_text())
    pinned = _watch().header()
    assert header["annotations"]["upstream_commit"] == pinned["commit"]
    assert header["annotations"]["upstream_created"] == pinned["created"]


def test_the_licence_is_apache_2_0():
    licence = (UPSTREAM / "LICENSE").read_text(encoding="utf-8")
    assert "Apache License" in licence and "Version 2.0, January 2004" in licence


def test_the_notice_states_the_position():
    """NOTICE names the Apache grant, the rights line that disagrees with it and the
    descriptive text the catalogue leaves out."""
    notice = " ".join((ROOT / "NOTICE").read_text(encoding="utf-8").split())
    assert "Apache License, Version 2.0" in notice
    assert "All Rights Reserved" in notice
    assert "documentation" in notice
    assert "No endorsement" in notice or "has endorsed" in notice
