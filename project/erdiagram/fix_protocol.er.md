erDiagram
AllocationFragmentationFieldMap {
    string fragment_count_field  
    string message_name  
    string msg_type  
    string principal_message_reference  
    string total_count_field  
}
AllocationStatusDescription {
    string description  
    string status_code  
    string status_label  
}
ApplicationMessageReferenceKey {
    string business_reject_ref_id_value  
    string category_label  
    string fix_message  
}
BusinessArea {
    string description  
    BusinessAreaEnum area  
    string title  
}
BusinessRejectReasonDescription {
    integer reject_reason_code  
    string reject_reason_label  
}
ClearingServicePostTradeProcessingFormat {
    ClearingServiceForPostTradeProcessingEnum message_format  
    stringList supported_actions  
}
CommonComponentDetail {
    string description  
    PreTradeCommonComponentName component_name  
    uri layout_url  
    ComponentRepetition repetition  
}
Component {
    string description  
    string component_name  
    boolean is_repeating_group  
    ComponentScope scope  
}
ComponentTableFootnote {
    string component_name  
    integer footnote_number  
    string introduced_in  
    PreTradeCategoryEnum sole_category  
    string text  
}
ExtensionPack {
    boolean applies_to_fixml_only  
    boolean applies_to_session_layer_only  
    string enhancement_summary  
    ExtensionPackNumber number  
    ExtensionPackSize size  
    string title  
}
FIXDatatype {
    FIXDatatypeName datatype_name  
    string definition  
    boolean deprecated_for_new_designs  
    string external_code_set  
    integerList footnote_numbers  
    integer index_lower_bound  
    integer index_upper_bound  
    integer maximum_value  
    integer minimum_value  
    integer radix  
    string repertoire  
    TimePrecisionList time_unit  
    ISO11404ValueSpaceList value_space  
    string value_space_notes  
}
FIXFamilyStandard {
    string id  
    string name  
    string description  
    string acronym  
    StandardEncodingName encoding_name  
    StandardLayer layer  
    uriList see_also  
    SessionProtocolName session_profile  
    string version  
}
FIXIntroduction {
    string introduction_text  
    string preface  
    ProductCoverageList product_coverage  
    date published_date  
    string published_version  
    string publisher  
    string utc_leap_seconds_note  
}
FIXProtocolLimited {
    string brand_name  
    uri committees_url  
    FPLCommitteeRoleList governance_bodies  
    string legal_name  
    uri member_firms_url  
    FPLMemberTypeList member_types  
    FPLProductGroupList product_committees  
    FPLRegionList regional_committees  
    uri website  
    uri working_groups_url  
}
Field {
    string description  
    FIXDatatypeName datatype  
    string field_name  
    boolean is_user_defined  
    FieldRequirement requirement  
    TagNumber tag  
}
GlobalComponent {
    boolean applies_to_instrument  
    boolean applies_to_leg  
    boolean applies_to_underlying  
    ComponentGroup component_group  
    stringList conceptually_identical_to  
    integer gc_id  
    GlobalComponentBusinessAreaEnumList gc_referenced_in  
    ComponentScope scope  
    string description  
    string component_name  
    boolean is_repeating_group  
}
InfrastructureBusinessArea {
    BusinessAreaEnum area  
    string components_overview_note  
    string diagram_conventions  
    InfrastructureComponentNameList infra_common_components  
    string infra_introduction  
    string messages_overview_note  
    string published_version  
    string publisher  
    string title  
}
InfrastructureCategorySection {
    string description  
    ApplicationMessageReportTypeEnumList application_message_report_uses  
    InfrastructureCategoryEnum category  
    string category_components_note  
    NetworkRequestTypeEnumList network_request_types_referenced  
    NetworkStatusScenarioEnumList network_status_scenarios  
    string title  
}
InfrastructureComponentDetail {
    string description  
    string component_name  
    uri layout_url  
    ComponentRepetition repetition  
}
InfrastructureComponentEntry {
    InfrastructureCategoryEnum category  
    string component_name  
    integer footnote_number  
    ComponentRepetition repetition  
}
InfrastructureComponentTableFootnote {
    string component_name  
    integer footnote_number  
    InfrastructureCategoryEnum infra_sole_category  
    string introduced_in  
    string text  
}
InfrastructureGlobalComponentReference {
    stringList infra_global_component_field_names  
    integerList infra_global_component_field_tags  
    stringList infra_global_component_msg_types  
    InfrastructureGlobalComponentName infra_global_component_name  
    string infra_global_component_repetition  
    InfrastructureCategoryEnumList infra_global_component_used_in  
}
InfrastructureLayoutRow {
    string infra_layout_description  
    string infra_layout_element_name  
    integer infra_layout_field_tag  
    InfrastructureLayoutRowKindEnum infra_layout_kind  
    boolean infra_layout_nested  
    boolean infra_layout_required  
}
InfrastructureMessageDetail {
    string description  
    uri layout_url  
    string message_name  
    string msg_type  
}
InfrastructureMessageEntry {
    InfrastructureCategoryEnum category  
    string message_name  
    string msg_type  
}
Message {
    string description  
    MessageCategoryEnum category  
    string message_name  
    string msg_type  
}
MessageCategory {
    string description  
    BusinessAreaEnum business_area  
    MessageCategoryEnum category  
    string title  
}
MessageGroup {
    string description  
    string group_title  
}
PostTradeBusinessArea {
    BusinessAreaEnum area  
    string components_overview_note  
    string diagram_conventions  
    string messages_overview_note  
    PostTradeCommonComponentNameList post_common_components  
    string post_introduction  
    string published_version  
    string publisher  
    string title  
}
PostTradeCategorySection {
    string description  
    AllocationRoleEnumList allocation_roles  
    AllocationScenarioEnumList allocation_scenarios  
    PostTradeCategoryEnum category  
    string category_components_note  
    ClearingServiceForPositionManagementEnumList clearing_services_for_position_management  
    CollateralAssignmentPurposeEnumList collateral_assignment_purposes  
    CollateralManagementUsageEnumList collateral_management_usages  
    PostTradeAllocationPricingMethodEnumList post_trade_allocation_pricing_methods  
    string title  
}
PostTradeCommonComponentDetail {
    string description  
    PostTradeCommonComponentName component_name  
    uri layout_url  
    ComponentRepetition repetition  
}
PostTradeComponentDetail {
    string description  
    string component_name  
    uri layout_url  
    ComponentRepetition repetition  
}
PostTradeComponentEntry {
    string category  
    string component_name  
    integer footnote_number  
    boolean is_common  
    ComponentRepetition repetition  
}
PostTradeComponentTableFootnote {
    string component_name  
    integer footnote_number  
    string introduced_in  
    PostTradeCategoryEnum post_sole_category  
    string text  
}
PostTradeLayoutRow {
    string post_layout_description  
    string post_layout_element_name  
    integer post_layout_field_tag  
    PostTradeLayoutRowKindEnum post_layout_kind  
    boolean post_layout_nested  
    boolean post_layout_required  
}
PostTradeMessageDetail {
    string description  
    uri layout_url  
    string message_name  
    string msg_type  
}
PostTradeMessageEntry {
    PostTradeCategoryEnum category  
    string message_name  
    string msg_type  
}
PostTradeMessageGroup {
    string group_title  
}
PreTradeBusinessArea {
    BusinessAreaEnum area  
    PreTradeCommonComponentNameList common_components  
    string components_overview_note  
    string diagram_conventions  
    string introduction  
    string messages_overview_note  
    string published_version  
    string publisher  
    string title  
}
PreTradeCategorySection {
    string description  
    PreTradeCategoryEnum category  
    string category_components_note  
    QuoteModelEnumList quote_models  
    string title  
}
PreTradeComponentDetail {
    string description  
    string component_name  
    uri layout_url  
    ComponentRepetition repetition  
}
PreTradeComponentEntry {
    string category  
    string component_name  
    integer footnote_number  
    boolean is_common  
    ComponentRepetition repetition  
}
PreTradeLayoutRow {
    string pre_layout_description  
    string pre_layout_element_name  
    integer pre_layout_field_tag  
    PreTradeLayoutRowKindEnum pre_layout_kind  
    boolean pre_layout_nested  
    boolean pre_layout_required  
}
PreTradeMessageDetail {
    string description  
    uri layout_url  
    string message_name  
    string msg_type  
}
PreTradeMessageEntry {
    PreTradeCategoryEnum category  
    string message_name  
    string msg_type  
}
RegistrationStatusDescription {
    string description  
    string status_code  
    string status_label  
}
StandardResponseMapping {
    string appropriate_responses  
    string category_label  
    string fix_message  
}
TradeAppendix {
    string description  
    string published_version  
    string publisher  
    string title  
}
TradeAppendixSection {
    string description  
    string title  
    string trade_appendix_category  
}
TradeBusinessArea {
    string published_version  
    string publisher  
    string title  
    BusinessAreaEnum trade_area  
    TradeCommonComponentNameList trade_common_components  
    string trade_components_overview_note  
    string trade_diagram_conventions  
    string trade_introduction  
    uri trade_message_diagram_template_url  
    string trade_messages_overview_note  
}
TradeCaptureReportIdentifierRule {
    string description  
    TradeCaptureReportIdentifierRoleEnum identifier_role  
}
TradeCaptureReportUsage {
    string description  
    TradeCaptureReportIdentifierRoleEnum identifier_role  
    string status_label  
}
TradeCategorySection {
    string description  
    TradeCategoryEnum category  
    string title  
    string trade_category_background  
    string trade_category_components_note  
}
TradeCommonComponentDetail {
    string description  
    TradeCommonComponentName component_name  
    uri trade_layout_url  
    TradeComponentRepetition trade_repetition  
}
TradeComponentDetail {
    string description  
    string component_name  
    uri trade_layout_url  
    TradeComponentRepetition trade_repetition  
}
TradeComponentEntry {
    string category  
    string component_name  
    integer trade_footnote_number  
    boolean trade_is_common  
    TradeComponentRepetition trade_repetition  
}
TradeComponentTableFootnote {
    string component_name  
    integer trade_footnote_number  
    string trade_footnote_text  
    string trade_introduced_in  
    TradeCategoryEnum trade_sole_category  
}
TradeFragmentationEntry {
    string trade_fragmentation_message  
    string trade_fragmentation_repeating_group  
    string trade_fragmentation_total_entries_field  
}
TradeLayoutRow {
    string trade_layout_description  
    string trade_layout_element_name  
    integer trade_layout_field_tag  
    TradeLayoutRowKindEnum trade_layout_kind  
    boolean trade_layout_nested  
    boolean trade_layout_required  
}
TradeMessageDetail {
    string description  
    string message_name  
    string msg_type  
    uri trade_layout_url  
}
TradeMessageEntry {
    TradeCategoryEnum category  
    string message_name  
    string msg_type  
}
TradeMessageGroup {
    string description  
    string trade_group_title  
}
TradeOrdStatusPrecedenceEntry {
    string description  
    string trade_ord_status_label  
    integer trade_ord_status_precedence  
}
UDFTagRange {
    string description  
    TagNumber high_tag  
    TagNumber low_tag  
    string range_id  
    boolean requires_registration  
    UDFTagRangeUsage usage  
}

BusinessArea ||--}o MessageCategory : "categories"
CommonComponentDetail ||--}o PreTradeLayoutRow : "pre_layout_rows"
Component ||--}o Component : "nested_components"
Component ||--}o Field : "fields"
FIXIntroduction ||--|o FIXProtocolLimited : "about_fpl"
FIXIntroduction ||--}o BusinessArea : "business_areas"
FIXIntroduction ||--}o ExtensionPack : "extension_packs"
FIXIntroduction ||--}o FIXDatatype : "datatypes"
FIXIntroduction ||--}o FIXFamilyStandard : "standards"
FIXIntroduction ||--}o GlobalComponent : "global_components"
FIXIntroduction ||--}o UDFTagRange : "udf_ranges"
GlobalComponent ||--}o Component : "nested_components"
GlobalComponent ||--}o Field : "fields"
InfrastructureBusinessArea ||--}o ApplicationMessageReferenceKey : "key_fields_post_trade, key_fields_pre_trade, key_fields_trade"
InfrastructureBusinessArea ||--}o BusinessRejectReasonDescription : "business_reject_reason_descriptions"
InfrastructureBusinessArea ||--}o GlobalComponent : "referenced_global_components"
InfrastructureBusinessArea ||--}o InfrastructureCategorySection : "infra_category_sections"
InfrastructureBusinessArea ||--}o InfrastructureComponentTableFootnote : "infra_footnotes"
InfrastructureBusinessArea ||--}o InfrastructureGlobalComponentReference : "infra_global_components"
InfrastructureBusinessArea ||--}o StandardResponseMapping : "standard_responses_post_trade, standard_responses_pre_trade, standard_responses_trade"
InfrastructureBusinessArea ||--}| InfrastructureComponentEntry : "components"
InfrastructureBusinessArea ||--}| InfrastructureMessageEntry : "messages"
InfrastructureCategorySection ||--}o InfrastructureComponentDetail : "infra_category_specific_components"
InfrastructureCategorySection ||--}o InfrastructureMessageDetail : "messages"
InfrastructureComponentDetail ||--}o InfrastructureLayoutRow : "infra_layout_rows"
InfrastructureMessageDetail ||--}o InfrastructureLayoutRow : "infra_layout_rows"
Message ||--}o Component : "components"
Message ||--}o Field : "fields"
MessageCategory ||--}o Message : "messages"
MessageGroup ||--}| PreTradeMessageDetail : "messages"
PostTradeBusinessArea ||--}o GlobalComponent : "referenced_global_components"
PostTradeBusinessArea ||--}o PostTradeCategorySection : "post_category_sections"
PostTradeBusinessArea ||--}o PostTradeCommonComponentDetail : "post_common_component_details"
PostTradeBusinessArea ||--}o PostTradeComponentTableFootnote : "post_footnotes"
PostTradeBusinessArea ||--}| PostTradeComponentEntry : "components"
PostTradeBusinessArea ||--}| PostTradeMessageEntry : "messages"
PostTradeCategorySection ||--}o AllocationFragmentationFieldMap : "fragmentation_field_map"
PostTradeCategorySection ||--}o AllocationStatusDescription : "allocation_status_descriptions"
PostTradeCategorySection ||--}o ClearingServicePostTradeProcessingFormat : "clearing_services_for_post_trade_processing"
PostTradeCategorySection ||--}o PostTradeComponentDetail : "post_category_specific_components"
PostTradeCategorySection ||--}o PostTradeMessageDetail : "messages"
PostTradeCategorySection ||--}o PostTradeMessageGroup : "post_message_groups"
PostTradeCategorySection ||--}o RegistrationStatusDescription : "registration_status_descriptions"
PostTradeCategorySection ||--}o TradeCaptureReportIdentifierRule : "trade_capture_report_identifier_rules"
PostTradeCategorySection ||--}o TradeCaptureReportUsage : "trade_capture_report_usages"
PostTradeCommonComponentDetail ||--}o PostTradeLayoutRow : "post_layout_rows"
PostTradeComponentDetail ||--}o PostTradeLayoutRow : "post_layout_rows"
PostTradeMessageDetail ||--}o PostTradeLayoutRow : "post_layout_rows"
PostTradeMessageGroup ||--}| PostTradeMessageDetail : "messages"
PreTradeBusinessArea ||--}o CommonComponentDetail : "common_component_details"
PreTradeBusinessArea ||--}o ComponentTableFootnote : "footnotes"
PreTradeBusinessArea ||--}o GlobalComponent : "referenced_global_components"
PreTradeBusinessArea ||--}o PreTradeCategorySection : "category_sections"
PreTradeBusinessArea ||--}o PreTradeComponentEntry : "components"
PreTradeBusinessArea ||--}o PreTradeMessageEntry : "messages"
PreTradeCategorySection ||--}o MessageGroup : "message_groups"
PreTradeCategorySection ||--}o PreTradeComponentDetail : "category_specific_components"
PreTradeCategorySection ||--}o PreTradeMessageDetail : "messages"
PreTradeComponentDetail ||--}o PreTradeLayoutRow : "pre_layout_rows"
PreTradeMessageDetail ||--}o PreTradeLayoutRow : "pre_layout_rows"
TradeAppendix ||--}o TradeAppendixSection : "trade_appendix_sections"
TradeAppendixSection ||--}o TradeComponentDetail : "components"
TradeAppendixSection ||--}o TradeMessageDetail : "messages"
TradeBusinessArea ||--}o GlobalComponent : "referenced_global_components"
TradeBusinessArea ||--}o TradeCategorySection : "trade_category_sections"
TradeBusinessArea ||--}o TradeCommonComponentDetail : "trade_common_component_details"
TradeBusinessArea ||--}o TradeComponentEntry : "components"
TradeBusinessArea ||--}o TradeComponentTableFootnote : "trade_footnotes"
TradeBusinessArea ||--}o TradeMessageEntry : "messages"
TradeCategorySection ||--}o TradeComponentDetail : "trade_category_specific_components"
TradeCategorySection ||--}o TradeFragmentationEntry : "trade_fragmentation_entries"
TradeCategorySection ||--}o TradeMessageDetail : "messages"
TradeCategorySection ||--}o TradeMessageGroup : "trade_message_groups"
TradeCommonComponentDetail ||--}o TradeLayoutRow : "trade_layout_rows"
TradeComponentDetail ||--}o TradeLayoutRow : "trade_layout_rows"
TradeMessageDetail ||--}o TradeLayoutRow : "trade_layout_rows"
TradeMessageGroup ||--}o TradeOrdStatusPrecedenceEntry : "trade_ord_status_precedence_entries"
TradeMessageGroup ||--}| TradeMessageDetail : "messages"

