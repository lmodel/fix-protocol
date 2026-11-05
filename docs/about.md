# About fix-protocol

## What the schema models

FIX Latest is the FIX Trading Community's current FIX application layer. It changes by extension packs, several a month. The community publishes it as one Orchestra file, `FIX Standard/OrchestraFIXLatest.xml` in its [orchestrations](https://github.com/FIXTradingCommunity/orchestrations) repository. `upstream/` holds that file at the commit `scripts/upstream_pins.tsv` names, and the schema's `version` is the extension pack the file states.

The schema models what the file holds: sections, categories, datatypes, code sets and their codes, fields, components, repeating groups and messages. Each is a class with the `Fix` prefix, and every element of the file is a record in `src/fix_protocol/data/`. `scripts/fix_latest_to_records.py` writes them, and stops on an element or attribute it has no rule for.

## How a record reads

A record's `id` is a prefix for its kind and FIX's own identifier: `fix_field:55` for Symbol, `fix_message:14` for NewOrderSingle, `fix_code_set:54`, `fix_code:54001`, `fix_component:1003`, `fix_group:1012`. Datatypes, categories and sections have no number in FIX, so their name stands in: `fix_datatype:Price`, `fix_category:Allocation`, `fix_section:PreTrade`. The prefix matters because FIX numbers each kind on its own, and 159 message numbers are also field tags.

Each key is a snake_case slot whose `aliases` give the attribute FIX writes, such as `msg_type` for `msgType`. Values keep FIX's form: tags and extension packs are numbers, and codes and MsgTypes are strings. Four things differ from the file:

- A field's `type` names a datatype or a code set. The record splits it into `field_datatype` and `field_code_set`, so each reference has one range, as Orchestra 1.1 does.
- A message lists its fields, components and groups inside a structure element. Components and groups list theirs directly. All three records list them in `fix_members`, in FIX's order.
- The FIXML annotation becomes `fixml_not_required` on an element, or `fixml_inlined` on a member.
- The edition's metadata, from the file's Dublin Core elements, sits in `repository.yaml` under `metadata_` keys.

A member with no `presence` is optional, as Orchestra 1.0 defines.

## What the catalogue leaves out

The file carries FIX's descriptions of its elements in 29,430 documentation elements. Neither the catalogue nor anything generated from it holds them, and every title and description in the schema, the docs and the bundle is this project's own. [NOTICE](../NOTICE) gives the reasons, and `tests/test_own_words.py` checks both.

Nothing comes from fixtrading.org. The earlier schema described the online specification's chapters: business areas, footnotes, page layouts, committees and the like. Those pages are under a licence that allows no adapted copy, and the Orchestra file states what they said about messages and fields, so that part is gone.

## Rules beside the schema

`tests/fix_rules.py` checks what the data keeps and no JSON Schema can state:

- each identifier names one record, and each reference names a record that exists;
- no two records of a kind share a name, no two messages share a MsgType, and no two codes of a set share a value or a name;
- an extension pack comes with its version, and each code set, code, field, component, group and message states the version that added it;
- each message starts with the standard header and ends with the standard trailer;
- a raw-data field names the Length field that gives its length, and no other field names one;
- the field that counts a group's repeats is a NumInGroup, or takes a code set of NumInGroup values;
- a code set's number is the tag of a field that takes it, and some field takes every code set;
- a code of a char, int or Boolean code set has a value of that datatype;
- a category in a section groups messages, a message's category is in a section, and a category of fields holds no message, component or group;
- a field gives a short name in a base category only when it names that category.

FIX Latest breaks two of these rules, and `tests/upstream_departures.yaml` names both:

- the MsgType code BQ states no `added`;
- the raw-data field EncodedMDEntryStatusText names no length field.

## Mappings

Each class maps to Orchestra 1.0's type for it, under `fixr:`, the namespace the file uses, and to its class in [lmodel/fix-orchestra](https://github.com/lmodel/fix-orchestra)'s Orchestra 1.0 module. Each slot maps to the attribute it holds. `tests/test_mappings.py` holds the `fixr:` names to Orchestra 1.0's schema. The `fix_orchestra:` names wait for fix-orchestra's first release, whose copy then joins `tests/neighbours/`.

There is no SSSOM set. The six the earlier schema carried were a matching tool's guesses, and most named classes that no longer exist. FIX's own datatype mappings, to XML Schema types, sit on each datatype's record under `mapped_datatypes`.

## Keeping current

`upstream-watch.yaml` asks GitHub each week whether a newer commit changed the file. When one has, its issue names the new extension pack and the commit, and `just refresh-fix-latest <commit>` copies it and rebuilds the catalogue. `just gen-project`, `just gen-doc`, `just lokf-adapt` and the tests then show what changed.
