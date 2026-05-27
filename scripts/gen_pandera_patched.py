#!/usr/bin/env python3
"""Wrapper for linkml gen-pandera that patches two upstream bugs.

Bug A – No `--mergeimports` support (panderagen.py):
  `gen-pandera` does not expose a `--mergeimports` Click option, and although
  `Generator.mergeimports` defaults to True, the panderagen `DataframeGenerator`
  builds its `SchemaView` without actually calling `merge_imports()`. The
  result is that classes/enums defined in imported sub-modules are invisible
  to the generator, so the emitted Pandera code only covers the umbrella
  schema's local entities.
  Fix: monkey-patch `DataframeGenerator.__post_init__` to call
  `schemaview.merge_imports()` after super setup so the closure is flat.

Bug B – `ValueError` on cyclic class dependencies (dependency_sorter.py):
  `DependencySorter._visit` raises `ValueError: Cyclic dependency detected`
  for any back-edge encountered during DFS. Real-world schemas frequently
  have legitimate cycles (a class with a self-referential slot, or two
  classes that reference each other), so this aborts generation.
  Fix: monkey-patch `_visit` to treat a back-edge as a soft skip; the
  affected node is still emitted in some order, just not strictly after
  its cyclic dependent.

Bugs filed upstream. See `docs/about.md` Known issues for tracking.
"""
from __future__ import annotations

import sys

from linkml.generators.panderagen import cli as _upstream_cli
from linkml.generators.panderagen.dataframe_generator import DataframeGenerator
from linkml.generators.panderagen.dependency_sorter import DependencySorter


def _tolerant_visit(self, node, visited, in_progress, result):
    if node in visited or node in in_progress:
        return
    in_progress.add(node)
    for dep in self.dependency_dict.get(node, []):
        _tolerant_visit(self, dep, visited, in_progress, result)
    in_progress.remove(node)
    visited.add(node)
    result.append(node)


DependencySorter._visit = _tolerant_visit


_orig_post_init = DataframeGenerator.__post_init__


def _post_init_with_merge(self, *args, **kwargs):
    _orig_post_init(self, *args, **kwargs)
    self.schemaview.merge_imports()


DataframeGenerator.__post_init__ = _post_init_with_merge


if __name__ == "__main__":
    _upstream_cli(standalone_mode=True)
