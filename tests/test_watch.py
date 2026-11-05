"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py reads GitHub's API and, for a new file, its first
kilobyte. These tests replace its two network calls, `_get` and `_raw`, with tables of
answers, so they run offline. They show what the report says in each case the watch knows.
"""

import hashlib
import importlib.util
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
NEW = "f" * 40


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _tree(watch, file_sha=None, licence_sha=None):
    pins = watch.pins()
    return {
        "root": {
            "tree": [
                {"path": "FIX Standard", "type": "tree", "sha": "folder"},
                {
                    "path": "LICENSE",
                    "type": "blob",
                    "sha": licence_sha or pins["LICENSE"],
                },
            ]
        },
        "folder": {
            "tree": [
                {
                    "path": "OrchestraFIXLatest.xml",
                    "type": "blob",
                    "sha": file_sha or pins[watch.LATEST],
                }
            ]
        },
    }


def _answers(watch, newest=None, new_sha=None, licence_sha=None, spdx="Apache-2.0"):
    """The answers of an unchanged upstream, or of one with a newer file."""
    pinned = watch.header()["commit"]
    newest = newest or pinned
    old = _tree(watch)
    answers = {
        "/commits?sha=master&path=FIX%20Standard/OrchestraFIXLatest.xml&per_page=1": [
            {"sha": newest}
        ],
        f"/git/trees/{pinned}": old["root"],
        "/git/trees/folder": old["folder"],
        "/git/trees/master": _tree(watch, licence_sha=licence_sha)["root"],
        "": {"license": {"spdx_id": spdx}},
    }
    if newest != pinned:
        new = _tree(watch, file_sha=new_sha)
        new["root"]["tree"][0]["sha"] = "newfolder"
        answers[f"/git/trees/{newest}"] = new["root"]
        answers["/git/trees/newfolder"] = new["folder"]
    return answers


def _run(watch, answers, capsys, raw=None, argv=()):
    def fake_get(path):
        answer = answers[path]
        if isinstance(answer, Exception):
            raise answer
        return answer

    def fake_raw(commit, path, first=None):
        return raw[(commit, path)]

    watch._get = fake_get
    watch._raw = fake_raw
    code = watch.main(list(argv))
    return code, capsys.readouterr().out


def test_an_unchanged_upstream_passes(watch, capsys):
    code, out = _run(watch, _answers(watch), capsys)
    assert code == 0, out
    assert "is the pinned one, FIX.Latest_EP312" in out
    assert "holds all 2 pinned files" in out
    assert "pinned Apache-2.0 file" in out


def test_a_new_extension_pack_is_named_with_the_refresh(watch, capsys):
    head = b'<?xml version="1.0"?>\n<fixr:repository xmlns:fixr="x" version="FIX.Latest_EP315">'
    raw = {(NEW, watch.LATEST): head}
    code, out = _run(watch, _answers(watch, newest=NEW, new_sha="9" * 40), capsys, raw)
    assert code == 1
    assert "FIX Latest moved to `FIX.Latest_EP315`" in out
    assert f"just refresh-fix-latest {NEW}" in out


def test_a_newer_commit_that_leaves_the_file_alone_passes(watch, capsys):
    code, out = _run(watch, _answers(watch, newest=NEW), capsys)
    assert code == 0, out
    assert "left it unchanged" in out


def test_a_rewritten_history_is_reported(watch, capsys):
    answers = _answers(watch)
    answers["/git/trees/folder"] = {"tree": []}
    answers[
        "/commits?sha=master&path=FIX%20Standard/OrchestraFIXLatest.xml&per_page=1"
    ] = [{"sha": watch.header()["commit"]}]
    code, out = _run(watch, answers, capsys)
    assert code == 1
    assert "no longer holds `FIX Standard/OrchestraFIXLatest.xml`" in out


def test_a_changed_licence_is_reported(watch, capsys):
    code, out = _run(watch, _answers(watch, licence_sha="1" * 40), capsys)
    assert code == 1
    assert "LICENSE on the default branch changed" in out


def test_another_licence_name_is_reported(watch, capsys):
    code, out = _run(watch, _answers(watch, spdx="CC-BY-ND-4.0"), capsys)
    assert code == 1
    assert "`CC-BY-ND-4.0`, not Apache-2.0" in out


def test_a_failed_request_is_reported_and_fails(watch, capsys):
    answers = _answers(watch)
    answers[""] = OSError("connection refused")
    code, out = _run(watch, answers, capsys)
    assert code == 1
    assert "The licence check could not finish: `connection refused`" in out


def test_server_text_is_quoted_as_code_on_one_line(watch, capsys):
    head = b'<fixr:repository version="@someone\n`x`">'
    raw = {(NEW, watch.LATEST): head}
    answers = _answers(watch, newest=NEW, new_sha="9" * 40)
    code, out = _run(watch, answers, capsys, raw)
    assert code == 1
    assert "`@someone 'x'`" in out


def test_a_redirect_off_github_is_refused(watch):
    handler = watch._Redirect()
    request = urllib.request.Request("https://api.github.com/x")
    with pytest.raises(ValueError, match="leads off GitHub"):
        handler.redirect_request(request, None, 302, "", {}, "https://example.com/x")
    with pytest.raises(ValueError, match="leads off GitHub"):
        handler.redirect_request(request, None, 302, "", {}, "http://api.github.com/x")


def test_a_redirect_to_the_raw_host_drops_the_token(watch):
    handler = watch._Redirect()
    request = urllib.request.Request(
        "https://api.github.com/x", headers={"Authorization": "Bearer t"}
    )
    new = handler.redirect_request(
        request, None, 302, "", {}, "https://raw.githubusercontent.com/x"
    )
    assert not new.has_header("Authorization")


def _blob(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def test_a_refresh_writes_the_files_and_the_pins(watch, tmp_path, capsys):
    xml = b'<fixr:repository version="FIX.Latest_EP315"><dcterms:created>2026-12-01</dcterms:created>'
    licence = b"Apache License\n"
    watch.UPSTREAM = tmp_path
    watch.PINS = tmp_path / "pins.tsv"
    tree = {"root": {"tree": [
        {"path": "FIX Standard", "type": "tree", "sha": "folder"},
        {"path": "LICENSE", "type": "blob", "sha": _blob(licence)},
    ]}, "folder": {"tree": [
        {"path": "OrchestraFIXLatest.xml", "type": "blob", "sha": _blob(xml)},
    ]}}  # fmt: skip
    answers = {f"/git/trees/{NEW}": tree["root"], "/git/trees/folder": tree["folder"]}
    raw = {(NEW, watch.LATEST): xml, (NEW, "LICENSE"): licence}
    code, out = _run(watch, answers, capsys, raw, argv=["--refresh", NEW])
    assert code == 0, out
    assert (tmp_path / "OrchestraFIXLatest.xml").read_bytes() == xml
    assert watch.header() == {
        "commit": NEW,
        "version": "FIX.Latest_EP315",
        "created": "2026-12-01",
    }
    assert watch.pins()[watch.LATEST] == _blob(xml)


def test_a_refresh_refuses_a_file_that_differs_from_the_tree(watch, tmp_path, capsys):
    tree = _tree(watch)
    watch.UPSTREAM = tmp_path
    watch.PINS = tmp_path / "pins.tsv"
    answers = {f"/git/trees/{NEW}": tree["root"], "/git/trees/folder": tree["folder"]}
    raw = {(NEW, watch.LATEST): b"something else", (NEW, "LICENSE"): b""}
    code, _ = _run(watch, answers, capsys, raw, argv=["--refresh", NEW])
    assert code == 1
    assert not (tmp_path / "OrchestraFIXLatest.xml").exists()


def test_a_refresh_wants_a_whole_commit_hash(watch, capsys):
    code, _ = _run(watch, {}, capsys, argv=["--refresh", "cd24169"])
    assert code == 2
