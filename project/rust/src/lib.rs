#![allow(non_camel_case_types)]

#[cfg(feature = "serde")]
mod serde_utils;
pub mod poly;
pub mod poly_containers;
#[cfg(feature = "stubgen")]
pub mod stub_utils;

#[cfg(feature = "serde")]
use serde_yml as _ ;
use chrono::NaiveDate;
#[cfg(feature = "pyo3")]
use pyo3::{FromPyObject,prelude::*};
#[cfg(feature = "stubgen")]
use pyo3_stub_gen::{define_stub_info_gatherer,derive::gen_stub_pyclass,derive::gen_stub_pymethods};
#[cfg(feature = "serde")]
use serde::{Deserialize,Serialize,de::IntoDeserializer};
use serde_value::Value;
#[cfg(feature = "serde")]
use serde_path_to_error;
use std::collections::HashMap;
use std::collections::BTreeMap;

// Types

pub type string = String;
pub type integer = String;
pub type boolean = String;
pub type float = f64;
pub type double = f64;
pub type decimal = String;
pub type time = String;
pub type date = String;
pub type datetime = String;
pub type date_or_datetime = String;
pub type uriorcurie = String;
pub type curie = String;
pub type uri = String;
pub type ncname = String;
pub type objectidentifier = String;
pub type nodeidentifier = String;
pub type jsonpointer = String;
pub type jsonpath = String;
pub type sparqlpath = String;
pub type TagNumber = String;
pub type ExtensionPackNumber = String;

// Slots

pub type id = String;
pub type name = String;
pub type description = String;
pub type acronym = String;
pub type see_also = Vec<uri>;
pub type title = String;
pub type published_version = String;
pub type published_date = NaiveDate;
pub type publisher = String;
pub type preface = String;
pub type introduction_text = String;
pub type utc_leap_seconds_note = String;
pub type about_fpl = FIXProtocolLimited;
pub type standards = Vec<FIXFamilyStandard>;
pub type extension_packs = Vec<ExtensionPack>;
pub type datatypes = Vec<FIXDatatype>;
pub type business_areas = Vec<BusinessArea>;
pub type global_components = Vec<GlobalComponent>;
pub type udf_ranges = Vec<UDFTagRange>;
pub type product_coverage = Vec<ProductCoverage>;
pub type brand_name = String;
pub type legal_name = String;
pub type website = uri;
pub type member_firms_url = uri;
pub type working_groups_url = uri;
pub type committees_url = uri;
pub type member_types = Vec<FPLMemberType>;
pub type governance_bodies = Vec<FPLCommitteeRole>;
pub type product_committees = Vec<FPLProductGroup>;
pub type regional_committees = Vec<FPLRegion>;
pub type layer = StandardLayer;
pub type version = String;
pub type session_profile = SessionProtocolName;
pub type encoding_name = StandardEncodingName;
pub type number = isize;
pub type size = ExtensionPackSize;
pub type enhancement_summary = String;
pub type applies_to_session_layer_only = bool;
pub type applies_to_fixml_only = bool;
pub type datatype_name = FIXDatatypeName;
pub type definition = String;
pub type value_space = Vec<ISO11404ValueSpace>;
pub type value_space_notes = String;
pub type deprecated_for_new_designs = bool;
pub type external_code_set = String;
pub type time_unit = Vec<TimePrecision>;
pub type radix = isize;
pub type repertoire = String;
pub type index_lower_bound = isize;
pub type index_upper_bound = isize;
pub type minimum_value = isize;
pub type maximum_value = isize;
pub type footnote_numbers = Vec<isize>;
pub type area = BusinessAreaEnum;
pub type categories = Vec<MessageCategory>;
pub type category = MessageCategoryEnum;
pub type business_area = BusinessAreaEnum;
pub type messages = Vec<Message>;
pub type tag = isize;
pub type field_name = String;
pub type datatype = FIXDatatypeName;
pub type requirement = FieldRequirement;
pub type is_user_defined = bool;
pub type component_name = String;
pub type scope = ComponentScope;
pub type is_repeating_group = bool;
pub type fields = Vec<Field>;
pub type nested_components = Vec<Component>;
pub type components = Vec<Component>;
pub type component_group = ComponentGroup;
pub type applies_to_instrument = bool;
pub type applies_to_leg = bool;
pub type applies_to_underlying = bool;
pub type conceptually_identical_to = Vec<String>;
pub type msg_type = String;
pub type message_name = String;
pub type range_id = String;
pub type low_tag = isize;
pub type high_tag = isize;
pub type usage = UDFTagRangeUsage;
pub type requires_registration = bool;
pub type gc_id = isize;
pub type gc_referenced_in = Vec<GlobalComponentBusinessAreaEnum>;
pub type referenced_global_components = Vec<GlobalComponent>;
pub type introduction = String;
pub type common_components = Vec<PreTradeCommonComponentName>;
pub type footnotes = Vec<ComponentTableFootnote>;
pub type category_sections = Vec<PreTradeCategorySection>;
pub type category_specific_components = Vec<PreTradeComponentDetail>;
pub type repetition = ComponentRepetition;
pub type is_common = bool;
pub type footnote_number = isize;
pub type introduced_in = String;
pub type sole_category = PreTradeCategoryEnum;
pub type text = String;
pub type layout_url = uri;
pub type diagram_conventions = String;
pub type messages_overview_note = String;
pub type components_overview_note = String;
pub type category_components_note = String;
pub type group_title = String;
pub type message_groups = Vec<MessageGroup>;
pub type common_component_details = Vec<CommonComponentDetail>;
pub type quote_models = Vec<QuoteModelEnum>;
pub type pre_layout_rows = Vec<PreTradeLayoutRow>;
pub type pre_layout_kind = PreTradeLayoutRowKindEnum;
pub type pre_layout_field_tag = isize;
pub type pre_layout_element_name = String;
pub type pre_layout_required = bool;
pub type pre_layout_description = String;
pub type pre_layout_nested = bool;
pub type trade_area = BusinessAreaEnum;
pub type trade_introduction = String;
pub type trade_common_components = Vec<TradeCommonComponentName>;
pub type trade_footnotes = Vec<TradeComponentTableFootnote>;
pub type trade_category_sections = Vec<TradeCategorySection>;
pub type trade_category_specific_components = Vec<TradeComponentDetail>;
pub type trade_repetition = TradeComponentRepetition;
pub type trade_is_common = bool;
pub type trade_footnote_number = isize;
pub type trade_introduced_in = String;
pub type trade_sole_category = TradeCategoryEnum;
pub type trade_footnote_text = String;
pub type trade_layout_url = uri;
pub type trade_diagram_conventions = String;
pub type trade_messages_overview_note = String;
pub type trade_components_overview_note = String;
pub type trade_category_components_note = String;
pub type trade_group_title = String;
pub type trade_message_groups = Vec<TradeMessageGroup>;
pub type trade_common_component_details = Vec<TradeCommonComponentDetail>;
pub type trade_message_diagram_template_url = uri;
pub type trade_category_background = String;
pub type trade_layout_rows = Vec<TradeLayoutRow>;
pub type trade_layout_kind = TradeLayoutRowKindEnum;
pub type trade_layout_field_tag = isize;
pub type trade_layout_element_name = String;
pub type trade_layout_required = bool;
pub type trade_layout_description = String;
pub type trade_layout_nested = bool;
pub type trade_ord_status_precedence_entries = Vec<TradeOrdStatusPrecedenceEntry>;
pub type trade_ord_status_precedence = isize;
pub type trade_ord_status_label = String;
pub type trade_fragmentation_entries = Vec<TradeFragmentationEntry>;
pub type trade_fragmentation_message = String;
pub type trade_fragmentation_total_entries_field = String;
pub type trade_fragmentation_repeating_group = String;
pub type trade_appendix_sections = Vec<TradeAppendixSection>;
pub type trade_appendix_category = String;
pub type post_introduction = String;
pub type post_common_components = Vec<PostTradeCommonComponentName>;
pub type post_footnotes = Vec<PostTradeComponentTableFootnote>;
pub type post_category_sections = Vec<PostTradeCategorySection>;
pub type post_category_specific_components = Vec<PostTradeComponentDetail>;
pub type post_sole_category = PostTradeCategoryEnum;
pub type post_message_groups = Vec<PostTradeMessageGroup>;
pub type post_common_component_details = Vec<PostTradeCommonComponentDetail>;
pub type allocation_scenarios = Vec<AllocationScenarioEnum>;
pub type post_trade_allocation_pricing_methods = Vec<PostTradeAllocationPricingMethodEnum>;
pub type allocation_status_descriptions = Vec<AllocationStatusDescription>;
pub type fragmentation_field_map = Vec<AllocationFragmentationFieldMap>;
pub type trade_capture_report_usages = Vec<TradeCaptureReportUsage>;
pub type trade_capture_report_identifier_rules = Vec<TradeCaptureReportIdentifierRule>;
pub type registration_status_descriptions = Vec<RegistrationStatusDescription>;
pub type clearing_services_for_position_management = Vec<ClearingServiceForPositionManagementEnum>;
pub type clearing_services_for_post_trade_processing = Vec<ClearingServicePostTradeProcessingFormat>;
pub type allocation_roles = Vec<AllocationRoleEnum>;
pub type collateral_management_usages = Vec<CollateralManagementUsageEnum>;
pub type collateral_assignment_purposes = Vec<CollateralAssignmentPurposeEnum>;
pub type identifier_role = TradeCaptureReportIdentifierRoleEnum;
pub type status_code = String;
pub type status_label = String;
pub type message_format = ClearingServiceForPostTradeProcessingEnum;
pub type supported_actions = Vec<String>;
pub type principal_message_reference = String;
pub type total_count_field = String;
pub type fragment_count_field = String;
pub type post_layout_rows = Vec<PostTradeLayoutRow>;
pub type post_layout_kind = PostTradeLayoutRowKindEnum;
pub type post_layout_field_tag = isize;
pub type post_layout_element_name = String;
pub type post_layout_required = bool;
pub type post_layout_description = String;
pub type post_layout_nested = bool;
pub type infra_introduction = String;
pub type infra_common_components = Vec<InfrastructureComponentName>;
pub type infra_footnotes = Vec<InfrastructureComponentTableFootnote>;
pub type infra_category_sections = Vec<InfrastructureCategorySection>;
pub type infra_category_specific_components = Vec<InfrastructureComponentDetail>;
pub type infra_sole_category = InfrastructureCategoryEnum;
pub type standard_responses_pre_trade = Vec<StandardResponseMapping>;
pub type standard_responses_trade = Vec<StandardResponseMapping>;
pub type standard_responses_post_trade = Vec<StandardResponseMapping>;
pub type key_fields_pre_trade = Vec<ApplicationMessageReferenceKey>;
pub type key_fields_trade = Vec<ApplicationMessageReferenceKey>;
pub type key_fields_post_trade = Vec<ApplicationMessageReferenceKey>;
pub type business_reject_reason_descriptions = Vec<BusinessRejectReasonDescription>;
pub type network_status_scenarios = Vec<NetworkStatusScenarioEnum>;
pub type network_request_types_referenced = Vec<NetworkRequestTypeEnum>;
pub type application_message_report_uses = Vec<ApplicationMessageReportTypeEnum>;
pub type category_label = String;
pub type fix_message = String;
pub type appropriate_responses = String;
pub type business_reject_ref_id_value = String;
pub type reject_reason_code = isize;
pub type reject_reason_label = String;
pub type infra_global_components = Vec<InfrastructureGlobalComponentReference>;
pub type infra_global_component_name = InfrastructureGlobalComponentName;
pub type infra_global_component_field_tags = Vec<isize>;
pub type infra_global_component_field_names = Vec<String>;
pub type infra_global_component_used_in = Vec<InfrastructureCategoryEnum>;
pub type infra_global_component_msg_types = Vec<String>;
pub type infra_global_component_repetition = String;
pub type infra_layout_rows = Vec<InfrastructureLayoutRow>;
pub type infra_layout_kind = InfrastructureLayoutRowKindEnum;
pub type infra_layout_field_tag = isize;
pub type infra_layout_element_name = String;
pub type infra_layout_required = bool;
pub type infra_layout_description = String;
pub type infra_layout_nested = bool;

// Enums

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum StandardLayer {
    APPLICATION,
    ENCODING,
    SESSION,
}

impl core::fmt::Display for StandardLayer {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            StandardLayer::APPLICATION => f.write_str("APPLICATION"),
            StandardLayer::ENCODING => f.write_str("ENCODING"),
            StandardLayer::SESSION => f.write_str("SESSION"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for StandardLayer {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            StandardLayer::APPLICATION => "APPLICATION",
            StandardLayer::ENCODING => "ENCODING",
            StandardLayer::SESSION => "SESSION",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for StandardLayer {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "APPLICATION" => Ok(StandardLayer::APPLICATION),
                "ENCODING" => Ok(StandardLayer::ENCODING),
                "SESSION" => Ok(StandardLayer::SESSION),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for StandardLayer: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(StandardLayer)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for StandardLayer {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['APPLICATION', 'ENCODING', 'SESSION']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ExtensionPackSize {
    XXS,
    XS,
    S,
    M,
    L,
    XL,
    XXL,
}

impl core::fmt::Display for ExtensionPackSize {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ExtensionPackSize::XXS => f.write_str("XXS"),
            ExtensionPackSize::XS => f.write_str("XS"),
            ExtensionPackSize::S => f.write_str("S"),
            ExtensionPackSize::M => f.write_str("M"),
            ExtensionPackSize::L => f.write_str("L"),
            ExtensionPackSize::XL => f.write_str("XL"),
            ExtensionPackSize::XXL => f.write_str("XXL"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ExtensionPackSize {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ExtensionPackSize::XXS => "XXS",
            ExtensionPackSize::XS => "XS",
            ExtensionPackSize::S => "S",
            ExtensionPackSize::M => "M",
            ExtensionPackSize::L => "L",
            ExtensionPackSize::XL => "XL",
            ExtensionPackSize::XXL => "XXL",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ExtensionPackSize {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "XXS" => Ok(ExtensionPackSize::XXS),
                "XS" => Ok(ExtensionPackSize::XS),
                "S" => Ok(ExtensionPackSize::S),
                "M" => Ok(ExtensionPackSize::M),
                "L" => Ok(ExtensionPackSize::L),
                "XL" => Ok(ExtensionPackSize::XL),
                "XXL" => Ok(ExtensionPackSize::XXL),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ExtensionPackSize: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ExtensionPackSize)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ExtensionPackSize {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum GlobalComponentBusinessAreaEnum {
    PRETRADE,
    TRADE,
    POSTTRADE,
    INFRASTRUCTURE,
}

impl core::fmt::Display for GlobalComponentBusinessAreaEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            GlobalComponentBusinessAreaEnum::PRETRADE => f.write_str("PRE_TRADE"),
            GlobalComponentBusinessAreaEnum::TRADE => f.write_str("TRADE"),
            GlobalComponentBusinessAreaEnum::POSTTRADE => f.write_str("POST_TRADE"),
            GlobalComponentBusinessAreaEnum::INFRASTRUCTURE => f.write_str("INFRASTRUCTURE"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for GlobalComponentBusinessAreaEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            GlobalComponentBusinessAreaEnum::PRETRADE => "PRE_TRADE",
            GlobalComponentBusinessAreaEnum::TRADE => "TRADE",
            GlobalComponentBusinessAreaEnum::POSTTRADE => "POST_TRADE",
            GlobalComponentBusinessAreaEnum::INFRASTRUCTURE => "INFRASTRUCTURE",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for GlobalComponentBusinessAreaEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "PRE_TRADE" | "PRETRADE" => Ok(GlobalComponentBusinessAreaEnum::PRETRADE),
                "TRADE" => Ok(GlobalComponentBusinessAreaEnum::TRADE),
                "POST_TRADE" | "POSTTRADE" => Ok(GlobalComponentBusinessAreaEnum::POSTTRADE),
                "INFRASTRUCTURE" => Ok(GlobalComponentBusinessAreaEnum::INFRASTRUCTURE),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for GlobalComponentBusinessAreaEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(GlobalComponentBusinessAreaEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for GlobalComponentBusinessAreaEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum BusinessAreaEnum {
    INTRODUCTION,
    PRETRADE,
    TRADE,
    POSTTRADE,
    INFRASTRUCTURE,
}

impl core::fmt::Display for BusinessAreaEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            BusinessAreaEnum::INTRODUCTION => f.write_str("INTRODUCTION"),
            BusinessAreaEnum::PRETRADE => f.write_str("PRE_TRADE"),
            BusinessAreaEnum::TRADE => f.write_str("TRADE"),
            BusinessAreaEnum::POSTTRADE => f.write_str("POST_TRADE"),
            BusinessAreaEnum::INFRASTRUCTURE => f.write_str("INFRASTRUCTURE"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for BusinessAreaEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            BusinessAreaEnum::INTRODUCTION => "INTRODUCTION",
            BusinessAreaEnum::PRETRADE => "PRE_TRADE",
            BusinessAreaEnum::TRADE => "TRADE",
            BusinessAreaEnum::POSTTRADE => "POST_TRADE",
            BusinessAreaEnum::INFRASTRUCTURE => "INFRASTRUCTURE",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for BusinessAreaEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "INTRODUCTION" => Ok(BusinessAreaEnum::INTRODUCTION),
                "PRE_TRADE" | "PRETRADE" => Ok(BusinessAreaEnum::PRETRADE),
                "TRADE" => Ok(BusinessAreaEnum::TRADE),
                "POST_TRADE" | "POSTTRADE" => Ok(BusinessAreaEnum::POSTTRADE),
                "INFRASTRUCTURE" => Ok(BusinessAreaEnum::INFRASTRUCTURE),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for BusinessAreaEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(BusinessAreaEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for BusinessAreaEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum MessageCategoryEnum {
    INDICATION,
    EVENTCOMMUNICATION,
    QUOTATIONNEGOTIATION,
    MARKETDATA,
    MARKETSTRUCTUREREFERENCEDATA,
    SECURITIESREFERENCEDATA,
    PARTIESREFERENCEDATA,
    PARTIESACTION,
    SINGLEGENERALORDERHANDLING,
    ORDERMASSHANDLING,
    CROSSORDERS,
    MULTILEGORDERS,
    LISTPROGRAMBASKETTRADING,
    ALLOCATIONANDREADYTOBOOK,
    CONFIRMATION,
    SETTLEMENTINSTRUCTIONS,
    TRADECAPTUREREPORTING,
    REGISTRATIONINSTRUCTIONS,
    POSITIONSMAINTENANCE,
    COLLATERALMANAGEMENT,
    MARGINREQUIREMENTMANAGEMENT,
    ACCOUNTREPORTING,
    TRADEMANAGEMENT,
    PAYMANAGEMENT,
    SETTLEMENTSTATUSMANAGEMENT,
    BUSINESSMESSAGEREJECTS,
    NETWORKSTATUSCOMMUNICATION,
    USERMANAGEMENT,
    APPLICATIONSEQUENCING,
}

impl core::fmt::Display for MessageCategoryEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            MessageCategoryEnum::INDICATION => f.write_str("INDICATION"),
            MessageCategoryEnum::EVENTCOMMUNICATION => f.write_str("EVENT_COMMUNICATION"),
            MessageCategoryEnum::QUOTATIONNEGOTIATION => f.write_str("QUOTATION_NEGOTIATION"),
            MessageCategoryEnum::MARKETDATA => f.write_str("MARKET_DATA"),
            MessageCategoryEnum::MARKETSTRUCTUREREFERENCEDATA => f.write_str("MARKET_STRUCTURE_REFERENCE_DATA"),
            MessageCategoryEnum::SECURITIESREFERENCEDATA => f.write_str("SECURITIES_REFERENCE_DATA"),
            MessageCategoryEnum::PARTIESREFERENCEDATA => f.write_str("PARTIES_REFERENCE_DATA"),
            MessageCategoryEnum::PARTIESACTION => f.write_str("PARTIES_ACTION"),
            MessageCategoryEnum::SINGLEGENERALORDERHANDLING => f.write_str("SINGLE_GENERAL_ORDER_HANDLING"),
            MessageCategoryEnum::ORDERMASSHANDLING => f.write_str("ORDER_MASS_HANDLING"),
            MessageCategoryEnum::CROSSORDERS => f.write_str("CROSS_ORDERS"),
            MessageCategoryEnum::MULTILEGORDERS => f.write_str("MULTILEG_ORDERS"),
            MessageCategoryEnum::LISTPROGRAMBASKETTRADING => f.write_str("LIST_PROGRAM_BASKET_TRADING"),
            MessageCategoryEnum::ALLOCATIONANDREADYTOBOOK => f.write_str("ALLOCATION_AND_READY_TO_BOOK"),
            MessageCategoryEnum::CONFIRMATION => f.write_str("CONFIRMATION"),
            MessageCategoryEnum::SETTLEMENTINSTRUCTIONS => f.write_str("SETTLEMENT_INSTRUCTIONS"),
            MessageCategoryEnum::TRADECAPTUREREPORTING => f.write_str("TRADE_CAPTURE_REPORTING"),
            MessageCategoryEnum::REGISTRATIONINSTRUCTIONS => f.write_str("REGISTRATION_INSTRUCTIONS"),
            MessageCategoryEnum::POSITIONSMAINTENANCE => f.write_str("POSITIONS_MAINTENANCE"),
            MessageCategoryEnum::COLLATERALMANAGEMENT => f.write_str("COLLATERAL_MANAGEMENT"),
            MessageCategoryEnum::MARGINREQUIREMENTMANAGEMENT => f.write_str("MARGIN_REQUIREMENT_MANAGEMENT"),
            MessageCategoryEnum::ACCOUNTREPORTING => f.write_str("ACCOUNT_REPORTING"),
            MessageCategoryEnum::TRADEMANAGEMENT => f.write_str("TRADE_MANAGEMENT"),
            MessageCategoryEnum::PAYMANAGEMENT => f.write_str("PAY_MANAGEMENT"),
            MessageCategoryEnum::SETTLEMENTSTATUSMANAGEMENT => f.write_str("SETTLEMENT_STATUS_MANAGEMENT"),
            MessageCategoryEnum::BUSINESSMESSAGEREJECTS => f.write_str("BUSINESS_MESSAGE_REJECTS"),
            MessageCategoryEnum::NETWORKSTATUSCOMMUNICATION => f.write_str("NETWORK_STATUS_COMMUNICATION"),
            MessageCategoryEnum::USERMANAGEMENT => f.write_str("USER_MANAGEMENT"),
            MessageCategoryEnum::APPLICATIONSEQUENCING => f.write_str("APPLICATION_SEQUENCING"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for MessageCategoryEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            MessageCategoryEnum::INDICATION => "INDICATION",
            MessageCategoryEnum::EVENTCOMMUNICATION => "EVENT_COMMUNICATION",
            MessageCategoryEnum::QUOTATIONNEGOTIATION => "QUOTATION_NEGOTIATION",
            MessageCategoryEnum::MARKETDATA => "MARKET_DATA",
            MessageCategoryEnum::MARKETSTRUCTUREREFERENCEDATA => "MARKET_STRUCTURE_REFERENCE_DATA",
            MessageCategoryEnum::SECURITIESREFERENCEDATA => "SECURITIES_REFERENCE_DATA",
            MessageCategoryEnum::PARTIESREFERENCEDATA => "PARTIES_REFERENCE_DATA",
            MessageCategoryEnum::PARTIESACTION => "PARTIES_ACTION",
            MessageCategoryEnum::SINGLEGENERALORDERHANDLING => "SINGLE_GENERAL_ORDER_HANDLING",
            MessageCategoryEnum::ORDERMASSHANDLING => "ORDER_MASS_HANDLING",
            MessageCategoryEnum::CROSSORDERS => "CROSS_ORDERS",
            MessageCategoryEnum::MULTILEGORDERS => "MULTILEG_ORDERS",
            MessageCategoryEnum::LISTPROGRAMBASKETTRADING => "LIST_PROGRAM_BASKET_TRADING",
            MessageCategoryEnum::ALLOCATIONANDREADYTOBOOK => "ALLOCATION_AND_READY_TO_BOOK",
            MessageCategoryEnum::CONFIRMATION => "CONFIRMATION",
            MessageCategoryEnum::SETTLEMENTINSTRUCTIONS => "SETTLEMENT_INSTRUCTIONS",
            MessageCategoryEnum::TRADECAPTUREREPORTING => "TRADE_CAPTURE_REPORTING",
            MessageCategoryEnum::REGISTRATIONINSTRUCTIONS => "REGISTRATION_INSTRUCTIONS",
            MessageCategoryEnum::POSITIONSMAINTENANCE => "POSITIONS_MAINTENANCE",
            MessageCategoryEnum::COLLATERALMANAGEMENT => "COLLATERAL_MANAGEMENT",
            MessageCategoryEnum::MARGINREQUIREMENTMANAGEMENT => "MARGIN_REQUIREMENT_MANAGEMENT",
            MessageCategoryEnum::ACCOUNTREPORTING => "ACCOUNT_REPORTING",
            MessageCategoryEnum::TRADEMANAGEMENT => "TRADE_MANAGEMENT",
            MessageCategoryEnum::PAYMANAGEMENT => "PAY_MANAGEMENT",
            MessageCategoryEnum::SETTLEMENTSTATUSMANAGEMENT => "SETTLEMENT_STATUS_MANAGEMENT",
            MessageCategoryEnum::BUSINESSMESSAGEREJECTS => "BUSINESS_MESSAGE_REJECTS",
            MessageCategoryEnum::NETWORKSTATUSCOMMUNICATION => "NETWORK_STATUS_COMMUNICATION",
            MessageCategoryEnum::USERMANAGEMENT => "USER_MANAGEMENT",
            MessageCategoryEnum::APPLICATIONSEQUENCING => "APPLICATION_SEQUENCING",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for MessageCategoryEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "INDICATION" => Ok(MessageCategoryEnum::INDICATION),
                "EVENT_COMMUNICATION" | "EVENTCOMMUNICATION" => Ok(MessageCategoryEnum::EVENTCOMMUNICATION),
                "QUOTATION_NEGOTIATION" | "QUOTATIONNEGOTIATION" => Ok(MessageCategoryEnum::QUOTATIONNEGOTIATION),
                "MARKET_DATA" | "MARKETDATA" => Ok(MessageCategoryEnum::MARKETDATA),
                "MARKET_STRUCTURE_REFERENCE_DATA" | "MARKETSTRUCTUREREFERENCEDATA" => Ok(MessageCategoryEnum::MARKETSTRUCTUREREFERENCEDATA),
                "SECURITIES_REFERENCE_DATA" | "SECURITIESREFERENCEDATA" => Ok(MessageCategoryEnum::SECURITIESREFERENCEDATA),
                "PARTIES_REFERENCE_DATA" | "PARTIESREFERENCEDATA" => Ok(MessageCategoryEnum::PARTIESREFERENCEDATA),
                "PARTIES_ACTION" | "PARTIESACTION" => Ok(MessageCategoryEnum::PARTIESACTION),
                "SINGLE_GENERAL_ORDER_HANDLING" | "SINGLEGENERALORDERHANDLING" => Ok(MessageCategoryEnum::SINGLEGENERALORDERHANDLING),
                "ORDER_MASS_HANDLING" | "ORDERMASSHANDLING" => Ok(MessageCategoryEnum::ORDERMASSHANDLING),
                "CROSS_ORDERS" | "CROSSORDERS" => Ok(MessageCategoryEnum::CROSSORDERS),
                "MULTILEG_ORDERS" | "MULTILEGORDERS" => Ok(MessageCategoryEnum::MULTILEGORDERS),
                "LIST_PROGRAM_BASKET_TRADING" | "LISTPROGRAMBASKETTRADING" => Ok(MessageCategoryEnum::LISTPROGRAMBASKETTRADING),
                "ALLOCATION_AND_READY_TO_BOOK" | "ALLOCATIONANDREADYTOBOOK" => Ok(MessageCategoryEnum::ALLOCATIONANDREADYTOBOOK),
                "CONFIRMATION" => Ok(MessageCategoryEnum::CONFIRMATION),
                "SETTLEMENT_INSTRUCTIONS" | "SETTLEMENTINSTRUCTIONS" => Ok(MessageCategoryEnum::SETTLEMENTINSTRUCTIONS),
                "TRADE_CAPTURE_REPORTING" | "TRADECAPTUREREPORTING" => Ok(MessageCategoryEnum::TRADECAPTUREREPORTING),
                "REGISTRATION_INSTRUCTIONS" | "REGISTRATIONINSTRUCTIONS" => Ok(MessageCategoryEnum::REGISTRATIONINSTRUCTIONS),
                "POSITIONS_MAINTENANCE" | "POSITIONSMAINTENANCE" => Ok(MessageCategoryEnum::POSITIONSMAINTENANCE),
                "COLLATERAL_MANAGEMENT" | "COLLATERALMANAGEMENT" => Ok(MessageCategoryEnum::COLLATERALMANAGEMENT),
                "MARGIN_REQUIREMENT_MANAGEMENT" | "MARGINREQUIREMENTMANAGEMENT" => Ok(MessageCategoryEnum::MARGINREQUIREMENTMANAGEMENT),
                "ACCOUNT_REPORTING" | "ACCOUNTREPORTING" => Ok(MessageCategoryEnum::ACCOUNTREPORTING),
                "TRADE_MANAGEMENT" | "TRADEMANAGEMENT" => Ok(MessageCategoryEnum::TRADEMANAGEMENT),
                "PAY_MANAGEMENT" | "PAYMANAGEMENT" => Ok(MessageCategoryEnum::PAYMANAGEMENT),
                "SETTLEMENT_STATUS_MANAGEMENT" | "SETTLEMENTSTATUSMANAGEMENT" => Ok(MessageCategoryEnum::SETTLEMENTSTATUSMANAGEMENT),
                "BUSINESS_MESSAGE_REJECTS" | "BUSINESSMESSAGEREJECTS" => Ok(MessageCategoryEnum::BUSINESSMESSAGEREJECTS),
                "NETWORK_STATUS_COMMUNICATION" | "NETWORKSTATUSCOMMUNICATION" => Ok(MessageCategoryEnum::NETWORKSTATUSCOMMUNICATION),
                "USER_MANAGEMENT" | "USERMANAGEMENT" => Ok(MessageCategoryEnum::USERMANAGEMENT),
                "APPLICATION_SEQUENCING" | "APPLICATIONSEQUENCING" => Ok(MessageCategoryEnum::APPLICATIONSEQUENCING),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for MessageCategoryEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(MessageCategoryEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for MessageCategoryEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', 'SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDERS', 'MULTILEG_ORDERS', 'LIST_PROGRAM_BASKET_TRADING', 'ALLOCATION_AND_READY_TO_BOOK', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTIONS', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTIONS', 'POSITIONS_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', 'BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ComponentScope {
    GLOBAL,
    COMMON,
    SPECIFIC,
}

impl core::fmt::Display for ComponentScope {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ComponentScope::GLOBAL => f.write_str("GLOBAL"),
            ComponentScope::COMMON => f.write_str("COMMON"),
            ComponentScope::SPECIFIC => f.write_str("SPECIFIC"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ComponentScope {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ComponentScope::GLOBAL => "GLOBAL",
            ComponentScope::COMMON => "COMMON",
            ComponentScope::SPECIFIC => "SPECIFIC",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ComponentScope {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "GLOBAL" => Ok(ComponentScope::GLOBAL),
                "COMMON" => Ok(ComponentScope::COMMON),
                "SPECIFIC" => Ok(ComponentScope::SPECIFIC),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ComponentScope: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ComponentScope)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ComponentScope {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['GLOBAL', 'COMMON', 'SPECIFIC']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ComponentGroup {
    SECURITIES,
    LEGSECURITIES,
    UNDERLYINGSECURITIES,
    PARTIES,
    ORDERSANDQUOTES,
    TRADES,
    COMMISSIONSANDFEES,
    FINANCING,
    PAYMENTS,
    STIPULATIONS,
    HEADERANDTRAILER,
    MISCELLANEOUS,
}

impl core::fmt::Display for ComponentGroup {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ComponentGroup::SECURITIES => f.write_str("SECURITIES"),
            ComponentGroup::LEGSECURITIES => f.write_str("LEG_SECURITIES"),
            ComponentGroup::UNDERLYINGSECURITIES => f.write_str("UNDERLYING_SECURITIES"),
            ComponentGroup::PARTIES => f.write_str("PARTIES"),
            ComponentGroup::ORDERSANDQUOTES => f.write_str("ORDERS_AND_QUOTES"),
            ComponentGroup::TRADES => f.write_str("TRADES"),
            ComponentGroup::COMMISSIONSANDFEES => f.write_str("COMMISSIONS_AND_FEES"),
            ComponentGroup::FINANCING => f.write_str("FINANCING"),
            ComponentGroup::PAYMENTS => f.write_str("PAYMENTS"),
            ComponentGroup::STIPULATIONS => f.write_str("STIPULATIONS"),
            ComponentGroup::HEADERANDTRAILER => f.write_str("HEADER_AND_TRAILER"),
            ComponentGroup::MISCELLANEOUS => f.write_str("MISCELLANEOUS"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ComponentGroup {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ComponentGroup::SECURITIES => "SECURITIES",
            ComponentGroup::LEGSECURITIES => "LEG_SECURITIES",
            ComponentGroup::UNDERLYINGSECURITIES => "UNDERLYING_SECURITIES",
            ComponentGroup::PARTIES => "PARTIES",
            ComponentGroup::ORDERSANDQUOTES => "ORDERS_AND_QUOTES",
            ComponentGroup::TRADES => "TRADES",
            ComponentGroup::COMMISSIONSANDFEES => "COMMISSIONS_AND_FEES",
            ComponentGroup::FINANCING => "FINANCING",
            ComponentGroup::PAYMENTS => "PAYMENTS",
            ComponentGroup::STIPULATIONS => "STIPULATIONS",
            ComponentGroup::HEADERANDTRAILER => "HEADER_AND_TRAILER",
            ComponentGroup::MISCELLANEOUS => "MISCELLANEOUS",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ComponentGroup {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "SECURITIES" => Ok(ComponentGroup::SECURITIES),
                "LEG_SECURITIES" | "LEGSECURITIES" => Ok(ComponentGroup::LEGSECURITIES),
                "UNDERLYING_SECURITIES" | "UNDERLYINGSECURITIES" => Ok(ComponentGroup::UNDERLYINGSECURITIES),
                "PARTIES" => Ok(ComponentGroup::PARTIES),
                "ORDERS_AND_QUOTES" | "ORDERSANDQUOTES" => Ok(ComponentGroup::ORDERSANDQUOTES),
                "TRADES" => Ok(ComponentGroup::TRADES),
                "COMMISSIONS_AND_FEES" | "COMMISSIONSANDFEES" => Ok(ComponentGroup::COMMISSIONSANDFEES),
                "FINANCING" => Ok(ComponentGroup::FINANCING),
                "PAYMENTS" => Ok(ComponentGroup::PAYMENTS),
                "STIPULATIONS" => Ok(ComponentGroup::STIPULATIONS),
                "HEADER_AND_TRAILER" | "HEADERANDTRAILER" => Ok(ComponentGroup::HEADERANDTRAILER),
                "MISCELLANEOUS" => Ok(ComponentGroup::MISCELLANEOUS),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ComponentGroup: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ComponentGroup)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ComponentGroup {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['SECURITIES', 'LEG_SECURITIES', 'UNDERLYING_SECURITIES', 'PARTIES', 'ORDERS_AND_QUOTES', 'TRADES', 'COMMISSIONS_AND_FEES', 'FINANCING', 'PAYMENTS', 'STIPULATIONS', 'HEADER_AND_TRAILER', 'MISCELLANEOUS']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum FieldRequirement {
    REQUIRED,
    OPTIONAL,
    CONDITIONALLYREQUIRED,
}

impl core::fmt::Display for FieldRequirement {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            FieldRequirement::REQUIRED => f.write_str("REQUIRED"),
            FieldRequirement::OPTIONAL => f.write_str("OPTIONAL"),
            FieldRequirement::CONDITIONALLYREQUIRED => f.write_str("CONDITIONALLY_REQUIRED"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for FieldRequirement {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            FieldRequirement::REQUIRED => "REQUIRED",
            FieldRequirement::OPTIONAL => "OPTIONAL",
            FieldRequirement::CONDITIONALLYREQUIRED => "CONDITIONALLY_REQUIRED",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for FieldRequirement {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "REQUIRED" => Ok(FieldRequirement::REQUIRED),
                "OPTIONAL" => Ok(FieldRequirement::OPTIONAL),
                "CONDITIONALLY_REQUIRED" | "CONDITIONALLYREQUIRED" => Ok(FieldRequirement::CONDITIONALLYREQUIRED),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for FieldRequirement: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(FieldRequirement)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for FieldRequirement {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['REQUIRED', 'OPTIONAL', 'CONDITIONALLY_REQUIRED']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ProductCoverage {
    EQUITIES,
    CIV,
    DERIVATIVES,
    FIXEDINCOME,
    FOREIGNEXCHANGE,
}

impl core::fmt::Display for ProductCoverage {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ProductCoverage::EQUITIES => f.write_str("EQUITIES"),
            ProductCoverage::CIV => f.write_str("CIV"),
            ProductCoverage::DERIVATIVES => f.write_str("DERIVATIVES"),
            ProductCoverage::FIXEDINCOME => f.write_str("FIXED_INCOME"),
            ProductCoverage::FOREIGNEXCHANGE => f.write_str("FOREIGN_EXCHANGE"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ProductCoverage {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ProductCoverage::EQUITIES => "EQUITIES",
            ProductCoverage::CIV => "CIV",
            ProductCoverage::DERIVATIVES => "DERIVATIVES",
            ProductCoverage::FIXEDINCOME => "FIXED_INCOME",
            ProductCoverage::FOREIGNEXCHANGE => "FOREIGN_EXCHANGE",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ProductCoverage {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "EQUITIES" => Ok(ProductCoverage::EQUITIES),
                "CIV" => Ok(ProductCoverage::CIV),
                "DERIVATIVES" => Ok(ProductCoverage::DERIVATIVES),
                "FIXED_INCOME" | "FIXEDINCOME" => Ok(ProductCoverage::FIXEDINCOME),
                "FOREIGN_EXCHANGE" | "FOREIGNEXCHANGE" => Ok(ProductCoverage::FOREIGNEXCHANGE),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ProductCoverage: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ProductCoverage)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ProductCoverage {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['EQUITIES', 'CIV', 'DERIVATIVES', 'FIXED_INCOME', 'FOREIGN_EXCHANGE']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum FIXDatatypeName {
    Int,
    TagNum,
    SeqNum,
    NumInGroup,
    DayOfMonth,
    Float,
    Qty,
    Price,
    PriceOffset,
    Amt,
    Percentage,
    Char,
    Boolean,
    String,
    MultipleCharValue,
    MultipleStringValue,
    Country,
    Currency,
    Exchange,
    MonthYear,
    UTCTimestamp,
    UTCTimeOnly,
    UTCDateOnly,
    LocalMktDate,
    TZTimeOnly,
    TZTimestamp,
    Length,
    Data,
    Tenor,
    Reserved100Plus,
    Reserved1000Plus,
    Reserved4000Plus,
    XMLData,
    Language,
    LocalMktTime,
}

impl core::fmt::Display for FIXDatatypeName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            FIXDatatypeName::Int => f.write_str("int"),
            FIXDatatypeName::TagNum => f.write_str("TagNum"),
            FIXDatatypeName::SeqNum => f.write_str("SeqNum"),
            FIXDatatypeName::NumInGroup => f.write_str("NumInGroup"),
            FIXDatatypeName::DayOfMonth => f.write_str("DayOfMonth"),
            FIXDatatypeName::Float => f.write_str("float"),
            FIXDatatypeName::Qty => f.write_str("Qty"),
            FIXDatatypeName::Price => f.write_str("Price"),
            FIXDatatypeName::PriceOffset => f.write_str("PriceOffset"),
            FIXDatatypeName::Amt => f.write_str("Amt"),
            FIXDatatypeName::Percentage => f.write_str("Percentage"),
            FIXDatatypeName::Char => f.write_str("char"),
            FIXDatatypeName::Boolean => f.write_str("Boolean"),
            FIXDatatypeName::String => f.write_str("String"),
            FIXDatatypeName::MultipleCharValue => f.write_str("MultipleCharValue"),
            FIXDatatypeName::MultipleStringValue => f.write_str("MultipleStringValue"),
            FIXDatatypeName::Country => f.write_str("Country"),
            FIXDatatypeName::Currency => f.write_str("Currency"),
            FIXDatatypeName::Exchange => f.write_str("Exchange"),
            FIXDatatypeName::MonthYear => f.write_str("MonthYear"),
            FIXDatatypeName::UTCTimestamp => f.write_str("UTCTimestamp"),
            FIXDatatypeName::UTCTimeOnly => f.write_str("UTCTimeOnly"),
            FIXDatatypeName::UTCDateOnly => f.write_str("UTCDateOnly"),
            FIXDatatypeName::LocalMktDate => f.write_str("LocalMktDate"),
            FIXDatatypeName::TZTimeOnly => f.write_str("TZTimeOnly"),
            FIXDatatypeName::TZTimestamp => f.write_str("TZTimestamp"),
            FIXDatatypeName::Length => f.write_str("Length"),
            FIXDatatypeName::Data => f.write_str("data"),
            FIXDatatypeName::Tenor => f.write_str("Tenor"),
            FIXDatatypeName::Reserved100Plus => f.write_str("Reserved100Plus"),
            FIXDatatypeName::Reserved1000Plus => f.write_str("Reserved1000Plus"),
            FIXDatatypeName::Reserved4000Plus => f.write_str("Reserved4000Plus"),
            FIXDatatypeName::XMLData => f.write_str("XMLData"),
            FIXDatatypeName::Language => f.write_str("Language"),
            FIXDatatypeName::LocalMktTime => f.write_str("LocalMktTime"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for FIXDatatypeName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            FIXDatatypeName::Int => "int",
            FIXDatatypeName::TagNum => "TagNum",
            FIXDatatypeName::SeqNum => "SeqNum",
            FIXDatatypeName::NumInGroup => "NumInGroup",
            FIXDatatypeName::DayOfMonth => "DayOfMonth",
            FIXDatatypeName::Float => "float",
            FIXDatatypeName::Qty => "Qty",
            FIXDatatypeName::Price => "Price",
            FIXDatatypeName::PriceOffset => "PriceOffset",
            FIXDatatypeName::Amt => "Amt",
            FIXDatatypeName::Percentage => "Percentage",
            FIXDatatypeName::Char => "char",
            FIXDatatypeName::Boolean => "Boolean",
            FIXDatatypeName::String => "String",
            FIXDatatypeName::MultipleCharValue => "MultipleCharValue",
            FIXDatatypeName::MultipleStringValue => "MultipleStringValue",
            FIXDatatypeName::Country => "Country",
            FIXDatatypeName::Currency => "Currency",
            FIXDatatypeName::Exchange => "Exchange",
            FIXDatatypeName::MonthYear => "MonthYear",
            FIXDatatypeName::UTCTimestamp => "UTCTimestamp",
            FIXDatatypeName::UTCTimeOnly => "UTCTimeOnly",
            FIXDatatypeName::UTCDateOnly => "UTCDateOnly",
            FIXDatatypeName::LocalMktDate => "LocalMktDate",
            FIXDatatypeName::TZTimeOnly => "TZTimeOnly",
            FIXDatatypeName::TZTimestamp => "TZTimestamp",
            FIXDatatypeName::Length => "Length",
            FIXDatatypeName::Data => "data",
            FIXDatatypeName::Tenor => "Tenor",
            FIXDatatypeName::Reserved100Plus => "Reserved100Plus",
            FIXDatatypeName::Reserved1000Plus => "Reserved1000Plus",
            FIXDatatypeName::Reserved4000Plus => "Reserved4000Plus",
            FIXDatatypeName::XMLData => "XMLData",
            FIXDatatypeName::Language => "Language",
            FIXDatatypeName::LocalMktTime => "LocalMktTime",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for FIXDatatypeName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "int" | "Int" => Ok(FIXDatatypeName::Int),
                "TagNum" => Ok(FIXDatatypeName::TagNum),
                "SeqNum" => Ok(FIXDatatypeName::SeqNum),
                "NumInGroup" => Ok(FIXDatatypeName::NumInGroup),
                "DayOfMonth" => Ok(FIXDatatypeName::DayOfMonth),
                "float" | "Float" => Ok(FIXDatatypeName::Float),
                "Qty" => Ok(FIXDatatypeName::Qty),
                "Price" => Ok(FIXDatatypeName::Price),
                "PriceOffset" => Ok(FIXDatatypeName::PriceOffset),
                "Amt" => Ok(FIXDatatypeName::Amt),
                "Percentage" => Ok(FIXDatatypeName::Percentage),
                "char" | "Char" => Ok(FIXDatatypeName::Char),
                "Boolean" => Ok(FIXDatatypeName::Boolean),
                "String" => Ok(FIXDatatypeName::String),
                "MultipleCharValue" => Ok(FIXDatatypeName::MultipleCharValue),
                "MultipleStringValue" => Ok(FIXDatatypeName::MultipleStringValue),
                "Country" => Ok(FIXDatatypeName::Country),
                "Currency" => Ok(FIXDatatypeName::Currency),
                "Exchange" => Ok(FIXDatatypeName::Exchange),
                "MonthYear" => Ok(FIXDatatypeName::MonthYear),
                "UTCTimestamp" => Ok(FIXDatatypeName::UTCTimestamp),
                "UTCTimeOnly" => Ok(FIXDatatypeName::UTCTimeOnly),
                "UTCDateOnly" => Ok(FIXDatatypeName::UTCDateOnly),
                "LocalMktDate" => Ok(FIXDatatypeName::LocalMktDate),
                "TZTimeOnly" => Ok(FIXDatatypeName::TZTimeOnly),
                "TZTimestamp" => Ok(FIXDatatypeName::TZTimestamp),
                "Length" => Ok(FIXDatatypeName::Length),
                "data" | "Data" => Ok(FIXDatatypeName::Data),
                "Tenor" => Ok(FIXDatatypeName::Tenor),
                "Reserved100Plus" => Ok(FIXDatatypeName::Reserved100Plus),
                "Reserved1000Plus" => Ok(FIXDatatypeName::Reserved1000Plus),
                "Reserved4000Plus" => Ok(FIXDatatypeName::Reserved4000Plus),
                "XMLData" => Ok(FIXDatatypeName::XMLData),
                "Language" => Ok(FIXDatatypeName::Language),
                "LocalMktTime" => Ok(FIXDatatypeName::LocalMktTime),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for FIXDatatypeName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(FIXDatatypeName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for FIXDatatypeName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['int', 'TagNum', 'SeqNum', 'NumInGroup', 'DayOfMonth', 'float', 'Qty', 'Price', 'PriceOffset', 'Amt', 'Percentage', 'char', 'Boolean', 'String', 'MultipleCharValue', 'MultipleStringValue', 'Country', 'Currency', 'Exchange', 'MonthYear', 'UTCTimestamp', 'UTCTimeOnly', 'UTCDateOnly', 'LocalMktDate', 'TZTimeOnly', 'TZTimestamp', 'Length', 'data', 'Tenor', 'Reserved100Plus', 'Reserved1000Plus', 'Reserved4000Plus', 'XMLData', 'Language', 'LocalMktTime']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ISO11404ValueSpace {
    Integer,
    Ordinal,
    Size,
    Real,
    Scaled,
    Character,
    Characterstring,
    Boolean,
    Set,
    Array,
    Time,
    Union,
}

impl core::fmt::Display for ISO11404ValueSpace {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ISO11404ValueSpace::Integer => f.write_str("integer"),
            ISO11404ValueSpace::Ordinal => f.write_str("ordinal"),
            ISO11404ValueSpace::Size => f.write_str("size"),
            ISO11404ValueSpace::Real => f.write_str("real"),
            ISO11404ValueSpace::Scaled => f.write_str("scaled"),
            ISO11404ValueSpace::Character => f.write_str("character"),
            ISO11404ValueSpace::Characterstring => f.write_str("characterstring"),
            ISO11404ValueSpace::Boolean => f.write_str("boolean"),
            ISO11404ValueSpace::Set => f.write_str("set"),
            ISO11404ValueSpace::Array => f.write_str("array"),
            ISO11404ValueSpace::Time => f.write_str("time"),
            ISO11404ValueSpace::Union => f.write_str("union"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ISO11404ValueSpace {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ISO11404ValueSpace::Integer => "integer",
            ISO11404ValueSpace::Ordinal => "ordinal",
            ISO11404ValueSpace::Size => "size",
            ISO11404ValueSpace::Real => "real",
            ISO11404ValueSpace::Scaled => "scaled",
            ISO11404ValueSpace::Character => "character",
            ISO11404ValueSpace::Characterstring => "characterstring",
            ISO11404ValueSpace::Boolean => "boolean",
            ISO11404ValueSpace::Set => "set",
            ISO11404ValueSpace::Array => "array",
            ISO11404ValueSpace::Time => "time",
            ISO11404ValueSpace::Union => "union",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ISO11404ValueSpace {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "integer" | "Integer" => Ok(ISO11404ValueSpace::Integer),
                "ordinal" | "Ordinal" => Ok(ISO11404ValueSpace::Ordinal),
                "size" | "Size" => Ok(ISO11404ValueSpace::Size),
                "real" | "Real" => Ok(ISO11404ValueSpace::Real),
                "scaled" | "Scaled" => Ok(ISO11404ValueSpace::Scaled),
                "character" | "Character" => Ok(ISO11404ValueSpace::Character),
                "characterstring" | "Characterstring" => Ok(ISO11404ValueSpace::Characterstring),
                "boolean" | "Boolean" => Ok(ISO11404ValueSpace::Boolean),
                "set" | "Set" => Ok(ISO11404ValueSpace::Set),
                "array" | "Array" => Ok(ISO11404ValueSpace::Array),
                "time" | "Time" => Ok(ISO11404ValueSpace::Time),
                "union" | "Union" => Ok(ISO11404ValueSpace::Union),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ISO11404ValueSpace: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ISO11404ValueSpace)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ISO11404ValueSpace {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['integer', 'ordinal', 'size', 'real', 'scaled', 'character', 'characterstring', 'boolean', 'set', 'array', 'time', 'union']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TenorUnit {
    D,
    W,
    M,
    Y,
}

impl core::fmt::Display for TenorUnit {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TenorUnit::D => f.write_str("D"),
            TenorUnit::W => f.write_str("W"),
            TenorUnit::M => f.write_str("M"),
            TenorUnit::Y => f.write_str("Y"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TenorUnit {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TenorUnit::D => "D",
            TenorUnit::W => "W",
            TenorUnit::M => "M",
            TenorUnit::Y => "Y",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TenorUnit {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "D" => Ok(TenorUnit::D),
                "W" => Ok(TenorUnit::W),
                "M" => Ok(TenorUnit::M),
                "Y" => Ok(TenorUnit::Y),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TenorUnit: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TenorUnit)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TenorUnit {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['D', 'W', 'M', 'Y']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum StandardEncodingName {
    TAGVALUE,
    FIXML,
    FAST,
    SBE,
    GPB,
    JSON,
    ASN1,
}

impl core::fmt::Display for StandardEncodingName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            StandardEncodingName::TAGVALUE => f.write_str("TAGVALUE"),
            StandardEncodingName::FIXML => f.write_str("FIXML"),
            StandardEncodingName::FAST => f.write_str("FAST"),
            StandardEncodingName::SBE => f.write_str("SBE"),
            StandardEncodingName::GPB => f.write_str("GPB"),
            StandardEncodingName::JSON => f.write_str("JSON"),
            StandardEncodingName::ASN1 => f.write_str("ASN_1"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for StandardEncodingName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            StandardEncodingName::TAGVALUE => "TAGVALUE",
            StandardEncodingName::FIXML => "FIXML",
            StandardEncodingName::FAST => "FAST",
            StandardEncodingName::SBE => "SBE",
            StandardEncodingName::GPB => "GPB",
            StandardEncodingName::JSON => "JSON",
            StandardEncodingName::ASN1 => "ASN_1",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for StandardEncodingName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "TAGVALUE" => Ok(StandardEncodingName::TAGVALUE),
                "FIXML" => Ok(StandardEncodingName::FIXML),
                "FAST" => Ok(StandardEncodingName::FAST),
                "SBE" => Ok(StandardEncodingName::SBE),
                "GPB" => Ok(StandardEncodingName::GPB),
                "JSON" => Ok(StandardEncodingName::JSON),
                "ASN_1" | "ASN1" => Ok(StandardEncodingName::ASN1),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for StandardEncodingName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(StandardEncodingName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for StandardEncodingName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['TAGVALUE', 'FIXML', 'FAST', 'SBE', 'GPB', 'JSON', 'ASN_1']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum SessionProtocolName {
    FIX42,
    FIX4,
    FIXT,
    LFIXT,
    FIXP,
    SOFH,
    FIXS,
    AMQP,
}

impl core::fmt::Display for SessionProtocolName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            SessionProtocolName::FIX42 => f.write_str("FIX_4_2"),
            SessionProtocolName::FIX4 => f.write_str("FIX4"),
            SessionProtocolName::FIXT => f.write_str("FIXT"),
            SessionProtocolName::LFIXT => f.write_str("LFIXT"),
            SessionProtocolName::FIXP => f.write_str("FIXP"),
            SessionProtocolName::SOFH => f.write_str("SOFH"),
            SessionProtocolName::FIXS => f.write_str("FIXS"),
            SessionProtocolName::AMQP => f.write_str("AMQP"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for SessionProtocolName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            SessionProtocolName::FIX42 => "FIX_4_2",
            SessionProtocolName::FIX4 => "FIX4",
            SessionProtocolName::FIXT => "FIXT",
            SessionProtocolName::LFIXT => "LFIXT",
            SessionProtocolName::FIXP => "FIXP",
            SessionProtocolName::SOFH => "SOFH",
            SessionProtocolName::FIXS => "FIXS",
            SessionProtocolName::AMQP => "AMQP",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for SessionProtocolName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "FIX_4_2" | "FIX42" => Ok(SessionProtocolName::FIX42),
                "FIX4" => Ok(SessionProtocolName::FIX4),
                "FIXT" => Ok(SessionProtocolName::FIXT),
                "LFIXT" => Ok(SessionProtocolName::LFIXT),
                "FIXP" => Ok(SessionProtocolName::FIXP),
                "SOFH" => Ok(SessionProtocolName::SOFH),
                "FIXS" => Ok(SessionProtocolName::FIXS),
                "AMQP" => Ok(SessionProtocolName::AMQP),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for SessionProtocolName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(SessionProtocolName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for SessionProtocolName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['FIX_4_2', 'FIX4', 'FIXT', 'LFIXT', 'FIXP', 'SOFH', 'FIXS', 'AMQP']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TimePrecision {
    SECOND,
    MILLISECOND,
    MICROSECOND,
    NANOSECOND,
    PICOSECOND,
    DAY,
}

impl core::fmt::Display for TimePrecision {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TimePrecision::SECOND => f.write_str("SECOND"),
            TimePrecision::MILLISECOND => f.write_str("MILLISECOND"),
            TimePrecision::MICROSECOND => f.write_str("MICROSECOND"),
            TimePrecision::NANOSECOND => f.write_str("NANOSECOND"),
            TimePrecision::PICOSECOND => f.write_str("PICOSECOND"),
            TimePrecision::DAY => f.write_str("DAY"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TimePrecision {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TimePrecision::SECOND => "SECOND",
            TimePrecision::MILLISECOND => "MILLISECOND",
            TimePrecision::MICROSECOND => "MICROSECOND",
            TimePrecision::NANOSECOND => "NANOSECOND",
            TimePrecision::PICOSECOND => "PICOSECOND",
            TimePrecision::DAY => "DAY",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TimePrecision {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "SECOND" => Ok(TimePrecision::SECOND),
                "MILLISECOND" => Ok(TimePrecision::MILLISECOND),
                "MICROSECOND" => Ok(TimePrecision::MICROSECOND),
                "NANOSECOND" => Ok(TimePrecision::NANOSECOND),
                "PICOSECOND" => Ok(TimePrecision::PICOSECOND),
                "DAY" => Ok(TimePrecision::DAY),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TimePrecision: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TimePrecision)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TimePrecision {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['SECOND', 'MILLISECOND', 'MICROSECOND', 'NANOSECOND', 'PICOSECOND', 'DAY']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum FPLCommitteeRole {
    GLOBALSTEERINGCOMMITTEE,
    GLOBALTECHNICALCOMMITTEE,
    GLOBALPRODUCTCOMMITTEE,
    GLOBALBUYSIDECOMMITTEE,
    GLOBALMEMBERSERVICESCOMMITTEE,
    REGIONALCOMMITTEE,
}

impl core::fmt::Display for FPLCommitteeRole {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            FPLCommitteeRole::GLOBALSTEERINGCOMMITTEE => f.write_str("GLOBAL_STEERING_COMMITTEE"),
            FPLCommitteeRole::GLOBALTECHNICALCOMMITTEE => f.write_str("GLOBAL_TECHNICAL_COMMITTEE"),
            FPLCommitteeRole::GLOBALPRODUCTCOMMITTEE => f.write_str("GLOBAL_PRODUCT_COMMITTEE"),
            FPLCommitteeRole::GLOBALBUYSIDECOMMITTEE => f.write_str("GLOBAL_BUY_SIDE_COMMITTEE"),
            FPLCommitteeRole::GLOBALMEMBERSERVICESCOMMITTEE => f.write_str("GLOBAL_MEMBER_SERVICES_COMMITTEE"),
            FPLCommitteeRole::REGIONALCOMMITTEE => f.write_str("REGIONAL_COMMITTEE"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for FPLCommitteeRole {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            FPLCommitteeRole::GLOBALSTEERINGCOMMITTEE => "GLOBAL_STEERING_COMMITTEE",
            FPLCommitteeRole::GLOBALTECHNICALCOMMITTEE => "GLOBAL_TECHNICAL_COMMITTEE",
            FPLCommitteeRole::GLOBALPRODUCTCOMMITTEE => "GLOBAL_PRODUCT_COMMITTEE",
            FPLCommitteeRole::GLOBALBUYSIDECOMMITTEE => "GLOBAL_BUY_SIDE_COMMITTEE",
            FPLCommitteeRole::GLOBALMEMBERSERVICESCOMMITTEE => "GLOBAL_MEMBER_SERVICES_COMMITTEE",
            FPLCommitteeRole::REGIONALCOMMITTEE => "REGIONAL_COMMITTEE",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for FPLCommitteeRole {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "GLOBAL_STEERING_COMMITTEE" | "GLOBALSTEERINGCOMMITTEE" => Ok(FPLCommitteeRole::GLOBALSTEERINGCOMMITTEE),
                "GLOBAL_TECHNICAL_COMMITTEE" | "GLOBALTECHNICALCOMMITTEE" => Ok(FPLCommitteeRole::GLOBALTECHNICALCOMMITTEE),
                "GLOBAL_PRODUCT_COMMITTEE" | "GLOBALPRODUCTCOMMITTEE" => Ok(FPLCommitteeRole::GLOBALPRODUCTCOMMITTEE),
                "GLOBAL_BUY_SIDE_COMMITTEE" | "GLOBALBUYSIDECOMMITTEE" => Ok(FPLCommitteeRole::GLOBALBUYSIDECOMMITTEE),
                "GLOBAL_MEMBER_SERVICES_COMMITTEE" | "GLOBALMEMBERSERVICESCOMMITTEE" => Ok(FPLCommitteeRole::GLOBALMEMBERSERVICESCOMMITTEE),
                "REGIONAL_COMMITTEE" | "REGIONALCOMMITTEE" => Ok(FPLCommitteeRole::REGIONALCOMMITTEE),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for FPLCommitteeRole: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(FPLCommitteeRole)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for FPLCommitteeRole {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['GLOBAL_STEERING_COMMITTEE', 'GLOBAL_TECHNICAL_COMMITTEE', 'GLOBAL_PRODUCT_COMMITTEE', 'GLOBAL_BUY_SIDE_COMMITTEE', 'GLOBAL_MEMBER_SERVICES_COMMITTEE', 'REGIONAL_COMMITTEE']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum FPLRegion {
    AMERICAS,
    ASIAPACIFIC,
    EMEA,
    JAPAN,
}

impl core::fmt::Display for FPLRegion {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            FPLRegion::AMERICAS => f.write_str("AMERICAS"),
            FPLRegion::ASIAPACIFIC => f.write_str("ASIA_PACIFIC"),
            FPLRegion::EMEA => f.write_str("EMEA"),
            FPLRegion::JAPAN => f.write_str("JAPAN"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for FPLRegion {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            FPLRegion::AMERICAS => "AMERICAS",
            FPLRegion::ASIAPACIFIC => "ASIA_PACIFIC",
            FPLRegion::EMEA => "EMEA",
            FPLRegion::JAPAN => "JAPAN",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for FPLRegion {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "AMERICAS" => Ok(FPLRegion::AMERICAS),
                "ASIA_PACIFIC" | "ASIAPACIFIC" => Ok(FPLRegion::ASIAPACIFIC),
                "EMEA" => Ok(FPLRegion::EMEA),
                "JAPAN" => Ok(FPLRegion::JAPAN),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for FPLRegion: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(FPLRegion)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for FPLRegion {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['AMERICAS', 'ASIA_PACIFIC', 'EMEA', 'JAPAN']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum FPLProductGroup {
    FIXEDINCOMEANDCURRENCIES,
    LISTEDPRODUCTSANDEXCHANGES,
}

impl core::fmt::Display for FPLProductGroup {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            FPLProductGroup::FIXEDINCOMEANDCURRENCIES => f.write_str("FIXED_INCOME_AND_CURRENCIES"),
            FPLProductGroup::LISTEDPRODUCTSANDEXCHANGES => f.write_str("LISTED_PRODUCTS_AND_EXCHANGES"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for FPLProductGroup {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            FPLProductGroup::FIXEDINCOMEANDCURRENCIES => "FIXED_INCOME_AND_CURRENCIES",
            FPLProductGroup::LISTEDPRODUCTSANDEXCHANGES => "LISTED_PRODUCTS_AND_EXCHANGES",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for FPLProductGroup {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "FIXED_INCOME_AND_CURRENCIES" | "FIXEDINCOMEANDCURRENCIES" => Ok(FPLProductGroup::FIXEDINCOMEANDCURRENCIES),
                "LISTED_PRODUCTS_AND_EXCHANGES" | "LISTEDPRODUCTSANDEXCHANGES" => Ok(FPLProductGroup::LISTEDPRODUCTSANDEXCHANGES),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for FPLProductGroup: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(FPLProductGroup)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for FPLProductGroup {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['FIXED_INCOME_AND_CURRENCIES', 'LISTED_PRODUCTS_AND_EXCHANGES']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum FPLMemberType {
    BUYSIDEFIRM,
    SELLSIDEFIRM,
    EXCHANGE,
    ECNATS,
    UTILITY,
    VENDOR,
    OTHERASSOCIATION,
}

impl core::fmt::Display for FPLMemberType {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            FPLMemberType::BUYSIDEFIRM => f.write_str("BUY_SIDE_FIRM"),
            FPLMemberType::SELLSIDEFIRM => f.write_str("SELL_SIDE_FIRM"),
            FPLMemberType::EXCHANGE => f.write_str("EXCHANGE"),
            FPLMemberType::ECNATS => f.write_str("ECN_ATS"),
            FPLMemberType::UTILITY => f.write_str("UTILITY"),
            FPLMemberType::VENDOR => f.write_str("VENDOR"),
            FPLMemberType::OTHERASSOCIATION => f.write_str("OTHER_ASSOCIATION"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for FPLMemberType {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            FPLMemberType::BUYSIDEFIRM => "BUY_SIDE_FIRM",
            FPLMemberType::SELLSIDEFIRM => "SELL_SIDE_FIRM",
            FPLMemberType::EXCHANGE => "EXCHANGE",
            FPLMemberType::ECNATS => "ECN_ATS",
            FPLMemberType::UTILITY => "UTILITY",
            FPLMemberType::VENDOR => "VENDOR",
            FPLMemberType::OTHERASSOCIATION => "OTHER_ASSOCIATION",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for FPLMemberType {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "BUY_SIDE_FIRM" | "BUYSIDEFIRM" => Ok(FPLMemberType::BUYSIDEFIRM),
                "SELL_SIDE_FIRM" | "SELLSIDEFIRM" => Ok(FPLMemberType::SELLSIDEFIRM),
                "EXCHANGE" => Ok(FPLMemberType::EXCHANGE),
                "ECN_ATS" | "ECNATS" => Ok(FPLMemberType::ECNATS),
                "UTILITY" => Ok(FPLMemberType::UTILITY),
                "VENDOR" => Ok(FPLMemberType::VENDOR),
                "OTHER_ASSOCIATION" | "OTHERASSOCIATION" => Ok(FPLMemberType::OTHERASSOCIATION),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for FPLMemberType: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(FPLMemberType)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for FPLMemberType {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['BUY_SIDE_FIRM', 'SELL_SIDE_FIRM', 'EXCHANGE', 'ECN_ATS', 'UTILITY', 'VENDOR', 'OTHER_ASSOCIATION']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum UDFTagRangeUsage {
    INTERFIRMREGISTERED,
    INTERFIRMBILATERAL,
    GTCREGULATORYLEGACY,
    WIPCHINA,
    INTERNALFIRM,
    GTCOTCDERIVATIVES,
    GTCRESERVED,
}

impl core::fmt::Display for UDFTagRangeUsage {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            UDFTagRangeUsage::INTERFIRMREGISTERED => f.write_str("INTER_FIRM_REGISTERED"),
            UDFTagRangeUsage::INTERFIRMBILATERAL => f.write_str("INTER_FIRM_BILATERAL"),
            UDFTagRangeUsage::GTCREGULATORYLEGACY => f.write_str("GTC_REGULATORY_LEGACY"),
            UDFTagRangeUsage::WIPCHINA => f.write_str("WIP_CHINA"),
            UDFTagRangeUsage::INTERNALFIRM => f.write_str("INTERNAL_FIRM"),
            UDFTagRangeUsage::GTCOTCDERIVATIVES => f.write_str("GTC_OTC_DERIVATIVES"),
            UDFTagRangeUsage::GTCRESERVED => f.write_str("GTC_RESERVED"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for UDFTagRangeUsage {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            UDFTagRangeUsage::INTERFIRMREGISTERED => "INTER_FIRM_REGISTERED",
            UDFTagRangeUsage::INTERFIRMBILATERAL => "INTER_FIRM_BILATERAL",
            UDFTagRangeUsage::GTCREGULATORYLEGACY => "GTC_REGULATORY_LEGACY",
            UDFTagRangeUsage::WIPCHINA => "WIP_CHINA",
            UDFTagRangeUsage::INTERNALFIRM => "INTERNAL_FIRM",
            UDFTagRangeUsage::GTCOTCDERIVATIVES => "GTC_OTC_DERIVATIVES",
            UDFTagRangeUsage::GTCRESERVED => "GTC_RESERVED",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for UDFTagRangeUsage {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "INTER_FIRM_REGISTERED" | "INTERFIRMREGISTERED" => Ok(UDFTagRangeUsage::INTERFIRMREGISTERED),
                "INTER_FIRM_BILATERAL" | "INTERFIRMBILATERAL" => Ok(UDFTagRangeUsage::INTERFIRMBILATERAL),
                "GTC_REGULATORY_LEGACY" | "GTCREGULATORYLEGACY" => Ok(UDFTagRangeUsage::GTCREGULATORYLEGACY),
                "WIP_CHINA" | "WIPCHINA" => Ok(UDFTagRangeUsage::WIPCHINA),
                "INTERNAL_FIRM" | "INTERNALFIRM" => Ok(UDFTagRangeUsage::INTERNALFIRM),
                "GTC_OTC_DERIVATIVES" | "GTCOTCDERIVATIVES" => Ok(UDFTagRangeUsage::GTCOTCDERIVATIVES),
                "GTC_RESERVED" | "GTCRESERVED" => Ok(UDFTagRangeUsage::GTCRESERVED),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for UDFTagRangeUsage: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(UDFTagRangeUsage)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for UDFTagRangeUsage {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['INTER_FIRM_REGISTERED', 'INTER_FIRM_BILATERAL', 'GTC_REGULATORY_LEGACY', 'WIP_CHINA', 'INTERNAL_FIRM', 'GTC_OTC_DERIVATIVES', 'GTC_RESERVED']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PreTradeCategoryEnum {
    INDICATION,
    EVENTCOMMUNICATION,
    QUOTATIONNEGOTIATION,
    MARKETDATA,
    MARKETSTRUCTUREREFERENCEDATA,
    SECURITIESREFERENCEDATA,
    PARTIESREFERENCEDATA,
    PARTIESACTION,
}

impl core::fmt::Display for PreTradeCategoryEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PreTradeCategoryEnum::INDICATION => f.write_str("INDICATION"),
            PreTradeCategoryEnum::EVENTCOMMUNICATION => f.write_str("EVENT_COMMUNICATION"),
            PreTradeCategoryEnum::QUOTATIONNEGOTIATION => f.write_str("QUOTATION_NEGOTIATION"),
            PreTradeCategoryEnum::MARKETDATA => f.write_str("MARKET_DATA"),
            PreTradeCategoryEnum::MARKETSTRUCTUREREFERENCEDATA => f.write_str("MARKET_STRUCTURE_REFERENCE_DATA"),
            PreTradeCategoryEnum::SECURITIESREFERENCEDATA => f.write_str("SECURITIES_REFERENCE_DATA"),
            PreTradeCategoryEnum::PARTIESREFERENCEDATA => f.write_str("PARTIES_REFERENCE_DATA"),
            PreTradeCategoryEnum::PARTIESACTION => f.write_str("PARTIES_ACTION"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PreTradeCategoryEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PreTradeCategoryEnum::INDICATION => "INDICATION",
            PreTradeCategoryEnum::EVENTCOMMUNICATION => "EVENT_COMMUNICATION",
            PreTradeCategoryEnum::QUOTATIONNEGOTIATION => "QUOTATION_NEGOTIATION",
            PreTradeCategoryEnum::MARKETDATA => "MARKET_DATA",
            PreTradeCategoryEnum::MARKETSTRUCTUREREFERENCEDATA => "MARKET_STRUCTURE_REFERENCE_DATA",
            PreTradeCategoryEnum::SECURITIESREFERENCEDATA => "SECURITIES_REFERENCE_DATA",
            PreTradeCategoryEnum::PARTIESREFERENCEDATA => "PARTIES_REFERENCE_DATA",
            PreTradeCategoryEnum::PARTIESACTION => "PARTIES_ACTION",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PreTradeCategoryEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "INDICATION" => Ok(PreTradeCategoryEnum::INDICATION),
                "EVENT_COMMUNICATION" | "EVENTCOMMUNICATION" => Ok(PreTradeCategoryEnum::EVENTCOMMUNICATION),
                "QUOTATION_NEGOTIATION" | "QUOTATIONNEGOTIATION" => Ok(PreTradeCategoryEnum::QUOTATIONNEGOTIATION),
                "MARKET_DATA" | "MARKETDATA" => Ok(PreTradeCategoryEnum::MARKETDATA),
                "MARKET_STRUCTURE_REFERENCE_DATA" | "MARKETSTRUCTUREREFERENCEDATA" => Ok(PreTradeCategoryEnum::MARKETSTRUCTUREREFERENCEDATA),
                "SECURITIES_REFERENCE_DATA" | "SECURITIESREFERENCEDATA" => Ok(PreTradeCategoryEnum::SECURITIESREFERENCEDATA),
                "PARTIES_REFERENCE_DATA" | "PARTIESREFERENCEDATA" => Ok(PreTradeCategoryEnum::PARTIESREFERENCEDATA),
                "PARTIES_ACTION" | "PARTIESACTION" => Ok(PreTradeCategoryEnum::PARTIESACTION),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PreTradeCategoryEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PreTradeCategoryEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PreTradeCategoryEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ComponentRepetition {
    REPEATING,
    NONREPEATING,
}

impl core::fmt::Display for ComponentRepetition {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ComponentRepetition::REPEATING => f.write_str("REPEATING"),
            ComponentRepetition::NONREPEATING => f.write_str("NON_REPEATING"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ComponentRepetition {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ComponentRepetition::REPEATING => "REPEATING",
            ComponentRepetition::NONREPEATING => "NON_REPEATING",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ComponentRepetition {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "REPEATING" => Ok(ComponentRepetition::REPEATING),
                "NON_REPEATING" | "NONREPEATING" => Ok(ComponentRepetition::NONREPEATING),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ComponentRepetition: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ComponentRepetition)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ComponentRepetition {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['REPEATING', 'NON_REPEATING']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PreTradeCommonComponentName {
    AuctionTypeRuleGrp,
    BaseTradingRules,
    ExecInstRules,
    InstrumentScope,
    InstrumentScopeGrp,
    InstrumentScopeSecurityAltIDGrp,
    LotTypeRules,
    MarketDataFeedTypes,
    MarketSegmentScopeGrp,
    MatchRules,
    OrdTypeRules,
    PriceLimits,
    PriceRangeRuleGrp,
    QuoteSizeRuleGrp,
    RequestedPartyRoleGrp,
    RequestingPartyGrp,
    RequestingPartySubGrp,
    RoutingGrp,
    TickRules,
    TimeInForceRules,
    TradingSessionRules,
}

impl core::fmt::Display for PreTradeCommonComponentName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PreTradeCommonComponentName::AuctionTypeRuleGrp => f.write_str("AuctionTypeRuleGrp"),
            PreTradeCommonComponentName::BaseTradingRules => f.write_str("BaseTradingRules"),
            PreTradeCommonComponentName::ExecInstRules => f.write_str("ExecInstRules"),
            PreTradeCommonComponentName::InstrumentScope => f.write_str("InstrumentScope"),
            PreTradeCommonComponentName::InstrumentScopeGrp => f.write_str("InstrumentScopeGrp"),
            PreTradeCommonComponentName::InstrumentScopeSecurityAltIDGrp => f.write_str("InstrumentScopeSecurityAltIDGrp"),
            PreTradeCommonComponentName::LotTypeRules => f.write_str("LotTypeRules"),
            PreTradeCommonComponentName::MarketDataFeedTypes => f.write_str("MarketDataFeedTypes"),
            PreTradeCommonComponentName::MarketSegmentScopeGrp => f.write_str("MarketSegmentScopeGrp"),
            PreTradeCommonComponentName::MatchRules => f.write_str("MatchRules"),
            PreTradeCommonComponentName::OrdTypeRules => f.write_str("OrdTypeRules"),
            PreTradeCommonComponentName::PriceLimits => f.write_str("PriceLimits"),
            PreTradeCommonComponentName::PriceRangeRuleGrp => f.write_str("PriceRangeRuleGrp"),
            PreTradeCommonComponentName::QuoteSizeRuleGrp => f.write_str("QuoteSizeRuleGrp"),
            PreTradeCommonComponentName::RequestedPartyRoleGrp => f.write_str("RequestedPartyRoleGrp"),
            PreTradeCommonComponentName::RequestingPartyGrp => f.write_str("RequestingPartyGrp"),
            PreTradeCommonComponentName::RequestingPartySubGrp => f.write_str("RequestingPartySubGrp"),
            PreTradeCommonComponentName::RoutingGrp => f.write_str("RoutingGrp"),
            PreTradeCommonComponentName::TickRules => f.write_str("TickRules"),
            PreTradeCommonComponentName::TimeInForceRules => f.write_str("TimeInForceRules"),
            PreTradeCommonComponentName::TradingSessionRules => f.write_str("TradingSessionRules"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PreTradeCommonComponentName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PreTradeCommonComponentName::AuctionTypeRuleGrp => "AuctionTypeRuleGrp",
            PreTradeCommonComponentName::BaseTradingRules => "BaseTradingRules",
            PreTradeCommonComponentName::ExecInstRules => "ExecInstRules",
            PreTradeCommonComponentName::InstrumentScope => "InstrumentScope",
            PreTradeCommonComponentName::InstrumentScopeGrp => "InstrumentScopeGrp",
            PreTradeCommonComponentName::InstrumentScopeSecurityAltIDGrp => "InstrumentScopeSecurityAltIDGrp",
            PreTradeCommonComponentName::LotTypeRules => "LotTypeRules",
            PreTradeCommonComponentName::MarketDataFeedTypes => "MarketDataFeedTypes",
            PreTradeCommonComponentName::MarketSegmentScopeGrp => "MarketSegmentScopeGrp",
            PreTradeCommonComponentName::MatchRules => "MatchRules",
            PreTradeCommonComponentName::OrdTypeRules => "OrdTypeRules",
            PreTradeCommonComponentName::PriceLimits => "PriceLimits",
            PreTradeCommonComponentName::PriceRangeRuleGrp => "PriceRangeRuleGrp",
            PreTradeCommonComponentName::QuoteSizeRuleGrp => "QuoteSizeRuleGrp",
            PreTradeCommonComponentName::RequestedPartyRoleGrp => "RequestedPartyRoleGrp",
            PreTradeCommonComponentName::RequestingPartyGrp => "RequestingPartyGrp",
            PreTradeCommonComponentName::RequestingPartySubGrp => "RequestingPartySubGrp",
            PreTradeCommonComponentName::RoutingGrp => "RoutingGrp",
            PreTradeCommonComponentName::TickRules => "TickRules",
            PreTradeCommonComponentName::TimeInForceRules => "TimeInForceRules",
            PreTradeCommonComponentName::TradingSessionRules => "TradingSessionRules",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PreTradeCommonComponentName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "AuctionTypeRuleGrp" => Ok(PreTradeCommonComponentName::AuctionTypeRuleGrp),
                "BaseTradingRules" => Ok(PreTradeCommonComponentName::BaseTradingRules),
                "ExecInstRules" => Ok(PreTradeCommonComponentName::ExecInstRules),
                "InstrumentScope" => Ok(PreTradeCommonComponentName::InstrumentScope),
                "InstrumentScopeGrp" => Ok(PreTradeCommonComponentName::InstrumentScopeGrp),
                "InstrumentScopeSecurityAltIDGrp" => Ok(PreTradeCommonComponentName::InstrumentScopeSecurityAltIDGrp),
                "LotTypeRules" => Ok(PreTradeCommonComponentName::LotTypeRules),
                "MarketDataFeedTypes" => Ok(PreTradeCommonComponentName::MarketDataFeedTypes),
                "MarketSegmentScopeGrp" => Ok(PreTradeCommonComponentName::MarketSegmentScopeGrp),
                "MatchRules" => Ok(PreTradeCommonComponentName::MatchRules),
                "OrdTypeRules" => Ok(PreTradeCommonComponentName::OrdTypeRules),
                "PriceLimits" => Ok(PreTradeCommonComponentName::PriceLimits),
                "PriceRangeRuleGrp" => Ok(PreTradeCommonComponentName::PriceRangeRuleGrp),
                "QuoteSizeRuleGrp" => Ok(PreTradeCommonComponentName::QuoteSizeRuleGrp),
                "RequestedPartyRoleGrp" => Ok(PreTradeCommonComponentName::RequestedPartyRoleGrp),
                "RequestingPartyGrp" => Ok(PreTradeCommonComponentName::RequestingPartyGrp),
                "RequestingPartySubGrp" => Ok(PreTradeCommonComponentName::RequestingPartySubGrp),
                "RoutingGrp" => Ok(PreTradeCommonComponentName::RoutingGrp),
                "TickRules" => Ok(PreTradeCommonComponentName::TickRules),
                "TimeInForceRules" => Ok(PreTradeCommonComponentName::TimeInForceRules),
                "TradingSessionRules" => Ok(PreTradeCommonComponentName::TradingSessionRules),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PreTradeCommonComponentName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PreTradeCommonComponentName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PreTradeCommonComponentName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['AuctionTypeRuleGrp', 'BaseTradingRules', 'ExecInstRules', 'InstrumentScope', 'InstrumentScopeGrp', 'InstrumentScopeSecurityAltIDGrp', 'LotTypeRules', 'MarketDataFeedTypes', 'MarketSegmentScopeGrp', 'MatchRules', 'OrdTypeRules', 'PriceLimits', 'PriceRangeRuleGrp', 'QuoteSizeRuleGrp', 'RequestedPartyRoleGrp', 'RequestingPartyGrp', 'RequestingPartySubGrp', 'RoutingGrp', 'TickRules', 'TimeInForceRules', 'TradingSessionRules']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum QuoteModelEnum {
    INDICATIVE,
    TRADEABLE,
    RESTRICTEDTRADEABLE,
    NEGOTIATION,
}

impl core::fmt::Display for QuoteModelEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            QuoteModelEnum::INDICATIVE => f.write_str("INDICATIVE"),
            QuoteModelEnum::TRADEABLE => f.write_str("TRADEABLE"),
            QuoteModelEnum::RESTRICTEDTRADEABLE => f.write_str("RESTRICTED_TRADEABLE"),
            QuoteModelEnum::NEGOTIATION => f.write_str("NEGOTIATION"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for QuoteModelEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            QuoteModelEnum::INDICATIVE => "INDICATIVE",
            QuoteModelEnum::TRADEABLE => "TRADEABLE",
            QuoteModelEnum::RESTRICTEDTRADEABLE => "RESTRICTED_TRADEABLE",
            QuoteModelEnum::NEGOTIATION => "NEGOTIATION",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for QuoteModelEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "INDICATIVE" => Ok(QuoteModelEnum::INDICATIVE),
                "TRADEABLE" => Ok(QuoteModelEnum::TRADEABLE),
                "RESTRICTED_TRADEABLE" | "RESTRICTEDTRADEABLE" => Ok(QuoteModelEnum::RESTRICTEDTRADEABLE),
                "NEGOTIATION" => Ok(QuoteModelEnum::NEGOTIATION),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for QuoteModelEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(QuoteModelEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for QuoteModelEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['INDICATIVE', 'TRADEABLE', 'RESTRICTED_TRADEABLE', 'NEGOTIATION']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PreTradeLayoutRowKindEnum {
    FIELD,
    COMPONENT,
}

impl core::fmt::Display for PreTradeLayoutRowKindEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PreTradeLayoutRowKindEnum::FIELD => f.write_str("FIELD"),
            PreTradeLayoutRowKindEnum::COMPONENT => f.write_str("COMPONENT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PreTradeLayoutRowKindEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PreTradeLayoutRowKindEnum::FIELD => "FIELD",
            PreTradeLayoutRowKindEnum::COMPONENT => "COMPONENT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PreTradeLayoutRowKindEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "FIELD" => Ok(PreTradeLayoutRowKindEnum::FIELD),
                "COMPONENT" => Ok(PreTradeLayoutRowKindEnum::COMPONENT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PreTradeLayoutRowKindEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PreTradeLayoutRowKindEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PreTradeLayoutRowKindEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['FIELD', 'COMPONENT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TradeCategoryEnum {
    SINGLEGENERALORDERHANDLING,
    ORDERMASSHANDLING,
    CROSSORDERHANDLING,
    MULTILEGORDERHANDLING,
    LISTPROGRAMBASKETTRADING,
}

impl core::fmt::Display for TradeCategoryEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TradeCategoryEnum::SINGLEGENERALORDERHANDLING => f.write_str("SINGLE_GENERAL_ORDER_HANDLING"),
            TradeCategoryEnum::ORDERMASSHANDLING => f.write_str("ORDER_MASS_HANDLING"),
            TradeCategoryEnum::CROSSORDERHANDLING => f.write_str("CROSS_ORDER_HANDLING"),
            TradeCategoryEnum::MULTILEGORDERHANDLING => f.write_str("MULTILEG_ORDER_HANDLING"),
            TradeCategoryEnum::LISTPROGRAMBASKETTRADING => f.write_str("LIST_PROGRAM_BASKET_TRADING"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TradeCategoryEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TradeCategoryEnum::SINGLEGENERALORDERHANDLING => "SINGLE_GENERAL_ORDER_HANDLING",
            TradeCategoryEnum::ORDERMASSHANDLING => "ORDER_MASS_HANDLING",
            TradeCategoryEnum::CROSSORDERHANDLING => "CROSS_ORDER_HANDLING",
            TradeCategoryEnum::MULTILEGORDERHANDLING => "MULTILEG_ORDER_HANDLING",
            TradeCategoryEnum::LISTPROGRAMBASKETTRADING => "LIST_PROGRAM_BASKET_TRADING",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TradeCategoryEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "SINGLE_GENERAL_ORDER_HANDLING" | "SINGLEGENERALORDERHANDLING" => Ok(TradeCategoryEnum::SINGLEGENERALORDERHANDLING),
                "ORDER_MASS_HANDLING" | "ORDERMASSHANDLING" => Ok(TradeCategoryEnum::ORDERMASSHANDLING),
                "CROSS_ORDER_HANDLING" | "CROSSORDERHANDLING" => Ok(TradeCategoryEnum::CROSSORDERHANDLING),
                "MULTILEG_ORDER_HANDLING" | "MULTILEGORDERHANDLING" => Ok(TradeCategoryEnum::MULTILEGORDERHANDLING),
                "LIST_PROGRAM_BASKET_TRADING" | "LISTPROGRAMBASKETTRADING" => Ok(TradeCategoryEnum::LISTPROGRAMBASKETTRADING),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TradeCategoryEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TradeCategoryEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TradeCategoryEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TradeComponentRepetition {
    REPEATING,
    NONREPEATING,
}

impl core::fmt::Display for TradeComponentRepetition {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TradeComponentRepetition::REPEATING => f.write_str("REPEATING"),
            TradeComponentRepetition::NONREPEATING => f.write_str("NON_REPEATING"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TradeComponentRepetition {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TradeComponentRepetition::REPEATING => "REPEATING",
            TradeComponentRepetition::NONREPEATING => "NON_REPEATING",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TradeComponentRepetition {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "REPEATING" => Ok(TradeComponentRepetition::REPEATING),
                "NON_REPEATING" | "NONREPEATING" => Ok(TradeComponentRepetition::NONREPEATING),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TradeComponentRepetition: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TradeComponentRepetition)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TradeComponentRepetition {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['REPEATING', 'NON_REPEATING']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TradeCommonComponentName {
    DisclosureInstructionGrp,
    DiscretionInstructions,
    PegInstructions,
    PreAllocGrp,
    StrategyParametersGrp,
    TriggeringInstruction,
}

impl core::fmt::Display for TradeCommonComponentName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TradeCommonComponentName::DisclosureInstructionGrp => f.write_str("DisclosureInstructionGrp"),
            TradeCommonComponentName::DiscretionInstructions => f.write_str("DiscretionInstructions"),
            TradeCommonComponentName::PegInstructions => f.write_str("PegInstructions"),
            TradeCommonComponentName::PreAllocGrp => f.write_str("PreAllocGrp"),
            TradeCommonComponentName::StrategyParametersGrp => f.write_str("StrategyParametersGrp"),
            TradeCommonComponentName::TriggeringInstruction => f.write_str("TriggeringInstruction"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TradeCommonComponentName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TradeCommonComponentName::DisclosureInstructionGrp => "DisclosureInstructionGrp",
            TradeCommonComponentName::DiscretionInstructions => "DiscretionInstructions",
            TradeCommonComponentName::PegInstructions => "PegInstructions",
            TradeCommonComponentName::PreAllocGrp => "PreAllocGrp",
            TradeCommonComponentName::StrategyParametersGrp => "StrategyParametersGrp",
            TradeCommonComponentName::TriggeringInstruction => "TriggeringInstruction",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TradeCommonComponentName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "DisclosureInstructionGrp" => Ok(TradeCommonComponentName::DisclosureInstructionGrp),
                "DiscretionInstructions" => Ok(TradeCommonComponentName::DiscretionInstructions),
                "PegInstructions" => Ok(TradeCommonComponentName::PegInstructions),
                "PreAllocGrp" => Ok(TradeCommonComponentName::PreAllocGrp),
                "StrategyParametersGrp" => Ok(TradeCommonComponentName::StrategyParametersGrp),
                "TriggeringInstruction" => Ok(TradeCommonComponentName::TriggeringInstruction),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TradeCommonComponentName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TradeCommonComponentName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TradeCommonComponentName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['DisclosureInstructionGrp', 'DiscretionInstructions', 'PegInstructions', 'PreAllocGrp', 'StrategyParametersGrp', 'TriggeringInstruction']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TradeLayoutRowKindEnum {
    FIELD,
    COMPONENT,
}

impl core::fmt::Display for TradeLayoutRowKindEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TradeLayoutRowKindEnum::FIELD => f.write_str("FIELD"),
            TradeLayoutRowKindEnum::COMPONENT => f.write_str("COMPONENT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TradeLayoutRowKindEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TradeLayoutRowKindEnum::FIELD => "FIELD",
            TradeLayoutRowKindEnum::COMPONENT => "COMPONENT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TradeLayoutRowKindEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "FIELD" => Ok(TradeLayoutRowKindEnum::FIELD),
                "COMPONENT" => Ok(TradeLayoutRowKindEnum::COMPONENT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TradeLayoutRowKindEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TradeLayoutRowKindEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TradeLayoutRowKindEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['FIELD', 'COMPONENT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PostTradeCategoryEnum {
    ALLOCATION,
    CONFIRMATION,
    SETTLEMENTINSTRUCTION,
    TRADECAPTUREREPORTING,
    REGISTRATIONINSTRUCTION,
    POSITIONMAINTENANCE,
    COLLATERALMANAGEMENT,
    MARGINREQUIREMENTMANAGEMENT,
    ACCOUNTREPORTING,
    TRADEMANAGEMENT,
    PAYMANAGEMENT,
    SETTLEMENTSTATUSMANAGEMENT,
}

impl core::fmt::Display for PostTradeCategoryEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PostTradeCategoryEnum::ALLOCATION => f.write_str("ALLOCATION"),
            PostTradeCategoryEnum::CONFIRMATION => f.write_str("CONFIRMATION"),
            PostTradeCategoryEnum::SETTLEMENTINSTRUCTION => f.write_str("SETTLEMENT_INSTRUCTION"),
            PostTradeCategoryEnum::TRADECAPTUREREPORTING => f.write_str("TRADE_CAPTURE_REPORTING"),
            PostTradeCategoryEnum::REGISTRATIONINSTRUCTION => f.write_str("REGISTRATION_INSTRUCTION"),
            PostTradeCategoryEnum::POSITIONMAINTENANCE => f.write_str("POSITION_MAINTENANCE"),
            PostTradeCategoryEnum::COLLATERALMANAGEMENT => f.write_str("COLLATERAL_MANAGEMENT"),
            PostTradeCategoryEnum::MARGINREQUIREMENTMANAGEMENT => f.write_str("MARGIN_REQUIREMENT_MANAGEMENT"),
            PostTradeCategoryEnum::ACCOUNTREPORTING => f.write_str("ACCOUNT_REPORTING"),
            PostTradeCategoryEnum::TRADEMANAGEMENT => f.write_str("TRADE_MANAGEMENT"),
            PostTradeCategoryEnum::PAYMANAGEMENT => f.write_str("PAY_MANAGEMENT"),
            PostTradeCategoryEnum::SETTLEMENTSTATUSMANAGEMENT => f.write_str("SETTLEMENT_STATUS_MANAGEMENT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PostTradeCategoryEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PostTradeCategoryEnum::ALLOCATION => "ALLOCATION",
            PostTradeCategoryEnum::CONFIRMATION => "CONFIRMATION",
            PostTradeCategoryEnum::SETTLEMENTINSTRUCTION => "SETTLEMENT_INSTRUCTION",
            PostTradeCategoryEnum::TRADECAPTUREREPORTING => "TRADE_CAPTURE_REPORTING",
            PostTradeCategoryEnum::REGISTRATIONINSTRUCTION => "REGISTRATION_INSTRUCTION",
            PostTradeCategoryEnum::POSITIONMAINTENANCE => "POSITION_MAINTENANCE",
            PostTradeCategoryEnum::COLLATERALMANAGEMENT => "COLLATERAL_MANAGEMENT",
            PostTradeCategoryEnum::MARGINREQUIREMENTMANAGEMENT => "MARGIN_REQUIREMENT_MANAGEMENT",
            PostTradeCategoryEnum::ACCOUNTREPORTING => "ACCOUNT_REPORTING",
            PostTradeCategoryEnum::TRADEMANAGEMENT => "TRADE_MANAGEMENT",
            PostTradeCategoryEnum::PAYMANAGEMENT => "PAY_MANAGEMENT",
            PostTradeCategoryEnum::SETTLEMENTSTATUSMANAGEMENT => "SETTLEMENT_STATUS_MANAGEMENT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PostTradeCategoryEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "ALLOCATION" => Ok(PostTradeCategoryEnum::ALLOCATION),
                "CONFIRMATION" => Ok(PostTradeCategoryEnum::CONFIRMATION),
                "SETTLEMENT_INSTRUCTION" | "SETTLEMENTINSTRUCTION" => Ok(PostTradeCategoryEnum::SETTLEMENTINSTRUCTION),
                "TRADE_CAPTURE_REPORTING" | "TRADECAPTUREREPORTING" => Ok(PostTradeCategoryEnum::TRADECAPTUREREPORTING),
                "REGISTRATION_INSTRUCTION" | "REGISTRATIONINSTRUCTION" => Ok(PostTradeCategoryEnum::REGISTRATIONINSTRUCTION),
                "POSITION_MAINTENANCE" | "POSITIONMAINTENANCE" => Ok(PostTradeCategoryEnum::POSITIONMAINTENANCE),
                "COLLATERAL_MANAGEMENT" | "COLLATERALMANAGEMENT" => Ok(PostTradeCategoryEnum::COLLATERALMANAGEMENT),
                "MARGIN_REQUIREMENT_MANAGEMENT" | "MARGINREQUIREMENTMANAGEMENT" => Ok(PostTradeCategoryEnum::MARGINREQUIREMENTMANAGEMENT),
                "ACCOUNT_REPORTING" | "ACCOUNTREPORTING" => Ok(PostTradeCategoryEnum::ACCOUNTREPORTING),
                "TRADE_MANAGEMENT" | "TRADEMANAGEMENT" => Ok(PostTradeCategoryEnum::TRADEMANAGEMENT),
                "PAY_MANAGEMENT" | "PAYMANAGEMENT" => Ok(PostTradeCategoryEnum::PAYMANAGEMENT),
                "SETTLEMENT_STATUS_MANAGEMENT" | "SETTLEMENTSTATUSMANAGEMENT" => Ok(PostTradeCategoryEnum::SETTLEMENTSTATUSMANAGEMENT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PostTradeCategoryEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PostTradeCategoryEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PostTradeCategoryEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PostTradeCommonComponentName {
    AllocCommissionDataGrp,
    AllocRegulatoryTradeIDGrp,
    ClrInstGrp,
    CollateralAmountGrp,
    CollateralReinvestmentGrp,
    DlvyInstGrp,
    ExecAllocGrp,
    MarginAmount,
    OrdAllocGrp,
    PositionAmountData,
    SettlDetails,
    SettlInstructionsData,
    SettlParties,
    SettlPtysSubGrp,
    TradeAllocAmtGrp,
    TransactionAttributeGrp,
}

impl core::fmt::Display for PostTradeCommonComponentName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PostTradeCommonComponentName::AllocCommissionDataGrp => f.write_str("AllocCommissionDataGrp"),
            PostTradeCommonComponentName::AllocRegulatoryTradeIDGrp => f.write_str("AllocRegulatoryTradeIDGrp"),
            PostTradeCommonComponentName::ClrInstGrp => f.write_str("ClrInstGrp"),
            PostTradeCommonComponentName::CollateralAmountGrp => f.write_str("CollateralAmountGrp"),
            PostTradeCommonComponentName::CollateralReinvestmentGrp => f.write_str("CollateralReinvestmentGrp"),
            PostTradeCommonComponentName::DlvyInstGrp => f.write_str("DlvyInstGrp"),
            PostTradeCommonComponentName::ExecAllocGrp => f.write_str("ExecAllocGrp"),
            PostTradeCommonComponentName::MarginAmount => f.write_str("MarginAmount"),
            PostTradeCommonComponentName::OrdAllocGrp => f.write_str("OrdAllocGrp"),
            PostTradeCommonComponentName::PositionAmountData => f.write_str("PositionAmountData"),
            PostTradeCommonComponentName::SettlDetails => f.write_str("SettlDetails"),
            PostTradeCommonComponentName::SettlInstructionsData => f.write_str("SettlInstructionsData"),
            PostTradeCommonComponentName::SettlParties => f.write_str("SettlParties"),
            PostTradeCommonComponentName::SettlPtysSubGrp => f.write_str("SettlPtysSubGrp"),
            PostTradeCommonComponentName::TradeAllocAmtGrp => f.write_str("TradeAllocAmtGrp"),
            PostTradeCommonComponentName::TransactionAttributeGrp => f.write_str("TransactionAttributeGrp"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PostTradeCommonComponentName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PostTradeCommonComponentName::AllocCommissionDataGrp => "AllocCommissionDataGrp",
            PostTradeCommonComponentName::AllocRegulatoryTradeIDGrp => "AllocRegulatoryTradeIDGrp",
            PostTradeCommonComponentName::ClrInstGrp => "ClrInstGrp",
            PostTradeCommonComponentName::CollateralAmountGrp => "CollateralAmountGrp",
            PostTradeCommonComponentName::CollateralReinvestmentGrp => "CollateralReinvestmentGrp",
            PostTradeCommonComponentName::DlvyInstGrp => "DlvyInstGrp",
            PostTradeCommonComponentName::ExecAllocGrp => "ExecAllocGrp",
            PostTradeCommonComponentName::MarginAmount => "MarginAmount",
            PostTradeCommonComponentName::OrdAllocGrp => "OrdAllocGrp",
            PostTradeCommonComponentName::PositionAmountData => "PositionAmountData",
            PostTradeCommonComponentName::SettlDetails => "SettlDetails",
            PostTradeCommonComponentName::SettlInstructionsData => "SettlInstructionsData",
            PostTradeCommonComponentName::SettlParties => "SettlParties",
            PostTradeCommonComponentName::SettlPtysSubGrp => "SettlPtysSubGrp",
            PostTradeCommonComponentName::TradeAllocAmtGrp => "TradeAllocAmtGrp",
            PostTradeCommonComponentName::TransactionAttributeGrp => "TransactionAttributeGrp",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PostTradeCommonComponentName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "AllocCommissionDataGrp" => Ok(PostTradeCommonComponentName::AllocCommissionDataGrp),
                "AllocRegulatoryTradeIDGrp" => Ok(PostTradeCommonComponentName::AllocRegulatoryTradeIDGrp),
                "ClrInstGrp" => Ok(PostTradeCommonComponentName::ClrInstGrp),
                "CollateralAmountGrp" => Ok(PostTradeCommonComponentName::CollateralAmountGrp),
                "CollateralReinvestmentGrp" => Ok(PostTradeCommonComponentName::CollateralReinvestmentGrp),
                "DlvyInstGrp" => Ok(PostTradeCommonComponentName::DlvyInstGrp),
                "ExecAllocGrp" => Ok(PostTradeCommonComponentName::ExecAllocGrp),
                "MarginAmount" => Ok(PostTradeCommonComponentName::MarginAmount),
                "OrdAllocGrp" => Ok(PostTradeCommonComponentName::OrdAllocGrp),
                "PositionAmountData" => Ok(PostTradeCommonComponentName::PositionAmountData),
                "SettlDetails" => Ok(PostTradeCommonComponentName::SettlDetails),
                "SettlInstructionsData" => Ok(PostTradeCommonComponentName::SettlInstructionsData),
                "SettlParties" => Ok(PostTradeCommonComponentName::SettlParties),
                "SettlPtysSubGrp" => Ok(PostTradeCommonComponentName::SettlPtysSubGrp),
                "TradeAllocAmtGrp" => Ok(PostTradeCommonComponentName::TradeAllocAmtGrp),
                "TransactionAttributeGrp" => Ok(PostTradeCommonComponentName::TransactionAttributeGrp),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PostTradeCommonComponentName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PostTradeCommonComponentName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PostTradeCommonComponentName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['AllocCommissionDataGrp', 'AllocRegulatoryTradeIDGrp', 'ClrInstGrp', 'CollateralAmountGrp', 'CollateralReinvestmentGrp', 'DlvyInstGrp', 'ExecAllocGrp', 'MarginAmount', 'OrdAllocGrp', 'PositionAmountData', 'SettlDetails', 'SettlInstructionsData', 'SettlParties', 'SettlPtysSubGrp', 'TradeAllocAmtGrp', 'TransactionAttributeGrp']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum AllocationScenarioEnum {
    PREALLOCATEDORDER,
    PRETRADEALLOCATION,
    POSTTRADEALLOCATION,
    READYTOBOOK,
}

impl core::fmt::Display for AllocationScenarioEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            AllocationScenarioEnum::PREALLOCATEDORDER => f.write_str("PRE_ALLOCATED_ORDER"),
            AllocationScenarioEnum::PRETRADEALLOCATION => f.write_str("PRE_TRADE_ALLOCATION"),
            AllocationScenarioEnum::POSTTRADEALLOCATION => f.write_str("POST_TRADE_ALLOCATION"),
            AllocationScenarioEnum::READYTOBOOK => f.write_str("READY_TO_BOOK"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for AllocationScenarioEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            AllocationScenarioEnum::PREALLOCATEDORDER => "PRE_ALLOCATED_ORDER",
            AllocationScenarioEnum::PRETRADEALLOCATION => "PRE_TRADE_ALLOCATION",
            AllocationScenarioEnum::POSTTRADEALLOCATION => "POST_TRADE_ALLOCATION",
            AllocationScenarioEnum::READYTOBOOK => "READY_TO_BOOK",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for AllocationScenarioEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "PRE_ALLOCATED_ORDER" | "PREALLOCATEDORDER" => Ok(AllocationScenarioEnum::PREALLOCATEDORDER),
                "PRE_TRADE_ALLOCATION" | "PRETRADEALLOCATION" => Ok(AllocationScenarioEnum::PRETRADEALLOCATION),
                "POST_TRADE_ALLOCATION" | "POSTTRADEALLOCATION" => Ok(AllocationScenarioEnum::POSTTRADEALLOCATION),
                "READY_TO_BOOK" | "READYTOBOOK" => Ok(AllocationScenarioEnum::READYTOBOOK),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for AllocationScenarioEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(AllocationScenarioEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for AllocationScenarioEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['PRE_ALLOCATED_ORDER', 'PRE_TRADE_ALLOCATION', 'POST_TRADE_ALLOCATION', 'READY_TO_BOOK']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum AllocationStatusEnum {
    ACCEPTED,
    BLOCKLEVELREJECT,
    ACCOUNTLEVELREJECT,
    RECEIVEDNOTYETPROCESSED,
}

impl core::fmt::Display for AllocationStatusEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            AllocationStatusEnum::ACCEPTED => f.write_str("ACCEPTED"),
            AllocationStatusEnum::BLOCKLEVELREJECT => f.write_str("BLOCK_LEVEL_REJECT"),
            AllocationStatusEnum::ACCOUNTLEVELREJECT => f.write_str("ACCOUNT_LEVEL_REJECT"),
            AllocationStatusEnum::RECEIVEDNOTYETPROCESSED => f.write_str("RECEIVED_NOT_YET_PROCESSED"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for AllocationStatusEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            AllocationStatusEnum::ACCEPTED => "ACCEPTED",
            AllocationStatusEnum::BLOCKLEVELREJECT => "BLOCK_LEVEL_REJECT",
            AllocationStatusEnum::ACCOUNTLEVELREJECT => "ACCOUNT_LEVEL_REJECT",
            AllocationStatusEnum::RECEIVEDNOTYETPROCESSED => "RECEIVED_NOT_YET_PROCESSED",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for AllocationStatusEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "ACCEPTED" => Ok(AllocationStatusEnum::ACCEPTED),
                "BLOCK_LEVEL_REJECT" | "BLOCKLEVELREJECT" => Ok(AllocationStatusEnum::BLOCKLEVELREJECT),
                "ACCOUNT_LEVEL_REJECT" | "ACCOUNTLEVELREJECT" => Ok(AllocationStatusEnum::ACCOUNTLEVELREJECT),
                "RECEIVED_NOT_YET_PROCESSED" | "RECEIVEDNOTYETPROCESSED" => Ok(AllocationStatusEnum::RECEIVEDNOTYETPROCESSED),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for AllocationStatusEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(AllocationStatusEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for AllocationStatusEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['ACCEPTED', 'BLOCK_LEVEL_REJECT', 'ACCOUNT_LEVEL_REJECT', 'RECEIVED_NOT_YET_PROCESSED']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum AllocationTransactionTypeEnum {
    NEW,
    REPLACE,
    CANCEL,
}

impl core::fmt::Display for AllocationTransactionTypeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            AllocationTransactionTypeEnum::NEW => f.write_str("NEW"),
            AllocationTransactionTypeEnum::REPLACE => f.write_str("REPLACE"),
            AllocationTransactionTypeEnum::CANCEL => f.write_str("CANCEL"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for AllocationTransactionTypeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            AllocationTransactionTypeEnum::NEW => "NEW",
            AllocationTransactionTypeEnum::REPLACE => "REPLACE",
            AllocationTransactionTypeEnum::CANCEL => "CANCEL",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for AllocationTransactionTypeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "NEW" => Ok(AllocationTransactionTypeEnum::NEW),
                "REPLACE" => Ok(AllocationTransactionTypeEnum::REPLACE),
                "CANCEL" => Ok(AllocationTransactionTypeEnum::CANCEL),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for AllocationTransactionTypeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(AllocationTransactionTypeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for AllocationTransactionTypeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['NEW', 'REPLACE', 'CANCEL']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PostTradeAllocationPricingMethodEnum {
    AVERAGEPRICE,
    EXECUTEDPRICE,
}

impl core::fmt::Display for PostTradeAllocationPricingMethodEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PostTradeAllocationPricingMethodEnum::AVERAGEPRICE => f.write_str("AVERAGE_PRICE"),
            PostTradeAllocationPricingMethodEnum::EXECUTEDPRICE => f.write_str("EXECUTED_PRICE"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PostTradeAllocationPricingMethodEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PostTradeAllocationPricingMethodEnum::AVERAGEPRICE => "AVERAGE_PRICE",
            PostTradeAllocationPricingMethodEnum::EXECUTEDPRICE => "EXECUTED_PRICE",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PostTradeAllocationPricingMethodEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "AVERAGE_PRICE" | "AVERAGEPRICE" => Ok(PostTradeAllocationPricingMethodEnum::AVERAGEPRICE),
                "EXECUTED_PRICE" | "EXECUTEDPRICE" => Ok(PostTradeAllocationPricingMethodEnum::EXECUTEDPRICE),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PostTradeAllocationPricingMethodEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PostTradeAllocationPricingMethodEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PostTradeAllocationPricingMethodEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['AVERAGE_PRICE', 'EXECUTED_PRICE']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TradeCaptureReportDirectionEnum {
    INBOUND,
    OUTBOUND,
}

impl core::fmt::Display for TradeCaptureReportDirectionEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TradeCaptureReportDirectionEnum::INBOUND => f.write_str("INBOUND"),
            TradeCaptureReportDirectionEnum::OUTBOUND => f.write_str("OUTBOUND"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TradeCaptureReportDirectionEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TradeCaptureReportDirectionEnum::INBOUND => "INBOUND",
            TradeCaptureReportDirectionEnum::OUTBOUND => "OUTBOUND",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TradeCaptureReportDirectionEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "INBOUND" => Ok(TradeCaptureReportDirectionEnum::INBOUND),
                "OUTBOUND" => Ok(TradeCaptureReportDirectionEnum::OUTBOUND),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TradeCaptureReportDirectionEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TradeCaptureReportDirectionEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TradeCaptureReportDirectionEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['INBOUND', 'OUTBOUND']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TradeCaptureReportUsageEnum {
    RELAYCONFIRMEDTRADESTONONPARTICIPANTS,
    RELAYCONFIRMEDTRADESTOCOUNTERPARTIES,
    REPORTINGPRIVATELYNEGOTIATEDTRADES,
    REPORTINGFLOORORROUTEDEXECUTIONS,
    REQUESTTRADECANCELORAMENDMENT,
}

impl core::fmt::Display for TradeCaptureReportUsageEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TradeCaptureReportUsageEnum::RELAYCONFIRMEDTRADESTONONPARTICIPANTS => f.write_str("RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS"),
            TradeCaptureReportUsageEnum::RELAYCONFIRMEDTRADESTOCOUNTERPARTIES => f.write_str("RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES"),
            TradeCaptureReportUsageEnum::REPORTINGPRIVATELYNEGOTIATEDTRADES => f.write_str("REPORTING_PRIVATELY_NEGOTIATED_TRADES"),
            TradeCaptureReportUsageEnum::REPORTINGFLOORORROUTEDEXECUTIONS => f.write_str("REPORTING_FLOOR_OR_ROUTED_EXECUTIONS"),
            TradeCaptureReportUsageEnum::REQUESTTRADECANCELORAMENDMENT => f.write_str("REQUEST_TRADE_CANCEL_OR_AMENDMENT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TradeCaptureReportUsageEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TradeCaptureReportUsageEnum::RELAYCONFIRMEDTRADESTONONPARTICIPANTS => "RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS",
            TradeCaptureReportUsageEnum::RELAYCONFIRMEDTRADESTOCOUNTERPARTIES => "RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES",
            TradeCaptureReportUsageEnum::REPORTINGPRIVATELYNEGOTIATEDTRADES => "REPORTING_PRIVATELY_NEGOTIATED_TRADES",
            TradeCaptureReportUsageEnum::REPORTINGFLOORORROUTEDEXECUTIONS => "REPORTING_FLOOR_OR_ROUTED_EXECUTIONS",
            TradeCaptureReportUsageEnum::REQUESTTRADECANCELORAMENDMENT => "REQUEST_TRADE_CANCEL_OR_AMENDMENT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TradeCaptureReportUsageEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS" | "RELAYCONFIRMEDTRADESTONONPARTICIPANTS" => Ok(TradeCaptureReportUsageEnum::RELAYCONFIRMEDTRADESTONONPARTICIPANTS),
                "RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES" | "RELAYCONFIRMEDTRADESTOCOUNTERPARTIES" => Ok(TradeCaptureReportUsageEnum::RELAYCONFIRMEDTRADESTOCOUNTERPARTIES),
                "REPORTING_PRIVATELY_NEGOTIATED_TRADES" | "REPORTINGPRIVATELYNEGOTIATEDTRADES" => Ok(TradeCaptureReportUsageEnum::REPORTINGPRIVATELYNEGOTIATEDTRADES),
                "REPORTING_FLOOR_OR_ROUTED_EXECUTIONS" | "REPORTINGFLOORORROUTEDEXECUTIONS" => Ok(TradeCaptureReportUsageEnum::REPORTINGFLOORORROUTEDEXECUTIONS),
                "REQUEST_TRADE_CANCEL_OR_AMENDMENT" | "REQUESTTRADECANCELORAMENDMENT" => Ok(TradeCaptureReportUsageEnum::REQUESTTRADECANCELORAMENDMENT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TradeCaptureReportUsageEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TradeCaptureReportUsageEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TradeCaptureReportUsageEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS', 'RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES', 'REPORTING_PRIVATELY_NEGOTIATED_TRADES', 'REPORTING_FLOOR_OR_ROUTED_EXECUTIONS', 'REQUEST_TRADE_CANCEL_OR_AMENDMENT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum TradeCaptureReportIdentifierRoleEnum {
    TRADEREPORTID,
    TRADEID,
    TRADEREPORTREFID,
    SECONDARYTRADEID,
}

impl core::fmt::Display for TradeCaptureReportIdentifierRoleEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            TradeCaptureReportIdentifierRoleEnum::TRADEREPORTID => f.write_str("TRADE_REPORT_ID"),
            TradeCaptureReportIdentifierRoleEnum::TRADEID => f.write_str("TRADE_ID"),
            TradeCaptureReportIdentifierRoleEnum::TRADEREPORTREFID => f.write_str("TRADE_REPORT_REF_ID"),
            TradeCaptureReportIdentifierRoleEnum::SECONDARYTRADEID => f.write_str("SECONDARY_TRADE_ID"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for TradeCaptureReportIdentifierRoleEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            TradeCaptureReportIdentifierRoleEnum::TRADEREPORTID => "TRADE_REPORT_ID",
            TradeCaptureReportIdentifierRoleEnum::TRADEID => "TRADE_ID",
            TradeCaptureReportIdentifierRoleEnum::TRADEREPORTREFID => "TRADE_REPORT_REF_ID",
            TradeCaptureReportIdentifierRoleEnum::SECONDARYTRADEID => "SECONDARY_TRADE_ID",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for TradeCaptureReportIdentifierRoleEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "TRADE_REPORT_ID" | "TRADEREPORTID" => Ok(TradeCaptureReportIdentifierRoleEnum::TRADEREPORTID),
                "TRADE_ID" | "TRADEID" => Ok(TradeCaptureReportIdentifierRoleEnum::TRADEID),
                "TRADE_REPORT_REF_ID" | "TRADEREPORTREFID" => Ok(TradeCaptureReportIdentifierRoleEnum::TRADEREPORTREFID),
                "SECONDARY_TRADE_ID" | "SECONDARYTRADEID" => Ok(TradeCaptureReportIdentifierRoleEnum::SECONDARYTRADEID),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for TradeCaptureReportIdentifierRoleEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(TradeCaptureReportIdentifierRoleEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for TradeCaptureReportIdentifierRoleEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['TRADE_REPORT_ID', 'TRADE_ID', 'TRADE_REPORT_REF_ID', 'SECONDARY_TRADE_ID']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum RegistrationTransactionTypeEnum {
    NEW,
    REPLACE,
    CANCEL,
}

impl core::fmt::Display for RegistrationTransactionTypeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            RegistrationTransactionTypeEnum::NEW => f.write_str("NEW"),
            RegistrationTransactionTypeEnum::REPLACE => f.write_str("REPLACE"),
            RegistrationTransactionTypeEnum::CANCEL => f.write_str("CANCEL"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for RegistrationTransactionTypeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            RegistrationTransactionTypeEnum::NEW => "NEW",
            RegistrationTransactionTypeEnum::REPLACE => "REPLACE",
            RegistrationTransactionTypeEnum::CANCEL => "CANCEL",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for RegistrationTransactionTypeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "NEW" => Ok(RegistrationTransactionTypeEnum::NEW),
                "REPLACE" => Ok(RegistrationTransactionTypeEnum::REPLACE),
                "CANCEL" => Ok(RegistrationTransactionTypeEnum::CANCEL),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for RegistrationTransactionTypeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(RegistrationTransactionTypeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for RegistrationTransactionTypeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['NEW', 'REPLACE', 'CANCEL']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum RegistrationStatusEnum {
    ACCEPTED,
    REJECTED,
    HELD,
    REMINDER,
}

impl core::fmt::Display for RegistrationStatusEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            RegistrationStatusEnum::ACCEPTED => f.write_str("ACCEPTED"),
            RegistrationStatusEnum::REJECTED => f.write_str("REJECTED"),
            RegistrationStatusEnum::HELD => f.write_str("HELD"),
            RegistrationStatusEnum::REMINDER => f.write_str("REMINDER"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for RegistrationStatusEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            RegistrationStatusEnum::ACCEPTED => "ACCEPTED",
            RegistrationStatusEnum::REJECTED => "REJECTED",
            RegistrationStatusEnum::HELD => "HELD",
            RegistrationStatusEnum::REMINDER => "REMINDER",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for RegistrationStatusEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "ACCEPTED" => Ok(RegistrationStatusEnum::ACCEPTED),
                "REJECTED" => Ok(RegistrationStatusEnum::REJECTED),
                "HELD" => Ok(RegistrationStatusEnum::HELD),
                "REMINDER" => Ok(RegistrationStatusEnum::REMINDER),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for RegistrationStatusEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(RegistrationStatusEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for RegistrationStatusEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['ACCEPTED', 'REJECTED', 'HELD', 'REMINDER']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum SettlementInstructionModeEnum {
    STANDINGINSTRUCTIONS,
    SPECIFICORDER,
    REQUESTREJECT,
}

impl core::fmt::Display for SettlementInstructionModeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            SettlementInstructionModeEnum::STANDINGINSTRUCTIONS => f.write_str("STANDING_INSTRUCTIONS"),
            SettlementInstructionModeEnum::SPECIFICORDER => f.write_str("SPECIFIC_ORDER"),
            SettlementInstructionModeEnum::REQUESTREJECT => f.write_str("REQUEST_REJECT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for SettlementInstructionModeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            SettlementInstructionModeEnum::STANDINGINSTRUCTIONS => "STANDING_INSTRUCTIONS",
            SettlementInstructionModeEnum::SPECIFICORDER => "SPECIFIC_ORDER",
            SettlementInstructionModeEnum::REQUESTREJECT => "REQUEST_REJECT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for SettlementInstructionModeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "STANDING_INSTRUCTIONS" | "STANDINGINSTRUCTIONS" => Ok(SettlementInstructionModeEnum::STANDINGINSTRUCTIONS),
                "SPECIFIC_ORDER" | "SPECIFICORDER" => Ok(SettlementInstructionModeEnum::SPECIFICORDER),
                "REQUEST_REJECT" | "REQUESTREJECT" => Ok(SettlementInstructionModeEnum::REQUESTREJECT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for SettlementInstructionModeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(SettlementInstructionModeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for SettlementInstructionModeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['STANDING_INSTRUCTIONS', 'SPECIFIC_ORDER', 'REQUEST_REJECT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum SettlementObligationModeEnum {
    PRELIMINARY,
    FINAL,
}

impl core::fmt::Display for SettlementObligationModeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            SettlementObligationModeEnum::PRELIMINARY => f.write_str("PRELIMINARY"),
            SettlementObligationModeEnum::FINAL => f.write_str("FINAL"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for SettlementObligationModeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            SettlementObligationModeEnum::PRELIMINARY => "PRELIMINARY",
            SettlementObligationModeEnum::FINAL => "FINAL",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for SettlementObligationModeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "PRELIMINARY" => Ok(SettlementObligationModeEnum::PRELIMINARY),
                "FINAL" => Ok(SettlementObligationModeEnum::FINAL),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for SettlementObligationModeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(SettlementObligationModeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for SettlementObligationModeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['PRELIMINARY', 'FINAL']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PositionMaintenanceActionEnum {
    NEW,
    REPLACE,
    CANCEL,
    REVERSE,
}

impl core::fmt::Display for PositionMaintenanceActionEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PositionMaintenanceActionEnum::NEW => f.write_str("NEW"),
            PositionMaintenanceActionEnum::REPLACE => f.write_str("REPLACE"),
            PositionMaintenanceActionEnum::CANCEL => f.write_str("CANCEL"),
            PositionMaintenanceActionEnum::REVERSE => f.write_str("REVERSE"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PositionMaintenanceActionEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PositionMaintenanceActionEnum::NEW => "NEW",
            PositionMaintenanceActionEnum::REPLACE => "REPLACE",
            PositionMaintenanceActionEnum::CANCEL => "CANCEL",
            PositionMaintenanceActionEnum::REVERSE => "REVERSE",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PositionMaintenanceActionEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "NEW" => Ok(PositionMaintenanceActionEnum::NEW),
                "REPLACE" => Ok(PositionMaintenanceActionEnum::REPLACE),
                "CANCEL" => Ok(PositionMaintenanceActionEnum::CANCEL),
                "REVERSE" => Ok(PositionMaintenanceActionEnum::REVERSE),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PositionMaintenanceActionEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PositionMaintenanceActionEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PositionMaintenanceActionEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['NEW', 'REPLACE', 'CANCEL', 'REVERSE']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ClearingServiceForPositionManagementEnum {
    POSITIONCHANGESUBMISSION,
    POSITIONADJUSTMENT,
    EXERCISENOTICE,
    ABANDONMENTNOTICE,
    MARGINDISPOSITION,
    POSITIONPLEDGE,
    REQUESTFORPOSITION,
}

impl core::fmt::Display for ClearingServiceForPositionManagementEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ClearingServiceForPositionManagementEnum::POSITIONCHANGESUBMISSION => f.write_str("POSITION_CHANGE_SUBMISSION"),
            ClearingServiceForPositionManagementEnum::POSITIONADJUSTMENT => f.write_str("POSITION_ADJUSTMENT"),
            ClearingServiceForPositionManagementEnum::EXERCISENOTICE => f.write_str("EXERCISE_NOTICE"),
            ClearingServiceForPositionManagementEnum::ABANDONMENTNOTICE => f.write_str("ABANDONMENT_NOTICE"),
            ClearingServiceForPositionManagementEnum::MARGINDISPOSITION => f.write_str("MARGIN_DISPOSITION"),
            ClearingServiceForPositionManagementEnum::POSITIONPLEDGE => f.write_str("POSITION_PLEDGE"),
            ClearingServiceForPositionManagementEnum::REQUESTFORPOSITION => f.write_str("REQUEST_FOR_POSITION"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ClearingServiceForPositionManagementEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ClearingServiceForPositionManagementEnum::POSITIONCHANGESUBMISSION => "POSITION_CHANGE_SUBMISSION",
            ClearingServiceForPositionManagementEnum::POSITIONADJUSTMENT => "POSITION_ADJUSTMENT",
            ClearingServiceForPositionManagementEnum::EXERCISENOTICE => "EXERCISE_NOTICE",
            ClearingServiceForPositionManagementEnum::ABANDONMENTNOTICE => "ABANDONMENT_NOTICE",
            ClearingServiceForPositionManagementEnum::MARGINDISPOSITION => "MARGIN_DISPOSITION",
            ClearingServiceForPositionManagementEnum::POSITIONPLEDGE => "POSITION_PLEDGE",
            ClearingServiceForPositionManagementEnum::REQUESTFORPOSITION => "REQUEST_FOR_POSITION",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ClearingServiceForPositionManagementEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "POSITION_CHANGE_SUBMISSION" | "POSITIONCHANGESUBMISSION" => Ok(ClearingServiceForPositionManagementEnum::POSITIONCHANGESUBMISSION),
                "POSITION_ADJUSTMENT" | "POSITIONADJUSTMENT" => Ok(ClearingServiceForPositionManagementEnum::POSITIONADJUSTMENT),
                "EXERCISE_NOTICE" | "EXERCISENOTICE" => Ok(ClearingServiceForPositionManagementEnum::EXERCISENOTICE),
                "ABANDONMENT_NOTICE" | "ABANDONMENTNOTICE" => Ok(ClearingServiceForPositionManagementEnum::ABANDONMENTNOTICE),
                "MARGIN_DISPOSITION" | "MARGINDISPOSITION" => Ok(ClearingServiceForPositionManagementEnum::MARGINDISPOSITION),
                "POSITION_PLEDGE" | "POSITIONPLEDGE" => Ok(ClearingServiceForPositionManagementEnum::POSITIONPLEDGE),
                "REQUEST_FOR_POSITION" | "REQUESTFORPOSITION" => Ok(ClearingServiceForPositionManagementEnum::REQUESTFORPOSITION),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ClearingServiceForPositionManagementEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ClearingServiceForPositionManagementEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ClearingServiceForPositionManagementEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['POSITION_CHANGE_SUBMISSION', 'POSITION_ADJUSTMENT', 'EXERCISE_NOTICE', 'ABANDONMENT_NOTICE', 'MARGIN_DISPOSITION', 'POSITION_PLEDGE', 'REQUEST_FOR_POSITION']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ClearingServiceForPostTradeProcessingEnum {
    ETP,
    GIVEUP,
    EXCHANGEFORPHYSICAL,
    AVERAGEPRICESYSTEM,
    MUTUALOFFSETSYSTEM,
    TRADEENTRYEDIT,
}

impl core::fmt::Display for ClearingServiceForPostTradeProcessingEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ClearingServiceForPostTradeProcessingEnum::ETP => f.write_str("ETP"),
            ClearingServiceForPostTradeProcessingEnum::GIVEUP => f.write_str("GIVE_UP"),
            ClearingServiceForPostTradeProcessingEnum::EXCHANGEFORPHYSICAL => f.write_str("EXCHANGE_FOR_PHYSICAL"),
            ClearingServiceForPostTradeProcessingEnum::AVERAGEPRICESYSTEM => f.write_str("AVERAGE_PRICE_SYSTEM"),
            ClearingServiceForPostTradeProcessingEnum::MUTUALOFFSETSYSTEM => f.write_str("MUTUAL_OFFSET_SYSTEM"),
            ClearingServiceForPostTradeProcessingEnum::TRADEENTRYEDIT => f.write_str("TRADE_ENTRY_EDIT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ClearingServiceForPostTradeProcessingEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ClearingServiceForPostTradeProcessingEnum::ETP => "ETP",
            ClearingServiceForPostTradeProcessingEnum::GIVEUP => "GIVE_UP",
            ClearingServiceForPostTradeProcessingEnum::EXCHANGEFORPHYSICAL => "EXCHANGE_FOR_PHYSICAL",
            ClearingServiceForPostTradeProcessingEnum::AVERAGEPRICESYSTEM => "AVERAGE_PRICE_SYSTEM",
            ClearingServiceForPostTradeProcessingEnum::MUTUALOFFSETSYSTEM => "MUTUAL_OFFSET_SYSTEM",
            ClearingServiceForPostTradeProcessingEnum::TRADEENTRYEDIT => "TRADE_ENTRY_EDIT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ClearingServiceForPostTradeProcessingEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "ETP" => Ok(ClearingServiceForPostTradeProcessingEnum::ETP),
                "GIVE_UP" | "GIVEUP" => Ok(ClearingServiceForPostTradeProcessingEnum::GIVEUP),
                "EXCHANGE_FOR_PHYSICAL" | "EXCHANGEFORPHYSICAL" => Ok(ClearingServiceForPostTradeProcessingEnum::EXCHANGEFORPHYSICAL),
                "AVERAGE_PRICE_SYSTEM" | "AVERAGEPRICESYSTEM" => Ok(ClearingServiceForPostTradeProcessingEnum::AVERAGEPRICESYSTEM),
                "MUTUAL_OFFSET_SYSTEM" | "MUTUALOFFSETSYSTEM" => Ok(ClearingServiceForPostTradeProcessingEnum::MUTUALOFFSETSYSTEM),
                "TRADE_ENTRY_EDIT" | "TRADEENTRYEDIT" => Ok(ClearingServiceForPostTradeProcessingEnum::TRADEENTRYEDIT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ClearingServiceForPostTradeProcessingEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ClearingServiceForPostTradeProcessingEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ClearingServiceForPostTradeProcessingEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['ETP', 'GIVE_UP', 'EXCHANGE_FOR_PHYSICAL', 'AVERAGE_PRICE_SYSTEM', 'MUTUAL_OFFSET_SYSTEM', 'TRADE_ENTRY_EDIT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum CollateralManagementUsageEnum {
    SECURITIESFINANCINGCOLLATERALIZATION,
    CLEARINGHOUSECOLLATERALIZATION,
}

impl core::fmt::Display for CollateralManagementUsageEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            CollateralManagementUsageEnum::SECURITIESFINANCINGCOLLATERALIZATION => f.write_str("SECURITIES_FINANCING_COLLATERALIZATION"),
            CollateralManagementUsageEnum::CLEARINGHOUSECOLLATERALIZATION => f.write_str("CLEARING_HOUSE_COLLATERALIZATION"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for CollateralManagementUsageEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            CollateralManagementUsageEnum::SECURITIESFINANCINGCOLLATERALIZATION => "SECURITIES_FINANCING_COLLATERALIZATION",
            CollateralManagementUsageEnum::CLEARINGHOUSECOLLATERALIZATION => "CLEARING_HOUSE_COLLATERALIZATION",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for CollateralManagementUsageEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "SECURITIES_FINANCING_COLLATERALIZATION" | "SECURITIESFINANCINGCOLLATERALIZATION" => Ok(CollateralManagementUsageEnum::SECURITIESFINANCINGCOLLATERALIZATION),
                "CLEARING_HOUSE_COLLATERALIZATION" | "CLEARINGHOUSECOLLATERALIZATION" => Ok(CollateralManagementUsageEnum::CLEARINGHOUSECOLLATERALIZATION),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for CollateralManagementUsageEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(CollateralManagementUsageEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for CollateralManagementUsageEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['SECURITIES_FINANCING_COLLATERALIZATION', 'CLEARING_HOUSE_COLLATERALIZATION']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum CollateralAssignmentPurposeEnum {
    ASSIGNINITIALCOLLATERAL,
    REPLENISHCOLLATERAL,
    REPLACEORSUBSTITUTECOLLATERAL,
}

impl core::fmt::Display for CollateralAssignmentPurposeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            CollateralAssignmentPurposeEnum::ASSIGNINITIALCOLLATERAL => f.write_str("ASSIGN_INITIAL_COLLATERAL"),
            CollateralAssignmentPurposeEnum::REPLENISHCOLLATERAL => f.write_str("REPLENISH_COLLATERAL"),
            CollateralAssignmentPurposeEnum::REPLACEORSUBSTITUTECOLLATERAL => f.write_str("REPLACE_OR_SUBSTITUTE_COLLATERAL"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for CollateralAssignmentPurposeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            CollateralAssignmentPurposeEnum::ASSIGNINITIALCOLLATERAL => "ASSIGN_INITIAL_COLLATERAL",
            CollateralAssignmentPurposeEnum::REPLENISHCOLLATERAL => "REPLENISH_COLLATERAL",
            CollateralAssignmentPurposeEnum::REPLACEORSUBSTITUTECOLLATERAL => "REPLACE_OR_SUBSTITUTE_COLLATERAL",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for CollateralAssignmentPurposeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "ASSIGN_INITIAL_COLLATERAL" | "ASSIGNINITIALCOLLATERAL" => Ok(CollateralAssignmentPurposeEnum::ASSIGNINITIALCOLLATERAL),
                "REPLENISH_COLLATERAL" | "REPLENISHCOLLATERAL" => Ok(CollateralAssignmentPurposeEnum::REPLENISHCOLLATERAL),
                "REPLACE_OR_SUBSTITUTE_COLLATERAL" | "REPLACEORSUBSTITUTECOLLATERAL" => Ok(CollateralAssignmentPurposeEnum::REPLACEORSUBSTITUTECOLLATERAL),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for CollateralAssignmentPurposeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(CollateralAssignmentPurposeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for CollateralAssignmentPurposeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['ASSIGN_INITIAL_COLLATERAL', 'REPLENISH_COLLATERAL', 'REPLACE_OR_SUBSTITUTE_COLLATERAL']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum AllocationRoleEnum {
    INITIATOR,
    RESPONDENT,
}

impl core::fmt::Display for AllocationRoleEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            AllocationRoleEnum::INITIATOR => f.write_str("INITIATOR"),
            AllocationRoleEnum::RESPONDENT => f.write_str("RESPONDENT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for AllocationRoleEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            AllocationRoleEnum::INITIATOR => "INITIATOR",
            AllocationRoleEnum::RESPONDENT => "RESPONDENT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for AllocationRoleEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "INITIATOR" => Ok(AllocationRoleEnum::INITIATOR),
                "RESPONDENT" => Ok(AllocationRoleEnum::RESPONDENT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for AllocationRoleEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(AllocationRoleEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for AllocationRoleEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['INITIATOR', 'RESPONDENT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum MatchStatusEnum {
    COMPAREDMATCHEDORAFFIRMED,
    UNCOMPAREDUNMATCHEDORUNAFFIRMED,
}

impl core::fmt::Display for MatchStatusEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            MatchStatusEnum::COMPAREDMATCHEDORAFFIRMED => f.write_str("COMPARED_MATCHED_OR_AFFIRMED"),
            MatchStatusEnum::UNCOMPAREDUNMATCHEDORUNAFFIRMED => f.write_str("UNCOMPARED_UNMATCHED_OR_UNAFFIRMED"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for MatchStatusEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            MatchStatusEnum::COMPAREDMATCHEDORAFFIRMED => "COMPARED_MATCHED_OR_AFFIRMED",
            MatchStatusEnum::UNCOMPAREDUNMATCHEDORUNAFFIRMED => "UNCOMPARED_UNMATCHED_OR_UNAFFIRMED",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for MatchStatusEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "COMPARED_MATCHED_OR_AFFIRMED" | "COMPAREDMATCHEDORAFFIRMED" => Ok(MatchStatusEnum::COMPAREDMATCHEDORAFFIRMED),
                "UNCOMPARED_UNMATCHED_OR_UNAFFIRMED" | "UNCOMPAREDUNMATCHEDORUNAFFIRMED" => Ok(MatchStatusEnum::UNCOMPAREDUNMATCHEDORUNAFFIRMED),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for MatchStatusEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(MatchStatusEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for MatchStatusEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['COMPARED_MATCHED_OR_AFFIRMED', 'UNCOMPARED_UNMATCHED_OR_UNAFFIRMED']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum PostTradeLayoutRowKindEnum {
    FIELD,
    COMPONENT,
}

impl core::fmt::Display for PostTradeLayoutRowKindEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            PostTradeLayoutRowKindEnum::FIELD => f.write_str("FIELD"),
            PostTradeLayoutRowKindEnum::COMPONENT => f.write_str("COMPONENT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for PostTradeLayoutRowKindEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            PostTradeLayoutRowKindEnum::FIELD => "FIELD",
            PostTradeLayoutRowKindEnum::COMPONENT => "COMPONENT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for PostTradeLayoutRowKindEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "FIELD" => Ok(PostTradeLayoutRowKindEnum::FIELD),
                "COMPONENT" => Ok(PostTradeLayoutRowKindEnum::COMPONENT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for PostTradeLayoutRowKindEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(PostTradeLayoutRowKindEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for PostTradeLayoutRowKindEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['FIELD', 'COMPONENT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum InfrastructureCategoryEnum {
    BUSINESSMESSAGEREJECTS,
    NETWORKSTATUSCOMMUNICATION,
    USERMANAGEMENT,
    APPLICATIONSEQUENCING,
}

impl core::fmt::Display for InfrastructureCategoryEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            InfrastructureCategoryEnum::BUSINESSMESSAGEREJECTS => f.write_str("BUSINESS_MESSAGE_REJECTS"),
            InfrastructureCategoryEnum::NETWORKSTATUSCOMMUNICATION => f.write_str("NETWORK_STATUS_COMMUNICATION"),
            InfrastructureCategoryEnum::USERMANAGEMENT => f.write_str("USER_MANAGEMENT"),
            InfrastructureCategoryEnum::APPLICATIONSEQUENCING => f.write_str("APPLICATION_SEQUENCING"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for InfrastructureCategoryEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            InfrastructureCategoryEnum::BUSINESSMESSAGEREJECTS => "BUSINESS_MESSAGE_REJECTS",
            InfrastructureCategoryEnum::NETWORKSTATUSCOMMUNICATION => "NETWORK_STATUS_COMMUNICATION",
            InfrastructureCategoryEnum::USERMANAGEMENT => "USER_MANAGEMENT",
            InfrastructureCategoryEnum::APPLICATIONSEQUENCING => "APPLICATION_SEQUENCING",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for InfrastructureCategoryEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "BUSINESS_MESSAGE_REJECTS" | "BUSINESSMESSAGEREJECTS" => Ok(InfrastructureCategoryEnum::BUSINESSMESSAGEREJECTS),
                "NETWORK_STATUS_COMMUNICATION" | "NETWORKSTATUSCOMMUNICATION" => Ok(InfrastructureCategoryEnum::NETWORKSTATUSCOMMUNICATION),
                "USER_MANAGEMENT" | "USERMANAGEMENT" => Ok(InfrastructureCategoryEnum::USERMANAGEMENT),
                "APPLICATION_SEQUENCING" | "APPLICATIONSEQUENCING" => Ok(InfrastructureCategoryEnum::APPLICATIONSEQUENCING),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for InfrastructureCategoryEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(InfrastructureCategoryEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for InfrastructureCategoryEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum InfrastructureComponentName {
    ApplIDReportGrp,
    ApplIDRequestAckGrp,
    ApplIDRequestGrp,
    CompIDReqGrp,
    CompIDStatGrp,
    ThrottleMsgTypeGrp,
    ThrottleParamsGrp,
    UsernameGrp,
}

impl core::fmt::Display for InfrastructureComponentName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            InfrastructureComponentName::ApplIDReportGrp => f.write_str("ApplIDReportGrp"),
            InfrastructureComponentName::ApplIDRequestAckGrp => f.write_str("ApplIDRequestAckGrp"),
            InfrastructureComponentName::ApplIDRequestGrp => f.write_str("ApplIDRequestGrp"),
            InfrastructureComponentName::CompIDReqGrp => f.write_str("CompIDReqGrp"),
            InfrastructureComponentName::CompIDStatGrp => f.write_str("CompIDStatGrp"),
            InfrastructureComponentName::ThrottleMsgTypeGrp => f.write_str("ThrottleMsgTypeGrp"),
            InfrastructureComponentName::ThrottleParamsGrp => f.write_str("ThrottleParamsGrp"),
            InfrastructureComponentName::UsernameGrp => f.write_str("UsernameGrp"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for InfrastructureComponentName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            InfrastructureComponentName::ApplIDReportGrp => "ApplIDReportGrp",
            InfrastructureComponentName::ApplIDRequestAckGrp => "ApplIDRequestAckGrp",
            InfrastructureComponentName::ApplIDRequestGrp => "ApplIDRequestGrp",
            InfrastructureComponentName::CompIDReqGrp => "CompIDReqGrp",
            InfrastructureComponentName::CompIDStatGrp => "CompIDStatGrp",
            InfrastructureComponentName::ThrottleMsgTypeGrp => "ThrottleMsgTypeGrp",
            InfrastructureComponentName::ThrottleParamsGrp => "ThrottleParamsGrp",
            InfrastructureComponentName::UsernameGrp => "UsernameGrp",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for InfrastructureComponentName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "ApplIDReportGrp" => Ok(InfrastructureComponentName::ApplIDReportGrp),
                "ApplIDRequestAckGrp" => Ok(InfrastructureComponentName::ApplIDRequestAckGrp),
                "ApplIDRequestGrp" => Ok(InfrastructureComponentName::ApplIDRequestGrp),
                "CompIDReqGrp" => Ok(InfrastructureComponentName::CompIDReqGrp),
                "CompIDStatGrp" => Ok(InfrastructureComponentName::CompIDStatGrp),
                "ThrottleMsgTypeGrp" => Ok(InfrastructureComponentName::ThrottleMsgTypeGrp),
                "ThrottleParamsGrp" => Ok(InfrastructureComponentName::ThrottleParamsGrp),
                "UsernameGrp" => Ok(InfrastructureComponentName::UsernameGrp),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for InfrastructureComponentName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(InfrastructureComponentName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for InfrastructureComponentName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['ApplIDReportGrp', 'ApplIDRequestAckGrp', 'ApplIDRequestGrp', 'CompIDReqGrp', 'CompIDStatGrp', 'ThrottleMsgTypeGrp', 'ThrottleParamsGrp', 'UsernameGrp']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum BusinessRejectReasonEnum {
    OTHER,
    UNKNOWNID,
    UNKNOWNSECURITY,
    UNSUPPORTEDMESSAGETYPE,
    APPLICATIONNOTAVAILABLE,
    CONDITIONALLYREQUIREDFIELDMISSING,
    NOTAUTHORISED,
    DELIVERTOFIRMNOTAVAILABLE,
    THROTTLELIMITEXCEEDED,
    THROTTLELIMITEXCEEDEDSESSIONDISCONNECT,
    THROTTLEDMESSAGESREJECTEDONREQUEST,
    INVALIDPRICEINCREMENT,
}

impl core::fmt::Display for BusinessRejectReasonEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            BusinessRejectReasonEnum::OTHER => f.write_str("OTHER"),
            BusinessRejectReasonEnum::UNKNOWNID => f.write_str("UNKNOWN_ID"),
            BusinessRejectReasonEnum::UNKNOWNSECURITY => f.write_str("UNKNOWN_SECURITY"),
            BusinessRejectReasonEnum::UNSUPPORTEDMESSAGETYPE => f.write_str("UNSUPPORTED_MESSAGE_TYPE"),
            BusinessRejectReasonEnum::APPLICATIONNOTAVAILABLE => f.write_str("APPLICATION_NOT_AVAILABLE"),
            BusinessRejectReasonEnum::CONDITIONALLYREQUIREDFIELDMISSING => f.write_str("CONDITIONALLY_REQUIRED_FIELD_MISSING"),
            BusinessRejectReasonEnum::NOTAUTHORISED => f.write_str("NOT_AUTHORISED"),
            BusinessRejectReasonEnum::DELIVERTOFIRMNOTAVAILABLE => f.write_str("DELIVER_TO_FIRM_NOT_AVAILABLE"),
            BusinessRejectReasonEnum::THROTTLELIMITEXCEEDED => f.write_str("THROTTLE_LIMIT_EXCEEDED"),
            BusinessRejectReasonEnum::THROTTLELIMITEXCEEDEDSESSIONDISCONNECT => f.write_str("THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT"),
            BusinessRejectReasonEnum::THROTTLEDMESSAGESREJECTEDONREQUEST => f.write_str("THROTTLED_MESSAGES_REJECTED_ON_REQUEST"),
            BusinessRejectReasonEnum::INVALIDPRICEINCREMENT => f.write_str("INVALID_PRICE_INCREMENT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for BusinessRejectReasonEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            BusinessRejectReasonEnum::OTHER => "OTHER",
            BusinessRejectReasonEnum::UNKNOWNID => "UNKNOWN_ID",
            BusinessRejectReasonEnum::UNKNOWNSECURITY => "UNKNOWN_SECURITY",
            BusinessRejectReasonEnum::UNSUPPORTEDMESSAGETYPE => "UNSUPPORTED_MESSAGE_TYPE",
            BusinessRejectReasonEnum::APPLICATIONNOTAVAILABLE => "APPLICATION_NOT_AVAILABLE",
            BusinessRejectReasonEnum::CONDITIONALLYREQUIREDFIELDMISSING => "CONDITIONALLY_REQUIRED_FIELD_MISSING",
            BusinessRejectReasonEnum::NOTAUTHORISED => "NOT_AUTHORISED",
            BusinessRejectReasonEnum::DELIVERTOFIRMNOTAVAILABLE => "DELIVER_TO_FIRM_NOT_AVAILABLE",
            BusinessRejectReasonEnum::THROTTLELIMITEXCEEDED => "THROTTLE_LIMIT_EXCEEDED",
            BusinessRejectReasonEnum::THROTTLELIMITEXCEEDEDSESSIONDISCONNECT => "THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT",
            BusinessRejectReasonEnum::THROTTLEDMESSAGESREJECTEDONREQUEST => "THROTTLED_MESSAGES_REJECTED_ON_REQUEST",
            BusinessRejectReasonEnum::INVALIDPRICEINCREMENT => "INVALID_PRICE_INCREMENT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for BusinessRejectReasonEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "OTHER" => Ok(BusinessRejectReasonEnum::OTHER),
                "UNKNOWN_ID" | "UNKNOWNID" => Ok(BusinessRejectReasonEnum::UNKNOWNID),
                "UNKNOWN_SECURITY" | "UNKNOWNSECURITY" => Ok(BusinessRejectReasonEnum::UNKNOWNSECURITY),
                "UNSUPPORTED_MESSAGE_TYPE" | "UNSUPPORTEDMESSAGETYPE" => Ok(BusinessRejectReasonEnum::UNSUPPORTEDMESSAGETYPE),
                "APPLICATION_NOT_AVAILABLE" | "APPLICATIONNOTAVAILABLE" => Ok(BusinessRejectReasonEnum::APPLICATIONNOTAVAILABLE),
                "CONDITIONALLY_REQUIRED_FIELD_MISSING" | "CONDITIONALLYREQUIREDFIELDMISSING" => Ok(BusinessRejectReasonEnum::CONDITIONALLYREQUIREDFIELDMISSING),
                "NOT_AUTHORISED" | "NOTAUTHORISED" => Ok(BusinessRejectReasonEnum::NOTAUTHORISED),
                "DELIVER_TO_FIRM_NOT_AVAILABLE" | "DELIVERTOFIRMNOTAVAILABLE" => Ok(BusinessRejectReasonEnum::DELIVERTOFIRMNOTAVAILABLE),
                "THROTTLE_LIMIT_EXCEEDED" | "THROTTLELIMITEXCEEDED" => Ok(BusinessRejectReasonEnum::THROTTLELIMITEXCEEDED),
                "THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT" | "THROTTLELIMITEXCEEDEDSESSIONDISCONNECT" => Ok(BusinessRejectReasonEnum::THROTTLELIMITEXCEEDEDSESSIONDISCONNECT),
                "THROTTLED_MESSAGES_REJECTED_ON_REQUEST" | "THROTTLEDMESSAGESREJECTEDONREQUEST" => Ok(BusinessRejectReasonEnum::THROTTLEDMESSAGESREJECTEDONREQUEST),
                "INVALID_PRICE_INCREMENT" | "INVALIDPRICEINCREMENT" => Ok(BusinessRejectReasonEnum::INVALIDPRICEINCREMENT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for BusinessRejectReasonEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(BusinessRejectReasonEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for BusinessRejectReasonEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['OTHER', 'UNKNOWN_ID', 'UNKNOWN_SECURITY', 'UNSUPPORTED_MESSAGE_TYPE', 'APPLICATION_NOT_AVAILABLE', 'CONDITIONALLY_REQUIRED_FIELD_MISSING', 'NOT_AUTHORISED', 'DELIVER_TO_FIRM_NOT_AVAILABLE', 'THROTTLE_LIMIT_EXCEEDED', 'THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT', 'THROTTLED_MESSAGES_REJECTED_ON_REQUEST', 'INVALID_PRICE_INCREMENT']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum NetworkStatusScenarioEnum {
    SCENARIOA,
    SCENARIOB,
}

impl core::fmt::Display for NetworkStatusScenarioEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            NetworkStatusScenarioEnum::SCENARIOA => f.write_str("SCENARIO_A"),
            NetworkStatusScenarioEnum::SCENARIOB => f.write_str("SCENARIO_B"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for NetworkStatusScenarioEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            NetworkStatusScenarioEnum::SCENARIOA => "SCENARIO_A",
            NetworkStatusScenarioEnum::SCENARIOB => "SCENARIO_B",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for NetworkStatusScenarioEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "SCENARIO_A" | "SCENARIOA" => Ok(NetworkStatusScenarioEnum::SCENARIOA),
                "SCENARIO_B" | "SCENARIOB" => Ok(NetworkStatusScenarioEnum::SCENARIOB),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for NetworkStatusScenarioEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(NetworkStatusScenarioEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for NetworkStatusScenarioEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['SCENARIO_A', 'SCENARIO_B']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ApplicationMessageReportTypeEnum {
    RESET,
    LASTMESSAGE,
    KEEPALIVE,
    RESENDCOMPLETED,
}

impl core::fmt::Display for ApplicationMessageReportTypeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ApplicationMessageReportTypeEnum::RESET => f.write_str("RESET"),
            ApplicationMessageReportTypeEnum::LASTMESSAGE => f.write_str("LAST_MESSAGE"),
            ApplicationMessageReportTypeEnum::KEEPALIVE => f.write_str("KEEP_ALIVE"),
            ApplicationMessageReportTypeEnum::RESENDCOMPLETED => f.write_str("RESEND_COMPLETED"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ApplicationMessageReportTypeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ApplicationMessageReportTypeEnum::RESET => "RESET",
            ApplicationMessageReportTypeEnum::LASTMESSAGE => "LAST_MESSAGE",
            ApplicationMessageReportTypeEnum::KEEPALIVE => "KEEP_ALIVE",
            ApplicationMessageReportTypeEnum::RESENDCOMPLETED => "RESEND_COMPLETED",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ApplicationMessageReportTypeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "RESET" => Ok(ApplicationMessageReportTypeEnum::RESET),
                "LAST_MESSAGE" | "LASTMESSAGE" => Ok(ApplicationMessageReportTypeEnum::LASTMESSAGE),
                "KEEP_ALIVE" | "KEEPALIVE" => Ok(ApplicationMessageReportTypeEnum::KEEPALIVE),
                "RESEND_COMPLETED" | "RESENDCOMPLETED" => Ok(ApplicationMessageReportTypeEnum::RESENDCOMPLETED),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ApplicationMessageReportTypeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ApplicationMessageReportTypeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ApplicationMessageReportTypeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['RESET', 'LAST_MESSAGE', 'KEEP_ALIVE', 'RESEND_COMPLETED']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum NetworkRequestTypeEnum {
    SNAPSHOT,
    STOPSUBSCRIBING,
}

impl core::fmt::Display for NetworkRequestTypeEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            NetworkRequestTypeEnum::SNAPSHOT => f.write_str("SNAPSHOT"),
            NetworkRequestTypeEnum::STOPSUBSCRIBING => f.write_str("STOP_SUBSCRIBING"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for NetworkRequestTypeEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            NetworkRequestTypeEnum::SNAPSHOT => "SNAPSHOT",
            NetworkRequestTypeEnum::STOPSUBSCRIBING => "STOP_SUBSCRIBING",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for NetworkRequestTypeEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "SNAPSHOT" => Ok(NetworkRequestTypeEnum::SNAPSHOT),
                "STOP_SUBSCRIBING" | "STOPSUBSCRIBING" => Ok(NetworkRequestTypeEnum::STOPSUBSCRIBING),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for NetworkRequestTypeEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(NetworkRequestTypeEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for NetworkRequestTypeEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['SNAPSHOT', 'STOP_SUBSCRIBING']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum StandardResponseDirectionEnum {
    PRETRADE,
    TRADE,
    POSTTRADE,
}

impl core::fmt::Display for StandardResponseDirectionEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            StandardResponseDirectionEnum::PRETRADE => f.write_str("PRE_TRADE"),
            StandardResponseDirectionEnum::TRADE => f.write_str("TRADE"),
            StandardResponseDirectionEnum::POSTTRADE => f.write_str("POST_TRADE"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for StandardResponseDirectionEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            StandardResponseDirectionEnum::PRETRADE => "PRE_TRADE",
            StandardResponseDirectionEnum::TRADE => "TRADE",
            StandardResponseDirectionEnum::POSTTRADE => "POST_TRADE",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for StandardResponseDirectionEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "PRE_TRADE" | "PRETRADE" => Ok(StandardResponseDirectionEnum::PRETRADE),
                "TRADE" => Ok(StandardResponseDirectionEnum::TRADE),
                "POST_TRADE" | "POSTTRADE" => Ok(StandardResponseDirectionEnum::POSTTRADE),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for StandardResponseDirectionEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(StandardResponseDirectionEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for StandardResponseDirectionEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['PRE_TRADE', 'TRADE', 'POST_TRADE']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum BusinessMessageReferenceDirectionEnum {
    PRETRADE,
    TRADE,
    POSTTRADE,
}

impl core::fmt::Display for BusinessMessageReferenceDirectionEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            BusinessMessageReferenceDirectionEnum::PRETRADE => f.write_str("PRE_TRADE"),
            BusinessMessageReferenceDirectionEnum::TRADE => f.write_str("TRADE"),
            BusinessMessageReferenceDirectionEnum::POSTTRADE => f.write_str("POST_TRADE"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for BusinessMessageReferenceDirectionEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            BusinessMessageReferenceDirectionEnum::PRETRADE => "PRE_TRADE",
            BusinessMessageReferenceDirectionEnum::TRADE => "TRADE",
            BusinessMessageReferenceDirectionEnum::POSTTRADE => "POST_TRADE",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for BusinessMessageReferenceDirectionEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "PRE_TRADE" | "PRETRADE" => Ok(BusinessMessageReferenceDirectionEnum::PRETRADE),
                "TRADE" => Ok(BusinessMessageReferenceDirectionEnum::TRADE),
                "POST_TRADE" | "POSTTRADE" => Ok(BusinessMessageReferenceDirectionEnum::POSTTRADE),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for BusinessMessageReferenceDirectionEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(BusinessMessageReferenceDirectionEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for BusinessMessageReferenceDirectionEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['PRE_TRADE', 'TRADE', 'POST_TRADE']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum InfrastructureGlobalComponentName {
    ApplicationSequenceControl,
}

impl core::fmt::Display for InfrastructureGlobalComponentName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            InfrastructureGlobalComponentName::ApplicationSequenceControl => f.write_str("ApplicationSequenceControl"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for InfrastructureGlobalComponentName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            InfrastructureGlobalComponentName::ApplicationSequenceControl => "ApplicationSequenceControl",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for InfrastructureGlobalComponentName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "ApplicationSequenceControl" => Ok(InfrastructureGlobalComponentName::ApplicationSequenceControl),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for InfrastructureGlobalComponentName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(InfrastructureGlobalComponentName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for InfrastructureGlobalComponentName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['ApplicationSequenceControl']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum ApplicationSequenceControlFieldName {
    ApplID,
    ApplSeqNum,
    ApplLastSeqNum,
    ApplResendFlag,
}

impl core::fmt::Display for ApplicationSequenceControlFieldName {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            ApplicationSequenceControlFieldName::ApplID => f.write_str("ApplID"),
            ApplicationSequenceControlFieldName::ApplSeqNum => f.write_str("ApplSeqNum"),
            ApplicationSequenceControlFieldName::ApplLastSeqNum => f.write_str("ApplLastSeqNum"),
            ApplicationSequenceControlFieldName::ApplResendFlag => f.write_str("ApplResendFlag"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ApplicationSequenceControlFieldName {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            ApplicationSequenceControlFieldName::ApplID => "ApplID",
            ApplicationSequenceControlFieldName::ApplSeqNum => "ApplSeqNum",
            ApplicationSequenceControlFieldName::ApplLastSeqNum => "ApplLastSeqNum",
            ApplicationSequenceControlFieldName::ApplResendFlag => "ApplResendFlag",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ApplicationSequenceControlFieldName {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "ApplID" => Ok(ApplicationSequenceControlFieldName::ApplID),
                "ApplSeqNum" => Ok(ApplicationSequenceControlFieldName::ApplSeqNum),
                "ApplLastSeqNum" => Ok(ApplicationSequenceControlFieldName::ApplLastSeqNum),
                "ApplResendFlag" => Ok(ApplicationSequenceControlFieldName::ApplResendFlag),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for ApplicationSequenceControlFieldName: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(ApplicationSequenceControlFieldName)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for ApplicationSequenceControlFieldName {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['ApplID', 'ApplSeqNum', 'ApplLastSeqNum', 'ApplResendFlag']",
            "typing".into(),
        )
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
pub enum InfrastructureLayoutRowKindEnum {
    FIELD,
    COMPONENT,
}

impl core::fmt::Display for InfrastructureLayoutRowKindEnum {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        match self {
            InfrastructureLayoutRowKindEnum::FIELD => f.write_str("FIELD"),
            InfrastructureLayoutRowKindEnum::COMPONENT => f.write_str("COMPONENT"),
        }
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for InfrastructureLayoutRowKindEnum {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        let s: &str = match self {
            InfrastructureLayoutRowKindEnum::FIELD => "FIELD",
            InfrastructureLayoutRowKindEnum::COMPONENT => "COMPONENT",
        };
        Ok(pyo3::types::PyString::new(py, s).into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for InfrastructureLayoutRowKindEnum {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(s) = ob.extract::<&str>() {
            match s {
                "FIELD" => Ok(InfrastructureLayoutRowKindEnum::FIELD),
                "COMPONENT" => Ok(InfrastructureLayoutRowKindEnum::COMPONENT),
                _ => Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("invalid value for InfrastructureLayoutRowKindEnum: {}", s),
                )),
            }
        } else {
            Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                concat!("expected str for ", stringify!(InfrastructureLayoutRowKindEnum)),
            ))
        }
    }
}

#[cfg(feature = "stubgen")]
impl ::pyo3_stub_gen::PyStubType for InfrastructureLayoutRowKindEnum {
    fn type_output() -> ::pyo3_stub_gen::TypeInfo {
        ::pyo3_stub_gen::TypeInfo::with_module(
            "typing.Literal['FIELD', 'COMPONENT']",
            "typing".into(),
        )
    }
}

// Classes

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct FIXIntroduction {
    #[cfg_attr(feature = "serde", serde(default))]
    pub published_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub published_date: Option<NaiveDate>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub publisher: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub preface: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub introduction_text: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub utc_leap_seconds_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub about_fpl: Option<FIXProtocolLimited>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub standards: Option<Vec<FIXFamilyStandard>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub extension_packs: Option<Vec<ExtensionPack>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub datatypes: Option<Vec<FIXDatatype>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub business_areas: Option<Vec<BusinessArea>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub global_components: Option<Vec<GlobalComponent>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub udf_ranges: Option<Vec<UDFTagRange>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub product_coverage: Option<Vec<ProductCoverage>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl FIXIntroduction {
    #[new]
    #[pyo3(signature = (published_version=None, published_date=None, publisher=None, preface=None, introduction_text=None, utc_leap_seconds_note=None, about_fpl=None, standards=None, extension_packs=None, datatypes=None, business_areas=None, global_components=None, udf_ranges=None, product_coverage=None))]
    pub fn new(published_version: Option<String>, published_date: Option<NaiveDate>, publisher: Option<String>, preface: Option<String>, introduction_text: Option<String>, utc_leap_seconds_note: Option<String>, about_fpl: Option<serde_utils::PyValue<FIXProtocolLimited>>, standards: Option<serde_utils::PyValue<Vec<FIXFamilyStandard>>>, extension_packs: Option<serde_utils::PyValue<Vec<ExtensionPack>>>, datatypes: Option<serde_utils::PyValue<Vec<FIXDatatype>>>, business_areas: Option<serde_utils::PyValue<Vec<BusinessArea>>>, global_components: Option<serde_utils::PyValue<Vec<GlobalComponent>>>, udf_ranges: Option<serde_utils::PyValue<Vec<UDFTagRange>>>, product_coverage: Option<Vec<ProductCoverage>>) -> Self {
        let about_fpl = about_fpl.map(|v| v.into_inner());
        let standards = standards.map(|v| v.into_inner());
        let extension_packs = extension_packs.map(|v| v.into_inner());
        let datatypes = datatypes.map(|v| v.into_inner());
        let business_areas = business_areas.map(|v| v.into_inner());
        let global_components = global_components.map(|v| v.into_inner());
        let udf_ranges = udf_ranges.map(|v| v.into_inner());
        FIXIntroduction{published_version, published_date, publisher, preface, introduction_text, utc_leap_seconds_note, about_fpl, standards, extension_packs, datatypes, business_areas, global_components, udf_ranges, product_coverage}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<FIXIntroduction>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<FIXIntroduction> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<FIXIntroduction>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid FIXIntroduction",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct FIXProtocolLimited {
    #[cfg_attr(feature = "serde", serde(default))]
    pub brand_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub legal_name: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub website: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub member_firms_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub working_groups_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub committees_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub member_types: Option<Vec<FPLMemberType>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub governance_bodies: Option<Vec<FPLCommitteeRole>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub product_committees: Option<Vec<FPLProductGroup>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub regional_committees: Option<Vec<FPLRegion>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl FIXProtocolLimited {
    #[new]
    #[pyo3(signature = (brand_name=None, legal_name=None, website=None, member_firms_url=None, working_groups_url=None, committees_url=None, member_types=None, governance_bodies=None, product_committees=None, regional_committees=None))]
    pub fn new(brand_name: Option<String>, legal_name: Option<String>, website: Option<uri>, member_firms_url: Option<uri>, working_groups_url: Option<uri>, committees_url: Option<uri>, member_types: Option<Vec<FPLMemberType>>, governance_bodies: Option<Vec<FPLCommitteeRole>>, product_committees: Option<Vec<FPLProductGroup>>, regional_committees: Option<Vec<FPLRegion>>) -> Self {
        FIXProtocolLimited{brand_name, legal_name, website, member_firms_url, working_groups_url, committees_url, member_types, governance_bodies, product_committees, regional_committees}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<FIXProtocolLimited>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<FIXProtocolLimited> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<FIXProtocolLimited>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid FIXProtocolLimited",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct FIXFamilyStandard {
    pub id: String,
    pub name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub acronym: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub see_also: Option<Vec<uri>>,
    pub layer: StandardLayer,
    #[cfg_attr(feature = "serde", serde(default))]
    pub version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub session_profile: Option<SessionProtocolName>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub encoding_name: Option<StandardEncodingName>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl FIXFamilyStandard {
    #[new]
    #[pyo3(signature = (id, name, layer, description=None, acronym=None, see_also=None, version=None, session_profile=None, encoding_name=None))]
    pub fn new(id: String, name: String, layer: StandardLayer, description: Option<String>, acronym: Option<String>, see_also: Option<Vec<uri>>, version: Option<String>, session_profile: Option<SessionProtocolName>, encoding_name: Option<StandardEncodingName>) -> Self {
        FIXFamilyStandard{id, name, layer, description, acronym, see_also, version, session_profile, encoding_name}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<FIXFamilyStandard>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<FIXFamilyStandard> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<FIXFamilyStandard>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid FIXFamilyStandard",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for FIXFamilyStandard {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a FIXFamilyStandard from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ExtensionPack {
    pub number: isize,
    pub title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub size: Option<ExtensionPackSize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub enhancement_summary: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub applies_to_session_layer_only: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub applies_to_fixml_only: Option<bool>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ExtensionPack {
    #[new]
    #[pyo3(signature = (number, title, size=None, enhancement_summary=None, applies_to_session_layer_only=None, applies_to_fixml_only=None))]
    pub fn new(number: isize, title: String, size: Option<ExtensionPackSize>, enhancement_summary: Option<String>, applies_to_session_layer_only: Option<bool>, applies_to_fixml_only: Option<bool>) -> Self {
        ExtensionPack{number, title, size, enhancement_summary, applies_to_session_layer_only, applies_to_fixml_only}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ExtensionPack>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ExtensionPack> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ExtensionPack>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ExtensionPack",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ExtensionPack {
    type Key   = isize;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.number;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("number".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ExtensionPack from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("number".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct FIXDatatype {
    pub datatype_name: FIXDatatypeName,
    pub definition: String,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub value_space: Option<Vec<ISO11404ValueSpace>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub value_space_notes: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub deprecated_for_new_designs: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub external_code_set: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub time_unit: Option<Vec<TimePrecision>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub radix: Option<isize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub repertoire: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub index_lower_bound: Option<isize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub index_upper_bound: Option<isize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub minimum_value: Option<isize>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub maximum_value: Option<isize>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub footnote_numbers: Option<Vec<isize>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl FIXDatatype {
    #[new]
    #[pyo3(signature = (datatype_name, definition, value_space=None, value_space_notes=None, deprecated_for_new_designs=None, external_code_set=None, time_unit=None, radix=None, repertoire=None, index_lower_bound=None, index_upper_bound=None, minimum_value=None, maximum_value=None, footnote_numbers=None))]
    pub fn new(datatype_name: FIXDatatypeName, definition: String, value_space: Option<Vec<ISO11404ValueSpace>>, value_space_notes: Option<String>, deprecated_for_new_designs: Option<bool>, external_code_set: Option<String>, time_unit: Option<Vec<TimePrecision>>, radix: Option<isize>, repertoire: Option<String>, index_lower_bound: Option<isize>, index_upper_bound: Option<isize>, minimum_value: Option<isize>, maximum_value: Option<isize>, footnote_numbers: Option<Vec<isize>>) -> Self {
        FIXDatatype{datatype_name, definition, value_space, value_space_notes, deprecated_for_new_designs, external_code_set, time_unit, radix, repertoire, index_lower_bound, index_upper_bound, minimum_value, maximum_value, footnote_numbers}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<FIXDatatype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<FIXDatatype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<FIXDatatype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid FIXDatatype",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for FIXDatatype {
    type Key   = FIXDatatypeName;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.datatype_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("datatype_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a FIXDatatype from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("datatype_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct BusinessArea {
    pub area: BusinessAreaEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub categories: Option<Vec<MessageCategory>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl BusinessArea {
    #[new]
    #[pyo3(signature = (area, title=None, description=None, categories=None))]
    pub fn new(area: BusinessAreaEnum, title: Option<String>, description: Option<String>, categories: Option<serde_utils::PyValue<Vec<MessageCategory>>>) -> Self {
        let categories = categories.map(|v| v.into_inner());
        BusinessArea{area, title, description, categories}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<BusinessArea>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<BusinessArea> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<BusinessArea>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid BusinessArea",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for BusinessArea {
    type Key   = BusinessAreaEnum;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.area;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("area".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("area".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("area".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct MessageCategory {
    pub category: MessageCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    pub business_area: BusinessAreaEnum,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Option<Vec<Message>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl MessageCategory {
    #[new]
    #[pyo3(signature = (category, business_area, title=None, description=None, messages=None))]
    pub fn new(category: MessageCategoryEnum, business_area: BusinessAreaEnum, title: Option<String>, description: Option<String>, messages: Option<serde_utils::PyValue<Vec<Message>>>) -> Self {
        let messages = messages.map(|v| v.into_inner());
        MessageCategory{category, business_area, title, description, messages}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<MessageCategory>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<MessageCategory> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<MessageCategory>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid MessageCategory",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for MessageCategory {
    type Key   = MessageCategoryEnum;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.category;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("category".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a MessageCategory from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("category".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Field {
    pub tag: isize,
    pub field_name: String,
    pub datatype: FIXDatatypeName,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub requirement: Option<FieldRequirement>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub is_user_defined: Option<bool>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Field {
    #[new]
    #[pyo3(signature = (tag, field_name, datatype, description=None, requirement=None, is_user_defined=None))]
    pub fn new(tag: isize, field_name: String, datatype: FIXDatatypeName, description: Option<String>, requirement: Option<FieldRequirement>, is_user_defined: Option<bool>) -> Self {
        Field{tag, field_name, datatype, description, requirement, is_user_defined}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Field>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Field> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Field>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Field",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Field {
    type Key   = isize;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.tag;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("tag".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Field from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("tag".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Component {
    pub component_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    pub scope: ComponentScope,
    #[cfg_attr(feature = "serde", serde(default))]
    pub is_repeating_group: Option<bool>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub fields: Option<Vec<Field>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub nested_components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Component {
    #[new]
    #[pyo3(signature = (component_name, scope, description=None, is_repeating_group=None, fields=None, nested_components=None))]
    pub fn new(component_name: String, scope: ComponentScope, description: Option<String>, is_repeating_group: Option<bool>, fields: Option<serde_utils::PyValue<Vec<Field>>>, nested_components: Option<Vec<String>>) -> Self {
        let fields = fields.map(|v| v.into_inner());
        Component{component_name, scope, description, is_repeating_group, fields, nested_components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Component>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Component> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Component>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Component",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Component {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Component from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}
#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature="serde", serde(untagged))]
pub enum ComponentOrSubtype {    GlobalComponent(GlobalComponent),     CommonComponent(CommonComponent),     SpecificComponent(SpecificComponent)}

impl From<GlobalComponent>   for ComponentOrSubtype { fn from(x: GlobalComponent)   -> Self { Self::GlobalComponent(x) } }
impl From<CommonComponent>   for ComponentOrSubtype { fn from(x: CommonComponent)   -> Self { Self::CommonComponent(x) } }
impl From<SpecificComponent>   for ComponentOrSubtype { fn from(x: SpecificComponent)   -> Self { Self::SpecificComponent(x) } }

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for ComponentOrSubtype {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<GlobalComponent>() {
            return Ok(ComponentOrSubtype::GlobalComponent(val));
        }        if let Ok(val) = ob.extract::<CommonComponent>() {
            return Ok(ComponentOrSubtype::CommonComponent(val));
        }        if let Ok(val) = ob.extract::<SpecificComponent>() {
            return Ok(ComponentOrSubtype::SpecificComponent(val));
        }Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ComponentOrSubtype",
        ))
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for ComponentOrSubtype {
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;

    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        match self {
            ComponentOrSubtype::GlobalComponent(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ComponentOrSubtype::CommonComponent(val) => val.into_pyobject(py).map(move |b| b.into_any()),
            ComponentOrSubtype::SpecificComponent(val) => val.into_pyobject(py).map(move |b| b.into_any()),
        }
    }
}


#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ComponentOrSubtype>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ComponentOrSubtype> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ComponentOrSubtype>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ComponentOrSubtype",
        ))
    }
}

#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ComponentOrSubtype {
    type Key       = String;
    type Value     = serde_value::Value;
    type Error     = String;

    fn from_pair_mapping(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = GlobalComponent::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ComponentOrSubtype::GlobalComponent(x));
        }
        if let Ok(x) = CommonComponent::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ComponentOrSubtype::CommonComponent(x));
        }
        if let Ok(x) = SpecificComponent::from_pair_mapping(k.clone(), v.clone()) {
            return Ok(ComponentOrSubtype::SpecificComponent(x));
        }
        Err("none of the variants matched the mapping form".into())
    }

    fn from_pair_simple(k: Self::Key, v: Self::Value) -> Result<Self, Self::Error> {
        if let Ok(x) = GlobalComponent::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ComponentOrSubtype::GlobalComponent(x));
        }
        if let Ok(x) = CommonComponent::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ComponentOrSubtype::CommonComponent(x));
        }
        if let Ok(x) = SpecificComponent::from_pair_simple(k.clone(), v.clone()) {
            return Ok(ComponentOrSubtype::SpecificComponent(x));
        }
        Err("none of the variants support the primitive form".into())
    }

    fn extract_key(&self) -> &Self::Key {
        match self {
            ComponentOrSubtype::GlobalComponent(inner) => inner.extract_key(),
            ComponentOrSubtype::CommonComponent(inner) => inner.extract_key(),
            ComponentOrSubtype::SpecificComponent(inner) => inner.extract_key(),
        }
    }
}

#[cfg(feature = "stubgen")]
::pyo3_stub_gen::impl_stub_type!(ComponentOrSubtype = GlobalComponent | CommonComponent | SpecificComponent);

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct GlobalComponent {
    pub component_group: ComponentGroup,
    #[cfg_attr(feature = "serde", serde(default))]
    pub applies_to_instrument: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub applies_to_leg: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub applies_to_underlying: Option<bool>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub conceptually_identical_to: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub gc_id: Option<isize>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub gc_referenced_in: Option<Vec<GlobalComponentBusinessAreaEnum>>,
    pub component_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    pub scope: ComponentScope,
    #[cfg_attr(feature = "serde", serde(default))]
    pub is_repeating_group: Option<bool>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub fields: Option<Vec<Field>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub nested_components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl GlobalComponent {
    #[new]
    #[pyo3(signature = (component_group, component_name, scope, applies_to_instrument=None, applies_to_leg=None, applies_to_underlying=None, conceptually_identical_to=None, gc_id=None, gc_referenced_in=None, description=None, is_repeating_group=None, fields=None, nested_components=None))]
    pub fn new(component_group: ComponentGroup, component_name: String, scope: ComponentScope, applies_to_instrument: Option<bool>, applies_to_leg: Option<bool>, applies_to_underlying: Option<bool>, conceptually_identical_to: Option<Vec<String>>, gc_id: Option<isize>, gc_referenced_in: Option<Vec<GlobalComponentBusinessAreaEnum>>, description: Option<String>, is_repeating_group: Option<bool>, fields: Option<serde_utils::PyValue<Vec<Field>>>, nested_components: Option<Vec<String>>) -> Self {
        let fields = fields.map(|v| v.into_inner());
        GlobalComponent{component_group, component_name, scope, applies_to_instrument, applies_to_leg, applies_to_underlying, conceptually_identical_to, gc_id, gc_referenced_in, description, is_repeating_group, fields, nested_components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<GlobalComponent>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<GlobalComponent> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<GlobalComponent>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid GlobalComponent",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for GlobalComponent {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a GlobalComponent from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct CommonComponent {
    pub business_area: BusinessAreaEnum,
    pub component_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    pub scope: ComponentScope,
    #[cfg_attr(feature = "serde", serde(default))]
    pub is_repeating_group: Option<bool>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub fields: Option<Vec<Field>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub nested_components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl CommonComponent {
    #[new]
    #[pyo3(signature = (business_area, component_name, scope, description=None, is_repeating_group=None, fields=None, nested_components=None))]
    pub fn new(business_area: BusinessAreaEnum, component_name: String, scope: ComponentScope, description: Option<String>, is_repeating_group: Option<bool>, fields: Option<serde_utils::PyValue<Vec<Field>>>, nested_components: Option<Vec<String>>) -> Self {
        let fields = fields.map(|v| v.into_inner());
        CommonComponent{business_area, component_name, scope, description, is_repeating_group, fields, nested_components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<CommonComponent>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<CommonComponent> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<CommonComponent>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid CommonComponent",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for CommonComponent {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a CommonComponent from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct SpecificComponent {
    pub business_area: BusinessAreaEnum,
    pub category: MessageCategoryEnum,
    pub component_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    pub scope: ComponentScope,
    #[cfg_attr(feature = "serde", serde(default))]
    pub is_repeating_group: Option<bool>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub fields: Option<Vec<Field>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub nested_components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl SpecificComponent {
    #[new]
    #[pyo3(signature = (business_area, category, component_name, scope, description=None, is_repeating_group=None, fields=None, nested_components=None))]
    pub fn new(business_area: BusinessAreaEnum, category: MessageCategoryEnum, component_name: String, scope: ComponentScope, description: Option<String>, is_repeating_group: Option<bool>, fields: Option<serde_utils::PyValue<Vec<Field>>>, nested_components: Option<Vec<String>>) -> Self {
        let fields = fields.map(|v| v.into_inner());
        SpecificComponent{business_area, category, component_name, scope, description, is_repeating_group, fields, nested_components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<SpecificComponent>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<SpecificComponent> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<SpecificComponent>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid SpecificComponent",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for SpecificComponent {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a SpecificComponent from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct Message {
    pub msg_type: String,
    pub message_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub category: Option<MessageCategoryEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub fields: Option<Vec<Field>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl Message {
    #[new]
    #[pyo3(signature = (msg_type, message_name, description=None, category=None, fields=None, components=None))]
    pub fn new(msg_type: String, message_name: String, description: Option<String>, category: Option<MessageCategoryEnum>, fields: Option<serde_utils::PyValue<Vec<Field>>>, components: Option<Vec<String>>) -> Self {
        let fields = fields.map(|v| v.into_inner());
        Message{msg_type, message_name, description, category, fields, components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<Message>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<Message> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<Message>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid Message",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for Message {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.msg_type;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("msg_type".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a Message from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("msg_type".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct UDFTagRange {
    pub range_id: String,
    pub low_tag: isize,
    #[cfg_attr(feature = "serde", serde(default))]
    pub high_tag: Option<isize>,
    pub usage: UDFTagRangeUsage,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub requires_registration: Option<bool>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl UDFTagRange {
    #[new]
    #[pyo3(signature = (range_id, low_tag, usage, high_tag=None, description=None, requires_registration=None))]
    pub fn new(range_id: String, low_tag: isize, usage: UDFTagRangeUsage, high_tag: Option<isize>, description: Option<String>, requires_registration: Option<bool>) -> Self {
        UDFTagRange{range_id, low_tag, usage, high_tag, description, requires_registration}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<UDFTagRange>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<UDFTagRange> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<UDFTagRange>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid UDFTagRange",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for UDFTagRange {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.range_id;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("range_id".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a UDFTagRange from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("range_id".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PreTradeBusinessArea {
    pub area: BusinessAreaEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub published_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub publisher: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub introduction: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub diagram_conventions: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages_overview_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Option<Vec<PreTradeMessageEntry>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub components_overview_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub components: Option<Vec<PreTradeComponentEntry>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub common_components: Option<Vec<PreTradeCommonComponentName>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub common_component_details: Option<Vec<CommonComponentDetail>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub footnotes: Option<Vec<ComponentTableFootnote>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub category_sections: Option<Vec<PreTradeCategorySection>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub referenced_global_components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PreTradeBusinessArea {
    #[new]
    #[pyo3(signature = (area, title=None, published_version=None, publisher=None, introduction=None, diagram_conventions=None, messages_overview_note=None, messages=None, components_overview_note=None, components=None, common_components=None, common_component_details=None, footnotes=None, category_sections=None, referenced_global_components=None))]
    pub fn new(area: BusinessAreaEnum, title: Option<String>, published_version: Option<String>, publisher: Option<String>, introduction: Option<String>, diagram_conventions: Option<String>, messages_overview_note: Option<String>, messages: Option<serde_utils::PyValue<Vec<PreTradeMessageEntry>>>, components_overview_note: Option<String>, components: Option<serde_utils::PyValue<Vec<PreTradeComponentEntry>>>, common_components: Option<Vec<PreTradeCommonComponentName>>, common_component_details: Option<serde_utils::PyValue<Vec<CommonComponentDetail>>>, footnotes: Option<serde_utils::PyValue<Vec<ComponentTableFootnote>>>, category_sections: Option<serde_utils::PyValue<Vec<PreTradeCategorySection>>>, referenced_global_components: Option<Vec<String>>) -> Self {
        let messages = messages.map(|v| v.into_inner());
        let components = components.map(|v| v.into_inner());
        let common_component_details = common_component_details.map(|v| v.into_inner());
        let footnotes = footnotes.map(|v| v.into_inner());
        let category_sections = category_sections.map(|v| v.into_inner());
        PreTradeBusinessArea{area, title, published_version, publisher, introduction, diagram_conventions, messages_overview_note, messages, components_overview_note, components, common_components, common_component_details, footnotes, category_sections, referenced_global_components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PreTradeBusinessArea>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PreTradeBusinessArea> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PreTradeBusinessArea>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PreTradeBusinessArea",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PreTradeMessageEntry {
    pub msg_type: String,
    pub message_name: String,
    pub category: PreTradeCategoryEnum
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PreTradeMessageEntry {
    #[new]
    #[pyo3(signature = (msg_type, message_name, category))]
    pub fn new(msg_type: String, message_name: String, category: PreTradeCategoryEnum) -> Self {
        PreTradeMessageEntry{msg_type, message_name, category}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PreTradeMessageEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PreTradeMessageEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PreTradeMessageEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PreTradeMessageEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PreTradeMessageEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.msg_type;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("msg_type".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a PreTradeMessageEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("msg_type".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PreTradeComponentEntry {
    pub component_name: String,
    pub repetition: ComponentRepetition,
    pub category: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub is_common: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub footnote_number: Option<isize>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PreTradeComponentEntry {
    #[new]
    #[pyo3(signature = (component_name, repetition, category, is_common=None, footnote_number=None))]
    pub fn new(component_name: String, repetition: ComponentRepetition, category: String, is_common: Option<bool>, footnote_number: Option<isize>) -> Self {
        PreTradeComponentEntry{component_name, repetition, category, is_common, footnote_number}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PreTradeComponentEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PreTradeComponentEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PreTradeComponentEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PreTradeComponentEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PreTradeComponentEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a PreTradeComponentEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ComponentTableFootnote {
    pub footnote_number: isize,
    pub component_name: String,
    pub introduced_in: String,
    pub sole_category: PreTradeCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub text: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ComponentTableFootnote {
    #[new]
    #[pyo3(signature = (footnote_number, component_name, introduced_in, sole_category, text=None))]
    pub fn new(footnote_number: isize, component_name: String, introduced_in: String, sole_category: PreTradeCategoryEnum, text: Option<String>) -> Self {
        ComponentTableFootnote{footnote_number, component_name, introduced_in, sole_category, text}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ComponentTableFootnote>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ComponentTableFootnote> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ComponentTableFootnote>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ComponentTableFootnote",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for ComponentTableFootnote {
    type Key   = isize;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.footnote_number;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("footnote_number".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a ComponentTableFootnote from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("footnote_number".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PreTradeCategorySection {
    pub category: PreTradeCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub quote_models: Option<Vec<QuoteModelEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub message_groups: Option<Vec<MessageGroup>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Option<Vec<PreTradeMessageDetail>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub category_components_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub category_specific_components: Option<Vec<PreTradeComponentDetail>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PreTradeCategorySection {
    #[new]
    #[pyo3(signature = (category, title=None, description=None, quote_models=None, message_groups=None, messages=None, category_components_note=None, category_specific_components=None))]
    pub fn new(category: PreTradeCategoryEnum, title: Option<String>, description: Option<String>, quote_models: Option<Vec<QuoteModelEnum>>, message_groups: Option<serde_utils::PyValue<Vec<MessageGroup>>>, messages: Option<serde_utils::PyValue<Vec<PreTradeMessageDetail>>>, category_components_note: Option<String>, category_specific_components: Option<serde_utils::PyValue<Vec<PreTradeComponentDetail>>>) -> Self {
        let message_groups = message_groups.map(|v| v.into_inner());
        let messages = messages.map(|v| v.into_inner());
        let category_specific_components = category_specific_components.map(|v| v.into_inner());
        PreTradeCategorySection{category, title, description, quote_models, message_groups, messages, category_components_note, category_specific_components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PreTradeCategorySection>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PreTradeCategorySection> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PreTradeCategorySection>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PreTradeCategorySection",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PreTradeCategorySection {
    type Key   = PreTradeCategoryEnum;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.category;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("category".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("category".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("category".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PreTradeMessageDetail {
    pub msg_type: String,
    pub message_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub pre_layout_rows: Option<Vec<PreTradeLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PreTradeMessageDetail {
    #[new]
    #[pyo3(signature = (msg_type, message_name, description=None, layout_url=None, pre_layout_rows=None))]
    pub fn new(msg_type: String, message_name: String, description: Option<String>, layout_url: Option<uri>, pre_layout_rows: Option<serde_utils::PyValue<Vec<PreTradeLayoutRow>>>) -> Self {
        let pre_layout_rows = pre_layout_rows.map(|v| v.into_inner());
        PreTradeMessageDetail{msg_type, message_name, description, layout_url, pre_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PreTradeMessageDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PreTradeMessageDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PreTradeMessageDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PreTradeMessageDetail",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PreTradeMessageDetail {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.msg_type;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("msg_type".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a PreTradeMessageDetail from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("msg_type".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PreTradeComponentDetail {
    pub component_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub repetition: Option<ComponentRepetition>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub pre_layout_rows: Option<Vec<PreTradeLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PreTradeComponentDetail {
    #[new]
    #[pyo3(signature = (component_name, repetition=None, description=None, layout_url=None, pre_layout_rows=None))]
    pub fn new(component_name: String, repetition: Option<ComponentRepetition>, description: Option<String>, layout_url: Option<uri>, pre_layout_rows: Option<serde_utils::PyValue<Vec<PreTradeLayoutRow>>>) -> Self {
        let pre_layout_rows = pre_layout_rows.map(|v| v.into_inner());
        PreTradeComponentDetail{component_name, repetition, description, layout_url, pre_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PreTradeComponentDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PreTradeComponentDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PreTradeComponentDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PreTradeComponentDetail",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PreTradeComponentDetail {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct MessageGroup {
    pub group_title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list",
        serialize_with = "serde_utils::serialize_inlined_dict_list"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Vec<PreTradeMessageDetail>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl MessageGroup {
    #[new]
    #[pyo3(signature = (group_title, messages, description=None))]
    pub fn new(group_title: String, messages: serde_utils::PyValue<Vec<PreTradeMessageDetail>>, description: Option<String>) -> Self {
        let messages = messages.into_inner();
        MessageGroup{group_title, messages, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<MessageGroup>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<MessageGroup> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<MessageGroup>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid MessageGroup",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for MessageGroup {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.group_title;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("group_title".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("group_title".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("group_title".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct CommonComponentDetail {
    pub component_name: PreTradeCommonComponentName,
    #[cfg_attr(feature = "serde", serde(default))]
    pub repetition: Option<ComponentRepetition>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub pre_layout_rows: Option<Vec<PreTradeLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl CommonComponentDetail {
    #[new]
    #[pyo3(signature = (component_name, repetition=None, description=None, layout_url=None, pre_layout_rows=None))]
    pub fn new(component_name: PreTradeCommonComponentName, repetition: Option<ComponentRepetition>, description: Option<String>, layout_url: Option<uri>, pre_layout_rows: Option<serde_utils::PyValue<Vec<PreTradeLayoutRow>>>) -> Self {
        let pre_layout_rows = pre_layout_rows.map(|v| v.into_inner());
        CommonComponentDetail{component_name, repetition, description, layout_url, pre_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<CommonComponentDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<CommonComponentDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<CommonComponentDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid CommonComponentDetail",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for CommonComponentDetail {
    type Key   = PreTradeCommonComponentName;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PreTradeLayoutRow {
    pub pre_layout_kind: PreTradeLayoutRowKindEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub pre_layout_field_tag: Option<isize>,
    pub pre_layout_element_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub pre_layout_required: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub pre_layout_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub pre_layout_nested: Option<bool>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PreTradeLayoutRow {
    #[new]
    #[pyo3(signature = (pre_layout_kind, pre_layout_element_name, pre_layout_field_tag=None, pre_layout_required=None, pre_layout_description=None, pre_layout_nested=None))]
    pub fn new(pre_layout_kind: PreTradeLayoutRowKindEnum, pre_layout_element_name: String, pre_layout_field_tag: Option<isize>, pre_layout_required: Option<bool>, pre_layout_description: Option<String>, pre_layout_nested: Option<bool>) -> Self {
        PreTradeLayoutRow{pre_layout_kind, pre_layout_element_name, pre_layout_field_tag, pre_layout_required, pre_layout_description, pre_layout_nested}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PreTradeLayoutRow>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PreTradeLayoutRow> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PreTradeLayoutRow>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PreTradeLayoutRow",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeBusinessArea {
    pub trade_area: BusinessAreaEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub published_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub publisher: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_introduction: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_diagram_conventions: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_message_diagram_template_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_messages_overview_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Option<Vec<TradeMessageEntry>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_components_overview_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub components: Option<Vec<TradeComponentEntry>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_common_components: Option<Vec<TradeCommonComponentName>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_common_component_details: Option<Vec<TradeCommonComponentDetail>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_footnotes: Option<Vec<TradeComponentTableFootnote>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_category_sections: Option<Vec<TradeCategorySection>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub referenced_global_components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeBusinessArea {
    #[new]
    #[pyo3(signature = (trade_area, title=None, published_version=None, publisher=None, trade_introduction=None, trade_diagram_conventions=None, trade_message_diagram_template_url=None, trade_messages_overview_note=None, messages=None, trade_components_overview_note=None, components=None, trade_common_components=None, trade_common_component_details=None, trade_footnotes=None, trade_category_sections=None, referenced_global_components=None))]
    pub fn new(trade_area: BusinessAreaEnum, title: Option<String>, published_version: Option<String>, publisher: Option<String>, trade_introduction: Option<String>, trade_diagram_conventions: Option<String>, trade_message_diagram_template_url: Option<uri>, trade_messages_overview_note: Option<String>, messages: Option<serde_utils::PyValue<Vec<TradeMessageEntry>>>, trade_components_overview_note: Option<String>, components: Option<serde_utils::PyValue<Vec<TradeComponentEntry>>>, trade_common_components: Option<Vec<TradeCommonComponentName>>, trade_common_component_details: Option<serde_utils::PyValue<Vec<TradeCommonComponentDetail>>>, trade_footnotes: Option<serde_utils::PyValue<Vec<TradeComponentTableFootnote>>>, trade_category_sections: Option<serde_utils::PyValue<Vec<TradeCategorySection>>>, referenced_global_components: Option<Vec<String>>) -> Self {
        let messages = messages.map(|v| v.into_inner());
        let components = components.map(|v| v.into_inner());
        let trade_common_component_details = trade_common_component_details.map(|v| v.into_inner());
        let trade_footnotes = trade_footnotes.map(|v| v.into_inner());
        let trade_category_sections = trade_category_sections.map(|v| v.into_inner());
        TradeBusinessArea{trade_area, title, published_version, publisher, trade_introduction, trade_diagram_conventions, trade_message_diagram_template_url, trade_messages_overview_note, messages, trade_components_overview_note, components, trade_common_components, trade_common_component_details, trade_footnotes, trade_category_sections, referenced_global_components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeBusinessArea>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeBusinessArea> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeBusinessArea>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeBusinessArea",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeMessageEntry {
    pub msg_type: String,
    pub message_name: String,
    pub category: TradeCategoryEnum
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeMessageEntry {
    #[new]
    #[pyo3(signature = (msg_type, message_name, category))]
    pub fn new(msg_type: String, message_name: String, category: TradeCategoryEnum) -> Self {
        TradeMessageEntry{msg_type, message_name, category}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeMessageEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeMessageEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeMessageEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeMessageEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeMessageEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.msg_type;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("msg_type".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a TradeMessageEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("msg_type".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeComponentEntry {
    pub component_name: String,
    pub trade_repetition: TradeComponentRepetition,
    pub category: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_is_common: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_footnote_number: Option<isize>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeComponentEntry {
    #[new]
    #[pyo3(signature = (component_name, trade_repetition, category, trade_is_common=None, trade_footnote_number=None))]
    pub fn new(component_name: String, trade_repetition: TradeComponentRepetition, category: String, trade_is_common: Option<bool>, trade_footnote_number: Option<isize>) -> Self {
        TradeComponentEntry{component_name, trade_repetition, category, trade_is_common, trade_footnote_number}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeComponentEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeComponentEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeComponentEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeComponentEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeComponentEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a TradeComponentEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeComponentTableFootnote {
    pub trade_footnote_number: isize,
    pub component_name: String,
    pub trade_introduced_in: String,
    pub trade_sole_category: TradeCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_footnote_text: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeComponentTableFootnote {
    #[new]
    #[pyo3(signature = (trade_footnote_number, component_name, trade_introduced_in, trade_sole_category, trade_footnote_text=None))]
    pub fn new(trade_footnote_number: isize, component_name: String, trade_introduced_in: String, trade_sole_category: TradeCategoryEnum, trade_footnote_text: Option<String>) -> Self {
        TradeComponentTableFootnote{trade_footnote_number, component_name, trade_introduced_in, trade_sole_category, trade_footnote_text}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeComponentTableFootnote>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeComponentTableFootnote> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeComponentTableFootnote>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeComponentTableFootnote",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeComponentTableFootnote {
    type Key   = isize;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.trade_footnote_number;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("trade_footnote_number".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a TradeComponentTableFootnote from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("trade_footnote_number".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeCategorySection {
    pub category: TradeCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_category_background: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_message_groups: Option<Vec<TradeMessageGroup>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Option<Vec<TradeMessageDetail>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_category_components_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_category_specific_components: Option<Vec<TradeComponentDetail>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_fragmentation_entries: Option<Vec<TradeFragmentationEntry>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeCategorySection {
    #[new]
    #[pyo3(signature = (category, title=None, description=None, trade_category_background=None, trade_message_groups=None, messages=None, trade_category_components_note=None, trade_category_specific_components=None, trade_fragmentation_entries=None))]
    pub fn new(category: TradeCategoryEnum, title: Option<String>, description: Option<String>, trade_category_background: Option<String>, trade_message_groups: Option<serde_utils::PyValue<Vec<TradeMessageGroup>>>, messages: Option<serde_utils::PyValue<Vec<TradeMessageDetail>>>, trade_category_components_note: Option<String>, trade_category_specific_components: Option<serde_utils::PyValue<Vec<TradeComponentDetail>>>, trade_fragmentation_entries: Option<serde_utils::PyValue<Vec<TradeFragmentationEntry>>>) -> Self {
        let trade_message_groups = trade_message_groups.map(|v| v.into_inner());
        let messages = messages.map(|v| v.into_inner());
        let trade_category_specific_components = trade_category_specific_components.map(|v| v.into_inner());
        let trade_fragmentation_entries = trade_fragmentation_entries.map(|v| v.into_inner());
        TradeCategorySection{category, title, description, trade_category_background, trade_message_groups, messages, trade_category_components_note, trade_category_specific_components, trade_fragmentation_entries}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeCategorySection>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeCategorySection> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeCategorySection>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeCategorySection",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeCategorySection {
    type Key   = TradeCategoryEnum;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.category;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("category".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("category".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("category".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeMessageDetail {
    pub msg_type: String,
    pub message_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_rows: Option<Vec<TradeLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeMessageDetail {
    #[new]
    #[pyo3(signature = (msg_type, message_name, description=None, trade_layout_url=None, trade_layout_rows=None))]
    pub fn new(msg_type: String, message_name: String, description: Option<String>, trade_layout_url: Option<uri>, trade_layout_rows: Option<serde_utils::PyValue<Vec<TradeLayoutRow>>>) -> Self {
        let trade_layout_rows = trade_layout_rows.map(|v| v.into_inner());
        TradeMessageDetail{msg_type, message_name, description, trade_layout_url, trade_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeMessageDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeMessageDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeMessageDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeMessageDetail",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeMessageDetail {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.msg_type;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("msg_type".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a TradeMessageDetail from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("msg_type".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeComponentDetail {
    pub component_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_repetition: Option<TradeComponentRepetition>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_rows: Option<Vec<TradeLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeComponentDetail {
    #[new]
    #[pyo3(signature = (component_name, trade_repetition=None, description=None, trade_layout_url=None, trade_layout_rows=None))]
    pub fn new(component_name: String, trade_repetition: Option<TradeComponentRepetition>, description: Option<String>, trade_layout_url: Option<uri>, trade_layout_rows: Option<serde_utils::PyValue<Vec<TradeLayoutRow>>>) -> Self {
        let trade_layout_rows = trade_layout_rows.map(|v| v.into_inner());
        TradeComponentDetail{component_name, trade_repetition, description, trade_layout_url, trade_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeComponentDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeComponentDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeComponentDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeComponentDetail",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeComponentDetail {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeMessageGroup {
    pub trade_group_title: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list",
        serialize_with = "serde_utils::serialize_inlined_dict_list"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Vec<TradeMessageDetail>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_ord_status_precedence_entries: Option<Vec<TradeOrdStatusPrecedenceEntry>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeMessageGroup {
    #[new]
    #[pyo3(signature = (trade_group_title, messages, description=None, trade_ord_status_precedence_entries=None))]
    pub fn new(trade_group_title: String, messages: serde_utils::PyValue<Vec<TradeMessageDetail>>, description: Option<String>, trade_ord_status_precedence_entries: Option<serde_utils::PyValue<Vec<TradeOrdStatusPrecedenceEntry>>>) -> Self {
        let messages = messages.into_inner();
        let trade_ord_status_precedence_entries = trade_ord_status_precedence_entries.map(|v| v.into_inner());
        TradeMessageGroup{trade_group_title, messages, description, trade_ord_status_precedence_entries}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeMessageGroup>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeMessageGroup> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeMessageGroup>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeMessageGroup",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeMessageGroup {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.trade_group_title;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("trade_group_title".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("trade_group_title".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("trade_group_title".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeCommonComponentDetail {
    pub component_name: TradeCommonComponentName,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_repetition: Option<TradeComponentRepetition>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_rows: Option<Vec<TradeLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeCommonComponentDetail {
    #[new]
    #[pyo3(signature = (component_name, trade_repetition=None, description=None, trade_layout_url=None, trade_layout_rows=None))]
    pub fn new(component_name: TradeCommonComponentName, trade_repetition: Option<TradeComponentRepetition>, description: Option<String>, trade_layout_url: Option<uri>, trade_layout_rows: Option<serde_utils::PyValue<Vec<TradeLayoutRow>>>) -> Self {
        let trade_layout_rows = trade_layout_rows.map(|v| v.into_inner());
        TradeCommonComponentDetail{component_name, trade_repetition, description, trade_layout_url, trade_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeCommonComponentDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeCommonComponentDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeCommonComponentDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeCommonComponentDetail",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeCommonComponentDetail {
    type Key   = TradeCommonComponentName;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeLayoutRow {
    pub trade_layout_kind: TradeLayoutRowKindEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_field_tag: Option<isize>,
    pub trade_layout_element_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_required: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_layout_nested: Option<bool>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeLayoutRow {
    #[new]
    #[pyo3(signature = (trade_layout_kind, trade_layout_element_name, trade_layout_field_tag=None, trade_layout_required=None, trade_layout_description=None, trade_layout_nested=None))]
    pub fn new(trade_layout_kind: TradeLayoutRowKindEnum, trade_layout_element_name: String, trade_layout_field_tag: Option<isize>, trade_layout_required: Option<bool>, trade_layout_description: Option<String>, trade_layout_nested: Option<bool>) -> Self {
        TradeLayoutRow{trade_layout_kind, trade_layout_element_name, trade_layout_field_tag, trade_layout_required, trade_layout_description, trade_layout_nested}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeLayoutRow>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeLayoutRow> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeLayoutRow>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeLayoutRow",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeOrdStatusPrecedenceEntry {
    pub trade_ord_status_precedence: isize,
    pub trade_ord_status_label: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeOrdStatusPrecedenceEntry {
    #[new]
    #[pyo3(signature = (trade_ord_status_precedence, trade_ord_status_label, description=None))]
    pub fn new(trade_ord_status_precedence: isize, trade_ord_status_label: String, description: Option<String>) -> Self {
        TradeOrdStatusPrecedenceEntry{trade_ord_status_precedence, trade_ord_status_label, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeOrdStatusPrecedenceEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeOrdStatusPrecedenceEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeOrdStatusPrecedenceEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeOrdStatusPrecedenceEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeOrdStatusPrecedenceEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.trade_ord_status_label;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("trade_ord_status_label".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a TradeOrdStatusPrecedenceEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("trade_ord_status_label".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeFragmentationEntry {
    pub trade_fragmentation_message: String,
    pub trade_fragmentation_total_entries_field: String,
    pub trade_fragmentation_repeating_group: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeFragmentationEntry {
    #[new]
    #[pyo3(signature = (trade_fragmentation_message, trade_fragmentation_total_entries_field, trade_fragmentation_repeating_group))]
    pub fn new(trade_fragmentation_message: String, trade_fragmentation_total_entries_field: String, trade_fragmentation_repeating_group: String) -> Self {
        TradeFragmentationEntry{trade_fragmentation_message, trade_fragmentation_total_entries_field, trade_fragmentation_repeating_group}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeFragmentationEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeFragmentationEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeFragmentationEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeFragmentationEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeFragmentationEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.trade_fragmentation_message;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("trade_fragmentation_message".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a TradeFragmentationEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("trade_fragmentation_message".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeAppendix {
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub published_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub publisher: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_appendix_sections: Option<Vec<TradeAppendixSection>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeAppendix {
    #[new]
    #[pyo3(signature = (title=None, published_version=None, publisher=None, description=None, trade_appendix_sections=None))]
    pub fn new(title: Option<String>, published_version: Option<String>, publisher: Option<String>, description: Option<String>, trade_appendix_sections: Option<serde_utils::PyValue<Vec<TradeAppendixSection>>>) -> Self {
        let trade_appendix_sections = trade_appendix_sections.map(|v| v.into_inner());
        TradeAppendix{title, published_version, publisher, description, trade_appendix_sections}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeAppendix>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeAppendix> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeAppendix>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeAppendix",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeAppendixSection {
    pub trade_appendix_category: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Option<Vec<TradeMessageDetail>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeAppendixSection {
    #[new]
    #[pyo3(signature = (trade_appendix_category, title=None, description=None, messages=None, components=None))]
    pub fn new(trade_appendix_category: String, title: Option<String>, description: Option<String>, messages: Option<serde_utils::PyValue<Vec<TradeMessageDetail>>>, components: Option<Vec<String>>) -> Self {
        let messages = messages.map(|v| v.into_inner());
        TradeAppendixSection{trade_appendix_category, title, description, messages, components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeAppendixSection>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeAppendixSection> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeAppendixSection>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeAppendixSection",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeAppendixSection {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.trade_appendix_category;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("trade_appendix_category".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("trade_appendix_category".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("trade_appendix_category".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeBusinessArea {
    pub area: BusinessAreaEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub published_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub publisher: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_introduction: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub diagram_conventions: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_common_components: Option<Vec<PostTradeCommonComponentName>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list",
        serialize_with = "serde_utils::serialize_inlined_dict_list"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Vec<PostTradeMessageEntry>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list",
        serialize_with = "serde_utils::serialize_inlined_dict_list"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub components: Vec<PostTradeComponentEntry>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_footnotes: Option<Vec<PostTradeComponentTableFootnote>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_category_sections: Option<Vec<PostTradeCategorySection>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_common_component_details: Option<Vec<PostTradeCommonComponentDetail>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages_overview_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub components_overview_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub referenced_global_components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeBusinessArea {
    #[new]
    #[pyo3(signature = (area, messages, components, title=None, published_version=None, publisher=None, post_introduction=None, diagram_conventions=None, post_common_components=None, post_footnotes=None, post_category_sections=None, post_common_component_details=None, messages_overview_note=None, components_overview_note=None, referenced_global_components=None))]
    pub fn new(area: BusinessAreaEnum, messages: serde_utils::PyValue<Vec<PostTradeMessageEntry>>, components: serde_utils::PyValue<Vec<PostTradeComponentEntry>>, title: Option<String>, published_version: Option<String>, publisher: Option<String>, post_introduction: Option<String>, diagram_conventions: Option<String>, post_common_components: Option<Vec<PostTradeCommonComponentName>>, post_footnotes: Option<serde_utils::PyValue<Vec<PostTradeComponentTableFootnote>>>, post_category_sections: Option<serde_utils::PyValue<Vec<PostTradeCategorySection>>>, post_common_component_details: Option<serde_utils::PyValue<Vec<PostTradeCommonComponentDetail>>>, messages_overview_note: Option<String>, components_overview_note: Option<String>, referenced_global_components: Option<Vec<String>>) -> Self {
        let messages = messages.into_inner();
        let components = components.into_inner();
        let post_footnotes = post_footnotes.map(|v| v.into_inner());
        let post_category_sections = post_category_sections.map(|v| v.into_inner());
        let post_common_component_details = post_common_component_details.map(|v| v.into_inner());
        PostTradeBusinessArea{area, messages, components, title, published_version, publisher, post_introduction, diagram_conventions, post_common_components, post_footnotes, post_category_sections, post_common_component_details, messages_overview_note, components_overview_note, referenced_global_components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeBusinessArea>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeBusinessArea> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeBusinessArea>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeBusinessArea",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeMessageEntry {
    pub msg_type: String,
    pub message_name: String,
    pub category: PostTradeCategoryEnum
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeMessageEntry {
    #[new]
    #[pyo3(signature = (msg_type, message_name, category))]
    pub fn new(msg_type: String, message_name: String, category: PostTradeCategoryEnum) -> Self {
        PostTradeMessageEntry{msg_type, message_name, category}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeMessageEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeMessageEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeMessageEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeMessageEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PostTradeMessageEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.msg_type;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("msg_type".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a PostTradeMessageEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("msg_type".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeComponentEntry {
    pub component_name: String,
    pub repetition: ComponentRepetition,
    pub category: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub is_common: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub footnote_number: Option<isize>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeComponentEntry {
    #[new]
    #[pyo3(signature = (component_name, repetition, category, is_common=None, footnote_number=None))]
    pub fn new(component_name: String, repetition: ComponentRepetition, category: String, is_common: Option<bool>, footnote_number: Option<isize>) -> Self {
        PostTradeComponentEntry{component_name, repetition, category, is_common, footnote_number}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeComponentEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeComponentEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeComponentEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeComponentEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PostTradeComponentEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a PostTradeComponentEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeComponentTableFootnote {
    pub footnote_number: isize,
    pub component_name: String,
    pub introduced_in: String,
    pub post_sole_category: PostTradeCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub text: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeComponentTableFootnote {
    #[new]
    #[pyo3(signature = (footnote_number, component_name, introduced_in, post_sole_category, text=None))]
    pub fn new(footnote_number: isize, component_name: String, introduced_in: String, post_sole_category: PostTradeCategoryEnum, text: Option<String>) -> Self {
        PostTradeComponentTableFootnote{footnote_number, component_name, introduced_in, post_sole_category, text}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeComponentTableFootnote>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeComponentTableFootnote> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeComponentTableFootnote>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeComponentTableFootnote",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PostTradeComponentTableFootnote {
    type Key   = isize;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.footnote_number;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("footnote_number".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a PostTradeComponentTableFootnote from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("footnote_number".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeCategorySection {
    pub category: PostTradeCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub category_components_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_message_groups: Option<Vec<PostTradeMessageGroup>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Option<Vec<PostTradeMessageDetail>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_category_specific_components: Option<Vec<PostTradeComponentDetail>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub allocation_scenarios: Option<Vec<AllocationScenarioEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub allocation_roles: Option<Vec<AllocationRoleEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_trade_allocation_pricing_methods: Option<Vec<PostTradeAllocationPricingMethodEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub allocation_status_descriptions: Option<Vec<AllocationStatusDescription>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub fragmentation_field_map: Option<Vec<AllocationFragmentationFieldMap>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_capture_report_usages: Option<Vec<TradeCaptureReportUsage>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub trade_capture_report_identifier_rules: Option<Vec<TradeCaptureReportIdentifierRule>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub registration_status_descriptions: Option<Vec<RegistrationStatusDescription>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub clearing_services_for_position_management: Option<Vec<ClearingServiceForPositionManagementEnum>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub clearing_services_for_post_trade_processing: Option<Vec<ClearingServicePostTradeProcessingFormat>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub collateral_management_usages: Option<Vec<CollateralManagementUsageEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub collateral_assignment_purposes: Option<Vec<CollateralAssignmentPurposeEnum>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeCategorySection {
    #[new]
    #[pyo3(signature = (category, title=None, description=None, category_components_note=None, post_message_groups=None, messages=None, post_category_specific_components=None, allocation_scenarios=None, allocation_roles=None, post_trade_allocation_pricing_methods=None, allocation_status_descriptions=None, fragmentation_field_map=None, trade_capture_report_usages=None, trade_capture_report_identifier_rules=None, registration_status_descriptions=None, clearing_services_for_position_management=None, clearing_services_for_post_trade_processing=None, collateral_management_usages=None, collateral_assignment_purposes=None))]
    pub fn new(category: PostTradeCategoryEnum, title: Option<String>, description: Option<String>, category_components_note: Option<String>, post_message_groups: Option<serde_utils::PyValue<Vec<PostTradeMessageGroup>>>, messages: Option<serde_utils::PyValue<Vec<PostTradeMessageDetail>>>, post_category_specific_components: Option<serde_utils::PyValue<Vec<PostTradeComponentDetail>>>, allocation_scenarios: Option<Vec<AllocationScenarioEnum>>, allocation_roles: Option<Vec<AllocationRoleEnum>>, post_trade_allocation_pricing_methods: Option<Vec<PostTradeAllocationPricingMethodEnum>>, allocation_status_descriptions: Option<serde_utils::PyValue<Vec<AllocationStatusDescription>>>, fragmentation_field_map: Option<serde_utils::PyValue<Vec<AllocationFragmentationFieldMap>>>, trade_capture_report_usages: Option<serde_utils::PyValue<Vec<TradeCaptureReportUsage>>>, trade_capture_report_identifier_rules: Option<serde_utils::PyValue<Vec<TradeCaptureReportIdentifierRule>>>, registration_status_descriptions: Option<serde_utils::PyValue<Vec<RegistrationStatusDescription>>>, clearing_services_for_position_management: Option<Vec<ClearingServiceForPositionManagementEnum>>, clearing_services_for_post_trade_processing: Option<serde_utils::PyValue<Vec<ClearingServicePostTradeProcessingFormat>>>, collateral_management_usages: Option<Vec<CollateralManagementUsageEnum>>, collateral_assignment_purposes: Option<Vec<CollateralAssignmentPurposeEnum>>) -> Self {
        let post_message_groups = post_message_groups.map(|v| v.into_inner());
        let messages = messages.map(|v| v.into_inner());
        let post_category_specific_components = post_category_specific_components.map(|v| v.into_inner());
        let allocation_status_descriptions = allocation_status_descriptions.map(|v| v.into_inner());
        let fragmentation_field_map = fragmentation_field_map.map(|v| v.into_inner());
        let trade_capture_report_usages = trade_capture_report_usages.map(|v| v.into_inner());
        let trade_capture_report_identifier_rules = trade_capture_report_identifier_rules.map(|v| v.into_inner());
        let registration_status_descriptions = registration_status_descriptions.map(|v| v.into_inner());
        let clearing_services_for_post_trade_processing = clearing_services_for_post_trade_processing.map(|v| v.into_inner());
        PostTradeCategorySection{category, title, description, category_components_note, post_message_groups, messages, post_category_specific_components, allocation_scenarios, allocation_roles, post_trade_allocation_pricing_methods, allocation_status_descriptions, fragmentation_field_map, trade_capture_report_usages, trade_capture_report_identifier_rules, registration_status_descriptions, clearing_services_for_position_management, clearing_services_for_post_trade_processing, collateral_management_usages, collateral_assignment_purposes}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeCategorySection>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeCategorySection> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeCategorySection>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeCategorySection",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PostTradeCategorySection {
    type Key   = PostTradeCategoryEnum;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.category;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("category".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("category".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("category".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeMessageGroup {
    pub group_title: String,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list",
        serialize_with = "serde_utils::serialize_inlined_dict_list"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Vec<PostTradeMessageDetail>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeMessageGroup {
    #[new]
    #[pyo3(signature = (group_title, messages))]
    pub fn new(group_title: String, messages: serde_utils::PyValue<Vec<PostTradeMessageDetail>>) -> Self {
        let messages = messages.into_inner();
        PostTradeMessageGroup{group_title, messages}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeMessageGroup>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeMessageGroup> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeMessageGroup>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeMessageGroup",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeMessageDetail {
    pub msg_type: String,
    pub message_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_layout_rows: Option<Vec<PostTradeLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeMessageDetail {
    #[new]
    #[pyo3(signature = (msg_type, message_name, description=None, layout_url=None, post_layout_rows=None))]
    pub fn new(msg_type: String, message_name: String, description: Option<String>, layout_url: Option<uri>, post_layout_rows: Option<serde_utils::PyValue<Vec<PostTradeLayoutRow>>>) -> Self {
        let post_layout_rows = post_layout_rows.map(|v| v.into_inner());
        PostTradeMessageDetail{msg_type, message_name, description, layout_url, post_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeMessageDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeMessageDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeMessageDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeMessageDetail",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PostTradeMessageDetail {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.msg_type;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("msg_type".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a PostTradeMessageDetail from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("msg_type".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeComponentDetail {
    pub component_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub repetition: Option<ComponentRepetition>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_layout_rows: Option<Vec<PostTradeLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeComponentDetail {
    #[new]
    #[pyo3(signature = (component_name, repetition=None, description=None, layout_url=None, post_layout_rows=None))]
    pub fn new(component_name: String, repetition: Option<ComponentRepetition>, description: Option<String>, layout_url: Option<uri>, post_layout_rows: Option<serde_utils::PyValue<Vec<PostTradeLayoutRow>>>) -> Self {
        let post_layout_rows = post_layout_rows.map(|v| v.into_inner());
        PostTradeComponentDetail{component_name, repetition, description, layout_url, post_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeComponentDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeComponentDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeComponentDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeComponentDetail",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PostTradeComponentDetail {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeCommonComponentDetail {
    pub component_name: PostTradeCommonComponentName,
    #[cfg_attr(feature = "serde", serde(default))]
    pub repetition: Option<ComponentRepetition>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_layout_rows: Option<Vec<PostTradeLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeCommonComponentDetail {
    #[new]
    #[pyo3(signature = (component_name, repetition=None, description=None, layout_url=None, post_layout_rows=None))]
    pub fn new(component_name: PostTradeCommonComponentName, repetition: Option<ComponentRepetition>, description: Option<String>, layout_url: Option<uri>, post_layout_rows: Option<serde_utils::PyValue<Vec<PostTradeLayoutRow>>>) -> Self {
        let post_layout_rows = post_layout_rows.map(|v| v.into_inner());
        PostTradeCommonComponentDetail{component_name, repetition, description, layout_url, post_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeCommonComponentDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeCommonComponentDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeCommonComponentDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeCommonComponentDetail",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for PostTradeCommonComponentDetail {
    type Key   = PostTradeCommonComponentName;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct AllocationStatusDescription {
    pub status_code: String,
    pub status_label: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl AllocationStatusDescription {
    #[new]
    #[pyo3(signature = (status_code, status_label, description=None))]
    pub fn new(status_code: String, status_label: String, description: Option<String>) -> Self {
        AllocationStatusDescription{status_code, status_label, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<AllocationStatusDescription>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<AllocationStatusDescription> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<AllocationStatusDescription>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid AllocationStatusDescription",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for AllocationStatusDescription {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.status_code;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("status_code".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a AllocationStatusDescription from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("status_code".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct AllocationFragmentationFieldMap {
    pub msg_type: String,
    pub message_name: String,
    pub total_count_field: String,
    pub fragment_count_field: String,
    pub principal_message_reference: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl AllocationFragmentationFieldMap {
    #[new]
    #[pyo3(signature = (msg_type, message_name, total_count_field, fragment_count_field, principal_message_reference))]
    pub fn new(msg_type: String, message_name: String, total_count_field: String, fragment_count_field: String, principal_message_reference: String) -> Self {
        AllocationFragmentationFieldMap{msg_type, message_name, total_count_field, fragment_count_field, principal_message_reference}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<AllocationFragmentationFieldMap>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<AllocationFragmentationFieldMap> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<AllocationFragmentationFieldMap>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid AllocationFragmentationFieldMap",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for AllocationFragmentationFieldMap {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.msg_type;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("msg_type".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a AllocationFragmentationFieldMap from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("msg_type".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeCaptureReportUsage {
    pub status_label: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub identifier_role: Option<TradeCaptureReportIdentifierRoleEnum>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeCaptureReportUsage {
    #[new]
    #[pyo3(signature = (status_label, description=None, identifier_role=None))]
    pub fn new(status_label: String, description: Option<String>, identifier_role: Option<TradeCaptureReportIdentifierRoleEnum>) -> Self {
        TradeCaptureReportUsage{status_label, description, identifier_role}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeCaptureReportUsage>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeCaptureReportUsage> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeCaptureReportUsage>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeCaptureReportUsage",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeCaptureReportUsage {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.status_label;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("status_label".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("status_label".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("status_label".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct TradeCaptureReportIdentifierRule {
    pub identifier_role: TradeCaptureReportIdentifierRoleEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl TradeCaptureReportIdentifierRule {
    #[new]
    #[pyo3(signature = (identifier_role, description=None))]
    pub fn new(identifier_role: TradeCaptureReportIdentifierRoleEnum, description: Option<String>) -> Self {
        TradeCaptureReportIdentifierRule{identifier_role, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<TradeCaptureReportIdentifierRule>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<TradeCaptureReportIdentifierRule> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<TradeCaptureReportIdentifierRule>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid TradeCaptureReportIdentifierRule",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for TradeCaptureReportIdentifierRule {
    type Key   = TradeCaptureReportIdentifierRoleEnum;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.identifier_role;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("identifier_role".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("identifier_role".into()), key_value);
        map.insert(Value::String("description".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        self.description.as_ref()
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("identifier_role".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct RegistrationStatusDescription {
    pub status_code: String,
    pub status_label: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl RegistrationStatusDescription {
    #[new]
    #[pyo3(signature = (status_code, status_label, description=None))]
    pub fn new(status_code: String, status_label: String, description: Option<String>) -> Self {
        RegistrationStatusDescription{status_code, status_label, description}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<RegistrationStatusDescription>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<RegistrationStatusDescription> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<RegistrationStatusDescription>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid RegistrationStatusDescription",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for RegistrationStatusDescription {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.status_code;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("status_code".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a RegistrationStatusDescription from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("status_code".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ClearingServicePostTradeProcessingFormat {
    pub message_format: ClearingServiceForPostTradeProcessingEnum,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub supported_actions: Vec<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ClearingServicePostTradeProcessingFormat {
    #[new]
    #[pyo3(signature = (message_format, supported_actions))]
    pub fn new(message_format: ClearingServiceForPostTradeProcessingEnum, supported_actions: Vec<String>) -> Self {
        ClearingServicePostTradeProcessingFormat{message_format, supported_actions}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ClearingServicePostTradeProcessingFormat>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ClearingServicePostTradeProcessingFormat> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ClearingServicePostTradeProcessingFormat>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ClearingServicePostTradeProcessingFormat",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct PostTradeLayoutRow {
    pub post_layout_kind: PostTradeLayoutRowKindEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_layout_field_tag: Option<isize>,
    pub post_layout_element_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_layout_required: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_layout_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub post_layout_nested: Option<bool>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl PostTradeLayoutRow {
    #[new]
    #[pyo3(signature = (post_layout_kind, post_layout_element_name, post_layout_field_tag=None, post_layout_required=None, post_layout_description=None, post_layout_nested=None))]
    pub fn new(post_layout_kind: PostTradeLayoutRowKindEnum, post_layout_element_name: String, post_layout_field_tag: Option<isize>, post_layout_required: Option<bool>, post_layout_description: Option<String>, post_layout_nested: Option<bool>) -> Self {
        PostTradeLayoutRow{post_layout_kind, post_layout_element_name, post_layout_field_tag, post_layout_required, post_layout_description, post_layout_nested}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<PostTradeLayoutRow>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<PostTradeLayoutRow> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<PostTradeLayoutRow>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid PostTradeLayoutRow",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InfrastructureBusinessArea {
    pub area: BusinessAreaEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub published_version: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub publisher: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_introduction: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub diagram_conventions: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_common_components: Option<Vec<InfrastructureComponentName>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list",
        serialize_with = "serde_utils::serialize_inlined_dict_list"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Vec<InfrastructureMessageEntry>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages_overview_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list",
        serialize_with = "serde_utils::serialize_inlined_dict_list"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub components: Vec<InfrastructureComponentEntry>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub components_overview_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_footnotes: Option<Vec<InfrastructureComponentTableFootnote>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_category_sections: Option<Vec<InfrastructureCategorySection>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub standard_responses_pre_trade: Option<Vec<StandardResponseMapping>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub standard_responses_trade: Option<Vec<StandardResponseMapping>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub standard_responses_post_trade: Option<Vec<StandardResponseMapping>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub key_fields_pre_trade: Option<Vec<ApplicationMessageReferenceKey>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub key_fields_trade: Option<Vec<ApplicationMessageReferenceKey>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub key_fields_post_trade: Option<Vec<ApplicationMessageReferenceKey>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub business_reject_reason_descriptions: Option<Vec<BusinessRejectReasonDescription>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_inlined_dict_list_optional",
        serialize_with = "serde_utils::serialize_inlined_dict_list_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_global_components: Option<Vec<InfrastructureGlobalComponentReference>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub referenced_global_components: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InfrastructureBusinessArea {
    #[new]
    #[pyo3(signature = (area, messages, components, title=None, published_version=None, publisher=None, infra_introduction=None, diagram_conventions=None, infra_common_components=None, messages_overview_note=None, components_overview_note=None, infra_footnotes=None, infra_category_sections=None, standard_responses_pre_trade=None, standard_responses_trade=None, standard_responses_post_trade=None, key_fields_pre_trade=None, key_fields_trade=None, key_fields_post_trade=None, business_reject_reason_descriptions=None, infra_global_components=None, referenced_global_components=None))]
    pub fn new(area: BusinessAreaEnum, messages: serde_utils::PyValue<Vec<InfrastructureMessageEntry>>, components: serde_utils::PyValue<Vec<InfrastructureComponentEntry>>, title: Option<String>, published_version: Option<String>, publisher: Option<String>, infra_introduction: Option<String>, diagram_conventions: Option<String>, infra_common_components: Option<Vec<InfrastructureComponentName>>, messages_overview_note: Option<String>, components_overview_note: Option<String>, infra_footnotes: Option<serde_utils::PyValue<Vec<InfrastructureComponentTableFootnote>>>, infra_category_sections: Option<serde_utils::PyValue<Vec<InfrastructureCategorySection>>>, standard_responses_pre_trade: Option<serde_utils::PyValue<Vec<StandardResponseMapping>>>, standard_responses_trade: Option<serde_utils::PyValue<Vec<StandardResponseMapping>>>, standard_responses_post_trade: Option<serde_utils::PyValue<Vec<StandardResponseMapping>>>, key_fields_pre_trade: Option<serde_utils::PyValue<Vec<ApplicationMessageReferenceKey>>>, key_fields_trade: Option<serde_utils::PyValue<Vec<ApplicationMessageReferenceKey>>>, key_fields_post_trade: Option<serde_utils::PyValue<Vec<ApplicationMessageReferenceKey>>>, business_reject_reason_descriptions: Option<serde_utils::PyValue<Vec<BusinessRejectReasonDescription>>>, infra_global_components: Option<serde_utils::PyValue<Vec<InfrastructureGlobalComponentReference>>>, referenced_global_components: Option<Vec<String>>) -> Self {
        let messages = messages.into_inner();
        let components = components.into_inner();
        let infra_footnotes = infra_footnotes.map(|v| v.into_inner());
        let infra_category_sections = infra_category_sections.map(|v| v.into_inner());
        let standard_responses_pre_trade = standard_responses_pre_trade.map(|v| v.into_inner());
        let standard_responses_trade = standard_responses_trade.map(|v| v.into_inner());
        let standard_responses_post_trade = standard_responses_post_trade.map(|v| v.into_inner());
        let key_fields_pre_trade = key_fields_pre_trade.map(|v| v.into_inner());
        let key_fields_trade = key_fields_trade.map(|v| v.into_inner());
        let key_fields_post_trade = key_fields_post_trade.map(|v| v.into_inner());
        let business_reject_reason_descriptions = business_reject_reason_descriptions.map(|v| v.into_inner());
        let infra_global_components = infra_global_components.map(|v| v.into_inner());
        InfrastructureBusinessArea{area, messages, components, title, published_version, publisher, infra_introduction, diagram_conventions, infra_common_components, messages_overview_note, components_overview_note, infra_footnotes, infra_category_sections, standard_responses_pre_trade, standard_responses_trade, standard_responses_post_trade, key_fields_pre_trade, key_fields_trade, key_fields_post_trade, business_reject_reason_descriptions, infra_global_components, referenced_global_components}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InfrastructureBusinessArea>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InfrastructureBusinessArea> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InfrastructureBusinessArea>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InfrastructureBusinessArea",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InfrastructureMessageEntry {
    pub msg_type: String,
    pub message_name: String,
    pub category: InfrastructureCategoryEnum
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InfrastructureMessageEntry {
    #[new]
    #[pyo3(signature = (msg_type, message_name, category))]
    pub fn new(msg_type: String, message_name: String, category: InfrastructureCategoryEnum) -> Self {
        InfrastructureMessageEntry{msg_type, message_name, category}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InfrastructureMessageEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InfrastructureMessageEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InfrastructureMessageEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InfrastructureMessageEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InfrastructureMessageEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.msg_type;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("msg_type".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InfrastructureMessageEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("msg_type".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InfrastructureComponentEntry {
    pub component_name: String,
    pub repetition: ComponentRepetition,
    pub category: InfrastructureCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub footnote_number: Option<isize>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InfrastructureComponentEntry {
    #[new]
    #[pyo3(signature = (component_name, repetition, category, footnote_number=None))]
    pub fn new(component_name: String, repetition: ComponentRepetition, category: InfrastructureCategoryEnum, footnote_number: Option<isize>) -> Self {
        InfrastructureComponentEntry{component_name, repetition, category, footnote_number}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InfrastructureComponentEntry>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InfrastructureComponentEntry> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InfrastructureComponentEntry>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InfrastructureComponentEntry",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InfrastructureComponentEntry {
    type Key   = String;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InfrastructureComponentEntry from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InfrastructureComponentTableFootnote {
    pub footnote_number: isize,
    pub component_name: String,
    pub introduced_in: String,
    pub infra_sole_category: InfrastructureCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub text: Option<String>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InfrastructureComponentTableFootnote {
    #[new]
    #[pyo3(signature = (footnote_number, component_name, introduced_in, infra_sole_category, text=None))]
    pub fn new(footnote_number: isize, component_name: String, introduced_in: String, infra_sole_category: InfrastructureCategoryEnum, text: Option<String>) -> Self {
        InfrastructureComponentTableFootnote{footnote_number, component_name, introduced_in, infra_sole_category, text}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InfrastructureComponentTableFootnote>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InfrastructureComponentTableFootnote> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InfrastructureComponentTableFootnote>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InfrastructureComponentTableFootnote",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InfrastructureComponentTableFootnote {
    type Key   = isize;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.footnote_number;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("footnote_number".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(_k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        Err("Cannot create a InfrastructureComponentTableFootnote from a primitive value!".into())
    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("footnote_number".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InfrastructureCategorySection {
    pub category: InfrastructureCategoryEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub title: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub category_components_note: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub messages: Option<Vec<InfrastructureMessageDetail>>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_category_specific_components: Option<Vec<InfrastructureComponentDetail>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub network_status_scenarios: Option<Vec<NetworkStatusScenarioEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub network_request_types_referenced: Option<Vec<NetworkRequestTypeEnum>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub application_message_report_uses: Option<Vec<ApplicationMessageReportTypeEnum>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InfrastructureCategorySection {
    #[new]
    #[pyo3(signature = (category, title=None, description=None, category_components_note=None, messages=None, infra_category_specific_components=None, network_status_scenarios=None, network_request_types_referenced=None, application_message_report_uses=None))]
    pub fn new(category: InfrastructureCategoryEnum, title: Option<String>, description: Option<String>, category_components_note: Option<String>, messages: Option<serde_utils::PyValue<Vec<InfrastructureMessageDetail>>>, infra_category_specific_components: Option<serde_utils::PyValue<Vec<InfrastructureComponentDetail>>>, network_status_scenarios: Option<Vec<NetworkStatusScenarioEnum>>, network_request_types_referenced: Option<Vec<NetworkRequestTypeEnum>>, application_message_report_uses: Option<Vec<ApplicationMessageReportTypeEnum>>) -> Self {
        let messages = messages.map(|v| v.into_inner());
        let infra_category_specific_components = infra_category_specific_components.map(|v| v.into_inner());
        InfrastructureCategorySection{category, title, description, category_components_note, messages, infra_category_specific_components, network_status_scenarios, network_request_types_referenced, application_message_report_uses}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InfrastructureCategorySection>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InfrastructureCategorySection> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InfrastructureCategorySection>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InfrastructureCategorySection",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InfrastructureMessageDetail {
    pub msg_type: String,
    pub message_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_layout_rows: Option<Vec<InfrastructureLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InfrastructureMessageDetail {
    #[new]
    #[pyo3(signature = (msg_type, message_name, description=None, layout_url=None, infra_layout_rows=None))]
    pub fn new(msg_type: String, message_name: String, description: Option<String>, layout_url: Option<uri>, infra_layout_rows: Option<serde_utils::PyValue<Vec<InfrastructureLayoutRow>>>) -> Self {
        let infra_layout_rows = infra_layout_rows.map(|v| v.into_inner());
        InfrastructureMessageDetail{msg_type, message_name, description, layout_url, infra_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InfrastructureMessageDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InfrastructureMessageDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InfrastructureMessageDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InfrastructureMessageDetail",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InfrastructureComponentDetail {
    pub component_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub repetition: Option<ComponentRepetition>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub layout_url: Option<uri>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_layout_rows: Option<Vec<InfrastructureLayoutRow>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InfrastructureComponentDetail {
    #[new]
    #[pyo3(signature = (component_name, repetition=None, description=None, layout_url=None, infra_layout_rows=None))]
    pub fn new(component_name: String, repetition: Option<ComponentRepetition>, description: Option<String>, layout_url: Option<uri>, infra_layout_rows: Option<serde_utils::PyValue<Vec<InfrastructureLayoutRow>>>) -> Self {
        let infra_layout_rows = infra_layout_rows.map(|v| v.into_inner());
        InfrastructureComponentDetail{component_name, repetition, description, layout_url, infra_layout_rows}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InfrastructureComponentDetail>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InfrastructureComponentDetail> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InfrastructureComponentDetail>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InfrastructureComponentDetail",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InfrastructureLayoutRow {
    pub infra_layout_kind: InfrastructureLayoutRowKindEnum,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_layout_field_tag: Option<isize>,
    pub infra_layout_element_name: String,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_layout_required: Option<bool>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_layout_description: Option<String>,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_layout_nested: Option<bool>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InfrastructureLayoutRow {
    #[new]
    #[pyo3(signature = (infra_layout_kind, infra_layout_element_name, infra_layout_field_tag=None, infra_layout_required=None, infra_layout_description=None, infra_layout_nested=None))]
    pub fn new(infra_layout_kind: InfrastructureLayoutRowKindEnum, infra_layout_element_name: String, infra_layout_field_tag: Option<isize>, infra_layout_required: Option<bool>, infra_layout_description: Option<String>, infra_layout_nested: Option<bool>) -> Self {
        InfrastructureLayoutRow{infra_layout_kind, infra_layout_element_name, infra_layout_field_tag, infra_layout_required, infra_layout_description, infra_layout_nested}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InfrastructureLayoutRow>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InfrastructureLayoutRow> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InfrastructureLayoutRow>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InfrastructureLayoutRow",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct StandardResponseMapping {
    pub category_label: String,
    pub fix_message: String,
    pub appropriate_responses: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl StandardResponseMapping {
    #[new]
    #[pyo3(signature = (category_label, fix_message, appropriate_responses))]
    pub fn new(category_label: String, fix_message: String, appropriate_responses: String) -> Self {
        StandardResponseMapping{category_label, fix_message, appropriate_responses}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<StandardResponseMapping>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<StandardResponseMapping> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<StandardResponseMapping>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid StandardResponseMapping",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct ApplicationMessageReferenceKey {
    pub category_label: String,
    pub fix_message: String,
    pub business_reject_ref_id_value: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl ApplicationMessageReferenceKey {
    #[new]
    #[pyo3(signature = (category_label, fix_message, business_reject_ref_id_value))]
    pub fn new(category_label: String, fix_message: String, business_reject_ref_id_value: String) -> Self {
        ApplicationMessageReferenceKey{category_label, fix_message, business_reject_ref_id_value}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<ApplicationMessageReferenceKey>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<ApplicationMessageReferenceKey> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<ApplicationMessageReferenceKey>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid ApplicationMessageReferenceKey",
        ))
    }
}



#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct BusinessRejectReasonDescription {
    pub reject_reason_code: isize,
    pub reject_reason_label: String
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl BusinessRejectReasonDescription {
    #[new]
    #[pyo3(signature = (reject_reason_code, reject_reason_label))]
    pub fn new(reject_reason_code: isize, reject_reason_label: String) -> Self {
        BusinessRejectReasonDescription{reject_reason_code, reject_reason_label}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<BusinessRejectReasonDescription>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<BusinessRejectReasonDescription> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<BusinessRejectReasonDescription>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid BusinessRejectReasonDescription",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for BusinessRejectReasonDescription {
    type Key   = isize;
    type Value = String;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.reject_reason_code;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("reject_reason_code".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("reject_reason_code".into()), key_value);
        map.insert(Value::String("reject_reason_label".into()), v);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }

    }

    fn simple_value(&self) -> Option<&Self::Value> {
        Some(&self.reject_reason_label)
    }

    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("reject_reason_code".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}

#[derive(Debug, Clone, PartialEq)]
#[cfg_attr(feature = "serde", derive(Serialize, Deserialize))]
#[cfg_attr(feature = "stubgen", gen_stub_pyclass)]
#[cfg_attr(feature = "pyo3", pyclass(subclass, get_all, set_all))]
pub struct InfrastructureGlobalComponentReference {
    pub infra_global_component_name: InfrastructureGlobalComponentName,
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_global_component_repetition: Option<String>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_global_component_field_tags: Option<Vec<isize>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_global_component_field_names: Option<Vec<String>>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_global_component_used_in: Vec<InfrastructureCategoryEnum>,
    #[cfg_attr(feature = "serde", serde(
        deserialize_with = "serde_utils::deserialize_primitive_list_or_single_value_optional",
        serialize_with = "serde_utils::serialize_primitive_list_or_single_value_optional"
    ))]
    #[cfg_attr(feature = "serde", serde(default))]
    pub infra_global_component_msg_types: Option<Vec<String>>
}
#[cfg(feature = "pyo3")]
#[cfg_attr(feature = "stubgen", gen_stub_pymethods)]
#[pymethods]
impl InfrastructureGlobalComponentReference {
    #[new]
    #[pyo3(signature = (infra_global_component_name, infra_global_component_used_in, infra_global_component_repetition=None, infra_global_component_field_tags=None, infra_global_component_field_names=None, infra_global_component_msg_types=None))]
    pub fn new(infra_global_component_name: InfrastructureGlobalComponentName, infra_global_component_used_in: Vec<InfrastructureCategoryEnum>, infra_global_component_repetition: Option<String>, infra_global_component_field_tags: Option<Vec<isize>>, infra_global_component_field_names: Option<Vec<String>>, infra_global_component_msg_types: Option<Vec<String>>) -> Self {
        InfrastructureGlobalComponentReference{infra_global_component_name, infra_global_component_used_in, infra_global_component_repetition, infra_global_component_field_tags, infra_global_component_field_names, infra_global_component_msg_types}
    }
}

#[cfg(feature = "pyo3")]
impl<'py> IntoPyObject<'py> for Box<InfrastructureGlobalComponentReference>
{
    type Target = PyAny;
    type Output = Bound<'py, Self::Target>;
    type Error = PyErr;
    fn into_pyobject(self, py: Python<'py>) -> Result<Self::Output, Self::Error> {
        (*self).into_pyobject(py).map(move |x| x.into_any())
    }
}

#[cfg(feature = "pyo3")]
impl<'py> FromPyObject<'py> for Box<InfrastructureGlobalComponentReference> {
    fn extract_bound(ob: &pyo3::Bound<'py, pyo3::types::PyAny>) -> pyo3::PyResult<Self> {
        if let Ok(val) = ob.extract::<InfrastructureGlobalComponentReference>() {
            return Ok(Box::new(val));
        }
        Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
            "invalid InfrastructureGlobalComponentReference",
        ))
    }
}


#[cfg(feature = "serde")]
impl serde_utils::InlinedPair for InfrastructureGlobalComponentReference {
    type Key   = InfrastructureGlobalComponentName;
    type Value = Value;
    type Error = String;

    fn extract_key(&self) -> &Self::Key {
        return &self.infra_global_component_name;
    }

    fn from_pair_mapping(k: Self::Key, v: Value) -> Result<Self,Self::Error> {
        let mut map = match v {
            Value::Map(m) => m,
            _ => return Err("ClassDefinition must be a mapping".into()),
        };
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("infra_global_component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }
    }


    fn from_pair_simple(k: Self::Key, _v: Value) -> Result<Self,Self::Error> {
        let mut map:  BTreeMap<Value, Value> = BTreeMap::new();
        let key_value = serde_value::to_value(k.clone())
            .map_err(|e| format!("unable to serialize key: {}", e))?;
        map.insert(Value::String("infra_global_component_name".into()), key_value);
        let de          = Value::Map(map).into_deserializer();
        match serde_path_to_error::deserialize(de) {
            Ok(ok)  => Ok(ok),
            Err(e)  => Err(format!("at `{}`: {}", e.path(), e.inner())),
        }


    }


    fn compact_value(&self) -> Option<Value> {
        let value = match serde_value::to_value(self) {
            Ok(v) => v,
            Err(_) => return None,
        };
        match value {
            Value::Map(mut map) => {
                map.remove(&Value::String("infra_global_component_name".into()));
                Some(Value::Map(map))
            }
            _ => None,
        }
    }
}




#[cfg(feature = "stubgen")]
define_stub_info_gatherer!(stub_info);
