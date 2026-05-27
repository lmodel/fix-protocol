"""Data model package for fix-protocol."""

from pathlib import Path
from .fix_protocol import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "fix_protocol.yaml"
