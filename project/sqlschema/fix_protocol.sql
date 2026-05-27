-- # Class: FIXIntroduction Description: Container for the structural elements of the FIX Latest Introduction section. Tree root for instance data.
--     * Slot: id
--     * Slot: published_version Description: Version stamp from the document header.
--     * Slot: published_date Description: Publication date of the document.
--     * Slot: publisher Description: Publishing body of the FIX Latest specification.
--     * Slot: preface Description: The Preface text of the specification.
--     * Slot: introduction_text Description: The Introduction prose section.
--     * Slot: utc_leap_seconds_note Description: Prose note on UTC leap-second handling for UTCTimestamp.
--     * Slot: about_fpl_id Description: Information about FIX Protocol Limited.
-- # Class: FIXProtocolLimited Description: The organization that maintains the FIX Protocol specification.
--     * Slot: id
--     * Slot: brand_name Description: Brand name used by the organization.
--     * Slot: legal_name Description: Legal name of the organization.
--     * Slot: website Description: Main website URL of the organization.
--     * Slot: member_firms_url Description: URL listing current FPL Member firms.
--     * Slot: working_groups_url Description: URL listing currently active FPL Working Groups.
--     * Slot: committees_url Description: URL listing Product and Regional Committees.
-- # Class: FIXFamilyStandard Description: A member standard of the FIX Family of Standards.
--     * Slot: id Description: Unique identifier (CURIE or local name) of the element.
--     * Slot: name Description: Display name of the element.
--     * Slot: description Description: Free-text description.
--     * Slot: acronym Description: Short acronym used to refer to the standard.
--     * Slot: layer Description: The layer the standard belongs to.
--     * Slot: version Description: Version of the standard, if applicable.
--     * Slot: session_profile Description: Name of the session profile for session-layer variants.
--     * Slot: encoding_name Description: Named encoding, when layer is ENCODING.
--     * Slot: FIXIntroduction_id Description: Autocreated FK slot
-- # Class: ExtensionPack Description: A unit of change to FIX Latest.
--     * Slot: number Description: Sequential identifier of the Extension Pack.
--     * Slot: title Description: Short descriptive title.
--     * Slot: size Description: Qualitative size indicator (XXS..XXL).
--     * Slot: enhancement_summary Description: Narrative summary of what the EP introduces.
--     * Slot: applies_to_session_layer_only Description: True when the EP applies only to the FIX Session Layer.
--     * Slot: applies_to_fixml_only Description: True when the EP applies only to the FIXML encoding.
--     * Slot: FIXIntroduction_id Description: Autocreated FK slot
-- # Class: FIXDatatype Description: A FIX Protocol datatype.
--     * Slot: datatype_name Description: Canonical FIX datatype name.
--     * Slot: definition Description: Prose definition of the datatype.
--     * Slot: value_space_notes Description: Additional value-space constraints.
--     * Slot: deprecated_for_new_designs Description: True for datatypes not permitted in new designs.
--     * Slot: external_code_set Description: Reference standard for datatypes backed by an external code set.
--     * Slot: radix Description: Numeric radix for scaled value-space datatypes.
--     * Slot: repertoire Description: Character repertoire for character/string datatypes.
--     * Slot: index_lower_bound Description: Inclusive lower bound of a bounded-array index.
--     * Slot: index_upper_bound Description: Inclusive upper bound of a bounded-array index.
--     * Slot: minimum_value Description: Inclusive lower bound on the integer value space.
--     * Slot: maximum_value Description: Inclusive upper bound on the integer value space.
--     * Slot: FIXIntroduction_id Description: Autocreated FK slot
-- # Class: BusinessArea Description: A top-level business area of the FIX Latest specification.
--     * Slot: area Description: Identity of the business area.
--     * Slot: title Description: Display title of the area.
--     * Slot: description Description: Description of the area.
--     * Slot: FIXIntroduction_id Description: Autocreated FK slot
-- # Class: MessageCategory Description: A message category within a business area.
--     * Slot: category Description: Identity of the message category.
--     * Slot: title Description: Display title of the category.
--     * Slot: description Description: Description of the category.
--     * Slot: business_area Description: Business area the element belongs to.
--     * Slot: BusinessArea_area Description: Autocreated FK slot
-- # Class: Field Description: A FIX field — a uniquely tagged data element with a FIX datatype.
--     * Slot: tag Description: Numeric tag of the field.
--     * Slot: field_name Description: PascalCase name of the field.
--     * Slot: datatype Description: FIX datatype of the field.
--     * Slot: description Description: Description of the field's purpose.
--     * Slot: requirement Description: Required-status of the field within the enclosing context.
--     * Slot: is_user_defined Description: True when the field is a User Defined Field.
--     * Slot: Component_component_name Description: Autocreated FK slot
--     * Slot: GlobalComponent_component_name Description: Autocreated FK slot
--     * Slot: CommonComponent_component_name Description: Autocreated FK slot
--     * Slot: SpecificComponent_component_name Description: Autocreated FK slot
--     * Slot: Message_msg_type Description: Autocreated FK slot
-- # Abstract Class: Component Description: A FIX component — a named set of related fields.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: description Description: Description of the component.
--     * Slot: scope Description: Sharing scope of the component.
--     * Slot: is_repeating_group Description: True when the component is a repeating group.
-- # Class: GlobalComponent Description: A component shared by messages of two or more business areas.
--     * Slot: component_group Description: Thematic group under which the component is presented.
--     * Slot: applies_to_instrument Description: Applicable at the Instrument level.
--     * Slot: applies_to_leg Description: Applicable at the InstrumentLeg level.
--     * Slot: applies_to_underlying Description: Applicable at the UnderlyingInstrument level.
--     * Slot: gc_id Description: Numeric component identifier extracted from the FIX Latest "Global Components" page anchor ID (e.g. "comp1057-1" → 1057). Stable across Extension Packs and shared with the FIX Orchestra repository.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: description Description: Description of the component.
--     * Slot: scope Description: Sharing scope of the component.
--     * Slot: is_repeating_group Description: True when the component is a repeating group.
--     * Slot: FIXIntroduction_id Description: Autocreated FK slot
-- # Class: CommonComponent Description: A component used only by messages within a single business area.
--     * Slot: business_area Description: Business area the element belongs to.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: description Description: Description of the component.
--     * Slot: scope Description: Sharing scope of the component.
--     * Slot: is_repeating_group Description: True when the component is a repeating group.
-- # Class: SpecificComponent Description: A component used only by messages within a single category.
--     * Slot: business_area Description: Business area the element belongs to.
--     * Slot: category Description: Message category.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: description Description: Description of the component.
--     * Slot: scope Description: Sharing scope of the component.
--     * Slot: is_repeating_group Description: True when the component is a repeating group.
-- # Class: Message Description: A FIX application message.
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: description Description: Description of the message's purpose.
--     * Slot: category Description: Message category.
--     * Slot: MessageCategory_category Description: Autocreated FK slot
-- # Class: UDFTagRange Description: A reserved range of tag numbers for User Defined Fields.
--     * Slot: range_id Description: Identifier of the range.
--     * Slot: low_tag Description: Inclusive lower bound of the range.
--     * Slot: high_tag Description: Upper bound of the tag range. Required for all ``usage`` values except ``GTC_RESERVED`` (which is open-ended, 50000+). Downstream validators should enforce this; the constraint cannot be expressed here because LinkML's ``equals_string`` operator only accepts string-ranged slots and ``usage`` is an enum.
--     * Slot: usage Description: Usage policy assigned to the range.
--     * Slot: description Description: Notes on the range's intended use.
--     * Slot: requires_registration Description: True when tags in the range must be registered.
--     * Slot: FIXIntroduction_id Description: Autocreated FK slot
-- # Class: PreTradeBusinessArea Description: Tree-root container for the Pre-Trade business area of FIX Latest.
--     * Slot: id
--     * Slot: area Description: Identity of the business area.
--     * Slot: title Description: Display title.
--     * Slot: published_version Description: Version stamp from the document header.
--     * Slot: publisher Description: Publishing body of the FIX Latest specification.
--     * Slot: introduction Description: Prose introduction of the chapter.
--     * Slot: diagram_conventions Description: Sentence describing diagram conventions used in the chapter.
--     * Slot: messages_overview_note Description: Intro prose of the area-wide Messages sub-section.
--     * Slot: components_overview_note Description: Intro prose of the area-wide Components sub-section.
-- # Class: PreTradeMessageEntry Description: One row of the area-wide pre-trade messages table.
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: category Description: Message category.
--     * Slot: PreTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: PreTradeComponentEntry Description: One row of the area-wide pre-trade components table.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: repetition Description: REPEATING or NON_REPEATING.
--     * Slot: category Description: Category the component is listed under. Common Components are listed under the synthetic "Common Components" value.
--     * Slot: is_common Description: True when the component is declared as a Common Component.
--     * Slot: footnote_number Description: Footnote indicator on a component-table row.
--     * Slot: PreTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: ComponentTableFootnote Description: A footnote on the area-wide components table.
--     * Slot: footnote_number Description: Footnote indicator on a component-table row.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: introduced_in Description: FIX version or Extension Pack that introduced the component.
--     * Slot: sole_category Description: Single category that actually uses the component.
--     * Slot: text Description: Footnote text.
--     * Slot: PreTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: PreTradeCategorySection Description: A per-category sub-section of the Pre-Trade chapter.
--     * Slot: category Description: Message category.
--     * Slot: title Description: Display title.
--     * Slot: description Description: Free-text description.
--     * Slot: category_components_note Description: Intro prose of a category's Components sub-section.
--     * Slot: PreTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: PreTradeMessageDetail Description: Per-category message description.
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: description Description: Description of the message's purpose and usage.
--     * Slot: layout_url Description: URL of the detailed message- or component-layout.
--     * Slot: PreTradeCategorySection_category Description: Autocreated FK slot
--     * Slot: MessageGroup_group_title Description: Autocreated FK slot
-- # Class: PreTradeComponentDetail Description: Per-category component description.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: repetition Description: REPEATING or NON_REPEATING.
--     * Slot: description Description: Description of the component's purpose.
--     * Slot: layout_url Description: URL of the detailed message- or component-layout.
--     * Slot: PreTradeCategorySection_category Description: Autocreated FK slot
-- # Class: MessageGroup Description: Purpose-grouped sub-section inside a category's Messages section.
--     * Slot: group_title Description: Purpose-group heading inside a category's Messages sub-section.
--     * Slot: description Description: Description of the purpose-group's role within the category.
--     * Slot: PreTradeCategorySection_category Description: Autocreated FK slot
-- # Class: CommonComponentDetail Description: Per-common-component description.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: repetition Description: REPEATING or NON_REPEATING.
--     * Slot: description Description: Description of the common component's purpose.
--     * Slot: layout_url Description: URL of the detailed message- or component-layout.
--     * Slot: PreTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: PreTradeLayoutRow Description: One row of the layout table published in the Pre-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
--     * Slot: id
--     * Slot: pre_layout_kind Description: Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table).
--     * Slot: pre_layout_field_tag Description: FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.
--     * Slot: pre_layout_element_name Description: Element name as printed in the Name column — either the FIX field name or the component name.
--     * Slot: pre_layout_required Description: Whether the field or component is required, as printed in the Req’d column of the source layout table ("Y" / "N").
--     * Slot: pre_layout_description Description: Free-text content of the Description column of the row (may be empty).
--     * Slot: pre_layout_nested Description: Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table).
--     * Slot: PreTradeMessageDetail_msg_type Description: Autocreated FK slot
--     * Slot: PreTradeComponentDetail_component_name Description: Autocreated FK slot
--     * Slot: CommonComponentDetail_component_name Description: Autocreated FK slot
-- # Class: TradeBusinessArea Description: Tree-root container for the Trade (Orders and Executions) business area of FIX Latest.
--     * Slot: id
--     * Slot: trade_area Description: Identity of the business area the chapter describes.
--     * Slot: title Description: Display title.
--     * Slot: published_version Description: Version stamp from the document header.
--     * Slot: publisher Description: Publishing body of the FIX Latest specification.
--     * Slot: trade_introduction Description: Prose introduction of the chapter.
--     * Slot: trade_diagram_conventions Description: Sentence describing diagram conventions used in the chapter.
--     * Slot: trade_message_diagram_template_url Description: URL of the "Message Diagram Templates" page referenced by the chapter introduction.
--     * Slot: trade_messages_overview_note Description: Intro prose of the area-wide Messages sub-section.
--     * Slot: trade_components_overview_note Description: Intro prose of the area-wide Components sub-section.
-- # Class: TradeMessageEntry Description: One row of the area-wide trade messages table.
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: category Description: Message category.
--     * Slot: TradeBusinessArea_id Description: Autocreated FK slot
-- # Class: TradeComponentEntry Description: One row of the area-wide trade components table.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: trade_repetition Description: REPEATING or NON_REPEATING.
--     * Slot: category Description: Category the component is listed under. Common Components are listed under the synthetic "Common Components" value.
--     * Slot: trade_is_common Description: True when the component is declared as a Common Component.
--     * Slot: trade_footnote_number Description: Footnote indicator on a component-table row.
--     * Slot: TradeBusinessArea_id Description: Autocreated FK slot
-- # Class: TradeComponentTableFootnote Description: A footnote on the area-wide components table.
--     * Slot: trade_footnote_number Description: Footnote indicator on a component-table row.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: trade_introduced_in Description: FIX version or Extension Pack that introduced the component.
--     * Slot: trade_sole_category Description: Single category that actually uses the component.
--     * Slot: trade_footnote_text Description: Footnote text.
--     * Slot: TradeBusinessArea_id Description: Autocreated FK slot
-- # Class: TradeCategorySection Description: A per-category sub-section of the Trade chapter.
--     * Slot: category Description: Message category.
--     * Slot: title Description: Display title.
--     * Slot: description Description: Free-text description.
--     * Slot: trade_category_background Description: Optional "Background" prose preceding a category's message descriptions (e.g. the Cross Order Handling chapter's cross-trade overview).
--     * Slot: trade_category_components_note Description: Intro prose of a category's Components sub-section.
--     * Slot: TradeBusinessArea_id Description: Autocreated FK slot
-- # Class: TradeMessageDetail Description: Per-category message description.
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: description Description: Description of the message's purpose and usage.
--     * Slot: trade_layout_url Description: URL of the detailed message- or component-layout in the Trade Appendix.
--     * Slot: TradeCategorySection_category Description: Autocreated FK slot
--     * Slot: TradeMessageGroup_trade_group_title Description: Autocreated FK slot
--     * Slot: TradeAppendixSection_trade_appendix_category Description: Autocreated FK slot
-- # Class: TradeComponentDetail Description: Per-category component description.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: trade_repetition Description: REPEATING or NON_REPEATING.
--     * Slot: description Description: Description of the component's purpose.
--     * Slot: trade_layout_url Description: URL of the detailed message- or component-layout in the Trade Appendix.
--     * Slot: TradeCategorySection_category Description: Autocreated FK slot
-- # Class: TradeMessageGroup Description: Purpose-grouped sub-section inside a category's Messages sub-section (e.g. "New Order Single", "Execution Reports", "Order Cancel Requests" under Single/General Order Handling).
--     * Slot: trade_group_title Description: Purpose-group heading inside a category's Messages sub-section.
--     * Slot: description Description: Description of the purpose-group's role within the category.
--     * Slot: TradeCategorySection_category Description: Autocreated FK slot
-- # Class: TradeCommonComponentDetail Description: Per-common-component description from the chapter's final "Common Components" section.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: trade_repetition Description: REPEATING or NON_REPEATING.
--     * Slot: description Description: Description of the common component's purpose.
--     * Slot: trade_layout_url Description: URL of the detailed message- or component-layout in the Trade Appendix.
--     * Slot: TradeBusinessArea_id Description: Autocreated FK slot
-- # Class: TradeLayoutRow Description: One row of the layout table published in the Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
--     * Slot: id
--     * Slot: trade_layout_kind Description: Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table).
--     * Slot: trade_layout_field_tag Description: FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.
--     * Slot: trade_layout_element_name Description: Element name as printed in the Name column — either the FIX field name or the component name.
--     * Slot: trade_layout_required Description: Whether the field or component is required, as printed in the Req'd column of the source layout table ("Y" / "N").
--     * Slot: trade_layout_description Description: Free-text content of the Description column of the row (may be empty).
--     * Slot: trade_layout_nested Description: Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table).
--     * Slot: TradeMessageDetail_msg_type Description: Autocreated FK slot
--     * Slot: TradeComponentDetail_component_name Description: Autocreated FK slot
--     * Slot: TradeCommonComponentDetail_component_name Description: Autocreated FK slot
-- # Class: TradeOrdStatusPrecedenceEntry Description: One row of the OrdStatus(39) precedence table published in the Execution Reports purpose-group of the Single/General Order Handling category. Defines the precedence ranking used to resolve simultaneous state transitions on an order, paired with the human-readable OrdStatus label and its descriptive prose.
--     * Slot: trade_ord_status_precedence Description: Precedence rank (1 = lowest, higher numbers take precedence) of an OrdStatus(39) value used to resolve simultaneous state transitions on an order.
--     * Slot: trade_ord_status_label Description: Human-readable OrdStatus(39) label as printed in the Execution Reports precedence table (e.g. "Pending Cancel", "Done for Day", "Filled").
--     * Slot: description Description: Verbatim OrdStatus description from the table.
--     * Slot: TradeMessageGroup_trade_group_title Description: Autocreated FK slot
-- # Class: TradeFragmentationEntry Description: One row of a fragmentation table published in a Trade category (currently only List/Program/Basket Trading) identifying a message that may be fragmented, the "Total Entries" field used to indicate the total count across all fragments of the batch, and the verbatim description of the repeating group that may be fragmented.
--     * Slot: trade_fragmentation_message Description: Message that may be fragmented — verbatim text from the Message column of the fragmentation table (e.g. "NewOrderList(35=E)").
--     * Slot: trade_fragmentation_total_entries_field Description: Name and tag of the "Total Entries" field used to indicate the total count across all fragments of the batch (e.g. "TotNoOrders(68)").
--     * Slot: trade_fragmentation_repeating_group Description: Verbatim description of the repeating group that may be fragmented — from the table's third column.
--     * Slot: TradeCategorySection_category Description: Autocreated FK slot
-- # Class: TradeAppendix Description: Tree-root container for the Trade Appendix — the spec companion document that publishes the full message- and component-layout tables for every message and component used in the Trade business area, organized into one "Appendix – <X> Category" sub-section per Trade category plus a final "Appendix – Common Category" sub-section covering the layouts of the chapter's common components.
--     * Slot: id
--     * Slot: title Description: Display title.
--     * Slot: published_version Description: Version stamp from the document header.
--     * Slot: publisher Description: Publishing body of the FIX Latest specification.
--     * Slot: description Description: Optional preface prose for the Trade Appendix as a whole.
-- # Class: TradeAppendixSection Description: One "Appendix – <X> Category" sub-section of the Trade Appendix. Bundles the per-message layout tables (TradeMessageDetail) and per-component layout tables (TradeComponentDetail) for messages and components that belong to one Trade category — or, for the synthetic "Common" section, the layouts of the chapter's common components.
--     * Slot: trade_appendix_category Description: Identifier for an appendix section — either the Trade category name as printed in the heading (e.g. "CrossOrders", "MultilegOrders", "OrderMassHandling", "ProgramTrading", "SingleGeneralOrderHandling") or the literal "Common" for the common-components appendix.
--     * Slot: title Description: Section heading exactly as printed in the Trade Appendix (e.g. "Appendix – CrossOrders Category").
--     * Slot: description Description: Free-text description.
--     * Slot: TradeAppendix_id Description: Autocreated FK slot
-- # Class: PostTradeBusinessArea Description: Tree-root container for the Post-Trade business area of FIX Latest.
--     * Slot: id
--     * Slot: area Description: Identity of the business area.
--     * Slot: title Description: Display title.
--     * Slot: published_version Description: Version stamp from the document header.
--     * Slot: publisher Description: Publishing body of the FIX Latest specification.
--     * Slot: post_introduction Description: Prose introduction of the Post-Trade chapter.
--     * Slot: diagram_conventions Description: Sentence describing diagram conventions used in the chapter.
--     * Slot: messages_overview_note Description: Intro prose of the area-wide Messages sub-section.
--     * Slot: components_overview_note Description: Intro prose of the area-wide Components sub-section.
-- # Class: PostTradeMessageEntry Description: One row of the area-wide "Messages for Post-Trade Business Area" table.
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: category Description: Message category.
--     * Slot: PostTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: PostTradeComponentEntry Description: One row of the area-wide "Components for Post-Trade Business Area" table.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: repetition Description: REPEATING or NON_REPEATING.
--     * Slot: category Description: Category label as printed in the component table; the token "Common Components" is allowed in addition to the PostTradeCategoryEnum values.
--     * Slot: is_common Description: True when the component is declared as a Common Component.
--     * Slot: footnote_number Description: Footnote indicator on a component-table row.
--     * Slot: PostTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: PostTradeComponentTableFootnote Description: A footnote attached to a row of the area-wide Post-Trade components table.
--     * Slot: footnote_number Description: Footnote indicator on a component-table row.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: introduced_in Description: FIX version or Extension Pack that introduced the component.
--     * Slot: post_sole_category Description: Single Post-Trade category that actually uses the component (per footnote).
--     * Slot: text Description: Footnote text.
--     * Slot: PostTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: PostTradeCategorySection Description: A "Category – <name>" sub-section of the Post-Trade chapter.
--     * Slot: category Description: Message category.
--     * Slot: title Description: Display title.
--     * Slot: description Description: Free-text description.
--     * Slot: category_components_note Description: Intro prose of a category's Components sub-section.
--     * Slot: PostTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: PostTradeMessageGroup Description: A purpose-themed grouping of messages within a Post-Trade category (e.g. "Allocation Instructions").
--     * Slot: group_title Description: Purpose-group heading inside a category's Messages sub-section.
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
-- # Class: PostTradeMessageDetail Description: Per-message description block from a Post-Trade category section.
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: description Description: Free-text description.
--     * Slot: layout_url Description: URL of the detailed message- or component-layout.
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
--     * Slot: PostTradeMessageGroup_group_title Description: Autocreated FK slot
-- # Class: PostTradeComponentDetail Description: Per-component description block from a Post-Trade category section's Components sub-section.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: repetition Description: REPEATING or NON_REPEATING.
--     * Slot: description Description: Free-text description.
--     * Slot: layout_url Description: URL of the detailed message- or component-layout.
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
-- # Class: PostTradeCommonComponentDetail Description: Per-common-component description block from the chapter's final "Common Components" section.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: repetition Description: REPEATING or NON_REPEATING.
--     * Slot: description Description: Free-text description.
--     * Slot: layout_url Description: URL of the detailed message- or component-layout.
--     * Slot: PostTradeBusinessArea_id Description: Autocreated FK slot
-- # Class: AllocationStatusDescription Description: One row of the AllocStatus(87) value/description table.
--     * Slot: status_code Description: Wire status code as referenced in the chapter.
--     * Slot: status_label Description: Human-readable label of the status code.
--     * Slot: description Description: Free-text description.
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
-- # Class: AllocationFragmentationFieldMap Description: One row of the table mapping an allocation message to its fragmentation-related fields.
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: total_count_field Description: Field carrying the total number of repeating-group entries across all fragments (e.g. TotNoAllocs).
--     * Slot: fragment_count_field Description: Field carrying the number of entries in the current message fragment (e.g. NoAllocs).
--     * Slot: principal_message_reference Description: Principal message reference field used to bind allocation message fragments together (e.g. AllocID, AllocReportID).
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
-- # Class: TradeCaptureReportUsage Description: One documented usage of the TradeCaptureReport(35=AE) message.
--     * Slot: status_label Description: Short label for the usage.
--     * Slot: description Description: Free-text description.
--     * Slot: identifier_role Description: Role of the trade-capture-report identifier field.
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
-- # Class: TradeCaptureReportIdentifierRule Description: A rule governing one of the TradeCaptureReport(35=AE) identifier fields.
--     * Slot: identifier_role Description: Role of the trade-capture-report identifier field.
--     * Slot: description Description: Free-text description.
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
-- # Class: RegistrationStatusDescription Description: One row of the RegistStatus(506) value/description table.
--     * Slot: status_code Description: Wire status code as referenced in the chapter.
--     * Slot: status_label Description: Human-readable label of the status code.
--     * Slot: description Description: Free-text description.
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
-- # Class: ClearingServicePostTradeProcessingFormat Description: One message-format row from the Post-Trade Processing Clearing Services section, with its supported actions.
--     * Slot: message_format Description: Clearing-service message format family referenced in the chapter.
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
-- # Class: PostTradeLayoutRow Description: One row of the layout table published in the Post-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
--     * Slot: id
--     * Slot: post_layout_kind Description: Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table).
--     * Slot: post_layout_field_tag Description: FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.
--     * Slot: post_layout_element_name Description: Element name as printed in the Name column — either the FIX field name or the component name.
--     * Slot: post_layout_required Description: Whether the field or component is required, as printed in the Req’d column of the source layout table ("Y" / "N").
--     * Slot: post_layout_description Description: Free-text content of the Description column of the row (may be empty).
--     * Slot: post_layout_nested Description: Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table).
--     * Slot: PostTradeMessageDetail_msg_type Description: Autocreated FK slot
--     * Slot: PostTradeComponentDetail_component_name Description: Autocreated FK slot
--     * Slot: PostTradeCommonComponentDetail_component_name Description: Autocreated FK slot
-- # Class: InfrastructureBusinessArea Description: Tree-root container for the Infrastructure business area of FIX Latest.
--     * Slot: id
--     * Slot: area Description: Identity of the business area.
--     * Slot: title Description: Display title.
--     * Slot: published_version Description: Version stamp from the document header.
--     * Slot: publisher Description: Publishing body of the FIX Latest specification.
--     * Slot: infra_introduction Description: Prose introduction of the Infrastructure chapter.
--     * Slot: diagram_conventions Description: Sentence describing diagram conventions used in the chapter.
--     * Slot: messages_overview_note Description: Intro prose of the area-wide Messages sub-section.
--     * Slot: components_overview_note Description: Intro prose of the area-wide Components sub-section.
-- # Class: InfrastructureMessageEntry Description: One row of the area-wide "Messages for Infrastructure Business Area" table.
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: category Description: Message category.
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
-- # Class: InfrastructureComponentEntry Description: One row of the area-wide "Components for Infrastructure Business Area" table.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: repetition Description: REPEATING or NON_REPEATING.
--     * Slot: category Description: Message category.
--     * Slot: footnote_number Description: Footnote indicator on a component-table row.
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
-- # Class: InfrastructureComponentTableFootnote Description: A footnote attached to a row of the area-wide Infrastructure components table.
--     * Slot: footnote_number Description: Footnote indicator on a component-table row.
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: introduced_in Description: FIX version or Extension Pack that introduced the component.
--     * Slot: infra_sole_category Description: Single Infrastructure category that actually uses the footnoted component.
--     * Slot: text Description: Footnote text.
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
-- # Class: InfrastructureCategorySection Description: A "Category – <name>" sub-section of the Infrastructure chapter.
--     * Slot: id
--     * Slot: category Description: Message category.
--     * Slot: title Description: Display title.
--     * Slot: description Description: Free-text description.
--     * Slot: category_components_note Description: Intro prose of a category's Components sub-section.
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
-- # Class: InfrastructureMessageDetail Description: Per-message description appearing in a category's Messages sub-section.
--     * Slot: id
--     * Slot: msg_type Description: MsgType(35) wire value identifying the message.
--     * Slot: message_name Description: PascalCase name of the message.
--     * Slot: description Description: Free-text description.
--     * Slot: layout_url Description: URL of the detailed message- or component-layout.
--     * Slot: InfrastructureCategorySection_id Description: Autocreated FK slot
-- # Class: InfrastructureComponentDetail Description: Per-component description appearing in a category's Components sub-section.
--     * Slot: id
--     * Slot: component_name Description: PascalCase name of the component.
--     * Slot: repetition Description: REPEATING or NON_REPEATING.
--     * Slot: description Description: Free-text description.
--     * Slot: layout_url Description: URL of the detailed message- or component-layout.
--     * Slot: InfrastructureCategorySection_id Description: Autocreated FK slot
-- # Class: InfrastructureLayoutRow Description: One row of the layout table published in the Infrastructure Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
--     * Slot: id
--     * Slot: infra_layout_kind Description: Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table).
--     * Slot: infra_layout_field_tag Description: FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.
--     * Slot: infra_layout_element_name Description: Element name as printed in the Name column — either the FIX field name (e.g. ApplReqID) or the component name (e.g. StandardHeader, ApplIDRequestGrp).
--     * Slot: infra_layout_required Description: Whether the field or component is required, as printed in the Req’d column of the source layout table ("Y" / "N").
--     * Slot: infra_layout_description Description: Free-text content of the Description column of the row (may be empty).
--     * Slot: infra_layout_nested Description: Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table).
--     * Slot: InfrastructureMessageDetail_id Description: Autocreated FK slot
--     * Slot: InfrastructureComponentDetail_id Description: Autocreated FK slot
-- # Class: StandardResponseMapping Description: One row of a "Standard Responses for <area> Messages" table mapping a request message to its appropriate response(s).
--     * Slot: id
--     * Slot: category_label Description: Category label as printed in the source table (free text; may include parenthesised sub-categories such as "Single General Order Handling").
--     * Slot: fix_message Description: FIX message name with MsgType in parentheses, e.g. AllocationInstruction(35=J).
--     * Slot: appropriate_responses Description: Free-text appropriate-response cell from the Standard Responses tables.
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
-- # Class: ApplicationMessageReferenceKey Description: One row of a "Key Fields for <area> Application Message References" table identifying the field whose value is copied into BusinessRejectRefID(379).
--     * Slot: id
--     * Slot: category_label Description: Category label as printed in the source table (free text; may include parenthesised sub-categories such as "Single General Order Handling").
--     * Slot: fix_message Description: FIX message name with MsgType in parentheses, e.g. AllocationInstruction(35=J).
--     * Slot: business_reject_ref_id_value Description: Source field copied into BusinessRejectRefID(379) when the target message lacks its own reject. May enumerate several alternatives joined by "or".
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
-- # Class: BusinessRejectReasonDescription Description: One entry of the BusinessRejectReason(380) code table.
--     * Slot: reject_reason_code Description: Numeric code value of BusinessRejectReason(380).
--     * Slot: reject_reason_label Description: Human-readable label of a BusinessRejectReason(380) code.
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
-- # Class: InfrastructureGlobalComponentReference Description: A reference from the Infrastructure business area to a Global Component declared on the FIX Latest "Global Components" page. Records the component name, the FIX tags it contributes, and the Infrastructure categories and messages that embed it.
--     * Slot: infra_global_component_name Description: Name of a Global Component referenced from within the Infrastructure business area.
--     * Slot: infra_global_component_repetition Description: Repetition indicator for the Global Component as it appears in the referenced Infrastructure messages.
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
-- # Class: FIXIntroduction_product_coverage
--     * Slot: FIXIntroduction_id Description: Autocreated FK slot
--     * Slot: product_coverage Description: Product/asset classes covered by FIX at the application layer.
-- # Class: FIXProtocolLimited_member_types
--     * Slot: FIXProtocolLimited_id Description: Autocreated FK slot
--     * Slot: member_types Description: Organization categories represented in FPL membership.
-- # Class: FIXProtocolLimited_governance_bodies
--     * Slot: FIXProtocolLimited_id Description: Autocreated FK slot
--     * Slot: governance_bodies Description: High-level governance bodies that represent FPL.
-- # Class: FIXProtocolLimited_product_committees
--     * Slot: FIXProtocolLimited_id Description: Autocreated FK slot
--     * Slot: product_committees Description: Global Product Committees maintained by FPL.
-- # Class: FIXProtocolLimited_regional_committees
--     * Slot: FIXProtocolLimited_id Description: Autocreated FK slot
--     * Slot: regional_committees Description: Regional Committees maintained by FPL.
-- # Class: FIXFamilyStandard_see_also
--     * Slot: FIXFamilyStandard_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related external resources.
-- # Class: FIXDatatype_value_space
--     * Slot: FIXDatatype_datatype_name Description: Autocreated FK slot
--     * Slot: value_space Description: ISO/IEC 11404:2007 GPD value space assigned to the datatype.
-- # Class: FIXDatatype_time_unit
--     * Slot: FIXDatatype_datatype_name Description: Autocreated FK slot
--     * Slot: time_unit Description: Time-unit precision for time-bearing datatypes.
-- # Class: FIXDatatype_footnote_numbers
--     * Slot: FIXDatatype_datatype_name Description: Autocreated FK slot
--     * Slot: footnote_numbers Description: Footnote indicators attached to a datatype row.
-- # Class: Component_nested_components
--     * Slot: Component_component_name Description: Autocreated FK slot
--     * Slot: nested_components_component_name Description: Components nested within this component.
-- # Class: GlobalComponent_conceptually_identical_to
--     * Slot: GlobalComponent_component_name Description: Autocreated FK slot
--     * Slot: conceptually_identical_to Description: Names of other components conceptually identical to this one.
-- # Class: GlobalComponent_gc_referenced_in
--     * Slot: GlobalComponent_component_name Description: Autocreated FK slot
--     * Slot: gc_referenced_in Description: FIX business areas whose messages embed the Global Component.
-- # Class: GlobalComponent_nested_components
--     * Slot: GlobalComponent_component_name Description: Autocreated FK slot
--     * Slot: nested_components_component_name Description: Components nested within this component.
-- # Class: CommonComponent_nested_components
--     * Slot: CommonComponent_component_name Description: Autocreated FK slot
--     * Slot: nested_components_component_name Description: Components nested within this component.
-- # Class: SpecificComponent_nested_components
--     * Slot: SpecificComponent_component_name Description: Autocreated FK slot
--     * Slot: nested_components_component_name Description: Components nested within this component.
-- # Class: Message_components
--     * Slot: Message_msg_type Description: Autocreated FK slot
--     * Slot: components_component_name Description: Components referenced by the enclosing element.
-- # Class: PreTradeBusinessArea_common_components
--     * Slot: PreTradeBusinessArea_id Description: Autocreated FK slot
--     * Slot: common_components Description: Common Components declared at the top of the chapter.
-- # Class: PreTradeBusinessArea_referenced_global_components
--     * Slot: PreTradeBusinessArea_id Description: Autocreated FK slot
--     * Slot: referenced_global_components_component_name Description: Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.
-- # Class: PreTradeCategorySection_quote_models
--     * Slot: PreTradeCategorySection_category Description: Autocreated FK slot
--     * Slot: quote_models Description: Quoting business models referenced in the Quotation / Negotiation category.
-- # Class: TradeBusinessArea_trade_common_components
--     * Slot: TradeBusinessArea_id Description: Autocreated FK slot
--     * Slot: trade_common_components Description: Common Components declared at the bottom of the chapter.
-- # Class: TradeBusinessArea_referenced_global_components
--     * Slot: TradeBusinessArea_id Description: Autocreated FK slot
--     * Slot: referenced_global_components_component_name Description: Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.
-- # Class: TradeAppendixSection_components
--     * Slot: TradeAppendixSection_trade_appendix_category Description: Autocreated FK slot
--     * Slot: components_component_name Description: Layout tables for the components that belong to the appendix section.
-- # Class: PostTradeBusinessArea_post_common_components
--     * Slot: PostTradeBusinessArea_id Description: Autocreated FK slot
--     * Slot: post_common_components Description: Common Components declared at the top of the Post-Trade chapter.
-- # Class: PostTradeBusinessArea_referenced_global_components
--     * Slot: PostTradeBusinessArea_id Description: Autocreated FK slot
--     * Slot: referenced_global_components_component_name Description: Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.
-- # Class: PostTradeCategorySection_allocation_scenarios
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
--     * Slot: allocation_scenarios Description: Communication options supported by the Allocation category for conveying allocation instructions.
-- # Class: PostTradeCategorySection_allocation_roles
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
--     * Slot: allocation_roles Description: Role labels used throughout the Allocation category prose.
-- # Class: PostTradeCategorySection_post_trade_allocation_pricing_methods
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
--     * Slot: post_trade_allocation_pricing_methods Description: Methods supported for computing post-trade allocations.
-- # Class: PostTradeCategorySection_clearing_services_for_position_management
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
--     * Slot: clearing_services_for_position_management Description: Business functions exposed by the Position Management Clearing Services.
-- # Class: PostTradeCategorySection_collateral_management_usages
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
--     * Slot: collateral_management_usages Description: Documented usages for the Collateral Management messages.
-- # Class: PostTradeCategorySection_collateral_assignment_purposes
--     * Slot: PostTradeCategorySection_category Description: Autocreated FK slot
--     * Slot: collateral_assignment_purposes Description: Documented purposes for the CollateralAssignment(35=AY) message.
-- # Class: ClearingServicePostTradeProcessingFormat_supported_actions
--     * Slot: ClearingServicePostTradeProcessingFormat_message_format Description: Autocreated FK slot
--     * Slot: supported_actions Description: Action labels (e.g. Allocation, Accept, Reject, Release, Change, Delete) supported by a clearing-service message format.
-- # Class: InfrastructureBusinessArea_infra_common_components
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
--     * Slot: infra_common_components Description: Component names declared in the area-wide components listing. Per the chapter prose, none of these are shared across categories within the area.
-- # Class: InfrastructureBusinessArea_referenced_global_components
--     * Slot: InfrastructureBusinessArea_id Description: Autocreated FK slot
--     * Slot: referenced_global_components_component_name Description: Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.
-- # Class: InfrastructureCategorySection_network_status_scenarios
--     * Slot: InfrastructureCategorySection_id Description: Autocreated FK slot
--     * Slot: network_status_scenarios Description: Network Status Communication usage scenarios.
-- # Class: InfrastructureCategorySection_network_request_types_referenced
--     * Slot: InfrastructureCategorySection_id Description: Autocreated FK slot
--     * Slot: network_request_types_referenced Description: NetworkRequestType(935) values explicitly cited in the Network Status Communication category prose.
-- # Class: InfrastructureCategorySection_application_message_report_uses
--     * Slot: InfrastructureCategorySection_id Description: Autocreated FK slot
--     * Slot: application_message_report_uses Description: Documented uses of ApplicationMessageReport(35=BY).
-- # Class: InfrastructureGlobalComponentReference_infra_global_component_field_tags
--     * Slot: InfrastructureGlobalComponentReference_infra_global_component_name Description: Autocreated FK slot
--     * Slot: infra_global_component_field_tags Description: FIX tag numbers contributed by the referenced Global Component (as listed on the Global Components page).
-- # Class: InfrastructureGlobalComponentReference_infra_global_component_field_names
--     * Slot: InfrastructureGlobalComponentReference_infra_global_component_name Description: Autocreated FK slot
--     * Slot: infra_global_component_field_names Description: Human-readable field names of the tags contributed by the referenced Global Component.
-- # Class: InfrastructureGlobalComponentReference_infra_global_component_used_in
--     * Slot: InfrastructureGlobalComponentReference_infra_global_component_name Description: Autocreated FK slot
--     * Slot: infra_global_component_used_in Description: Infrastructure categories that reference the Global Component.
-- # Class: InfrastructureGlobalComponentReference_infra_global_component_msg_types
--     * Slot: InfrastructureGlobalComponentReference_infra_global_component_name Description: Autocreated FK slot
--     * Slot: infra_global_component_msg_types Description: MsgType values within the Infrastructure business area that embed the referenced Global Component.

CREATE TABLE "FIXProtocolLimited" (
	id INTEGER NOT NULL,
	brand_name TEXT,
	legal_name TEXT,
	website TEXT,
	member_firms_url TEXT,
	working_groups_url TEXT,
	committees_url TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_FIXProtocolLimited_id" ON "FIXProtocolLimited" (id);

CREATE TABLE "Component" (
	component_name TEXT NOT NULL,
	description TEXT,
	scope VARCHAR(8) NOT NULL,
	is_repeating_group BOOLEAN,
	PRIMARY KEY (component_name)
);
CREATE INDEX "ix_Component_component_name" ON "Component" (component_name);

CREATE TABLE "CommonComponent" (
	business_area VARCHAR(14) NOT NULL,
	component_name TEXT NOT NULL,
	description TEXT,
	scope VARCHAR(8) NOT NULL,
	is_repeating_group BOOLEAN,
	PRIMARY KEY (component_name)
);
CREATE INDEX "ix_CommonComponent_component_name" ON "CommonComponent" (component_name);

CREATE TABLE "SpecificComponent" (
	business_area VARCHAR(14) NOT NULL,
	category VARCHAR(31) NOT NULL,
	component_name TEXT NOT NULL,
	description TEXT,
	scope VARCHAR(8) NOT NULL,
	is_repeating_group BOOLEAN,
	PRIMARY KEY (component_name)
);
CREATE INDEX "ix_SpecificComponent_component_name" ON "SpecificComponent" (component_name);

CREATE TABLE "PreTradeBusinessArea" (
	id INTEGER NOT NULL,
	area VARCHAR(14) NOT NULL,
	title TEXT,
	published_version TEXT,
	publisher TEXT,
	introduction TEXT,
	diagram_conventions TEXT,
	messages_overview_note TEXT,
	components_overview_note TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PreTradeBusinessArea_id" ON "PreTradeBusinessArea" (id);

CREATE TABLE "TradeBusinessArea" (
	id INTEGER NOT NULL,
	trade_area VARCHAR(14) NOT NULL,
	title TEXT,
	published_version TEXT,
	publisher TEXT,
	trade_introduction TEXT,
	trade_diagram_conventions TEXT,
	trade_message_diagram_template_url TEXT,
	trade_messages_overview_note TEXT,
	trade_components_overview_note TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TradeBusinessArea_id" ON "TradeBusinessArea" (id);

CREATE TABLE "TradeAppendix" (
	id INTEGER NOT NULL,
	title TEXT,
	published_version TEXT,
	publisher TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_TradeAppendix_id" ON "TradeAppendix" (id);

CREATE TABLE "PostTradeBusinessArea" (
	id INTEGER NOT NULL,
	area VARCHAR(14) NOT NULL,
	title TEXT,
	published_version TEXT,
	publisher TEXT,
	post_introduction TEXT,
	diagram_conventions TEXT,
	messages_overview_note TEXT,
	components_overview_note TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PostTradeBusinessArea_id" ON "PostTradeBusinessArea" (id);

CREATE TABLE "InfrastructureBusinessArea" (
	id INTEGER NOT NULL,
	area VARCHAR(14) NOT NULL,
	title TEXT,
	published_version TEXT,
	publisher TEXT,
	infra_introduction TEXT,
	diagram_conventions TEXT,
	messages_overview_note TEXT,
	components_overview_note TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_InfrastructureBusinessArea_id" ON "InfrastructureBusinessArea" (id);

CREATE TABLE "FIXIntroduction" (
	id INTEGER NOT NULL,
	published_version TEXT,
	published_date DATE,
	publisher TEXT,
	preface TEXT,
	introduction_text TEXT,
	utc_leap_seconds_note TEXT,
	about_fpl_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(about_fpl_id) REFERENCES "FIXProtocolLimited" (id)
);
CREATE INDEX "ix_FIXIntroduction_id" ON "FIXIntroduction" (id);

CREATE TABLE "PreTradeMessageEntry" (
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	category VARCHAR(31) NOT NULL,
	"PreTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (msg_type),
	FOREIGN KEY("PreTradeBusinessArea_id") REFERENCES "PreTradeBusinessArea" (id)
);
CREATE INDEX "ix_PreTradeMessageEntry_msg_type" ON "PreTradeMessageEntry" (msg_type);

CREATE TABLE "PreTradeComponentEntry" (
	component_name TEXT NOT NULL,
	repetition VARCHAR(13) NOT NULL,
	category TEXT NOT NULL,
	is_common BOOLEAN,
	footnote_number INTEGER,
	"PreTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (component_name),
	FOREIGN KEY("PreTradeBusinessArea_id") REFERENCES "PreTradeBusinessArea" (id)
);
CREATE INDEX "ix_PreTradeComponentEntry_component_name" ON "PreTradeComponentEntry" (component_name);

CREATE TABLE "ComponentTableFootnote" (
	footnote_number INTEGER NOT NULL,
	component_name TEXT NOT NULL,
	introduced_in TEXT NOT NULL,
	sole_category VARCHAR(31) NOT NULL,
	text TEXT,
	"PreTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (footnote_number),
	FOREIGN KEY("PreTradeBusinessArea_id") REFERENCES "PreTradeBusinessArea" (id)
);
CREATE INDEX "ix_ComponentTableFootnote_footnote_number" ON "ComponentTableFootnote" (footnote_number);

CREATE TABLE "PreTradeCategorySection" (
	category VARCHAR(31) NOT NULL,
	title TEXT,
	description TEXT,
	category_components_note TEXT,
	"PreTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (category),
	FOREIGN KEY("PreTradeBusinessArea_id") REFERENCES "PreTradeBusinessArea" (id)
);
CREATE INDEX "ix_PreTradeCategorySection_category" ON "PreTradeCategorySection" (category);

CREATE TABLE "CommonComponentDetail" (
	component_name VARCHAR(31) NOT NULL,
	repetition VARCHAR(13),
	description TEXT,
	layout_url TEXT,
	"PreTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (component_name),
	FOREIGN KEY("PreTradeBusinessArea_id") REFERENCES "PreTradeBusinessArea" (id)
);
CREATE INDEX "ix_CommonComponentDetail_component_name" ON "CommonComponentDetail" (component_name);

CREATE TABLE "TradeMessageEntry" (
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	category VARCHAR(29) NOT NULL,
	"TradeBusinessArea_id" INTEGER,
	PRIMARY KEY (msg_type),
	FOREIGN KEY("TradeBusinessArea_id") REFERENCES "TradeBusinessArea" (id)
);
CREATE INDEX "ix_TradeMessageEntry_msg_type" ON "TradeMessageEntry" (msg_type);

CREATE TABLE "TradeComponentEntry" (
	component_name TEXT NOT NULL,
	trade_repetition VARCHAR(13) NOT NULL,
	category TEXT NOT NULL,
	trade_is_common BOOLEAN,
	trade_footnote_number INTEGER,
	"TradeBusinessArea_id" INTEGER,
	PRIMARY KEY (component_name),
	FOREIGN KEY("TradeBusinessArea_id") REFERENCES "TradeBusinessArea" (id)
);
CREATE INDEX "ix_TradeComponentEntry_component_name" ON "TradeComponentEntry" (component_name);

CREATE TABLE "TradeComponentTableFootnote" (
	trade_footnote_number INTEGER NOT NULL,
	component_name TEXT NOT NULL,
	trade_introduced_in TEXT NOT NULL,
	trade_sole_category VARCHAR(29) NOT NULL,
	trade_footnote_text TEXT,
	"TradeBusinessArea_id" INTEGER,
	PRIMARY KEY (trade_footnote_number),
	FOREIGN KEY("TradeBusinessArea_id") REFERENCES "TradeBusinessArea" (id)
);
CREATE INDEX "ix_TradeComponentTableFootnote_trade_footnote_number" ON "TradeComponentTableFootnote" (trade_footnote_number);

CREATE TABLE "TradeCategorySection" (
	category VARCHAR(29) NOT NULL,
	title TEXT,
	description TEXT,
	trade_category_background TEXT,
	trade_category_components_note TEXT,
	"TradeBusinessArea_id" INTEGER,
	PRIMARY KEY (category),
	FOREIGN KEY("TradeBusinessArea_id") REFERENCES "TradeBusinessArea" (id)
);
CREATE INDEX "ix_TradeCategorySection_category" ON "TradeCategorySection" (category);

CREATE TABLE "TradeCommonComponentDetail" (
	component_name VARCHAR(24) NOT NULL,
	trade_repetition VARCHAR(13),
	description TEXT,
	trade_layout_url TEXT,
	"TradeBusinessArea_id" INTEGER,
	PRIMARY KEY (component_name),
	FOREIGN KEY("TradeBusinessArea_id") REFERENCES "TradeBusinessArea" (id)
);
CREATE INDEX "ix_TradeCommonComponentDetail_component_name" ON "TradeCommonComponentDetail" (component_name);

CREATE TABLE "TradeAppendixSection" (
	trade_appendix_category TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"TradeAppendix_id" INTEGER,
	PRIMARY KEY (trade_appendix_category),
	FOREIGN KEY("TradeAppendix_id") REFERENCES "TradeAppendix" (id)
);
CREATE INDEX "ix_TradeAppendixSection_trade_appendix_category" ON "TradeAppendixSection" (trade_appendix_category);

CREATE TABLE "PostTradeMessageEntry" (
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	category VARCHAR(29) NOT NULL,
	"PostTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (msg_type),
	FOREIGN KEY("PostTradeBusinessArea_id") REFERENCES "PostTradeBusinessArea" (id)
);
CREATE INDEX "ix_PostTradeMessageEntry_msg_type" ON "PostTradeMessageEntry" (msg_type);

CREATE TABLE "PostTradeComponentEntry" (
	component_name TEXT NOT NULL,
	repetition VARCHAR(13) NOT NULL,
	category TEXT NOT NULL,
	is_common BOOLEAN,
	footnote_number INTEGER,
	"PostTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (component_name),
	FOREIGN KEY("PostTradeBusinessArea_id") REFERENCES "PostTradeBusinessArea" (id)
);
CREATE INDEX "ix_PostTradeComponentEntry_component_name" ON "PostTradeComponentEntry" (component_name);

CREATE TABLE "PostTradeComponentTableFootnote" (
	footnote_number INTEGER NOT NULL,
	component_name TEXT NOT NULL,
	introduced_in TEXT NOT NULL,
	post_sole_category VARCHAR(29) NOT NULL,
	text TEXT,
	"PostTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (footnote_number),
	FOREIGN KEY("PostTradeBusinessArea_id") REFERENCES "PostTradeBusinessArea" (id)
);
CREATE INDEX "ix_PostTradeComponentTableFootnote_footnote_number" ON "PostTradeComponentTableFootnote" (footnote_number);

CREATE TABLE "PostTradeCategorySection" (
	category VARCHAR(29) NOT NULL,
	title TEXT,
	description TEXT,
	category_components_note TEXT,
	"PostTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (category),
	FOREIGN KEY("PostTradeBusinessArea_id") REFERENCES "PostTradeBusinessArea" (id)
);
CREATE INDEX "ix_PostTradeCategorySection_category" ON "PostTradeCategorySection" (category);

CREATE TABLE "PostTradeCommonComponentDetail" (
	component_name VARCHAR(25) NOT NULL,
	repetition VARCHAR(13),
	description TEXT,
	layout_url TEXT,
	"PostTradeBusinessArea_id" INTEGER,
	PRIMARY KEY (component_name),
	FOREIGN KEY("PostTradeBusinessArea_id") REFERENCES "PostTradeBusinessArea" (id)
);
CREATE INDEX "ix_PostTradeCommonComponentDetail_component_name" ON "PostTradeCommonComponentDetail" (component_name);

CREATE TABLE "InfrastructureMessageEntry" (
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	category VARCHAR(28) NOT NULL,
	"InfrastructureBusinessArea_id" INTEGER,
	PRIMARY KEY (msg_type),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id)
);
CREATE INDEX "ix_InfrastructureMessageEntry_msg_type" ON "InfrastructureMessageEntry" (msg_type);

CREATE TABLE "InfrastructureComponentEntry" (
	component_name TEXT NOT NULL,
	repetition VARCHAR(13) NOT NULL,
	category VARCHAR(28) NOT NULL,
	footnote_number INTEGER,
	"InfrastructureBusinessArea_id" INTEGER,
	PRIMARY KEY (component_name),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id)
);
CREATE INDEX "ix_InfrastructureComponentEntry_component_name" ON "InfrastructureComponentEntry" (component_name);

CREATE TABLE "InfrastructureComponentTableFootnote" (
	footnote_number INTEGER NOT NULL,
	component_name TEXT NOT NULL,
	introduced_in TEXT NOT NULL,
	infra_sole_category VARCHAR(28) NOT NULL,
	text TEXT,
	"InfrastructureBusinessArea_id" INTEGER,
	PRIMARY KEY (footnote_number),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id)
);
CREATE INDEX "ix_InfrastructureComponentTableFootnote_footnote_number" ON "InfrastructureComponentTableFootnote" (footnote_number);

CREATE TABLE "InfrastructureCategorySection" (
	id INTEGER NOT NULL,
	category VARCHAR(28) NOT NULL,
	title TEXT,
	description TEXT,
	category_components_note TEXT,
	"InfrastructureBusinessArea_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id)
);
CREATE INDEX "ix_InfrastructureCategorySection_id" ON "InfrastructureCategorySection" (id);

CREATE TABLE "StandardResponseMapping" (
	id INTEGER NOT NULL,
	category_label TEXT NOT NULL,
	fix_message TEXT NOT NULL,
	appropriate_responses TEXT NOT NULL,
	"InfrastructureBusinessArea_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id)
);
CREATE INDEX "ix_StandardResponseMapping_id" ON "StandardResponseMapping" (id);

CREATE TABLE "ApplicationMessageReferenceKey" (
	id INTEGER NOT NULL,
	category_label TEXT NOT NULL,
	fix_message TEXT NOT NULL,
	business_reject_ref_id_value TEXT NOT NULL,
	"InfrastructureBusinessArea_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id)
);
CREATE INDEX "ix_ApplicationMessageReferenceKey_id" ON "ApplicationMessageReferenceKey" (id);

CREATE TABLE "BusinessRejectReasonDescription" (
	reject_reason_code INTEGER NOT NULL,
	reject_reason_label TEXT NOT NULL,
	"InfrastructureBusinessArea_id" INTEGER,
	PRIMARY KEY (reject_reason_code),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id)
);
CREATE INDEX "ix_BusinessRejectReasonDescription_reject_reason_code" ON "BusinessRejectReasonDescription" (reject_reason_code);

CREATE TABLE "InfrastructureGlobalComponentReference" (
	infra_global_component_name VARCHAR(26) NOT NULL,
	infra_global_component_repetition TEXT,
	"InfrastructureBusinessArea_id" INTEGER,
	PRIMARY KEY (infra_global_component_name),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id)
);
CREATE INDEX "ix_InfrastructureGlobalComponentReference_infra_global_component_name" ON "InfrastructureGlobalComponentReference" (infra_global_component_name);

CREATE TABLE "FIXProtocolLimited_member_types" (
	"FIXProtocolLimited_id" INTEGER,
	member_types VARCHAR(17),
	PRIMARY KEY ("FIXProtocolLimited_id", member_types),
	FOREIGN KEY("FIXProtocolLimited_id") REFERENCES "FIXProtocolLimited" (id)
);
CREATE INDEX "ix_FIXProtocolLimited_member_types_FIXProtocolLimited_id" ON "FIXProtocolLimited_member_types" ("FIXProtocolLimited_id");
CREATE INDEX "ix_FIXProtocolLimited_member_types_member_types" ON "FIXProtocolLimited_member_types" (member_types);

CREATE TABLE "FIXProtocolLimited_governance_bodies" (
	"FIXProtocolLimited_id" INTEGER,
	governance_bodies VARCHAR(32),
	PRIMARY KEY ("FIXProtocolLimited_id", governance_bodies),
	FOREIGN KEY("FIXProtocolLimited_id") REFERENCES "FIXProtocolLimited" (id)
);
CREATE INDEX "ix_FIXProtocolLimited_governance_bodies_FIXProtocolLimited_id" ON "FIXProtocolLimited_governance_bodies" ("FIXProtocolLimited_id");
CREATE INDEX "ix_FIXProtocolLimited_governance_bodies_governance_bodies" ON "FIXProtocolLimited_governance_bodies" (governance_bodies);

CREATE TABLE "FIXProtocolLimited_product_committees" (
	"FIXProtocolLimited_id" INTEGER,
	product_committees VARCHAR(29),
	PRIMARY KEY ("FIXProtocolLimited_id", product_committees),
	FOREIGN KEY("FIXProtocolLimited_id") REFERENCES "FIXProtocolLimited" (id)
);
CREATE INDEX "ix_FIXProtocolLimited_product_committees_FIXProtocolLimited_id" ON "FIXProtocolLimited_product_committees" ("FIXProtocolLimited_id");
CREATE INDEX "ix_FIXProtocolLimited_product_committees_product_committees" ON "FIXProtocolLimited_product_committees" (product_committees);

CREATE TABLE "FIXProtocolLimited_regional_committees" (
	"FIXProtocolLimited_id" INTEGER,
	regional_committees VARCHAR(12),
	PRIMARY KEY ("FIXProtocolLimited_id", regional_committees),
	FOREIGN KEY("FIXProtocolLimited_id") REFERENCES "FIXProtocolLimited" (id)
);
CREATE INDEX "ix_FIXProtocolLimited_regional_committees_FIXProtocolLimited_id" ON "FIXProtocolLimited_regional_committees" ("FIXProtocolLimited_id");
CREATE INDEX "ix_FIXProtocolLimited_regional_committees_regional_committees" ON "FIXProtocolLimited_regional_committees" (regional_committees);

CREATE TABLE "Component_nested_components" (
	"Component_component_name" TEXT,
	nested_components_component_name TEXT,
	PRIMARY KEY ("Component_component_name", nested_components_component_name),
	FOREIGN KEY("Component_component_name") REFERENCES "Component" (component_name),
	FOREIGN KEY(nested_components_component_name) REFERENCES "Component" (component_name)
);
CREATE INDEX "ix_Component_nested_components_nested_components_component_name" ON "Component_nested_components" (nested_components_component_name);
CREATE INDEX "ix_Component_nested_components_Component_component_name" ON "Component_nested_components" ("Component_component_name");

CREATE TABLE "CommonComponent_nested_components" (
	"CommonComponent_component_name" TEXT,
	nested_components_component_name TEXT,
	PRIMARY KEY ("CommonComponent_component_name", nested_components_component_name),
	FOREIGN KEY("CommonComponent_component_name") REFERENCES "CommonComponent" (component_name),
	FOREIGN KEY(nested_components_component_name) REFERENCES "Component" (component_name)
);
CREATE INDEX "ix_CommonComponent_nested_components_CommonComponent_component_name" ON "CommonComponent_nested_components" ("CommonComponent_component_name");
CREATE INDEX "ix_CommonComponent_nested_components_nested_components_component_name" ON "CommonComponent_nested_components" (nested_components_component_name);

CREATE TABLE "SpecificComponent_nested_components" (
	"SpecificComponent_component_name" TEXT,
	nested_components_component_name TEXT,
	PRIMARY KEY ("SpecificComponent_component_name", nested_components_component_name),
	FOREIGN KEY("SpecificComponent_component_name") REFERENCES "SpecificComponent" (component_name),
	FOREIGN KEY(nested_components_component_name) REFERENCES "Component" (component_name)
);
CREATE INDEX "ix_SpecificComponent_nested_components_nested_components_component_name" ON "SpecificComponent_nested_components" (nested_components_component_name);
CREATE INDEX "ix_SpecificComponent_nested_components_SpecificComponent_component_name" ON "SpecificComponent_nested_components" ("SpecificComponent_component_name");

CREATE TABLE "PreTradeBusinessArea_common_components" (
	"PreTradeBusinessArea_id" INTEGER,
	common_components VARCHAR(31),
	PRIMARY KEY ("PreTradeBusinessArea_id", common_components),
	FOREIGN KEY("PreTradeBusinessArea_id") REFERENCES "PreTradeBusinessArea" (id)
);
CREATE INDEX "ix_PreTradeBusinessArea_common_components_PreTradeBusinessArea_id" ON "PreTradeBusinessArea_common_components" ("PreTradeBusinessArea_id");
CREATE INDEX "ix_PreTradeBusinessArea_common_components_common_components" ON "PreTradeBusinessArea_common_components" (common_components);

CREATE TABLE "TradeBusinessArea_trade_common_components" (
	"TradeBusinessArea_id" INTEGER,
	trade_common_components VARCHAR(24),
	PRIMARY KEY ("TradeBusinessArea_id", trade_common_components),
	FOREIGN KEY("TradeBusinessArea_id") REFERENCES "TradeBusinessArea" (id)
);
CREATE INDEX "ix_TradeBusinessArea_trade_common_components_TradeBusinessArea_id" ON "TradeBusinessArea_trade_common_components" ("TradeBusinessArea_id");
CREATE INDEX "ix_TradeBusinessArea_trade_common_components_trade_common_components" ON "TradeBusinessArea_trade_common_components" (trade_common_components);

CREATE TABLE "PostTradeBusinessArea_post_common_components" (
	"PostTradeBusinessArea_id" INTEGER,
	post_common_components VARCHAR(25),
	PRIMARY KEY ("PostTradeBusinessArea_id", post_common_components),
	FOREIGN KEY("PostTradeBusinessArea_id") REFERENCES "PostTradeBusinessArea" (id)
);
CREATE INDEX "ix_PostTradeBusinessArea_post_common_components_post_common_components" ON "PostTradeBusinessArea_post_common_components" (post_common_components);
CREATE INDEX "ix_PostTradeBusinessArea_post_common_components_PostTradeBusinessArea_id" ON "PostTradeBusinessArea_post_common_components" ("PostTradeBusinessArea_id");

CREATE TABLE "InfrastructureBusinessArea_infra_common_components" (
	"InfrastructureBusinessArea_id" INTEGER,
	infra_common_components VARCHAR(19),
	PRIMARY KEY ("InfrastructureBusinessArea_id", infra_common_components),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id)
);
CREATE INDEX "ix_InfrastructureBusinessArea_infra_common_components_InfrastructureBusinessArea_id" ON "InfrastructureBusinessArea_infra_common_components" ("InfrastructureBusinessArea_id");
CREATE INDEX "ix_InfrastructureBusinessArea_infra_common_components_infra_common_components" ON "InfrastructureBusinessArea_infra_common_components" (infra_common_components);

CREATE TABLE "FIXFamilyStandard" (
	id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	acronym TEXT,
	layer VARCHAR(11) NOT NULL,
	version TEXT,
	session_profile VARCHAR(7),
	encoding_name VARCHAR(8),
	"FIXIntroduction_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("FIXIntroduction_id") REFERENCES "FIXIntroduction" (id)
);
CREATE INDEX "ix_FIXFamilyStandard_id" ON "FIXFamilyStandard" (id);

CREATE TABLE "ExtensionPack" (
	number INTEGER NOT NULL,
	title TEXT NOT NULL,
	size VARCHAR(3),
	enhancement_summary TEXT,
	applies_to_session_layer_only BOOLEAN,
	applies_to_fixml_only BOOLEAN,
	"FIXIntroduction_id" INTEGER,
	PRIMARY KEY (number),
	FOREIGN KEY("FIXIntroduction_id") REFERENCES "FIXIntroduction" (id)
);
CREATE INDEX "ix_ExtensionPack_number" ON "ExtensionPack" (number);

CREATE TABLE "FIXDatatype" (
	datatype_name VARCHAR(19) NOT NULL,
	definition TEXT NOT NULL,
	value_space_notes TEXT,
	deprecated_for_new_designs BOOLEAN,
	external_code_set TEXT,
	radix INTEGER,
	repertoire TEXT,
	index_lower_bound INTEGER,
	index_upper_bound INTEGER,
	minimum_value INTEGER,
	maximum_value INTEGER,
	"FIXIntroduction_id" INTEGER,
	PRIMARY KEY (datatype_name),
	FOREIGN KEY("FIXIntroduction_id") REFERENCES "FIXIntroduction" (id)
);
CREATE INDEX "ix_FIXDatatype_datatype_name" ON "FIXDatatype" (datatype_name);

CREATE TABLE "BusinessArea" (
	area VARCHAR(14) NOT NULL,
	title TEXT,
	description TEXT,
	"FIXIntroduction_id" INTEGER,
	PRIMARY KEY (area),
	FOREIGN KEY("FIXIntroduction_id") REFERENCES "FIXIntroduction" (id)
);
CREATE INDEX "ix_BusinessArea_area" ON "BusinessArea" (area);

CREATE TABLE "GlobalComponent" (
	component_group VARCHAR(21) NOT NULL,
	applies_to_instrument BOOLEAN,
	applies_to_leg BOOLEAN,
	applies_to_underlying BOOLEAN,
	gc_id INTEGER,
	component_name TEXT NOT NULL,
	description TEXT,
	scope VARCHAR(8) NOT NULL,
	is_repeating_group BOOLEAN,
	"FIXIntroduction_id" INTEGER,
	PRIMARY KEY (component_name),
	FOREIGN KEY("FIXIntroduction_id") REFERENCES "FIXIntroduction" (id)
);
CREATE INDEX "ix_GlobalComponent_component_name" ON "GlobalComponent" (component_name);

CREATE TABLE "UDFTagRange" (
	range_id TEXT NOT NULL,
	low_tag INTEGER NOT NULL,
	high_tag INTEGER,
	usage VARCHAR(21) NOT NULL,
	description TEXT,
	requires_registration BOOLEAN,
	"FIXIntroduction_id" INTEGER,
	PRIMARY KEY (range_id),
	FOREIGN KEY("FIXIntroduction_id") REFERENCES "FIXIntroduction" (id)
);
CREATE INDEX "ix_UDFTagRange_range_id" ON "UDFTagRange" (range_id);

CREATE TABLE "PreTradeComponentDetail" (
	component_name TEXT NOT NULL,
	repetition VARCHAR(13),
	description TEXT,
	layout_url TEXT,
	"PreTradeCategorySection_category" VARCHAR(31),
	PRIMARY KEY (component_name),
	FOREIGN KEY("PreTradeCategorySection_category") REFERENCES "PreTradeCategorySection" (category)
);
CREATE INDEX "ix_PreTradeComponentDetail_component_name" ON "PreTradeComponentDetail" (component_name);

CREATE TABLE "MessageGroup" (
	group_title TEXT NOT NULL,
	description TEXT,
	"PreTradeCategorySection_category" VARCHAR(31),
	PRIMARY KEY (group_title),
	FOREIGN KEY("PreTradeCategorySection_category") REFERENCES "PreTradeCategorySection" (category)
);
CREATE INDEX "ix_MessageGroup_group_title" ON "MessageGroup" (group_title);

CREATE TABLE "TradeComponentDetail" (
	component_name TEXT NOT NULL,
	trade_repetition VARCHAR(13),
	description TEXT,
	trade_layout_url TEXT,
	"TradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (component_name),
	FOREIGN KEY("TradeCategorySection_category") REFERENCES "TradeCategorySection" (category)
);
CREATE INDEX "ix_TradeComponentDetail_component_name" ON "TradeComponentDetail" (component_name);

CREATE TABLE "TradeMessageGroup" (
	trade_group_title TEXT NOT NULL,
	description TEXT,
	"TradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (trade_group_title),
	FOREIGN KEY("TradeCategorySection_category") REFERENCES "TradeCategorySection" (category)
);
CREATE INDEX "ix_TradeMessageGroup_trade_group_title" ON "TradeMessageGroup" (trade_group_title);

CREATE TABLE "TradeFragmentationEntry" (
	trade_fragmentation_message TEXT NOT NULL,
	trade_fragmentation_total_entries_field TEXT NOT NULL,
	trade_fragmentation_repeating_group TEXT NOT NULL,
	"TradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (trade_fragmentation_message),
	FOREIGN KEY("TradeCategorySection_category") REFERENCES "TradeCategorySection" (category)
);
CREATE INDEX "ix_TradeFragmentationEntry_trade_fragmentation_message" ON "TradeFragmentationEntry" (trade_fragmentation_message);

CREATE TABLE "PostTradeMessageGroup" (
	group_title TEXT NOT NULL,
	"PostTradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (group_title),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_PostTradeMessageGroup_group_title" ON "PostTradeMessageGroup" (group_title);

CREATE TABLE "PostTradeComponentDetail" (
	component_name TEXT NOT NULL,
	repetition VARCHAR(13),
	description TEXT,
	layout_url TEXT,
	"PostTradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (component_name),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_PostTradeComponentDetail_component_name" ON "PostTradeComponentDetail" (component_name);

CREATE TABLE "AllocationStatusDescription" (
	status_code TEXT NOT NULL,
	status_label TEXT NOT NULL,
	description TEXT,
	"PostTradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (status_code),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_AllocationStatusDescription_status_code" ON "AllocationStatusDescription" (status_code);

CREATE TABLE "AllocationFragmentationFieldMap" (
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	total_count_field TEXT NOT NULL,
	fragment_count_field TEXT NOT NULL,
	principal_message_reference TEXT NOT NULL,
	"PostTradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (msg_type),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_AllocationFragmentationFieldMap_msg_type" ON "AllocationFragmentationFieldMap" (msg_type);

CREATE TABLE "TradeCaptureReportUsage" (
	status_label TEXT NOT NULL,
	description TEXT,
	identifier_role VARCHAR(19),
	"PostTradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (status_label),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_TradeCaptureReportUsage_status_label" ON "TradeCaptureReportUsage" (status_label);

CREATE TABLE "TradeCaptureReportIdentifierRule" (
	identifier_role VARCHAR(19) NOT NULL,
	description TEXT,
	"PostTradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (identifier_role),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_TradeCaptureReportIdentifierRule_identifier_role" ON "TradeCaptureReportIdentifierRule" (identifier_role);

CREATE TABLE "RegistrationStatusDescription" (
	status_code TEXT NOT NULL,
	status_label TEXT NOT NULL,
	description TEXT,
	"PostTradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (status_code),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_RegistrationStatusDescription_status_code" ON "RegistrationStatusDescription" (status_code);

CREATE TABLE "ClearingServicePostTradeProcessingFormat" (
	message_format VARCHAR(21) NOT NULL,
	"PostTradeCategorySection_category" VARCHAR(29),
	PRIMARY KEY (message_format),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_ClearingServicePostTradeProcessingFormat_message_format" ON "ClearingServicePostTradeProcessingFormat" (message_format);

CREATE TABLE "InfrastructureMessageDetail" (
	id INTEGER NOT NULL,
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	description TEXT,
	layout_url TEXT,
	"InfrastructureCategorySection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InfrastructureCategorySection_id") REFERENCES "InfrastructureCategorySection" (id)
);
CREATE INDEX "ix_InfrastructureMessageDetail_id" ON "InfrastructureMessageDetail" (id);

CREATE TABLE "InfrastructureComponentDetail" (
	id INTEGER NOT NULL,
	component_name TEXT NOT NULL,
	repetition VARCHAR(13),
	description TEXT,
	layout_url TEXT,
	"InfrastructureCategorySection_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InfrastructureCategorySection_id") REFERENCES "InfrastructureCategorySection" (id)
);
CREATE INDEX "ix_InfrastructureComponentDetail_id" ON "InfrastructureComponentDetail" (id);

CREATE TABLE "FIXIntroduction_product_coverage" (
	"FIXIntroduction_id" INTEGER,
	product_coverage VARCHAR(16),
	PRIMARY KEY ("FIXIntroduction_id", product_coverage),
	FOREIGN KEY("FIXIntroduction_id") REFERENCES "FIXIntroduction" (id)
);
CREATE INDEX "ix_FIXIntroduction_product_coverage_product_coverage" ON "FIXIntroduction_product_coverage" (product_coverage);
CREATE INDEX "ix_FIXIntroduction_product_coverage_FIXIntroduction_id" ON "FIXIntroduction_product_coverage" ("FIXIntroduction_id");

CREATE TABLE "PreTradeCategorySection_quote_models" (
	"PreTradeCategorySection_category" VARCHAR(31),
	quote_models VARCHAR(20),
	PRIMARY KEY ("PreTradeCategorySection_category", quote_models),
	FOREIGN KEY("PreTradeCategorySection_category") REFERENCES "PreTradeCategorySection" (category)
);
CREATE INDEX "ix_PreTradeCategorySection_quote_models_PreTradeCategorySection_category" ON "PreTradeCategorySection_quote_models" ("PreTradeCategorySection_category");
CREATE INDEX "ix_PreTradeCategorySection_quote_models_quote_models" ON "PreTradeCategorySection_quote_models" (quote_models);

CREATE TABLE "PostTradeCategorySection_allocation_scenarios" (
	"PostTradeCategorySection_category" VARCHAR(29),
	allocation_scenarios VARCHAR(21),
	PRIMARY KEY ("PostTradeCategorySection_category", allocation_scenarios),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_PostTradeCategorySection_allocation_scenarios_allocation_scenarios" ON "PostTradeCategorySection_allocation_scenarios" (allocation_scenarios);
CREATE INDEX "ix_PostTradeCategorySection_allocation_scenarios_PostTradeCategorySection_category" ON "PostTradeCategorySection_allocation_scenarios" ("PostTradeCategorySection_category");

CREATE TABLE "PostTradeCategorySection_allocation_roles" (
	"PostTradeCategorySection_category" VARCHAR(29),
	allocation_roles VARCHAR(10),
	PRIMARY KEY ("PostTradeCategorySection_category", allocation_roles),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_PostTradeCategorySection_allocation_roles_PostTradeCategorySection_category" ON "PostTradeCategorySection_allocation_roles" ("PostTradeCategorySection_category");
CREATE INDEX "ix_PostTradeCategorySection_allocation_roles_allocation_roles" ON "PostTradeCategorySection_allocation_roles" (allocation_roles);

CREATE TABLE "PostTradeCategorySection_post_trade_allocation_pricing_methods" (
	"PostTradeCategorySection_category" VARCHAR(29),
	post_trade_allocation_pricing_methods VARCHAR(14),
	PRIMARY KEY ("PostTradeCategorySection_category", post_trade_allocation_pricing_methods),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_PostTradeCategorySection_post_trade_allocation_pricing_methods_post_trade_allocation_pricing_methods" ON "PostTradeCategorySection_post_trade_allocation_pricing_methods" (post_trade_allocation_pricing_methods);
CREATE INDEX "ix_PostTradeCategorySection_post_trade_allocation_pricing_methods_PostTradeCategorySection_category" ON "PostTradeCategorySection_post_trade_allocation_pricing_methods" ("PostTradeCategorySection_category");

CREATE TABLE "PostTradeCategorySection_clearing_services_for_position_management" (
	"PostTradeCategorySection_category" VARCHAR(29),
	clearing_services_for_position_management VARCHAR(26),
	PRIMARY KEY ("PostTradeCategorySection_category", clearing_services_for_position_management),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_PostTradeCategorySection_clearing_services_for_position_management_clearing_services_for_position_management" ON "PostTradeCategorySection_clearing_services_for_position_management" (clearing_services_for_position_management);
CREATE INDEX "ix_PostTradeCategorySection_clearing_services_for_position_management_PostTradeCategorySection_category" ON "PostTradeCategorySection_clearing_services_for_position_management" ("PostTradeCategorySection_category");

CREATE TABLE "PostTradeCategorySection_collateral_management_usages" (
	"PostTradeCategorySection_category" VARCHAR(29),
	collateral_management_usages VARCHAR(38),
	PRIMARY KEY ("PostTradeCategorySection_category", collateral_management_usages),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_PostTradeCategorySection_collateral_management_usages_PostTradeCategorySection_category" ON "PostTradeCategorySection_collateral_management_usages" ("PostTradeCategorySection_category");
CREATE INDEX "ix_PostTradeCategorySection_collateral_management_usages_collateral_management_usages" ON "PostTradeCategorySection_collateral_management_usages" (collateral_management_usages);

CREATE TABLE "PostTradeCategorySection_collateral_assignment_purposes" (
	"PostTradeCategorySection_category" VARCHAR(29),
	collateral_assignment_purposes VARCHAR(32),
	PRIMARY KEY ("PostTradeCategorySection_category", collateral_assignment_purposes),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category)
);
CREATE INDEX "ix_PostTradeCategorySection_collateral_assignment_purposes_collateral_assignment_purposes" ON "PostTradeCategorySection_collateral_assignment_purposes" (collateral_assignment_purposes);
CREATE INDEX "ix_PostTradeCategorySection_collateral_assignment_purposes_PostTradeCategorySection_category" ON "PostTradeCategorySection_collateral_assignment_purposes" ("PostTradeCategorySection_category");

CREATE TABLE "InfrastructureCategorySection_network_status_scenarios" (
	"InfrastructureCategorySection_id" INTEGER,
	network_status_scenarios VARCHAR(10),
	PRIMARY KEY ("InfrastructureCategorySection_id", network_status_scenarios),
	FOREIGN KEY("InfrastructureCategorySection_id") REFERENCES "InfrastructureCategorySection" (id)
);
CREATE INDEX "ix_InfrastructureCategorySection_network_status_scenarios_network_status_scenarios" ON "InfrastructureCategorySection_network_status_scenarios" (network_status_scenarios);
CREATE INDEX "ix_InfrastructureCategorySection_network_status_scenarios_InfrastructureCategorySection_id" ON "InfrastructureCategorySection_network_status_scenarios" ("InfrastructureCategorySection_id");

CREATE TABLE "InfrastructureCategorySection_network_request_types_referenced" (
	"InfrastructureCategorySection_id" INTEGER,
	network_request_types_referenced VARCHAR(16),
	PRIMARY KEY ("InfrastructureCategorySection_id", network_request_types_referenced),
	FOREIGN KEY("InfrastructureCategorySection_id") REFERENCES "InfrastructureCategorySection" (id)
);
CREATE INDEX "ix_InfrastructureCategorySection_network_request_types_referenced_network_request_types_referenced" ON "InfrastructureCategorySection_network_request_types_referenced" (network_request_types_referenced);
CREATE INDEX "ix_InfrastructureCategorySection_network_request_types_referenced_InfrastructureCategorySection_id" ON "InfrastructureCategorySection_network_request_types_referenced" ("InfrastructureCategorySection_id");

CREATE TABLE "InfrastructureCategorySection_application_message_report_uses" (
	"InfrastructureCategorySection_id" INTEGER,
	application_message_report_uses VARCHAR(16),
	PRIMARY KEY ("InfrastructureCategorySection_id", application_message_report_uses),
	FOREIGN KEY("InfrastructureCategorySection_id") REFERENCES "InfrastructureCategorySection" (id)
);
CREATE INDEX "ix_InfrastructureCategorySection_application_message_report_uses_InfrastructureCategorySection_id" ON "InfrastructureCategorySection_application_message_report_uses" ("InfrastructureCategorySection_id");
CREATE INDEX "ix_InfrastructureCategorySection_application_message_report_uses_application_message_report_uses" ON "InfrastructureCategorySection_application_message_report_uses" (application_message_report_uses);

CREATE TABLE "InfrastructureGlobalComponentReference_infra_global_component_field_tags" (
	"InfrastructureGlobalComponentReference_infra_global_component_name" VARCHAR(26),
	infra_global_component_field_tags INTEGER,
	PRIMARY KEY ("InfrastructureGlobalComponentReference_infra_global_component_name", infra_global_component_field_tags),
	FOREIGN KEY("InfrastructureGlobalComponentReference_infra_global_component_name") REFERENCES "InfrastructureGlobalComponentReference" (infra_global_component_name)
);
CREATE INDEX "ix_InfrastructureGlobalComponentReference_infra_global_component_field_tags_InfrastructureGlobalComponentReference_infra_global_component_name" ON "InfrastructureGlobalComponentReference_infra_global_component_field_tags" ("InfrastructureGlobalComponentReference_infra_global_component_name");
CREATE INDEX "ix_InfrastructureGlobalComponentReference_infra_global_component_field_tags_infra_global_component_field_tags" ON "InfrastructureGlobalComponentReference_infra_global_component_field_tags" (infra_global_component_field_tags);

CREATE TABLE "InfrastructureGlobalComponentReference_infra_global_component_field_names" (
	"InfrastructureGlobalComponentReference_infra_global_component_name" VARCHAR(26),
	infra_global_component_field_names TEXT,
	PRIMARY KEY ("InfrastructureGlobalComponentReference_infra_global_component_name", infra_global_component_field_names),
	FOREIGN KEY("InfrastructureGlobalComponentReference_infra_global_component_name") REFERENCES "InfrastructureGlobalComponentReference" (infra_global_component_name)
);
CREATE INDEX "ix_InfrastructureGlobalComponentReference_infra_global_component_field_names_InfrastructureGlobalComponentReference_infra_global_component_name" ON "InfrastructureGlobalComponentReference_infra_global_component_field_names" ("InfrastructureGlobalComponentReference_infra_global_component_name");
CREATE INDEX "ix_InfrastructureGlobalComponentReference_infra_global_component_field_names_infra_global_component_field_names" ON "InfrastructureGlobalComponentReference_infra_global_component_field_names" (infra_global_component_field_names);

CREATE TABLE "InfrastructureGlobalComponentReference_infra_global_component_used_in" (
	"InfrastructureGlobalComponentReference_infra_global_component_name" VARCHAR(26),
	infra_global_component_used_in VARCHAR(28) NOT NULL,
	PRIMARY KEY ("InfrastructureGlobalComponentReference_infra_global_component_name", infra_global_component_used_in),
	FOREIGN KEY("InfrastructureGlobalComponentReference_infra_global_component_name") REFERENCES "InfrastructureGlobalComponentReference" (infra_global_component_name)
);
CREATE INDEX "ix_InfrastructureGlobalComponentReference_infra_global_component_used_in_infra_global_component_used_in" ON "InfrastructureGlobalComponentReference_infra_global_component_used_in" (infra_global_component_used_in);
CREATE INDEX "ix_InfrastructureGlobalComponentReference_infra_global_component_used_in_InfrastructureGlobalComponentReference_infra_global_component_name" ON "InfrastructureGlobalComponentReference_infra_global_component_used_in" ("InfrastructureGlobalComponentReference_infra_global_component_name");

CREATE TABLE "InfrastructureGlobalComponentReference_infra_global_component_msg_types" (
	"InfrastructureGlobalComponentReference_infra_global_component_name" VARCHAR(26),
	infra_global_component_msg_types TEXT,
	PRIMARY KEY ("InfrastructureGlobalComponentReference_infra_global_component_name", infra_global_component_msg_types),
	FOREIGN KEY("InfrastructureGlobalComponentReference_infra_global_component_name") REFERENCES "InfrastructureGlobalComponentReference" (infra_global_component_name)
);
CREATE INDEX "ix_InfrastructureGlobalComponentReference_infra_global_component_msg_types_InfrastructureGlobalComponentReference_infra_global_component_name" ON "InfrastructureGlobalComponentReference_infra_global_component_msg_types" ("InfrastructureGlobalComponentReference_infra_global_component_name");
CREATE INDEX "ix_InfrastructureGlobalComponentReference_infra_global_component_msg_types_infra_global_component_msg_types" ON "InfrastructureGlobalComponentReference_infra_global_component_msg_types" (infra_global_component_msg_types);

CREATE TABLE "MessageCategory" (
	category VARCHAR(31) NOT NULL,
	title TEXT,
	description TEXT,
	business_area VARCHAR(14) NOT NULL,
	"BusinessArea_area" VARCHAR(14),
	PRIMARY KEY (category),
	FOREIGN KEY("BusinessArea_area") REFERENCES "BusinessArea" (area)
);
CREATE INDEX "ix_MessageCategory_category" ON "MessageCategory" (category);

CREATE TABLE "PreTradeMessageDetail" (
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	description TEXT,
	layout_url TEXT,
	"PreTradeCategorySection_category" VARCHAR(31),
	"MessageGroup_group_title" TEXT,
	PRIMARY KEY (msg_type),
	FOREIGN KEY("PreTradeCategorySection_category") REFERENCES "PreTradeCategorySection" (category),
	FOREIGN KEY("MessageGroup_group_title") REFERENCES "MessageGroup" (group_title)
);
CREATE INDEX "ix_PreTradeMessageDetail_msg_type" ON "PreTradeMessageDetail" (msg_type);

CREATE TABLE "TradeMessageDetail" (
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	description TEXT,
	trade_layout_url TEXT,
	"TradeCategorySection_category" VARCHAR(29),
	"TradeMessageGroup_trade_group_title" TEXT,
	"TradeAppendixSection_trade_appendix_category" TEXT,
	PRIMARY KEY (msg_type),
	FOREIGN KEY("TradeCategorySection_category") REFERENCES "TradeCategorySection" (category),
	FOREIGN KEY("TradeMessageGroup_trade_group_title") REFERENCES "TradeMessageGroup" (trade_group_title),
	FOREIGN KEY("TradeAppendixSection_trade_appendix_category") REFERENCES "TradeAppendixSection" (trade_appendix_category)
);
CREATE INDEX "ix_TradeMessageDetail_msg_type" ON "TradeMessageDetail" (msg_type);

CREATE TABLE "TradeOrdStatusPrecedenceEntry" (
	trade_ord_status_precedence INTEGER NOT NULL,
	trade_ord_status_label TEXT NOT NULL,
	description TEXT,
	"TradeMessageGroup_trade_group_title" TEXT,
	PRIMARY KEY (trade_ord_status_label),
	FOREIGN KEY("TradeMessageGroup_trade_group_title") REFERENCES "TradeMessageGroup" (trade_group_title)
);
CREATE INDEX "ix_TradeOrdStatusPrecedenceEntry_trade_ord_status_label" ON "TradeOrdStatusPrecedenceEntry" (trade_ord_status_label);

CREATE TABLE "PostTradeMessageDetail" (
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	description TEXT,
	layout_url TEXT,
	"PostTradeCategorySection_category" VARCHAR(29),
	"PostTradeMessageGroup_group_title" TEXT,
	PRIMARY KEY (msg_type),
	FOREIGN KEY("PostTradeCategorySection_category") REFERENCES "PostTradeCategorySection" (category),
	FOREIGN KEY("PostTradeMessageGroup_group_title") REFERENCES "PostTradeMessageGroup" (group_title)
);
CREATE INDEX "ix_PostTradeMessageDetail_msg_type" ON "PostTradeMessageDetail" (msg_type);

CREATE TABLE "InfrastructureLayoutRow" (
	id INTEGER NOT NULL,
	infra_layout_kind VARCHAR(9) NOT NULL,
	infra_layout_field_tag INTEGER,
	infra_layout_element_name TEXT NOT NULL,
	infra_layout_required BOOLEAN,
	infra_layout_description TEXT,
	infra_layout_nested BOOLEAN,
	"InfrastructureMessageDetail_id" INTEGER,
	"InfrastructureComponentDetail_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("InfrastructureMessageDetail_id") REFERENCES "InfrastructureMessageDetail" (id),
	FOREIGN KEY("InfrastructureComponentDetail_id") REFERENCES "InfrastructureComponentDetail" (id)
);
CREATE INDEX "ix_InfrastructureLayoutRow_id" ON "InfrastructureLayoutRow" (id);

CREATE TABLE "FIXFamilyStandard_see_also" (
	"FIXFamilyStandard_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("FIXFamilyStandard_id", see_also),
	FOREIGN KEY("FIXFamilyStandard_id") REFERENCES "FIXFamilyStandard" (id)
);
CREATE INDEX "ix_FIXFamilyStandard_see_also_FIXFamilyStandard_id" ON "FIXFamilyStandard_see_also" ("FIXFamilyStandard_id");
CREATE INDEX "ix_FIXFamilyStandard_see_also_see_also" ON "FIXFamilyStandard_see_also" (see_also);

CREATE TABLE "FIXDatatype_value_space" (
	"FIXDatatype_datatype_name" VARCHAR(19),
	value_space VARCHAR(15),
	PRIMARY KEY ("FIXDatatype_datatype_name", value_space),
	FOREIGN KEY("FIXDatatype_datatype_name") REFERENCES "FIXDatatype" (datatype_name)
);
CREATE INDEX "ix_FIXDatatype_value_space_FIXDatatype_datatype_name" ON "FIXDatatype_value_space" ("FIXDatatype_datatype_name");
CREATE INDEX "ix_FIXDatatype_value_space_value_space" ON "FIXDatatype_value_space" (value_space);

CREATE TABLE "FIXDatatype_time_unit" (
	"FIXDatatype_datatype_name" VARCHAR(19),
	time_unit VARCHAR(11),
	PRIMARY KEY ("FIXDatatype_datatype_name", time_unit),
	FOREIGN KEY("FIXDatatype_datatype_name") REFERENCES "FIXDatatype" (datatype_name)
);
CREATE INDEX "ix_FIXDatatype_time_unit_FIXDatatype_datatype_name" ON "FIXDatatype_time_unit" ("FIXDatatype_datatype_name");
CREATE INDEX "ix_FIXDatatype_time_unit_time_unit" ON "FIXDatatype_time_unit" (time_unit);

CREATE TABLE "FIXDatatype_footnote_numbers" (
	"FIXDatatype_datatype_name" VARCHAR(19),
	footnote_numbers INTEGER,
	PRIMARY KEY ("FIXDatatype_datatype_name", footnote_numbers),
	FOREIGN KEY("FIXDatatype_datatype_name") REFERENCES "FIXDatatype" (datatype_name)
);
CREATE INDEX "ix_FIXDatatype_footnote_numbers_FIXDatatype_datatype_name" ON "FIXDatatype_footnote_numbers" ("FIXDatatype_datatype_name");
CREATE INDEX "ix_FIXDatatype_footnote_numbers_footnote_numbers" ON "FIXDatatype_footnote_numbers" (footnote_numbers);

CREATE TABLE "GlobalComponent_conceptually_identical_to" (
	"GlobalComponent_component_name" TEXT,
	conceptually_identical_to TEXT,
	PRIMARY KEY ("GlobalComponent_component_name", conceptually_identical_to),
	FOREIGN KEY("GlobalComponent_component_name") REFERENCES "GlobalComponent" (component_name)
);
CREATE INDEX "ix_GlobalComponent_conceptually_identical_to_GlobalComponent_component_name" ON "GlobalComponent_conceptually_identical_to" ("GlobalComponent_component_name");
CREATE INDEX "ix_GlobalComponent_conceptually_identical_to_conceptually_identical_to" ON "GlobalComponent_conceptually_identical_to" (conceptually_identical_to);

CREATE TABLE "GlobalComponent_gc_referenced_in" (
	"GlobalComponent_component_name" TEXT,
	gc_referenced_in VARCHAR(14),
	PRIMARY KEY ("GlobalComponent_component_name", gc_referenced_in),
	FOREIGN KEY("GlobalComponent_component_name") REFERENCES "GlobalComponent" (component_name)
);
CREATE INDEX "ix_GlobalComponent_gc_referenced_in_GlobalComponent_component_name" ON "GlobalComponent_gc_referenced_in" ("GlobalComponent_component_name");
CREATE INDEX "ix_GlobalComponent_gc_referenced_in_gc_referenced_in" ON "GlobalComponent_gc_referenced_in" (gc_referenced_in);

CREATE TABLE "GlobalComponent_nested_components" (
	"GlobalComponent_component_name" TEXT,
	nested_components_component_name TEXT,
	PRIMARY KEY ("GlobalComponent_component_name", nested_components_component_name),
	FOREIGN KEY("GlobalComponent_component_name") REFERENCES "GlobalComponent" (component_name),
	FOREIGN KEY(nested_components_component_name) REFERENCES "Component" (component_name)
);
CREATE INDEX "ix_GlobalComponent_nested_components_GlobalComponent_component_name" ON "GlobalComponent_nested_components" ("GlobalComponent_component_name");
CREATE INDEX "ix_GlobalComponent_nested_components_nested_components_component_name" ON "GlobalComponent_nested_components" (nested_components_component_name);

CREATE TABLE "PreTradeBusinessArea_referenced_global_components" (
	"PreTradeBusinessArea_id" INTEGER,
	referenced_global_components_component_name TEXT,
	PRIMARY KEY ("PreTradeBusinessArea_id", referenced_global_components_component_name),
	FOREIGN KEY("PreTradeBusinessArea_id") REFERENCES "PreTradeBusinessArea" (id),
	FOREIGN KEY(referenced_global_components_component_name) REFERENCES "GlobalComponent" (component_name)
);
CREATE INDEX "ix_PreTradeBusinessArea_referenced_global_components_PreTradeBusinessArea_id" ON "PreTradeBusinessArea_referenced_global_components" ("PreTradeBusinessArea_id");
CREATE INDEX "ix_PreTradeBusinessArea_referenced_global_components_referenced_global_components_component_name" ON "PreTradeBusinessArea_referenced_global_components" (referenced_global_components_component_name);

CREATE TABLE "TradeBusinessArea_referenced_global_components" (
	"TradeBusinessArea_id" INTEGER,
	referenced_global_components_component_name TEXT,
	PRIMARY KEY ("TradeBusinessArea_id", referenced_global_components_component_name),
	FOREIGN KEY("TradeBusinessArea_id") REFERENCES "TradeBusinessArea" (id),
	FOREIGN KEY(referenced_global_components_component_name) REFERENCES "GlobalComponent" (component_name)
);
CREATE INDEX "ix_TradeBusinessArea_referenced_global_components_referenced_global_components_component_name" ON "TradeBusinessArea_referenced_global_components" (referenced_global_components_component_name);
CREATE INDEX "ix_TradeBusinessArea_referenced_global_components_TradeBusinessArea_id" ON "TradeBusinessArea_referenced_global_components" ("TradeBusinessArea_id");

CREATE TABLE "TradeAppendixSection_components" (
	"TradeAppendixSection_trade_appendix_category" TEXT,
	components_component_name TEXT,
	PRIMARY KEY ("TradeAppendixSection_trade_appendix_category", components_component_name),
	FOREIGN KEY("TradeAppendixSection_trade_appendix_category") REFERENCES "TradeAppendixSection" (trade_appendix_category),
	FOREIGN KEY(components_component_name) REFERENCES "TradeComponentDetail" (component_name)
);
CREATE INDEX "ix_TradeAppendixSection_components_components_component_name" ON "TradeAppendixSection_components" (components_component_name);
CREATE INDEX "ix_TradeAppendixSection_components_TradeAppendixSection_trade_appendix_category" ON "TradeAppendixSection_components" ("TradeAppendixSection_trade_appendix_category");

CREATE TABLE "PostTradeBusinessArea_referenced_global_components" (
	"PostTradeBusinessArea_id" INTEGER,
	referenced_global_components_component_name TEXT,
	PRIMARY KEY ("PostTradeBusinessArea_id", referenced_global_components_component_name),
	FOREIGN KEY("PostTradeBusinessArea_id") REFERENCES "PostTradeBusinessArea" (id),
	FOREIGN KEY(referenced_global_components_component_name) REFERENCES "GlobalComponent" (component_name)
);
CREATE INDEX "ix_PostTradeBusinessArea_referenced_global_components_PostTradeBusinessArea_id" ON "PostTradeBusinessArea_referenced_global_components" ("PostTradeBusinessArea_id");
CREATE INDEX "ix_PostTradeBusinessArea_referenced_global_components_referenced_global_components_component_name" ON "PostTradeBusinessArea_referenced_global_components" (referenced_global_components_component_name);

CREATE TABLE "ClearingServicePostTradeProcessingFormat_supported_actions" (
	"ClearingServicePostTradeProcessingFormat_message_format" VARCHAR(21),
	supported_actions TEXT NOT NULL,
	PRIMARY KEY ("ClearingServicePostTradeProcessingFormat_message_format", supported_actions),
	FOREIGN KEY("ClearingServicePostTradeProcessingFormat_message_format") REFERENCES "ClearingServicePostTradeProcessingFormat" (message_format)
);
CREATE INDEX "ix_ClearingServicePostTradeProcessingFormat_supported_actions_supported_actions" ON "ClearingServicePostTradeProcessingFormat_supported_actions" (supported_actions);
CREATE INDEX "ix_ClearingServicePostTradeProcessingFormat_supported_actions_ClearingServicePostTradeProcessingFormat_message_format" ON "ClearingServicePostTradeProcessingFormat_supported_actions" ("ClearingServicePostTradeProcessingFormat_message_format");

CREATE TABLE "InfrastructureBusinessArea_referenced_global_components" (
	"InfrastructureBusinessArea_id" INTEGER,
	referenced_global_components_component_name TEXT,
	PRIMARY KEY ("InfrastructureBusinessArea_id", referenced_global_components_component_name),
	FOREIGN KEY("InfrastructureBusinessArea_id") REFERENCES "InfrastructureBusinessArea" (id),
	FOREIGN KEY(referenced_global_components_component_name) REFERENCES "GlobalComponent" (component_name)
);
CREATE INDEX "ix_InfrastructureBusinessArea_referenced_global_components_InfrastructureBusinessArea_id" ON "InfrastructureBusinessArea_referenced_global_components" ("InfrastructureBusinessArea_id");
CREATE INDEX "ix_InfrastructureBusinessArea_referenced_global_components_referenced_global_components_component_name" ON "InfrastructureBusinessArea_referenced_global_components" (referenced_global_components_component_name);

CREATE TABLE "Message" (
	msg_type TEXT NOT NULL,
	message_name TEXT NOT NULL,
	description TEXT,
	category VARCHAR(31),
	"MessageCategory_category" VARCHAR(31),
	PRIMARY KEY (msg_type),
	FOREIGN KEY("MessageCategory_category") REFERENCES "MessageCategory" (category)
);
CREATE INDEX "ix_Message_msg_type" ON "Message" (msg_type);

CREATE TABLE "PreTradeLayoutRow" (
	id INTEGER NOT NULL,
	pre_layout_kind VARCHAR(9) NOT NULL,
	pre_layout_field_tag INTEGER,
	pre_layout_element_name TEXT NOT NULL,
	pre_layout_required BOOLEAN,
	pre_layout_description TEXT,
	pre_layout_nested BOOLEAN,
	"PreTradeMessageDetail_msg_type" TEXT,
	"PreTradeComponentDetail_component_name" TEXT,
	"CommonComponentDetail_component_name" VARCHAR(31),
	PRIMARY KEY (id),
	FOREIGN KEY("PreTradeMessageDetail_msg_type") REFERENCES "PreTradeMessageDetail" (msg_type),
	FOREIGN KEY("PreTradeComponentDetail_component_name") REFERENCES "PreTradeComponentDetail" (component_name),
	FOREIGN KEY("CommonComponentDetail_component_name") REFERENCES "CommonComponentDetail" (component_name)
);
CREATE INDEX "ix_PreTradeLayoutRow_id" ON "PreTradeLayoutRow" (id);

CREATE TABLE "TradeLayoutRow" (
	id INTEGER NOT NULL,
	trade_layout_kind VARCHAR(9) NOT NULL,
	trade_layout_field_tag INTEGER,
	trade_layout_element_name TEXT NOT NULL,
	trade_layout_required BOOLEAN,
	trade_layout_description TEXT,
	trade_layout_nested BOOLEAN,
	"TradeMessageDetail_msg_type" TEXT,
	"TradeComponentDetail_component_name" TEXT,
	"TradeCommonComponentDetail_component_name" VARCHAR(24),
	PRIMARY KEY (id),
	FOREIGN KEY("TradeMessageDetail_msg_type") REFERENCES "TradeMessageDetail" (msg_type),
	FOREIGN KEY("TradeComponentDetail_component_name") REFERENCES "TradeComponentDetail" (component_name),
	FOREIGN KEY("TradeCommonComponentDetail_component_name") REFERENCES "TradeCommonComponentDetail" (component_name)
);
CREATE INDEX "ix_TradeLayoutRow_id" ON "TradeLayoutRow" (id);

CREATE TABLE "PostTradeLayoutRow" (
	id INTEGER NOT NULL,
	post_layout_kind VARCHAR(9) NOT NULL,
	post_layout_field_tag INTEGER,
	post_layout_element_name TEXT NOT NULL,
	post_layout_required BOOLEAN,
	post_layout_description TEXT,
	post_layout_nested BOOLEAN,
	"PostTradeMessageDetail_msg_type" TEXT,
	"PostTradeComponentDetail_component_name" TEXT,
	"PostTradeCommonComponentDetail_component_name" VARCHAR(25),
	PRIMARY KEY (id),
	FOREIGN KEY("PostTradeMessageDetail_msg_type") REFERENCES "PostTradeMessageDetail" (msg_type),
	FOREIGN KEY("PostTradeComponentDetail_component_name") REFERENCES "PostTradeComponentDetail" (component_name),
	FOREIGN KEY("PostTradeCommonComponentDetail_component_name") REFERENCES "PostTradeCommonComponentDetail" (component_name)
);
CREATE INDEX "ix_PostTradeLayoutRow_id" ON "PostTradeLayoutRow" (id);

CREATE TABLE "Field" (
	tag INTEGER NOT NULL,
	field_name TEXT NOT NULL,
	datatype VARCHAR(19) NOT NULL,
	description TEXT,
	requirement VARCHAR(22),
	is_user_defined BOOLEAN,
	"Component_component_name" TEXT,
	"GlobalComponent_component_name" TEXT,
	"CommonComponent_component_name" TEXT,
	"SpecificComponent_component_name" TEXT,
	"Message_msg_type" TEXT,
	PRIMARY KEY (tag),
	FOREIGN KEY("Component_component_name") REFERENCES "Component" (component_name),
	FOREIGN KEY("GlobalComponent_component_name") REFERENCES "GlobalComponent" (component_name),
	FOREIGN KEY("CommonComponent_component_name") REFERENCES "CommonComponent" (component_name),
	FOREIGN KEY("SpecificComponent_component_name") REFERENCES "SpecificComponent" (component_name),
	FOREIGN KEY("Message_msg_type") REFERENCES "Message" (msg_type)
);
CREATE INDEX "ix_Field_tag" ON "Field" (tag);

CREATE TABLE "Message_components" (
	"Message_msg_type" TEXT,
	components_component_name TEXT,
	PRIMARY KEY ("Message_msg_type", components_component_name),
	FOREIGN KEY("Message_msg_type") REFERENCES "Message" (msg_type),
	FOREIGN KEY(components_component_name) REFERENCES "Component" (component_name)
);
CREATE INDEX "ix_Message_components_Message_msg_type" ON "Message_components" ("Message_msg_type");
CREATE INDEX "ix_Message_components_components_component_name" ON "Message_components" (components_component_name);
