#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check FIX Latest on GitHub against the edition the catalogue renders, or refresh it.

The FIX Trading Community publishes FIX Latest as one Orchestra file,
``FIX Standard/OrchestraFIXLatest.xml``, in its ``orchestrations`` repository, and replaces
it as each extension pack is published. upstream/ holds the file at the commit pinned in
scripts/upstream_pins.tsv, with the repository's licence. Three things can change without
any change here:

- a newer commit replaces the file, which is a new extension pack;
- the pinned commit no longer holds the pinned files, which only a rewritten history does;
- the licence on the default branch changes.

The check lists trees through GitHub's API and compares git object hashes. For a new file it
reads only the first kilobyte, to name the extension pack. It prints a Markdown report and
exits 1 on any of the above, or when a check could not finish.

``--refresh COMMIT`` downloads the file and the licence at that commit into upstream/,
checks each against the hash GitHub's tree gives, and rewrites the pins.
``just refresh-fix-latest COMMIT`` runs it and then rebuilds the catalogue.

Text a server chose is quoted as code on one line in the report, so the issue the workflow
opens from it cannot mention anyone. A request or a redirect goes only to an https address
on api.github.com or raw.githubusercontent.com. Set ``GITHUB_TOKEN`` to raise the API's rate
limit; it is sent to api.github.com alone. Usage::

    python scripts/check_upstream_release.py [--report FILE]
    python scripts/check_upstream_release.py --refresh COMMIT
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PINS = ROOT / "scripts" / "upstream_pins.tsv"
UPSTREAM = ROOT / "upstream"
USER_AGENT = "lmodel-fix-protocol-upstream-check"
REPOSITORY = "FIXTradingCommunity/orchestrations"
API = f"https://api.github.com/repos/{REPOSITORY}"
RAW = f"https://raw.githubusercontent.com/{REPOSITORY}"
HOSTS = ("api.github.com", "raw.githubusercontent.com")
BRANCH = "master"

# The files the catalogue is built from, by their path in the repository, and the name each
# takes under upstream/.
FILES = {
    "FIX Standard/OrchestraFIXLatest.xml": "OrchestraFIXLatest.xml",
    "LICENSE": "LICENSE",
}
LATEST = "FIX Standard/OrchestraFIXLatest.xml"

# The most the script reads of one answer. The file is about 9 MB, and the API's listing of
# its folder about 10 kB.
MAX_BYTES = 30_000_000

# The repository element's version attribute, which names the extension pack.
VERSION = re.compile(rb'<fixr:repository\b[^>]*\bversion="([^"]+)"')


class _Redirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on GitHub's API or raw host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname not in HOSTS:
            raise ValueError(f"a redirect leads off GitHub, to {newurl}")
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is not None and parts.hostname != "api.github.com":
            new.remove_header("Authorization")
        return new


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_Redirect).open


def _fetch(url: str, limit: int = MAX_BYTES, first: int | None = None) -> bytes:
    """The body of one GitHub address, read up to the cap, or its first bytes."""
    host = urllib.parse.urlsplit(url).hostname
    headers = {"User-Agent": USER_AGENT}
    if host == "api.github.com":
        headers |= {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"Bearer {token}"
    if first is not None:
        headers["Range"] = f"bytes=0-{first - 1}"
        limit = first
    with _open(urllib.request.Request(url, headers=headers), timeout=60) as resp:
        body = resp.read(limit + 1)
    if first is not None:
        return body[:first]
    if len(body) > limit:
        raise ValueError(f"the answer from {url} is larger than {limit} bytes")
    return body


def _get(path: str):
    """The JSON answer to one API path."""
    return json.loads(_fetch(f"{API}{path}"))


def _raw(commit: str, path: str, first: int | None = None) -> bytes:
    """A file at a commit, whole or its first bytes."""
    return _fetch(f"{RAW}/{commit}/{urllib.parse.quote(path)}", first=first)


def _code(text: object) -> str:
    """Text a server chose, as a code span on one line, so it cannot mention a person or
    add a link in the issue. A blank line would end the span, so every run of spaces and
    line breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def _blob(data: bytes) -> str:
    """The git object hash of a file's bytes."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def header() -> dict[str, str]:
    """The pinned commit, the extension pack it holds and the file's creation date."""
    found = {}
    for line in PINS.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and ":" in line:
            key, _, value = line[2:].partition(":")
            found[key.strip()] = value.strip()
    return found


def pins() -> dict[str, str]:
    """Each pinned path in the repository and its git object hash."""
    rows = (
        line.split("\t")
        for line in PINS.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
    )
    return {path: sha for path, sha in rows}


def listing(commit: str) -> dict[str, str]:
    """The hash of each file the catalogue is built from, at a commit, by path."""
    root = {entry["path"]: entry for entry in _get(f"/git/trees/{commit}")["tree"]}
    found = {}
    if "LICENSE" in root:
        found["LICENSE"] = root["LICENSE"]["sha"]
    folder, _, name = LATEST.partition("/")
    if folder in root:
        tree = _get(f"/git/trees/{root[folder]['sha']}")
        if tree.get("truncated"):
            raise ValueError(f"GitHub cut short the listing of {folder}")
        for entry in tree["tree"]:
            if entry["path"] == name and entry["type"] == "blob":
                found[LATEST] = entry["sha"]
    return found


def version_at(commit: str) -> str:
    """The extension pack the file names at a commit, read from its first kilobyte."""
    match = VERSION.search(_raw(commit, LATEST, first=1024))
    if not match:
        raise ValueError(f"no version attribute in the first kilobyte at {commit}")
    return match.group(1).decode("ascii", "replace")


def check_latest() -> tuple[list[str], bool]:
    """Report whether a newer commit has replaced the file."""
    pinned = header()
    commits = _get(f"/commits?sha={BRANCH}&path={urllib.parse.quote(LATEST)}&per_page=1")
    newest = commits[0]["sha"]
    if newest == pinned["commit"]:
        return [
            f"- The newest commit to change FIX Latest is the pinned one, "
            f"{pinned['version']}."
        ], False
    if listing(newest).get(LATEST) == pins()[LATEST]:
        return [
            f"- A newer commit, {_code(newest)}, touched FIX Latest but left it unchanged."
        ], False
    return [
        f"- **FIX Latest moved to {_code(version_at(newest))} at {_code(newest)}; the "
        f"catalogue renders {pinned['version']}.** Refresh with `just refresh-fix-latest "
        f"{_code(newest)[1:-1]}`, read the changes the tests report, and commit "
        "upstream/, the pins, the catalogue and the regenerated files together."
    ], True


def check_pinned() -> tuple[list[str], bool]:
    """Report whether the pinned commit still holds the pinned files."""
    found = listing(header()["commit"])
    wrong = sorted(path for path, sha in pins().items() if found.get(path) != sha)
    if wrong:
        shown = ", ".join(_code(path) for path in wrong)
        return [
            f"- **The pinned commit no longer holds {shown} as pinned.** Find out why a "
            "published history changed before trusting the copy in upstream/."
        ], True
    return [f"- The pinned commit holds all {len(pins())} pinned files."], False


def check_licence() -> tuple[list[str], bool]:
    """Report whether the licence on the default branch is the pinned file."""
    root = {entry["path"]: entry["sha"] for entry in _get(f"/git/trees/{BRANCH}")["tree"]}
    spdx = (_get("").get("license") or {}).get("spdx_id")
    lines, attention = [], False
    if root.get("LICENSE") != pins()["LICENSE"]:
        attention = True
        lines.append(
            "- **LICENSE on the default branch changed.** Read what changed, and update "
            "NOTICE if the licence moved."
        )
    if spdx != "Apache-2.0":
        attention = True
        lines.append(f"- **GitHub names the licence {_code(spdx)}, not Apache-2.0.**")
    if not attention:
        lines.append("- The licence on the default branch is the pinned Apache-2.0 file.")
    return lines, attention


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("newest commit", check_latest),
    ("pinned commit", check_pinned),
    ("licence", check_licence),
)

# What a check can raise on the network or on an answer of another shape.
FAILURES = (OSError, http.client.HTTPException, EOFError, LookupError, ValueError)


def refresh(commit: str) -> int:
    """Download the files at a commit into upstream/ and rewrite the pins."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        print("Give the commit as its full 40-character hash.", file=sys.stderr)
        return 2
    expected = listing(commit)
    rows = []
    for path, name in FILES.items():
        data = _raw(commit, path)
        if path not in expected or _blob(data) != expected[path]:
            print(f"{path} at {commit} does not match GitHub's tree.", file=sys.stderr)
            return 1
        (UPSTREAM / name).write_bytes(data)
        rows.append(f"{path}\t{expected[path]}")
    data = (UPSTREAM / FILES[LATEST]).read_bytes()
    version = VERSION.search(data[:1024]).group(1).decode("ascii")
    created = re.search(rb"<dcterms:created>([^<]+)</dcterms:created>", data)
    lines = [
        "# The commit of FIXTradingCommunity/orchestrations that upstream/ copies, the",
        "# extension pack its FIX Latest file names, and the file's creation date. Each row",
        "# below is a file's path in that repository and its git object hash.",
        f"# commit: {commit}",
        f"# version: {version}",
        f"# created: {created.group(1).decode('ascii') if created else ''}",
        *rows,
    ]
    PINS.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"upstream/ now holds {version} at {commit}.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    parser.add_argument(
        "--refresh", metavar="COMMIT", help="Copy FIX Latest at COMMIT into upstream/"
    )
    args = parser.parse_args(argv)
    if args.refresh:
        try:
            return refresh(args.refresh)
        except FAILURES as err:
            print(f"The refresh could not finish: {err}", file=sys.stderr)
            return 1
    pinned = header()
    lines = [
        f"- Pinned edition: {pinned['version']}, created {pinned['created']}, at commit "
        f"{pinned['commit']} of {REPOSITORY}."
    ]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout, HTTPException and
        # EOFError a connection cut off mid-answer, LookupError and ValueError an answer
        # of another shape or too large.
        except FAILURES as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
