-- # Class: FixRepository Description: One file of the catalogue: the edition it renders and one or more kinds of FIX Latest's elements.
--     * Slot: id
--     * Slot: repository_name Description: The name FIX gives the repository, FIX.Latest.
--     * Slot: repository_version Description: The extension pack the repository stands at, such as FIX.Latest_EP312.
--     * Slot: metadata_title Description: The title the repository's metadata gives.
--     * Slot: metadata_description Description: The metadata's one-line statement of which extension pack the file holds.
--     * Slot: metadata_creator Description: Who made the repository, by its metadata.
--     * Slot: metadata_publisher Description: Who published the repository, by its metadata.
--     * Slot: metadata_rights Description: The rights line in the repository's metadata, word for word.
--     * Slot: metadata_format Description: The media type of the repository file.
--     * Slot: metadata_conforms_to Description: The Orchestra version the repository file follows.
--     * Slot: metadata_created Description: The date the repository file was made.
--     * Slot: metadata_source Description: The tool or source the metadata names for the file.
-- # Class: FixPedigreeMixin Description: When FIX added, last changed and deprecated an element, by version and extension pack.
--     * Slot: id
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
-- # Abstract Class: FixElement Description: An element of FIX Latest with an identifier and a name of its own.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
-- # Class: FixSection Description: One of the five parts of FIX by business area, such as pre-trade or post-trade.
--     * Slot: fixml_file_name Description: The name of the FIXML schema file that holds the section's or category's elements.
--     * Slot: fixml_not_required Description: True when the element is left out of FIXML, FIX's XML encoding.
--     * Slot: section_order Description: Where the section comes in FIX's own order of sections, counting from 0.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixRepository_id Description: Autocreated FK slot
-- # Class: FixCategory Description: A group of messages within a section, or one of the groups that hold the shared components and the fields.
--     * Slot: fixml_file_name Description: The name of the FIXML schema file that holds the section's or category's elements.
--     * Slot: in_section Description: The section a category belongs to.
--     * Slot: fixml_not_required Description: True when the element is left out of FIXML, FIX's XML encoding.
--     * Slot: category_kind Description: Whether the category groups messages or fields.
--     * Slot: include_file Description: The shared FIXML schema file that the category's own FIXML schema file brings in.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixRepository_id Description: Autocreated FK slot
-- # Class: FixDatatype Description: A kind of value a field holds, such as int, Price or UTCTimestamp, with the XML Schema types it maps to.
--     * Slot: base_type Description: The datatype this one narrows.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixRepository_id Description: Autocreated FK slot
-- # Class: FixMappedDatatype Description: The type of another standard that a FIX datatype takes, such as xs:decimal in XML Schema.
--     * Slot: id
--     * Slot: mapped_standard Description: The standard the type belongs to, such as XML.
--     * Slot: mapped_base Description: The standard's type, such as xs:decimal.
--     * Slot: mapped_builtin Description: True when the type is one the standard defines itself.
--     * Slot: mapped_min_inclusive Description: The smallest value the type allows, as FIX writes it.
--     * Slot: mapped_pattern Description: A regular expression in XML Schema's syntax that a value must match.
--     * Slot: FixDatatype_id Description: Autocreated FK slot
-- # Class: FixCodeSet Description: A list of the values a field may take, each a code with a name, such as the sides of an order.
--     * Slot: code_set_datatype Description: The datatype of the codes' values.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixRepository_id Description: Autocreated FK slot
-- # Class: FixCode Description: One value of a code set, with its name, such as 1 for Buy.
--     * Slot: code_value Description: The value as it travels on the wire.
--     * Slot: sort_order Description: Where the code comes when FIX lists the set.
--     * Slot: code_group Description: A label that groups some codes of a large set, such as one asset class.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixCodeSet_id Description: Autocreated FK slot
-- # Class: FixField Description: A field of FIX, known by its tag number, such as 55 for Symbol, with the datatype or code set of its values.
--     * Slot: abbr_name Description: The shorter name FIXML uses for the element's tag.
--     * Slot: fixml_not_required Description: True when the element is left out of FIXML, FIX's XML encoding.
--     * Slot: field_datatype Description: The datatype of the field's values, when no code set lists them.
--     * Slot: field_code_set Description: The code set that lists the field's values.
--     * Slot: union_datatype Description: A datatype whose values the field also takes, beside those of its code set, such as a range of numbers kept for private use.
--     * Slot: length_field Description: The field that gives this field's length in bytes.
--     * Slot: discriminator_field Description: The field whose value says how to read this field's value.
--     * Slot: base_category Description: The category whose FIXML element carries the field under the short name base_category_abbr_name gives.
--     * Slot: base_category_abbr_name Description: The field's short name within its base category's FIXML element.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixRepository_id Description: Autocreated FK slot
-- # Class: FixMember Description: One field, component or group in a message, component or group, and whether it must be there.
--     * Slot: id
--     * Slot: member_field Description: The field this member is.
--     * Slot: member_component Description: The component this member is.
--     * Slot: member_group Description: The repeating group this member is.
--     * Slot: presence Description: Whether the member must be there. A member that states none is optional.
--     * Slot: fixml_inlined Description: True when FIXML writes the component's fields directly in the enclosing element rather than in an element of its own.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixComponent_id Description: Autocreated FK slot
--     * Slot: FixGroup_id Description: Autocreated FK slot
--     * Slot: FixMessage_id Description: Autocreated FK slot
-- # Class: FixComponent Description: A named block of fields, components and groups that messages share, such as Instrument.
--     * Slot: abbr_name Description: The shorter name FIXML uses for the element's tag.
--     * Slot: in_category Description: The category a message, component or group belongs to.
--     * Slot: fixml_not_required Description: True when the element is left out of FIXML, FIX's XML encoding.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixRepository_id Description: Autocreated FK slot
-- # Class: FixGroup Description: A block of members that repeats in a message, with the field that counts the repeats.
--     * Slot: abbr_name Description: The shorter name FIXML uses for the element's tag.
--     * Slot: in_category Description: The category a message, component or group belongs to.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixRepository_id Description: Autocreated FK slot
--     * Slot: num_in_group_id Description: The field that states how many times the group repeats.
-- # Class: FixNumInGroup Description: The field that counts a group's repeats, as the group names it.
--     * Slot: id
--     * Slot: count_field Description: The field that holds the count.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
-- # Class: FixMessage Description: A FIX message, known by its MsgType, such as D for NewOrderSingle, with its members in order.
--     * Slot: abbr_name Description: The shorter name FIXML uses for the element's tag.
--     * Slot: in_category Description: The category a message, component or group belongs to.
--     * Slot: fixml_not_required Description: True when the element is left out of FIXML, FIX's XML encoding.
--     * Slot: msg_type Description: The value of field 35 that marks a message of this kind.
--     * Slot: id Description: The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.
--     * Slot: name Description: The element's name in FIX, such as NewOrderSingle or Symbol.
--     * Slot: added_in Description: The FIX version that added the element.
--     * Slot: added_in_ep Description: The extension pack that added the element.
--     * Slot: updated_in Description: The FIX version that last changed the element.
--     * Slot: updated_in_ep Description: The extension pack that last changed the element.
--     * Slot: deprecated_in Description: The FIX version that deprecated the element.
--     * Slot: deprecated_in_ep Description: The extension pack that deprecated the element.
--     * Slot: FixRepository_id Description: Autocreated FK slot

CREATE TABLE "FixRepository" (
	id INTEGER NOT NULL,
	repository_name TEXT NOT NULL,
	repository_version TEXT NOT NULL,
	metadata_title TEXT,
	metadata_description TEXT,
	metadata_creator TEXT,
	metadata_publisher TEXT,
	metadata_rights TEXT,
	metadata_format TEXT,
	metadata_conforms_to TEXT,
	metadata_created TEXT,
	metadata_source TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_FixRepository_id" ON "FixRepository" (id);

CREATE TABLE "FixPedigreeMixin" (
	id INTEGER NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_FixPedigreeMixin_id" ON "FixPedigreeMixin" (id);

CREATE TABLE "FixElement" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_FixElement_id" ON "FixElement" (id);

CREATE TABLE "FixSection" (
	fixml_file_name TEXT,
	fixml_not_required BOOLEAN,
	section_order INTEGER,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixRepository_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FixRepository_id") REFERENCES "FixRepository" (id)
);
CREATE INDEX "ix_FixSection_id" ON "FixSection" (id);

CREATE TABLE "FixDatatype" (
	base_type TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixRepository_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(base_type) REFERENCES "FixDatatype" (id),
	FOREIGN KEY("FixRepository_id") REFERENCES "FixRepository" (id)
);
CREATE INDEX "ix_FixDatatype_id" ON "FixDatatype" (id);

CREATE TABLE "FixCategory" (
	fixml_file_name TEXT,
	in_section TEXT,
	fixml_not_required BOOLEAN,
	category_kind VARCHAR(7),
	include_file VARCHAR(10),
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixRepository_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(in_section) REFERENCES "FixSection" (id),
	FOREIGN KEY("FixRepository_id") REFERENCES "FixRepository" (id)
);
CREATE INDEX "ix_FixCategory_id" ON "FixCategory" (id);

CREATE TABLE "FixMappedDatatype" (
	id INTEGER NOT NULL,
	mapped_standard TEXT NOT NULL,
	mapped_base TEXT,
	mapped_builtin BOOLEAN,
	mapped_min_inclusive TEXT,
	mapped_pattern TEXT,
	"FixDatatype_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("FixDatatype_id") REFERENCES "FixDatatype" (id)
);
CREATE INDEX "ix_FixMappedDatatype_id" ON "FixMappedDatatype" (id);

CREATE TABLE "FixCodeSet" (
	code_set_datatype TEXT NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixRepository_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(code_set_datatype) REFERENCES "FixDatatype" (id),
	FOREIGN KEY("FixRepository_id") REFERENCES "FixRepository" (id)
);
CREATE INDEX "ix_FixCodeSet_id" ON "FixCodeSet" (id);

CREATE TABLE "FixCode" (
	code_value TEXT NOT NULL,
	sort_order INTEGER,
	code_group TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixCodeSet_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("FixCodeSet_id") REFERENCES "FixCodeSet" (id)
);
CREATE INDEX "ix_FixCode_id" ON "FixCode" (id);

CREATE TABLE "FixField" (
	abbr_name TEXT,
	fixml_not_required BOOLEAN,
	field_datatype TEXT,
	field_code_set TEXT,
	union_datatype TEXT,
	length_field TEXT,
	discriminator_field TEXT,
	base_category TEXT,
	base_category_abbr_name TEXT,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixRepository_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(field_datatype) REFERENCES "FixDatatype" (id),
	FOREIGN KEY(field_code_set) REFERENCES "FixCodeSet" (id),
	FOREIGN KEY(union_datatype) REFERENCES "FixDatatype" (id),
	FOREIGN KEY(length_field) REFERENCES "FixField" (id),
	FOREIGN KEY(discriminator_field) REFERENCES "FixField" (id),
	FOREIGN KEY(base_category) REFERENCES "FixCategory" (id),
	FOREIGN KEY("FixRepository_id") REFERENCES "FixRepository" (id)
);
CREATE INDEX "ix_FixField_id" ON "FixField" (id);

CREATE TABLE "FixComponent" (
	abbr_name TEXT,
	in_category TEXT NOT NULL,
	fixml_not_required BOOLEAN,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixRepository_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(in_category) REFERENCES "FixCategory" (id),
	FOREIGN KEY("FixRepository_id") REFERENCES "FixRepository" (id)
);
CREATE INDEX "ix_FixComponent_id" ON "FixComponent" (id);

CREATE TABLE "FixMessage" (
	abbr_name TEXT,
	in_category TEXT NOT NULL,
	fixml_not_required BOOLEAN,
	msg_type TEXT NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixRepository_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(in_category) REFERENCES "FixCategory" (id),
	FOREIGN KEY("FixRepository_id") REFERENCES "FixRepository" (id)
);
CREATE INDEX "ix_FixMessage_id" ON "FixMessage" (id);

CREATE TABLE "FixNumInGroup" (
	id INTEGER NOT NULL,
	count_field TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(count_field) REFERENCES "FixField" (id)
);
CREATE INDEX "ix_FixNumInGroup_id" ON "FixNumInGroup" (id);

CREATE TABLE "FixGroup" (
	abbr_name TEXT,
	in_category TEXT NOT NULL,
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixRepository_id" INTEGER,
	num_in_group_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(in_category) REFERENCES "FixCategory" (id),
	FOREIGN KEY("FixRepository_id") REFERENCES "FixRepository" (id),
	FOREIGN KEY(num_in_group_id) REFERENCES "FixNumInGroup" (id)
);
CREATE INDEX "ix_FixGroup_id" ON "FixGroup" (id);

CREATE TABLE "FixMember" (
	id INTEGER NOT NULL,
	member_field TEXT,
	member_component TEXT,
	member_group TEXT,
	presence VARCHAR(9),
	fixml_inlined BOOLEAN,
	added_in TEXT,
	added_in_ep INTEGER,
	updated_in TEXT,
	updated_in_ep INTEGER,
	deprecated_in TEXT,
	deprecated_in_ep INTEGER,
	"FixComponent_id" TEXT,
	"FixGroup_id" TEXT,
	"FixMessage_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(member_field) REFERENCES "FixField" (id),
	FOREIGN KEY(member_component) REFERENCES "FixComponent" (id),
	FOREIGN KEY(member_group) REFERENCES "FixGroup" (id),
	FOREIGN KEY("FixComponent_id") REFERENCES "FixComponent" (id),
	FOREIGN KEY("FixGroup_id") REFERENCES "FixGroup" (id),
	FOREIGN KEY("FixMessage_id") REFERENCES "FixMessage" (id)
);
CREATE INDEX "ix_FixMember_id" ON "FixMember" (id);
