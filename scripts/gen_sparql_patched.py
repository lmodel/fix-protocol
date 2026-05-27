#!/usr/bin/env python3
"""Wrapper for linkml gen-sparql that patches one upstream bug.

Bug 13 – SparqlGenerator template iterates schema.classes (root-only) instead
of all_classes() (with imports):

  SparqlGenerator uses use_schemaloader=False and its Jinja2 template renders
  with schema=self.schema, iterating schema.classes.items() which contains only
  classes defined directly in the root YAML file.  For a split/multi-module
  schema like CDM, this means the template only renders SPARQL queries for
  classes in the root file and misses all classes defined in imported modules.

  Passing --mergeimports on the CLI has no effect because SparqlGenerator sets
  use_schemaloader=False; the mergeimports flag only applies to the SchemaLoader
  path.

  Fix: after normal construction, call schemaview.merge_imports() to populate
  schema.classes (which is the same object as self.schema.classes), then
  re-run generate_sparql() to re-render the template against the full class set.

See project.justfile gen-sparql-artifact for usage.
"""

import click
from linkml._version import __version__
from linkml.generators.sparqlgen import SparqlGenerator
from linkml.utils.generator import shared_arguments

@shared_arguments(SparqlGenerator)
@click.command(name="sparql")
@click.option("-d", "--dir", help="Directory in which queries will be deposited")
@click.version_option(__version__, "-V", "--version")
def cli(yamlfile, dir, **kwargs):
    """Generate SPARQL queries for validation (patched: merges imports before rendering)."""
    gen = SparqlGenerator(yamlfile, **kwargs)
    # Bug 13 fix: after Generator.__post_init__, merge imports and re-render
    gen.schemaview.merge_imports()
    gen.queries = gen.generate_sparql(named_graphs=gen.named_graphs, limit=gen.limit)
    gen.serialize(directory=dir)


if __name__ == "__main__":
    cli()
