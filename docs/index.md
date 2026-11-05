# fix-protocol

This project is a LinkML model of FIX Latest, the FIX protocol's application layer, at the extension pack its schema names. It holds every element of FIX Latest's Orchestra file as a record: FIX's names, numbers and codes, with none of FIX's descriptive text.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the schema reads FIX Latest, and what it leaves out
- [`fix_protocol.yaml`](schema/fix_protocol.yaml): the schema, with its modules merged

## Validating a file of the catalogue

```bash
uv run linkml-validate -s src/fix_protocol/schema/fix_protocol.yaml -C FixRepository src/fix_protocol/data/fields.yaml
```

`project/jsonschema/fix_protocol.schema.json` is the same schema for anyone without LinkML. `tests/fix_rules.py` adds what a validator cannot state, such as that a reference names a record that exists.

## What the catalogue holds

| File | Records |
| --- | --- |
| `repository.yaml` | The edition, its metadata, 5 sections and 34 categories |
| `datatypes.yaml` | 38 datatypes |
| `code-sets.yaml` | 694 code sets with 5,745 codes |
| `fields.yaml` | 6,203 fields |
| `components.yaml` | 167 components |
| `groups.yaml` | 580 repeating groups |
| `messages.yaml` | 181 messages |
