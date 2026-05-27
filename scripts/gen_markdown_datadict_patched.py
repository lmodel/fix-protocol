#!/usr/bin/env python3
"""Wrapper for linkml gen-markdown-datadict that patches one upstream perf bug.

Bug — `ERDiagramGenerator` re-instantiated for every class (markdowndatadictgen.py):
  `MarkdownDataDictGen._generate_class_diagram()` creates a new
  `ERDiagramGenerator` (and therefore a new `SchemaView` that re-parses the
  full schema YAML from disk) for every class:

      erd_gen = ERDiagramGenerator(self.schema_location, ...)
      diagram = erd_gen.serialize_classes(erd_classes, ...)

  With FIX's 7-module schema, and especially with CDM-scale schemas
  (2500+ classes, 37 modules), this is O(n) schema loads — the generator
  effectively hangs.

  Fix: override `_generate_class_diagram` to lazily create a single
  `ERDiagramGenerator` instance stored as `self._erd_gen` and reuse it for
  every subsequent per-class diagram call.

Dispatch note:
  The upstream `cli()` does `gen = MarkdownDataDictGen(yamlfile, **kwargs)`,
  resolving the class via the *module global*. To make `cli` use our
  subclass without re-implementing all its Click options, we rebind
  `markdowndatadictgen.MarkdownDataDictGen` to the patched subclass in the
  module globals before delegating.

See project.justfile gen-markdown-datadict-artifact for usage.
"""
from __future__ import annotations

from linkml.generators import markdowndatadictgen
from linkml.generators.erdiagramgen import ERDiagramGenerator
from linkml.generators.markdowndatadictgen import MarkdownDataDictGen, cli


class PatchedMarkdownDataDictGen(MarkdownDataDictGen):
    """`MarkdownDataDictGen` with `ERDiagramGenerator` caching to avoid O(n) schema loads."""

    def _generate_class_diagram(self, cls, relationships):
        items = []
        erd_classes = relationships["erd_classes"]
        children = relationships["children"]

        if erd_classes:
            if getattr(self, "_erd_gen", None) is None:
                self._erd_gen = ERDiagramGenerator(
                    self.schema_location,
                    exclude_attributes=True,
                    structural=False,
                )
            erd_classes.append(cls.name)
            diagram = self._erd_gen.serialize_classes(
                erd_classes, follow_references=False, max_hops=0
            )
            diagram_name = f"class_{cls.name.lower()}_erd"
            items.append(self._diagram_renderer.render(diagram, diagram_name=diagram_name))
        elif children or cls.is_a:
            items.append(self.header(4, "Local class diagram"))
            diagram_name = f"class_{cls.name.lower()}_local"
            items.append(
                self._diagram_renderer.render(
                    str(self.local_class_diagram(cls)), diagram_name=diagram_name
                )
            )

        return items


# Rebind the module global so upstream `cli` picks up the subclass.
markdowndatadictgen.MarkdownDataDictGen = PatchedMarkdownDataDictGen


if __name__ == "__main__":
    cli(standalone_mode=True)
