export type FixElementId = string;
export type FixSectionId = string;
export type FixCategoryId = string;
export type FixDatatypeId = string;
export type FixCodeSetId = string;
export type FixCodeId = string;
export type FixFieldId = string;
export type FixComponentId = string;
export type FixGroupId = string;
export type FixMessageId = string;
/**
* Whether a message, component or group must carry a member, in the terms Orchestra 1.0 defines.
*/
export enum FixPresence {
    
    /** The member may be left out. */
    Optional = "optional",
    /** The member must be there. */
    Required = "required",
    /** The member must be left out. */
    Forbidden = "forbidden",
    /** A receiver disregards the member if it is there. */
    Ignored = "ignored",
    /** The member always takes one fixed value. */
    Constant = "constant",
};
/**
* Whether a category groups messages or fields.
*/
export enum FixCategoryKind {
    
    /** The category groups messages and their components. */
    Messages = "Message",
    /** The category groups fields. */
    Fields = "Field",
};
/**
* Which shared FIXML schema file a category's own FIXML schema file brings in.
*/
export enum FixIncludeFile {
    
    /** The file that defines the shared components. */
    Components = "components",
    /** The file that defines the fields. */
    Fields = "fields",
};


/**
 * When FIX added, last changed and deprecated an element, by version and extension pack.
 */
export interface FixPedigreeMixin {
    /** The FIX version that added the element. */
    added_in?: string,
    /** The extension pack that added the element. */
    added_in_ep?: number,
    /** The FIX version that last changed the element. */
    updated_in?: string,
    /** The extension pack that last changed the element. */
    updated_in_ep?: number,
    /** The FIX version that deprecated the element. */
    deprecated_in?: string,
    /** The extension pack that deprecated the element. */
    deprecated_in_ep?: number,
}


/**
 * An element of FIX Latest with an identifier and a name of its own.
 */
export interface FixElement extends FixPedigreeMixin {
    /** The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation. */
    id: string,
    /** The element's name in FIX, such as NewOrderSingle or Symbol. */
    name: string,
}


/**
 * One of the five parts FIX divides its messages into by business area, such as PreTrade.
 */
export interface FixSection extends FixElement {
    /** The FIXML schema file that holds the section's or category's elements, by its file name. */
    fixml_file_name?: string,
    /** True when the element is left out of FIXML, FIX's XML encoding. */
    fixml_not_required?: boolean,
    /** Where the section comes in FIX's own order of sections, counting from 0. */
    section_order?: number,
}


/**
 * A group of messages within a section. Three categories belong to no section, and hold the shared components and the fields instead.
 */
export interface FixCategory extends FixElement {
    /** The FIXML schema file that holds the section's or category's elements, by its file name. */
    fixml_file_name?: string,
    /** The section a category belongs to. */
    in_section?: FixSectionId,
    /** True when the element is left out of FIXML, FIX's XML encoding. */
    fixml_not_required?: boolean,
    /** Whether the category groups messages or fields. */
    category_kind?: string,
    /** The shared FIXML schema file that the category's own FIXML schema file brings in. */
    include_file?: string,
}


/**
 * A kind of value a field holds, such as int, Price or UTCTimestamp, with the XML Schema types it maps to.
 */
export interface FixDatatype extends FixElement {
    /** The datatype this one narrows. */
    base_type?: FixDatatypeId,
    /** The types of other standards that FIX gives as this datatype's form. */
    mapped_datatypes?: FixMappedDatatype[],
}


/**
 * The type of another standard that a FIX datatype takes, such as xs:decimal in XML Schema.
 */
export interface FixMappedDatatype {
    /** The standard the type belongs to, such as XML. */
    mapped_standard: string,
    /** The standard's type, such as xs:decimal. */
    mapped_base?: string,
    /** True when the type is one the standard defines itself. */
    mapped_builtin?: boolean,
    /** The smallest value the type allows, as FIX writes it. */
    mapped_min_inclusive?: string,
    /** A regular expression in XML Schema's syntax that a value must match. */
    mapped_pattern?: string,
}


/**
 * A list of the values a field may take, each a code with a name, such as the sides of an order.
 */
export interface FixCodeSet extends FixElement {
    /** The datatype of the codes' values. */
    code_set_datatype: FixDatatypeId,
    /** The codes of the set, in FIX's order. */
    fix_codes?: FixCode[],
}


/**
 * One value of a code set, with its name, such as 1 for Buy.
 */
export interface FixCode extends FixElement {
    /** The value as it travels on the wire. */
    code_value: string,
    /** Where the code comes when FIX lists the set. */
    sort_order?: number,
    /** A label that groups some codes of a large set, such as one asset class. */
    code_group?: string,
}


/**
 * A field of FIX, known by its tag number, such as 55 for Symbol, with the datatype or code set of its values.
 */
export interface FixField extends FixElement {
    /** The shorter name FIXML uses for the element's tag. */
    abbr_name?: string,
    /** True when the element is left out of FIXML, FIX's XML encoding. */
    fixml_not_required?: boolean,
    /** The datatype of the field's values, when no code set lists them. */
    field_datatype?: FixDatatypeId,
    /** The code set that lists the field's values. */
    field_code_set?: FixCodeSetId,
    /** A datatype whose values the field also takes, beside those of its code set, such as a range of numbers kept for private use. */
    union_datatype?: FixDatatypeId,
    /** The field that gives this field's length in bytes. */
    length_field?: FixFieldId,
    /** The field whose value says how to read this field's value. */
    discriminator_field?: FixFieldId,
    /** The category whose FIXML element carries the field, under the short name in base_category_abbr_name. */
    base_category?: FixCategoryId,
    /** The field's short name within its base category's FIXML element. */
    base_category_abbr_name?: string,
}


/**
 * One field, component or group in a message, component or group, and whether it must be there.
 */
export interface FixMember extends FixPedigreeMixin {
    /** The field this member is. */
    member_field?: FixFieldId,
    /** The component this member is. */
    member_component?: FixComponentId,
    /** The repeating group this member is. */
    member_group?: FixGroupId,
    /** Whether the member must be there. A member that states none is optional. */
    presence?: string,
    /** True when FIXML writes the component's fields directly in the enclosing element rather than in an element of its own. */
    fixml_inlined?: boolean,
}


/**
 * A named block of fields, components and groups that messages share, such as Instrument.
 */
export interface FixComponent extends FixElement {
    /** The shorter name FIXML uses for the element's tag. */
    abbr_name?: string,
    /** The category a message, component or group belongs to. */
    in_category: FixCategoryId,
    /** The fields, components and groups the element holds, in the order FIX lists them. */
    fix_members?: FixMember[],
    /** True when the element is left out of FIXML, FIX's XML encoding. */
    fixml_not_required?: boolean,
}


/**
 * A block of members that repeats in a message, with the field that counts the repeats.
 */
export interface FixGroup extends FixElement {
    /** The shorter name FIXML uses for the element's tag. */
    abbr_name?: string,
    /** The category a message, component or group belongs to. */
    in_category: FixCategoryId,
    /** The fields, components and groups the element holds, in the order FIX lists them. */
    fix_members: FixMember[],
    /** The field that states how many times the group repeats. */
    num_in_group: FixNumInGroup,
}


/**
 * The field that counts a group's repeats, as the group names it.
 */
export interface FixNumInGroup extends FixPedigreeMixin {
    /** The field that holds the count. */
    count_field: FixFieldId,
}


/**
 * A FIX message, known by its MsgType, such as D for NewOrderSingle, with its members in order.
 */
export interface FixMessage extends FixElement {
    /** The shorter name FIXML uses for the element's tag. */
    abbr_name?: string,
    /** The category a message, component or group belongs to. */
    in_category: FixCategoryId,
    /** The fields, components and groups the element holds, in the order FIX lists them. */
    fix_members: FixMember[],
    /** True when the element is left out of FIXML, FIX's XML encoding. */
    fixml_not_required?: boolean,
    /** The value of field 35 that marks a message of this kind. */
    msg_type: string,
}


/**
 * One file of the catalogue: the edition it renders, with some kinds of FIX Latest's elements.
 */
export interface FixRepository {
    /** The name FIX gives the repository, FIX.Latest. */
    repository_name: string,
    /** The extension pack the repository stands at, such as FIX.Latest_EP312. */
    repository_version: string,
    /** The title the repository's metadata gives. */
    metadata_title?: string,
    /** The metadata's one-line statement of which extension pack the file holds. */
    metadata_description?: string,
    /** Who made the repository, as its metadata states. */
    metadata_creator?: string,
    /** Who published the repository, as its metadata states. */
    metadata_publisher?: string,
    /** The rights line in the repository's metadata, word for word. */
    metadata_rights?: string,
    /** The media type of the repository file. */
    metadata_format?: string,
    /** The Orchestra version the repository file follows. */
    metadata_conforms_to?: string,
    /** The date the repository file was made. */
    metadata_created?: string,
    /** The tool or source the metadata names for the file. */
    metadata_source?: string,
    /** The sections, in FIX's order. */
    fix_sections?: FixSection[],
    /** The categories, in FIX's order. */
    fix_categories?: FixCategory[],
    /** The datatypes, in FIX's order. */
    fix_datatypes?: FixDatatype[],
    /** The code sets, in FIX's order. */
    fix_code_sets?: FixCodeSet[],
    /** The fields, in FIX's order. */
    fix_fields?: FixField[],
    /** The components, in FIX's order. */
    fix_components?: FixComponent[],
    /** The repeating groups, in FIX's order. */
    fix_groups?: FixGroup[],
    /** The messages, in FIX's order. */
    fix_messages?: FixMessage[],
}



