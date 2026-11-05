"""The rules FIX Latest's data keeps that no generated schema can state.

The JSON Schema checks each record on its own. These rules check what a record says about
the others. A reference names a record that exists, a name or a value is unique where FIX
keeps it unique, and a field, a code set and a group fit together. FIX Latest's own data
keeps each rule, but for the departures tests/upstream_departures.yaml lists.

``rule_errors`` returns one finding per broken rule as (pointer, rule, id, message). The
pointer is the JSON Pointer of the value at fault, the rule is the function's name and the
id is the record's. A document that holds only some kinds of element is checked against
what it holds: a reference to a kind it does not hold is left alone, unless the document is
the whole edition.
"""

# Each reference slot and the list its target sits in.
REFERENCES = {
    "in_section": "fix_sections",
    "in_category": "fix_categories",
    "base_category": "fix_categories",
    "base_type": "fix_datatypes",
    "code_set_datatype": "fix_datatypes",
    "field_datatype": "fix_datatypes",
    "union_datatype": "fix_datatypes",
    "field_code_set": "fix_code_sets",
    "length_field": "fix_fields",
    "discriminator_field": "fix_fields",
    "member_field": "fix_fields",
    "count_field": "fix_fields",
    "member_component": "fix_components",
    "member_group": "fix_groups",
}

LISTS = (
    "fix_sections",
    "fix_categories",
    "fix_datatypes",
    "fix_code_sets",
    "fix_fields",
    "fix_components",
    "fix_groups",
    "fix_messages",
)

# The kinds whose every record states the version that added it.
DATED = ("fix_code_sets", "fix_fields", "fix_components", "fix_groups", "fix_messages")


def _walk(document):
    """Every record and nested value of the document, with its pointer and the id of the
    record it belongs to."""
    for key in LISTS:
        for i, record in enumerate(document.get(key) or ()):
            base = f"/{key}/{i}"
            yield base, record, record.get("id")
            for j, code in enumerate(record.get("fix_codes") or ()):
                yield f"{base}/fix_codes/{j}", code, code.get("id")
            for j, mapped in enumerate(record.get("mapped_datatypes") or ()):
                yield f"{base}/mapped_datatypes/{j}", mapped, record.get("id")
            for j, member in enumerate(record.get("fix_members") or ()):
                yield f"{base}/fix_members/{j}", member, record.get("id")
            if "num_in_group" in record:
                yield f"{base}/num_in_group", record["num_in_group"], record.get("id")


def _index(document, key):
    return {record["id"]: record for record in document.get(key) or ()}


def unique_ids(document, whole):
    """No identifier names two records. The second record that takes one is at fault."""
    seen = set()
    for pointer, value, owner in _walk(document):
        identifier = value.get("id")
        if identifier is None:
            continue
        if identifier in seen:
            yield f"{pointer}/id", owner, f"{identifier} names an earlier record"
        seen.add(identifier)


def references_resolve(document, whole):
    held = {key: _index(document, key) for key in LISTS if key in document}
    for pointer, value, owner in _walk(document):
        for slot, key in REFERENCES.items():
            target = value.get(slot)
            if target is None:
                continue
            if key not in held:
                if whole:
                    yield f"{pointer}/{slot}", owner, f"no {key} to find {target} in"
                continue
            if target not in held[key]:
                yield f"{pointer}/{slot}", owner, f"{target} names no record"


def _repeats(items, key):
    """The index of each item whose value of key an earlier item already has."""
    seen = set()
    for i, item in enumerate(items):
        if item[key] in seen:
            yield i, item
        seen.add(item[key])


def names_unique(document, whole):
    """No two records of a kind share a name, and no two messages a MsgType. The later
    record is at fault."""
    for key in LISTS:
        for i, record in _repeats(document.get(key) or (), "name"):
            yield f"/{key}/{i}/name", record["id"], f"{record['name']} is taken"
    for i, message in _repeats(document.get("fix_messages") or (), "msg_type"):
        yield (
            f"/fix_messages/{i}/msg_type",
            message["id"],
            f"MsgType {message['msg_type']} is taken",
        )


def codes_unique_in_their_set(document, whole):
    """No two codes of a set share a value or a name. The later code is at fault."""
    for i, code_set in enumerate(document.get("fix_code_sets") or ()):
        for key in ("code_value", "name"):
            for j, code in _repeats(code_set.get("fix_codes") or (), key):
                yield (
                    f"/fix_code_sets/{i}/fix_codes/{j}/{key}",
                    code["id"],
                    f"{code[key]} is taken in {code_set['name']}",
                )


def extension_pack_with_its_version(document, whole):
    """An extension pack number comes with the version it belongs to."""
    for pointer, value, owner in _walk(document):
        for change in ("added", "updated", "deprecated"):
            if f"{change}_in_ep" in value and f"{change}_in" not in value:
                yield (
                    f"{pointer}/{change}_in_ep",
                    owner,
                    f"{change}_in_ep without {change}_in",
                )


def dated(document, whole):
    """Each code set, code, field, component, group and message states when it was added."""
    for key in DATED:
        for i, record in enumerate(document.get(key) or ()):
            if "added_in" not in record:
                yield (
                    f"/{key}/{i}",
                    record["id"],
                    f"{record['name']} states no added_in",
                )
            for j, code in enumerate(record.get("fix_codes") or ()):
                if "added_in" not in code:
                    yield (
                        f"/{key}/{i}/fix_codes/{j}",
                        code["id"],
                        f"{code['name']} states no added_in",
                    )


def messages_open_and_close_with_header_and_trailer(document, whole):
    if "fix_components" not in document:
        return
    names = {c["id"]: c["name"] for c in document["fix_components"]}
    for i, message in enumerate(document.get("fix_messages") or ()):
        members = message["fix_members"]
        first = names.get(members[0].get("member_component"))
        last = names.get(members[-1].get("member_component"))
        if first != "StandardHeader":
            yield f"/fix_messages/{i}/fix_members/0", message["id"], "no header first"
        if last != "StandardTrailer":
            yield (
                f"/fix_messages/{i}/fix_members/{len(members) - 1}",
                message["id"],
                "no trailer last",
            )


def lengths_pair_with_data(document, whole):
    """A field of raw data names the field that gives its length, whose datatype is
    Length, and only such a field names one."""
    fields = _index(document, "fix_fields")
    raw = ("fix_datatype:data", "fix_datatype:XMLData")
    for i, field in enumerate(document.get("fix_fields") or ()):
        if "length_field" in field:
            if field.get("field_datatype") not in raw:
                yield (
                    f"/fix_fields/{i}/length_field",
                    field["id"],
                    "a length for a field that is not raw data",
                )
            target = fields.get(field["length_field"])
            if target and target.get("field_datatype") != "fix_datatype:Length":
                yield (
                    f"/fix_fields/{i}/length_field",
                    field["id"],
                    f"{target['name']} is not of datatype Length",
                )
        elif field.get("field_datatype") == "fix_datatype:data":
            yield f"/fix_fields/{i}", field["id"], f"{field['name']} names no length"


def counts_are_counts(document, whole):
    """The field that counts a group's repeats is a NumInGroup, or takes a code set of
    NumInGroup values."""
    fields = _index(document, "fix_fields")
    code_sets = _index(document, "fix_code_sets")
    for i, group in enumerate(document.get("fix_groups") or ()):
        field = fields.get(group["num_in_group"]["count_field"])
        if field is None:
            continue
        datatype = field.get("field_datatype")
        if datatype is None:
            code_set = code_sets.get(field["field_code_set"])
            datatype = code_set and code_set["code_set_datatype"]
        if datatype not in ("fix_datatype:NumInGroup", None):
            yield (
                f"/fix_groups/{i}/num_in_group/count_field",
                group["id"],
                f"{field['name']} is not a count",
            )


def code_sets_take_their_fields_tag(document, whole):
    """A code set's number is the tag of a field that takes it, and in the whole edition
    some field takes every code set."""
    if "fix_fields" not in document:
        return
    users = {}
    for field in document["fix_fields"]:
        if "field_code_set" in field:
            users.setdefault(field["field_code_set"], set()).add(field["id"])
    for i, code_set in enumerate(document.get("fix_code_sets") or ()):
        number = code_set["id"].partition(":")[2]
        found = users.get(code_set["id"], set())
        if not found:
            if whole:
                yield f"/fix_code_sets/{i}", code_set["id"], "no field takes it"
        elif f"fix_field:{number}" not in found:
            yield (
                f"/fix_code_sets/{i}/id",
                code_set["id"],
                "no field of its number takes it",
            )


def msg_types_are_the_codes_of_msg_type(document, whole):
    """Each message's MsgType is a code of the MsgType code set, and in the whole edition
    each code of that set names a message."""
    code_sets = _index(document, "fix_code_sets")
    code_set = code_sets.get("fix_code_set:35")
    if code_set is None:
        return
    codes = {code["code_value"] for code in code_set.get("fix_codes") or ()}
    msg_types = set()
    for i, message in enumerate(document.get("fix_messages") or ()):
        msg_types.add(message["msg_type"])
        if message["msg_type"] not in codes:
            yield (
                f"/fix_messages/{i}/msg_type",
                message["id"],
                f"MsgType {message['msg_type']} is no code of MsgTypeCodeSet",
            )
    if whole:
        i = next(
            i for i, found in enumerate(document["fix_code_sets"]) if found is code_set
        )
        for j, code in enumerate(code_set.get("fix_codes") or ()):
            if code["code_value"] not in msg_types:
                yield (
                    f"/fix_code_sets/{i}/fix_codes/{j}/code_value",
                    code["id"],
                    f"MsgType {code['code_value']} names no message",
                )


def code_values_fit_their_datatype(document, whole):
    for i, code_set in enumerate(document.get("fix_code_sets") or ()):
        datatype = code_set["code_set_datatype"]
        for j, code in enumerate(code_set.get("fix_codes") or ()):
            value = code["code_value"]
            wrong = (
                (datatype == "fix_datatype:char" and len(value) != 1)
                or (datatype == "fix_datatype:int" and not value.lstrip("-").isdigit())
                or (datatype == "fix_datatype:Boolean" and value not in ("Y", "N"))
            )
            if wrong:
                yield (
                    f"/fix_code_sets/{i}/fix_codes/{j}/code_value",
                    code["id"],
                    f"{value} is not a {datatype.partition(':')[2]}",
                )


def categories_fit_their_kind(document, whole):
    """A category of messages sits in a section, or holds only shared components; a
    category of fields holds no message, component or group."""
    categories = _index(document, "fix_categories")
    for i, category in enumerate(document.get("fix_categories") or ()):
        if "in_section" in category and category.get("category_kind") != "Message":
            yield (
                f"/fix_categories/{i}/in_section",
                category["id"],
                "fields in a section",
            )
    for key in ("fix_messages", "fix_components", "fix_groups"):
        for i, record in enumerate(document.get(key) or ()):
            category = categories.get(record["in_category"])
            if category is None:
                continue
            if category.get("category_kind") != "Message":
                yield f"/{key}/{i}/in_category", record["id"], "a category of fields"
            elif key == "fix_messages" and "in_section" not in category:
                yield (
                    f"/{key}/{i}/in_category",
                    record["id"],
                    "a category in no section",
                )


def base_category_names_come_together(document, whole):
    for i, field in enumerate(document.get("fix_fields") or ()):
        if "base_category_abbr_name" in field and "base_category" not in field:
            yield (
                f"/fix_fields/{i}/base_category_abbr_name",
                field["id"],
                "a short name in no base category",
            )


RULES = (
    unique_ids,
    references_resolve,
    names_unique,
    codes_unique_in_their_set,
    extension_pack_with_its_version,
    dated,
    messages_open_and_close_with_header_and_trailer,
    lengths_pair_with_data,
    counts_are_counts,
    code_sets_take_their_fields_tag,
    msg_types_are_the_codes_of_msg_type,
    code_values_fit_their_datatype,
    categories_fit_their_kind,
    base_category_names_come_together,
)


def rule_errors(document, whole=False):
    """Each finding of each rule, as (pointer, rule, id, message)."""
    return [
        (pointer, rule.__name__, owner, message)
        for rule in RULES
        for pointer, owner, message in rule(document, whole)
    ]
