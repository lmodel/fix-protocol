# Explanations

* [Why the schema holds FIX as records](elements-as-records.md) - Why the schema models each kind of FIX Latest element as a class and every element as a record, rather than describing the online specification's chapters as the earlier schema did.
* [What the records leave out](what-the-records-leave-out.md) - Why the catalogue holds none of the 29,430 documentation elements of FIX's file, and how a test keeps FIX's descriptive text out of every file the project writes.
* [Rules beside the schema](rules-and-departures.md) - What `tests/fix_rules.py` checks that no JSON Schema can state, such as that each reference resolves and each message opens with the standard header, and where FIX Latest breaks a rule.
* [Mappings](mappings.md) - How the schema maps to Orchestra 1.0's names under `fixr:` and to lmodel/fix-orchestra's classes, why it keeps no SSSOM set, and which test holds each mapping.
