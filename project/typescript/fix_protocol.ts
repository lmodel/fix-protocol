export type FIXFamilyStandardId = string;
export type ExtensionPackNumber = string;
export type FIXDatatypeDatatypeName = string;
export type BusinessAreaArea = string;
export type MessageCategoryCategory = string;
export type FieldTag = string;
export type ComponentComponentName = string;
export type GlobalComponentComponentName = string;
export type CommonComponentComponentName = string;
export type SpecificComponentComponentName = string;
export type MessageMsgType = string;
export type UDFTagRangeRangeId = string;
export type PreTradeMessageEntryMsgType = string;
export type PreTradeComponentEntryComponentName = string;
export type ComponentTableFootnoteFootnoteNumber = string;
export type PreTradeCategorySectionCategory = string;
export type PreTradeMessageDetailMsgType = string;
export type PreTradeComponentDetailComponentName = string;
export type MessageGroupGroupTitle = string;
export type CommonComponentDetailComponentName = string;
export type TradeMessageEntryMsgType = string;
export type TradeComponentEntryComponentName = string;
export type TradeComponentTableFootnoteTradeFootnoteNumber = string;
export type TradeCategorySectionCategory = string;
export type TradeMessageDetailMsgType = string;
export type TradeComponentDetailComponentName = string;
export type TradeMessageGroupTradeGroupTitle = string;
export type TradeCommonComponentDetailComponentName = string;
export type TradeOrdStatusPrecedenceEntryTradeOrdStatusLabel = string;
export type TradeFragmentationEntryTradeFragmentationMessage = string;
export type TradeAppendixSectionTradeAppendixCategory = string;
export type PostTradeMessageEntryMsgType = string;
export type PostTradeComponentEntryComponentName = string;
export type PostTradeComponentTableFootnoteFootnoteNumber = string;
export type PostTradeCategorySectionCategory = string;
export type PostTradeMessageGroupGroupTitle = string;
export type PostTradeMessageDetailMsgType = string;
export type PostTradeComponentDetailComponentName = string;
export type PostTradeCommonComponentDetailComponentName = string;
export type AllocationStatusDescriptionStatusCode = string;
export type AllocationFragmentationFieldMapMsgType = string;
export type TradeCaptureReportUsageStatusLabel = string;
export type TradeCaptureReportIdentifierRuleIdentifierRole = string;
export type RegistrationStatusDescriptionStatusCode = string;
export type ClearingServicePostTradeProcessingFormatMessageFormat = string;
export type InfrastructureMessageEntryMsgType = string;
export type InfrastructureComponentEntryComponentName = string;
export type InfrastructureComponentTableFootnoteFootnoteNumber = string;
export type BusinessRejectReasonDescriptionRejectReasonCode = string;
export type InfrastructureGlobalComponentReferenceInfraGlobalComponentName = string;
/**
* Layer of the FIX Technical Standard Stack.
*/
export enum StandardLayer {
    
    APPLICATION = "APPLICATION",
    ENCODING = "ENCODING",
    SESSION = "SESSION",
};
/**
* Qualitative size indicator for an Extension Pack.
*/
export enum ExtensionPackSize {
    
    XXS = "XXS",
    XS = "XS",
    S = "S",
    M = "M",
    L = "L",
    XL = "XL",
    XXL = "XXL",
};
/**
* FIX business areas that may reference a Global Component from the FIX Latest "Global Components" page.
*/
export enum GlobalComponentBusinessAreaEnum {
    
    PRE_TRADE = "PRE_TRADE",
    TRADE = "TRADE",
    POST_TRADE = "POST_TRADE",
    INFRASTRUCTURE = "INFRASTRUCTURE",
};
/**
* Top-level business areas of the FIX Latest specification.
*/
export enum BusinessAreaEnum {
    
    INTRODUCTION = "INTRODUCTION",
    PRE_TRADE = "PRE_TRADE",
    TRADE = "TRADE",
    POST_TRADE = "POST_TRADE",
    INFRASTRUCTURE = "INFRASTRUCTURE",
};
/**
* Message categories defined within FIX Latest business areas.
*/
export enum MessageCategoryEnum {
    
    INDICATION = "INDICATION",
    EVENT_COMMUNICATION = "EVENT_COMMUNICATION",
    QUOTATION_NEGOTIATION = "QUOTATION_NEGOTIATION",
    MARKET_DATA = "MARKET_DATA",
    MARKET_STRUCTURE_REFERENCE_DATA = "MARKET_STRUCTURE_REFERENCE_DATA",
    SECURITIES_REFERENCE_DATA = "SECURITIES_REFERENCE_DATA",
    PARTIES_REFERENCE_DATA = "PARTIES_REFERENCE_DATA",
    PARTIES_ACTION = "PARTIES_ACTION",
    SINGLE_GENERAL_ORDER_HANDLING = "SINGLE_GENERAL_ORDER_HANDLING",
    ORDER_MASS_HANDLING = "ORDER_MASS_HANDLING",
    CROSS_ORDERS = "CROSS_ORDERS",
    MULTILEG_ORDERS = "MULTILEG_ORDERS",
    LIST_PROGRAM_BASKET_TRADING = "LIST_PROGRAM_BASKET_TRADING",
    ALLOCATION_AND_READY_TO_BOOK = "ALLOCATION_AND_READY_TO_BOOK",
    CONFIRMATION = "CONFIRMATION",
    SETTLEMENT_INSTRUCTIONS = "SETTLEMENT_INSTRUCTIONS",
    TRADE_CAPTURE_REPORTING = "TRADE_CAPTURE_REPORTING",
    REGISTRATION_INSTRUCTIONS = "REGISTRATION_INSTRUCTIONS",
    POSITIONS_MAINTENANCE = "POSITIONS_MAINTENANCE",
    COLLATERAL_MANAGEMENT = "COLLATERAL_MANAGEMENT",
    MARGIN_REQUIREMENT_MANAGEMENT = "MARGIN_REQUIREMENT_MANAGEMENT",
    ACCOUNT_REPORTING = "ACCOUNT_REPORTING",
    TRADE_MANAGEMENT = "TRADE_MANAGEMENT",
    PAY_MANAGEMENT = "PAY_MANAGEMENT",
    SETTLEMENT_STATUS_MANAGEMENT = "SETTLEMENT_STATUS_MANAGEMENT",
    BUSINESS_MESSAGE_REJECTS = "BUSINESS_MESSAGE_REJECTS",
    NETWORK_STATUS_COMMUNICATION = "NETWORK_STATUS_COMMUNICATION",
    USER_MANAGEMENT = "USER_MANAGEMENT",
    APPLICATION_SEQUENCING = "APPLICATION_SEQUENCING",
};
/**
* Sharing scope of a FIX component.
*/
export enum ComponentScope {
    
    GLOBAL = "GLOBAL",
    COMMON = "COMMON",
    SPECIFIC = "SPECIFIC",
};
/**
* Thematic grouping under which a Global Component is presented.
*/
export enum ComponentGroup {
    
    SECURITIES = "SECURITIES",
    LEG_SECURITIES = "LEG_SECURITIES",
    UNDERLYING_SECURITIES = "UNDERLYING_SECURITIES",
    PARTIES = "PARTIES",
    ORDERS_AND_QUOTES = "ORDERS_AND_QUOTES",
    TRADES = "TRADES",
    COMMISSIONS_AND_FEES = "COMMISSIONS_AND_FEES",
    FINANCING = "FINANCING",
    PAYMENTS = "PAYMENTS",
    STIPULATIONS = "STIPULATIONS",
    HEADER_AND_TRAILER = "HEADER_AND_TRAILER",
    MISCELLANEOUS = "MISCELLANEOUS",
};
/**
* Required-status of a field within a message or component.
*/
export enum FieldRequirement {
    
    REQUIRED = "REQUIRED",
    OPTIONAL = "OPTIONAL",
    CONDITIONALLY_REQUIRED = "CONDITIONALLY_REQUIRED",
};
/**
* Product/asset classes covered by FIX at the application layer.
*/
export enum ProductCoverage {
    
    EQUITIES = "EQUITIES",
    CIV = "CIV",
    DERIVATIVES = "DERIVATIVES",
    FIXED_INCOME = "FIXED_INCOME",
    FOREIGN_EXCHANGE = "FOREIGN_EXCHANGE",
};
/**
* Names of FIX Protocol datatypes.
*/
export enum FIXDatatypeName {
    
    int = "int",
    TagNum = "TagNum",
    SeqNum = "SeqNum",
    NumInGroup = "NumInGroup",
    DayOfMonth = "DayOfMonth",
    float = "float",
    Qty = "Qty",
    Price = "Price",
    PriceOffset = "PriceOffset",
    Amt = "Amt",
    Percentage = "Percentage",
    char = "char",
    Boolean = "Boolean",
    String = "String",
    MultipleCharValue = "MultipleCharValue",
    MultipleStringValue = "MultipleStringValue",
    Country = "Country",
    Currency = "Currency",
    Exchange = "Exchange",
    MonthYear = "MonthYear",
    UTCTimestamp = "UTCTimestamp",
    UTCTimeOnly = "UTCTimeOnly",
    UTCDateOnly = "UTCDateOnly",
    LocalMktDate = "LocalMktDate",
    TZTimeOnly = "TZTimeOnly",
    TZTimestamp = "TZTimestamp",
    Length = "Length",
    data = "data",
    Tenor = "Tenor",
    Reserved100Plus = "Reserved100Plus",
    Reserved1000Plus = "Reserved1000Plus",
    Reserved4000Plus = "Reserved4000Plus",
    XMLData = "XMLData",
    Language = "Language",
    LocalMktTime = "LocalMktTime",
};
/**
* ISO/IEC 11404:2007 General-Purpose Datatypes value space.
*/
export enum ISO11404ValueSpace {
    
    integer = "integer",
    ordinal = "ordinal",
    size = "size",
    real = "real",
    scaled = "scaled",
    character = "character",
    characterstring = "characterstring",
    boolean = "boolean",
    set = "set",
    array = "array",
    time = "time",
    union = "union",
};
/**
* Time unit used in a FIX Tenor expression.
*/
export enum TenorUnit {
    
    D = "D",
    W = "W",
    M = "M",
    Y = "Y",
};
/**
* Named encodings of the FIX Family of Standards.
*/
export enum StandardEncodingName {
    
    TAGVALUE = "TAGVALUE",
    FIXML = "FIXML",
    FAST = "FAST",
    SBE = "SBE",
    GPB = "GPB",
    JSON = "JSON",
    ASN_1 = "ASN_1",
};
/**
* Named session-layer protocols in the FIX Family of Standards.
*/
export enum SessionProtocolName {
    
    FIX_4_2 = "FIX_4_2",
    FIX4 = "FIX4",
    FIXT = "FIXT",
    LFIXT = "LFIXT",
    FIXP = "FIXP",
    SOFH = "SOFH",
    FIXS = "FIXS",
    AMQP = "AMQP",
};
/**
* Time-unit precision for FIX time-bearing datatypes.
*/
export enum TimePrecision {
    
    SECOND = "SECOND",
    MILLISECOND = "MILLISECOND",
    MICROSECOND = "MICROSECOND",
    NANOSECOND = "NANOSECOND",
    PICOSECOND = "PICOSECOND",
    DAY = "DAY",
};
/**
* Organizational bodies of FIX Protocol Limited.
*/
export enum FPLCommitteeRole {
    
    GLOBAL_STEERING_COMMITTEE = "GLOBAL_STEERING_COMMITTEE",
    GLOBAL_TECHNICAL_COMMITTEE = "GLOBAL_TECHNICAL_COMMITTEE",
    GLOBAL_PRODUCT_COMMITTEE = "GLOBAL_PRODUCT_COMMITTEE",
    GLOBAL_BUY_SIDE_COMMITTEE = "GLOBAL_BUY_SIDE_COMMITTEE",
    GLOBAL_MEMBER_SERVICES_COMMITTEE = "GLOBAL_MEMBER_SERVICES_COMMITTEE",
    REGIONAL_COMMITTEE = "REGIONAL_COMMITTEE",
};
/**
* Geographic regions for FPL Regional Committees.
*/
export enum FPLRegion {
    
    AMERICAS = "AMERICAS",
    ASIA_PACIFIC = "ASIA_PACIFIC",
    EMEA = "EMEA",
    JAPAN = "JAPAN",
};
/**
* Global Product Committees maintained by FIX Protocol Limited.
*/
export enum FPLProductGroup {
    
    FIXED_INCOME_AND_CURRENCIES = "FIXED_INCOME_AND_CURRENCIES",
    LISTED_PRODUCTS_AND_EXCHANGES = "LISTED_PRODUCTS_AND_EXCHANGES",
};
/**
* Categories of organizations represented in FPL membership.
*/
export enum FPLMemberType {
    
    BUY_SIDE_FIRM = "BUY_SIDE_FIRM",
    SELL_SIDE_FIRM = "SELL_SIDE_FIRM",
    EXCHANGE = "EXCHANGE",
    ECN_ATS = "ECN_ATS",
    UTILITY = "UTILITY",
    VENDOR = "VENDOR",
    OTHER_ASSOCIATION = "OTHER_ASSOCIATION",
};
/**
* Usage policy assigned to a reserved range of UDF tag numbers.
*/
export enum UDFTagRangeUsage {
    
    INTER_FIRM_REGISTERED = "INTER_FIRM_REGISTERED",
    INTER_FIRM_BILATERAL = "INTER_FIRM_BILATERAL",
    GTC_REGULATORY_LEGACY = "GTC_REGULATORY_LEGACY",
    WIP_CHINA = "WIP_CHINA",
    INTERNAL_FIRM = "INTERNAL_FIRM",
    GTC_OTC_DERIVATIVES = "GTC_OTC_DERIVATIVES",
    GTC_RESERVED = "GTC_RESERVED",
};
/**
* The eight message categories of the FIX Latest Pre-Trade business area. Subset of MessageCategoryEnum.
*/
export enum PreTradeCategoryEnum {
    
    INDICATION = "INDICATION",
    EVENT_COMMUNICATION = "EVENT_COMMUNICATION",
    QUOTATION_NEGOTIATION = "QUOTATION_NEGOTIATION",
    MARKET_DATA = "MARKET_DATA",
    MARKET_STRUCTURE_REFERENCE_DATA = "MARKET_STRUCTURE_REFERENCE_DATA",
    SECURITIES_REFERENCE_DATA = "SECURITIES_REFERENCE_DATA",
    PARTIES_REFERENCE_DATA = "PARTIES_REFERENCE_DATA",
    PARTIES_ACTION = "PARTIES_ACTION",
};
/**
* Whether a FIX component is repeating or non-repeating.
*/
export enum ComponentRepetition {
    
    REPEATING = "REPEATING",
    NON_REPEATING = "NON_REPEATING",
};
/**
* Names of the Common Components declared at the top of the Pre-Trade business-area chapter.
*/
export enum PreTradeCommonComponentName {
    
    AuctionTypeRuleGrp = "AuctionTypeRuleGrp",
    BaseTradingRules = "BaseTradingRules",
    ExecInstRules = "ExecInstRules",
    InstrumentScope = "InstrumentScope",
    InstrumentScopeGrp = "InstrumentScopeGrp",
    InstrumentScopeSecurityAltIDGrp = "InstrumentScopeSecurityAltIDGrp",
    LotTypeRules = "LotTypeRules",
    MarketDataFeedTypes = "MarketDataFeedTypes",
    MarketSegmentScopeGrp = "MarketSegmentScopeGrp",
    MatchRules = "MatchRules",
    OrdTypeRules = "OrdTypeRules",
    PriceLimits = "PriceLimits",
    PriceRangeRuleGrp = "PriceRangeRuleGrp",
    QuoteSizeRuleGrp = "QuoteSizeRuleGrp",
    RequestedPartyRoleGrp = "RequestedPartyRoleGrp",
    RequestingPartyGrp = "RequestingPartyGrp",
    RequestingPartySubGrp = "RequestingPartySubGrp",
    RoutingGrp = "RoutingGrp",
    TickRules = "TickRules",
    TimeInForceRules = "TimeInForceRules",
    TradingSessionRules = "TradingSessionRules",
};
/**
* Quoting business models referenced in the Quotation / Negotiation category.
*/
export enum QuoteModelEnum {
    
    INDICATIVE = "INDICATIVE",
    TRADEABLE = "TRADEABLE",
    RESTRICTED_TRADEABLE = "RESTRICTED_TRADEABLE",
    NEGOTIATION = "NEGOTIATION",
};
/**
* Discriminator for a row in a Pre-Trade message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal "Component" in the Tag column).
*/
export enum PreTradeLayoutRowKindEnum {
    
    FIELD = "FIELD",
    COMPONENT = "COMPONENT",
};
/**
* The five message categories of the FIX Latest Trade (Orders and Executions) business area. Subset of MessageCategoryEnum.
*/
export enum TradeCategoryEnum {
    
    SINGLE_GENERAL_ORDER_HANDLING = "SINGLE_GENERAL_ORDER_HANDLING",
    ORDER_MASS_HANDLING = "ORDER_MASS_HANDLING",
    CROSS_ORDER_HANDLING = "CROSS_ORDER_HANDLING",
    MULTILEG_ORDER_HANDLING = "MULTILEG_ORDER_HANDLING",
    LIST_PROGRAM_BASKET_TRADING = "LIST_PROGRAM_BASKET_TRADING",
};
/**
* Whether a FIX component is repeating or non-repeating.
*/
export enum TradeComponentRepetition {
    
    REPEATING = "REPEATING",
    NON_REPEATING = "NON_REPEATING",
};
/**
* Names of the Common Components declared at the bottom of the Trade business-area chapter — components used by messages across more than one Trade category.
*/
export enum TradeCommonComponentName {
    
    DisclosureInstructionGrp = "DisclosureInstructionGrp",
    DiscretionInstructions = "DiscretionInstructions",
    PegInstructions = "PegInstructions",
    PreAllocGrp = "PreAllocGrp",
    StrategyParametersGrp = "StrategyParametersGrp",
    TriggeringInstruction = "TriggeringInstruction",
};
/**
* Discriminator for a row in a Trade message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal "Component" in the Tag column).
*/
export enum TradeLayoutRowKindEnum {
    
    FIELD = "FIELD",
    COMPONENT = "COMPONENT",
};
/**
* The twelve message categories of the FIX Latest Post-Trade business area. Subset of MessageCategoryEnum.
*/
export enum PostTradeCategoryEnum {
    
    ALLOCATION = "ALLOCATION",
    CONFIRMATION = "CONFIRMATION",
    SETTLEMENT_INSTRUCTION = "SETTLEMENT_INSTRUCTION",
    TRADE_CAPTURE_REPORTING = "TRADE_CAPTURE_REPORTING",
    REGISTRATION_INSTRUCTION = "REGISTRATION_INSTRUCTION",
    POSITION_MAINTENANCE = "POSITION_MAINTENANCE",
    COLLATERAL_MANAGEMENT = "COLLATERAL_MANAGEMENT",
    MARGIN_REQUIREMENT_MANAGEMENT = "MARGIN_REQUIREMENT_MANAGEMENT",
    ACCOUNT_REPORTING = "ACCOUNT_REPORTING",
    TRADE_MANAGEMENT = "TRADE_MANAGEMENT",
    PAY_MANAGEMENT = "PAY_MANAGEMENT",
    SETTLEMENT_STATUS_MANAGEMENT = "SETTLEMENT_STATUS_MANAGEMENT",
};
/**
* Names of the Common Components declared at the top of the Post-Trade business-area chapter.
*/
export enum PostTradeCommonComponentName {
    
    AllocCommissionDataGrp = "AllocCommissionDataGrp",
    AllocRegulatoryTradeIDGrp = "AllocRegulatoryTradeIDGrp",
    ClrInstGrp = "ClrInstGrp",
    CollateralAmountGrp = "CollateralAmountGrp",
    CollateralReinvestmentGrp = "CollateralReinvestmentGrp",
    DlvyInstGrp = "DlvyInstGrp",
    ExecAllocGrp = "ExecAllocGrp",
    MarginAmount = "MarginAmount",
    OrdAllocGrp = "OrdAllocGrp",
    PositionAmountData = "PositionAmountData",
    SettlDetails = "SettlDetails",
    SettlInstructionsData = "SettlInstructionsData",
    SettlParties = "SettlParties",
    SettlPtysSubGrp = "SettlPtysSubGrp",
    TradeAllocAmtGrp = "TradeAllocAmtGrp",
    TransactionAttributeGrp = "TransactionAttributeGrp",
};
/**
* Communication options by which an Initiator may convey allocation instructions to a Respondent.
*/
export enum AllocationScenarioEnum {
    
    PRE_ALLOCATED_ORDER = "PRE_ALLOCATED_ORDER",
    PRE_TRADE_ALLOCATION = "PRE_TRADE_ALLOCATION",
    POST_TRADE_ALLOCATION = "POST_TRADE_ALLOCATION",
    READY_TO_BOOK = "READY_TO_BOOK",
};
/**
* AllocStatus(87) values used in allocation acknowledgement messages.
*/
export enum AllocationStatusEnum {
    
    ACCEPTED = "ACCEPTED",
    BLOCK_LEVEL_REJECT = "BLOCK_LEVEL_REJECT",
    ACCOUNT_LEVEL_REJECT = "ACCOUNT_LEVEL_REJECT",
    RECEIVED_NOT_YET_PROCESSED = "RECEIVED_NOT_YET_PROCESSED",
};
/**
* AllocTransType(71) values.
*/
export enum AllocationTransactionTypeEnum {
    
    NEW = "NEW",
    REPLACE = "REPLACE",
    CANCEL = "CANCEL",
};
/**
* Methods by which post-trade allocations may be computed.
*/
export enum PostTradeAllocationPricingMethodEnum {
    
    AVERAGE_PRICE = "AVERAGE_PRICE",
    EXECUTED_PRICE = "EXECUTED_PRICE",
};
/**
* Direction of a TradeCaptureReport relative to the marketplace.
*/
export enum TradeCaptureReportDirectionEnum {
    
    INBOUND = "INBOUND",
    OUTBOUND = "OUTBOUND",
};
/**
* Documented usages of the TradeCaptureReport(35=AE) message.
*/
export enum TradeCaptureReportUsageEnum {
    
    RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS = "RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS",
    RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES = "RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES",
    REPORTING_PRIVATELY_NEGOTIATED_TRADES = "REPORTING_PRIVATELY_NEGOTIATED_TRADES",
    REPORTING_FLOOR_OR_ROUTED_EXECUTIONS = "REPORTING_FLOOR_OR_ROUTED_EXECUTIONS",
    REQUEST_TRADE_CANCEL_OR_AMENDMENT = "REQUEST_TRADE_CANCEL_OR_AMENDMENT",
};
/**
* Roles played by trade-capture-report identifier fields.
*/
export enum TradeCaptureReportIdentifierRoleEnum {
    
    TRADE_REPORT_ID = "TRADE_REPORT_ID",
    TRADE_ID = "TRADE_ID",
    TRADE_REPORT_REF_ID = "TRADE_REPORT_REF_ID",
    SECONDARY_TRADE_ID = "SECONDARY_TRADE_ID",
};
/**
* RegistTransType(514) values.
*/
export enum RegistrationTransactionTypeEnum {
    
    NEW = "NEW",
    REPLACE = "REPLACE",
    CANCEL = "CANCEL",
};
/**
* RegistStatus(506) values.
*/
export enum RegistrationStatusEnum {
    
    ACCEPTED = "ACCEPTED",
    REJECTED = "REJECTED",
    HELD = "HELD",
    REMINDER = "REMINDER",
};
/**
* SettlInstMode(160) values relevant in Post-Trade.
*/
export enum SettlementInstructionModeEnum {
    
    STANDING_INSTRUCTIONS = "STANDING_INSTRUCTIONS",
    SPECIFIC_ORDER = "SPECIFIC_ORDER",
    REQUEST_REJECT = "REQUEST_REJECT",
};
/**
* SettlObligMode(1159) values.
*/
export enum SettlementObligationModeEnum {
    
    PRELIMINARY = "PRELIMINARY",
    FINAL = "FINAL",
};
/**
* PosMaintAction(712) values.
*/
export enum PositionMaintenanceActionEnum {
    
    NEW = "NEW",
    REPLACE = "REPLACE",
    CANCEL = "CANCEL",
    REVERSE = "REVERSE",
};
/**
* Business functions invokable via the Position Management Clearing Services.
*/
export enum ClearingServiceForPositionManagementEnum {
    
    POSITION_CHANGE_SUBMISSION = "POSITION_CHANGE_SUBMISSION",
    POSITION_ADJUSTMENT = "POSITION_ADJUSTMENT",
    EXERCISE_NOTICE = "EXERCISE_NOTICE",
    ABANDONMENT_NOTICE = "ABANDONMENT_NOTICE",
    MARGIN_DISPOSITION = "MARGIN_DISPOSITION",
    POSITION_PLEDGE = "POSITION_PLEDGE",
    REQUEST_FOR_POSITION = "REQUEST_FOR_POSITION",
};
/**
* Message-format families used by the Post-Trade Processing Clearing Services.
*/
export enum ClearingServiceForPostTradeProcessingEnum {
    
    ETP = "ETP",
    GIVE_UP = "GIVE_UP",
    EXCHANGE_FOR_PHYSICAL = "EXCHANGE_FOR_PHYSICAL",
    AVERAGE_PRICE_SYSTEM = "AVERAGE_PRICE_SYSTEM",
    MUTUAL_OFFSET_SYSTEM = "MUTUAL_OFFSET_SYSTEM",
    TRADE_ENTRY_EDIT = "TRADE_ENTRY_EDIT",
};
/**
* Documented uses of the Collateral Management messages.
*/
export enum CollateralManagementUsageEnum {
    
    SECURITIES_FINANCING_COLLATERALIZATION = "SECURITIES_FINANCING_COLLATERALIZATION",
    CLEARING_HOUSE_COLLATERALIZATION = "CLEARING_HOUSE_COLLATERALIZATION",
};
/**
* Purposes for which a CollateralAssignment may be sent.
*/
export enum CollateralAssignmentPurposeEnum {
    
    ASSIGN_INITIAL_COLLATERAL = "ASSIGN_INITIAL_COLLATERAL",
    REPLENISH_COLLATERAL = "REPLENISH_COLLATERAL",
    REPLACE_OR_SUBSTITUTE_COLLATERAL = "REPLACE_OR_SUBSTITUTE_COLLATERAL",
};
/**
* Role labels used throughout the Allocation category prose to designate the sender and receiver of an AllocationInstruction.
*/
export enum AllocationRoleEnum {
    
    INITIATOR = "INITIATOR",
    RESPONDENT = "RESPONDENT",
};
/**
* MatchStatus(573) values referenced in Post-Trade prose.
*/
export enum MatchStatusEnum {
    
    COMPARED_MATCHED_OR_AFFIRMED = "COMPARED_MATCHED_OR_AFFIRMED",
    UNCOMPARED_UNMATCHED_OR_UNAFFIRMED = "UNCOMPARED_UNMATCHED_OR_UNAFFIRMED",
};
/**
* Discriminator for a row in a Post-Trade message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal "Component" in the Tag column).
*/
export enum PostTradeLayoutRowKindEnum {
    
    FIELD = "FIELD",
    COMPONENT = "COMPONENT",
};
/**
* The four message categories of the FIX Latest Infrastructure business area. Subset of MessageCategoryEnum.
*/
export enum InfrastructureCategoryEnum {
    
    BUSINESS_MESSAGE_REJECTS = "BUSINESS_MESSAGE_REJECTS",
    NETWORK_STATUS_COMMUNICATION = "NETWORK_STATUS_COMMUNICATION",
    USER_MANAGEMENT = "USER_MANAGEMENT",
    APPLICATION_SEQUENCING = "APPLICATION_SEQUENCING",
};
/**
* Names of the components defined in the Infrastructure business-area chapter. None of these are shared across categories within the area; footnotes 1–4 record that four of them were historically declared as common components.
*/
export enum InfrastructureComponentName {
    
    ApplIDReportGrp = "ApplIDReportGrp",
    ApplIDRequestAckGrp = "ApplIDRequestAckGrp",
    ApplIDRequestGrp = "ApplIDRequestGrp",
    CompIDReqGrp = "CompIDReqGrp",
    CompIDStatGrp = "CompIDStatGrp",
    ThrottleMsgTypeGrp = "ThrottleMsgTypeGrp",
    ThrottleParamsGrp = "ThrottleParamsGrp",
    UsernameGrp = "UsernameGrp",
};
/**
* Permissible values of BusinessRejectReason(380) on the BusinessMessageReject(35=j) message.
*/
export enum BusinessRejectReasonEnum {
    
    OTHER = "OTHER",
    UNKNOWN_ID = "UNKNOWN_ID",
    UNKNOWN_SECURITY = "UNKNOWN_SECURITY",
    UNSUPPORTED_MESSAGE_TYPE = "UNSUPPORTED_MESSAGE_TYPE",
    APPLICATION_NOT_AVAILABLE = "APPLICATION_NOT_AVAILABLE",
    CONDITIONALLY_REQUIRED_FIELD_MISSING = "CONDITIONALLY_REQUIRED_FIELD_MISSING",
    NOT_AUTHORISED = "NOT_AUTHORISED",
    DELIVER_TO_FIRM_NOT_AVAILABLE = "DELIVER_TO_FIRM_NOT_AVAILABLE",
    THROTTLE_LIMIT_EXCEEDED = "THROTTLE_LIMIT_EXCEEDED",
    THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT = "THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT",
    THROTTLED_MESSAGES_REJECTED_ON_REQUEST = "THROTTLED_MESSAGES_REJECTED_ON_REQUEST",
    INVALID_PRICE_INCREMENT = "INVALID_PRICE_INCREMENT",
};
/**
* Network Status Communication usage scenarios documented in the chapter (Scenario A: hub-and-spoke; Scenario B: global brokerage region availability).
*/
export enum NetworkStatusScenarioEnum {
    
    SCENARIO_A = "SCENARIO_A",
    SCENARIO_B = "SCENARIO_B",
};
/**
* Documented uses of ApplicationMessageReport(35=BY) selected via ApplReportType(1426).
*/
export enum ApplicationMessageReportTypeEnum {
    
    RESET = "RESET",
    LAST_MESSAGE = "LAST_MESSAGE",
    KEEP_ALIVE = "KEEP_ALIVE",
    RESEND_COMPLETED = "RESEND_COMPLETED",
};
/**
* Values of NetworkRequestType(935) explicitly cited in the NetworkCounterpartySystemStatusRequest(35=BC) prose.
*/
export enum NetworkRequestTypeEnum {
    
    SNAPSHOT = "SNAPSHOT",
    STOP_SUBSCRIBING = "STOP_SUBSCRIBING",
};
/**
* Direction of a "Standard Response" mapping — which area the requesting message belongs to.
*/
export enum StandardResponseDirectionEnum {
    
    PRE_TRADE = "PRE_TRADE",
    TRADE = "TRADE",
    POST_TRADE = "POST_TRADE",
};
/**
* Direction of an "application message reference" key-field mapping — which area the referenced message belongs to.
*/
export enum BusinessMessageReferenceDirectionEnum {
    
    PRE_TRADE = "PRE_TRADE",
    TRADE = "TRADE",
    POST_TRADE = "POST_TRADE",
};
/**
* Names of the Global Components (declared in the FIX Latest "Global Components" page) that the Infrastructure business-area messages explicitly reference. Global Components are reusable component blocks used across two or more business areas.
*/
export enum InfrastructureGlobalComponentName {
    
    ApplicationSequenceControl = "ApplicationSequenceControl",
};
/**
* Tags contributed by the ApplicationSequenceControl global component (used by Application Sequencing messages and by all FIX messages representing reports).
*/
export enum ApplicationSequenceControlFieldName {
    
    ApplID = "ApplID",
    ApplSeqNum = "ApplSeqNum",
    ApplLastSeqNum = "ApplLastSeqNum",
    ApplResendFlag = "ApplResendFlag",
};
/**
* Discriminator for a row in an Infrastructure message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal "Component" in the Tag column).
*/
export enum InfrastructureLayoutRowKindEnum {
    
    FIELD = "FIELD",
    COMPONENT = "COMPONENT",
};


/**
 * Container for the structural elements of the FIX Latest Introduction section. Tree root for instance data.
 */
export interface FIXIntroduction {
    /** Version stamp from the document header. */
    published_version?: string,
    /** Publication date of the document. */
    published_date?: date,
    /** Publishing body of the FIX Latest specification. */
    publisher?: string,
    /** The Preface text of the specification. */
    preface?: string,
    /** The Introduction prose section. */
    introduction_text?: string,
    /** Prose note on UTC leap-second handling for UTCTimestamp. */
    utc_leap_seconds_note?: string,
    /** Information about FIX Protocol Limited. */
    about_fpl?: FIXProtocolLimited,
    /** The FIX Family of Standards. */
    standards?: FIXFamilyStandard[],
    /** The list of Extension Packs. */
    extension_packs?: ExtensionPack[],
    /** FIX Protocol datatype definitions and value spaces. */
    datatypes?: FIXDatatype[],
    /** Top-level business areas of FIX Latest. */
    business_areas?: BusinessArea[],
    /** Global Components defined in the Introduction. */
    global_components?: GlobalComponent[],
    /** Reserved ranges of user-defined-field tag numbers. */
    udf_ranges?: UDFTagRange[],
    /** Product/asset classes covered by FIX at the application layer. */
    product_coverage?: string,
}


/**
 * The organization that maintains the FIX Protocol specification.
 */
export interface FIXProtocolLimited {
    /** Brand name used by the organization. */
    brand_name?: string,
    /** Legal name of the organization. */
    legal_name?: string,
    /** Main website URL of the organization. */
    website?: string,
    /** URL listing current FPL Member firms. */
    member_firms_url?: string,
    /** URL listing currently active FPL Working Groups. */
    working_groups_url?: string,
    /** URL listing Product and Regional Committees. */
    committees_url?: string,
    /** Organization categories represented in FPL membership. */
    member_types?: string,
    /** High-level governance bodies that represent FPL. */
    governance_bodies?: string,
    /** Global Product Committees maintained by FPL. */
    product_committees?: string,
    /** Regional Committees maintained by FPL. */
    regional_committees?: string,
}


/**
 * A member standard of the FIX Family of Standards.
 */
export interface FIXFamilyStandard {
    /** Unique identifier (CURIE or local name) of the element. */
    id: string,
    /** Display name of the element. */
    name: string,
    /** Free-text description. */
    description?: string,
    /** Short acronym used to refer to the standard. */
    acronym?: string,
    /** Related external resources. */
    see_also?: string[],
    /** The layer the standard belongs to. */
    layer: string,
    /** Version of the standard, if applicable. */
    version?: string,
    /** Name of the session profile for session-layer variants. */
    session_profile?: string,
    /** Named encoding, when layer is ENCODING. */
    encoding_name?: string,
}


/**
 * A unit of change to FIX Latest.
 */
export interface ExtensionPack {
    /** Sequential identifier of the Extension Pack. */
    number: number,
    /** Short descriptive title. */
    title: string,
    /** Qualitative size indicator (XXS..XXL). */
    size?: string,
    /** Narrative summary of what the EP introduces. */
    enhancement_summary?: string,
    /** True when the EP applies only to the FIX Session Layer. */
    applies_to_session_layer_only?: boolean,
    /** True when the EP applies only to the FIXML encoding. */
    applies_to_fixml_only?: boolean,
}


/**
 * A FIX Protocol datatype.
 */
export interface FIXDatatype {
    /** Canonical FIX datatype name. */
    datatype_name: string,
    /** Prose definition of the datatype. */
    definition: string,
    /** ISO/IEC 11404:2007 GPD value space assigned to the datatype. */
    value_space?: string,
    /** Additional value-space constraints. */
    value_space_notes?: string,
    /** True for datatypes not permitted in new designs. */
    deprecated_for_new_designs?: boolean,
    /** Reference standard for datatypes backed by an external code set. */
    external_code_set?: string,
    /** Time-unit precision for time-bearing datatypes. */
    time_unit?: string,
    /** Numeric radix for scaled value-space datatypes. */
    radix?: number,
    /** Character repertoire for character/string datatypes. */
    repertoire?: string,
    /** Inclusive lower bound of a bounded-array index. */
    index_lower_bound?: number,
    /** Inclusive upper bound of a bounded-array index. */
    index_upper_bound?: number,
    /** Inclusive lower bound on the integer value space. */
    minimum_value?: number,
    /** Inclusive upper bound on the integer value space. */
    maximum_value?: number,
    /** Footnote indicators attached to a datatype row. */
    footnote_numbers?: number[],
}


/**
 * A top-level business area of the FIX Latest specification.
 */
export interface BusinessArea {
    /** Identity of the business area. */
    area: string,
    /** Display title of the area. */
    title?: string,
    /** Description of the area. */
    description?: string,
    /** Message categories defined within a business area. */
    categories?: MessageCategory[],
}


/**
 * A message category within a business area.
 */
export interface MessageCategory {
    /** Identity of the message category. */
    category: string,
    /** Display title of the category. */
    title?: string,
    /** Description of the category. */
    description?: string,
    /** Business area the element belongs to. */
    business_area: string,
    /** Messages defined within the enclosing element. */
    messages?: Message[],
}


/**
 * A FIX field — a uniquely tagged data element with a FIX datatype.
 */
export interface Field {
    /** Numeric tag of the field. */
    tag: number,
    /** PascalCase name of the field. */
    field_name: string,
    /** FIX datatype of the field. */
    datatype: string,
    /** Description of the field's purpose. */
    description?: string,
    /** Required-status of the field within the enclosing context. */
    requirement?: string,
    /** True when the field is a User Defined Field. */
    is_user_defined?: boolean,
}


/**
 * A FIX component — a named set of related fields.
 */
export interface Component {
    /** PascalCase name of the component. */
    component_name: string,
    /** Description of the component. */
    description?: string,
    /** Sharing scope of the component. */
    scope: string,
    /** True when the component is a repeating group. */
    is_repeating_group?: boolean,
    /** Fields directly contained by the enclosing element. */
    fields?: Field[],
    /** Components nested within this component. */
    nested_components?: ComponentComponentName[],
}


/**
 * A component shared by messages of two or more business areas.
 */
export interface GlobalComponent extends Component {
    /** Thematic group under which the component is presented. */
    component_group: string,
    /** Applicable at the Instrument level. */
    applies_to_instrument?: boolean,
    /** Applicable at the InstrumentLeg level. */
    applies_to_leg?: boolean,
    /** Applicable at the UnderlyingInstrument level. */
    applies_to_underlying?: boolean,
    /** Names of other components conceptually identical to this one. */
    conceptually_identical_to?: string[],
    /** Numeric component identifier extracted from the FIX Latest "Global Components" page anchor ID (e.g. "comp1057-1" → 1057). Stable across Extension Packs and shared with the FIX Orchestra repository. */
    gc_id?: number,
    /** FIX business areas whose messages embed the Global Component. */
    gc_referenced_in?: string,
}


/**
 * A component used only by messages within a single business area.
 */
export interface CommonComponent extends Component {
    /** Business area the element belongs to. */
    business_area: string,
}


/**
 * A component used only by messages within a single category.
 */
export interface SpecificComponent extends Component {
    /** Business area the element belongs to. */
    business_area: string,
    /** Message category. */
    category: string,
}


/**
 * A FIX application message.
 */
export interface Message {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Description of the message's purpose. */
    description?: string,
    /** Message category. */
    category?: string,
    /** Fields directly contained by the enclosing element. */
    fields?: Field[],
    /** Components referenced by the enclosing element. */
    components?: ComponentComponentName[],
}


/**
 * A reserved range of tag numbers for User Defined Fields.
 */
export interface UDFTagRange {
    /** Identifier of the range. */
    range_id: string,
    /** Inclusive lower bound of the range. */
    low_tag: number,
    /** Upper bound of the tag range. Required for all ``usage`` values except ``GTC_RESERVED`` (which is open-ended, 50000+). Downstream validators should enforce this; the constraint cannot be expressed here because LinkML's ``equals_string`` operator only accepts string-ranged slots and ``usage`` is an enum. */
    high_tag?: number,
    /** Usage policy assigned to the range. */
    usage: string,
    /** Notes on the range's intended use. */
    description?: string,
    /** True when tags in the range must be registered. */
    requires_registration?: boolean,
}


/**
 * Tree-root container for the Pre-Trade business area of FIX Latest.
 */
export interface PreTradeBusinessArea {
    /** Identity of the business area. */
    area: string,
    /** Display title. */
    title?: string,
    /** Version stamp from the document header. */
    published_version?: string,
    /** Publishing body of the FIX Latest specification. */
    publisher?: string,
    /** Prose introduction of the chapter. */
    introduction?: string,
    /** Sentence describing diagram conventions used in the chapter. */
    diagram_conventions?: string,
    /** Intro prose of the area-wide Messages sub-section. */
    messages_overview_note?: string,
    /** Area-wide pre-trade messages table. */
    messages?: PreTradeMessageEntry[],
    /** Intro prose of the area-wide Components sub-section. */
    components_overview_note?: string,
    /** Area-wide pre-trade components table. */
    components?: PreTradeComponentEntry[],
    /** Common Components declared at the top of the chapter. */
    common_components?: string,
    /** Per-common-component descriptions from the chapter's final section. */
    common_component_details?: CommonComponentDetail[],
    /** Footnotes attached to the area-wide components table. */
    footnotes?: ComponentTableFootnote[],
    /** Per-category sub-sections of the chapter. */
    category_sections?: PreTradeCategorySection[],
    /** Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name. */
    referenced_global_components?: GlobalComponentComponentName[],
}


/**
 * One row of the area-wide pre-trade messages table.
 */
export interface PreTradeMessageEntry {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Message category. */
    category: string,
}


/**
 * One row of the area-wide pre-trade components table.
 */
export interface PreTradeComponentEntry {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    repetition: string,
    /** Category the component is listed under. Common Components are listed under the synthetic "Common Components" value. */
    category: string,
    /** True when the component is declared as a Common Component. */
    is_common?: boolean,
    /** Footnote indicator on a component-table row. */
    footnote_number?: number,
}


/**
 * A footnote on the area-wide components table.
 */
export interface ComponentTableFootnote {
    /** Footnote indicator on a component-table row. */
    footnote_number: number,
    /** PascalCase name of the component. */
    component_name: string,
    /** FIX version or Extension Pack that introduced the component. */
    introduced_in: string,
    /** Single category that actually uses the component. */
    sole_category: string,
    /** Footnote text. */
    text?: string,
}


/**
 * A per-category sub-section of the Pre-Trade chapter.
 */
export interface PreTradeCategorySection {
    /** Message category. */
    category: string,
    /** Display title. */
    title?: string,
    /** Free-text description. */
    description?: string,
    /** Quoting business models referenced in the Quotation / Negotiation category. */
    quote_models?: string,
    /** Purpose-grouped message descriptions inside a category. */
    message_groups?: MessageGroup[],
    /** Messages defined in this category. */
    messages?: PreTradeMessageDetail[],
    /** Intro prose of a category's Components sub-section. */
    category_components_note?: string,
    /** Components used exclusively by messages within a category. */
    category_specific_components?: PreTradeComponentDetail[],
}


/**
 * Per-category message description.
 */
export interface PreTradeMessageDetail {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Description of the message's purpose and usage. */
    description?: string,
    /** URL of the detailed message- or component-layout. */
    layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Pre-Trade Appendix. */
    pre_layout_rows?: PreTradeLayoutRow[],
}


/**
 * Per-category component description.
 */
export interface PreTradeComponentDetail {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    repetition?: string,
    /** Description of the component's purpose. */
    description?: string,
    /** URL of the detailed message- or component-layout. */
    layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Pre-Trade Appendix. */
    pre_layout_rows?: PreTradeLayoutRow[],
}


/**
 * Purpose-grouped sub-section inside a category's Messages section.
 */
export interface MessageGroup {
    /** Purpose-group heading inside a category's Messages sub-section. */
    group_title: string,
    /** Description of the purpose-group's role within the category. */
    description?: string,
    /** Messages bundled under the purpose-group heading. */
    messages: PreTradeMessageDetail[],
}


/**
 * Per-common-component description.
 */
export interface CommonComponentDetail {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    repetition?: string,
    /** Description of the common component's purpose. */
    description?: string,
    /** URL of the detailed message- or component-layout. */
    layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Pre-Trade Appendix. */
    pre_layout_rows?: PreTradeLayoutRow[],
}


/**
 * One row of the layout table published in the Pre-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
 */
export interface PreTradeLayoutRow {
    /** Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table). */
    pre_layout_kind: string,
    /** FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows. */
    pre_layout_field_tag?: number,
    /** Element name as printed in the Name column — either the FIX field name or the component name. */
    pre_layout_element_name: string,
    /** Whether the field or component is required, as printed in the Req’d column of the source layout table ("Y" / "N"). */
    pre_layout_required?: boolean,
    /** Free-text content of the Description column of the row (may be empty). */
    pre_layout_description?: string,
    /** Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table). */
    pre_layout_nested?: boolean,
}


/**
 * Tree-root container for the Trade (Orders and Executions) business area of FIX Latest.
 */
export interface TradeBusinessArea {
    /** Identity of the business area the chapter describes. */
    trade_area: string,
    /** Display title. */
    title?: string,
    /** Version stamp from the document header. */
    published_version?: string,
    /** Publishing body of the FIX Latest specification. */
    publisher?: string,
    /** Prose introduction of the chapter. */
    trade_introduction?: string,
    /** Sentence describing diagram conventions used in the chapter. */
    trade_diagram_conventions?: string,
    /** URL of the "Message Diagram Templates" page referenced by the chapter introduction. */
    trade_message_diagram_template_url?: string,
    /** Intro prose of the area-wide Messages sub-section. */
    trade_messages_overview_note?: string,
    /** Area-wide trade messages table. */
    messages?: TradeMessageEntry[],
    /** Intro prose of the area-wide Components sub-section. */
    trade_components_overview_note?: string,
    /** Area-wide trade components table. */
    components?: TradeComponentEntry[],
    /** Common Components declared at the bottom of the chapter. */
    trade_common_components?: string,
    /** Per-common-component descriptions from the chapter's final section. */
    trade_common_component_details?: TradeCommonComponentDetail[],
    /** Footnotes attached to the area-wide components table. */
    trade_footnotes?: TradeComponentTableFootnote[],
    /** Per-category sub-sections of the chapter. */
    trade_category_sections?: TradeCategorySection[],
    /** Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name. */
    referenced_global_components?: GlobalComponentComponentName[],
}


/**
 * One row of the area-wide trade messages table.
 */
export interface TradeMessageEntry {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Message category. */
    category: string,
}


/**
 * One row of the area-wide trade components table.
 */
export interface TradeComponentEntry {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    trade_repetition: string,
    /** Category the component is listed under. Common Components are listed under the synthetic "Common Components" value. */
    category: string,
    /** True when the component is declared as a Common Component. */
    trade_is_common?: boolean,
    /** Footnote indicator on a component-table row. */
    trade_footnote_number?: number,
}


/**
 * A footnote on the area-wide components table.
 */
export interface TradeComponentTableFootnote {
    /** Footnote indicator on a component-table row. */
    trade_footnote_number: number,
    /** PascalCase name of the component. */
    component_name: string,
    /** FIX version or Extension Pack that introduced the component. */
    trade_introduced_in: string,
    /** Single category that actually uses the component. */
    trade_sole_category: string,
    /** Footnote text. */
    trade_footnote_text?: string,
}


/**
 * A per-category sub-section of the Trade chapter.
 */
export interface TradeCategorySection {
    /** Message category. */
    category: string,
    /** Display title. */
    title?: string,
    /** Free-text description. */
    description?: string,
    /** Optional "Background" prose preceding a category's message descriptions (e.g. the Cross Order Handling chapter's cross-trade overview). */
    trade_category_background?: string,
    /** Purpose-grouped message descriptions inside a category. */
    trade_message_groups?: TradeMessageGroup[],
    /** Messages defined in this category. */
    messages?: TradeMessageDetail[],
    /** Intro prose of a category's Components sub-section. */
    trade_category_components_note?: string,
    /** Components used exclusively by messages within a single category. */
    trade_category_specific_components?: TradeComponentDetail[],
    /** Rows of the fragmentation table listed in a Trade category that documents which messages may be fragmented and which repeating group is fragmentable (currently published only for List/Program/Basket Trading). */
    trade_fragmentation_entries?: TradeFragmentationEntry[],
}


/**
 * Per-category message description.
 */
export interface TradeMessageDetail {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Description of the message's purpose and usage. */
    description?: string,
    /** URL of the detailed message- or component-layout in the Trade Appendix. */
    trade_layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Trade Appendix. */
    trade_layout_rows?: TradeLayoutRow[],
}


/**
 * Per-category component description.
 */
export interface TradeComponentDetail {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    trade_repetition?: string,
    /** Description of the component's purpose. */
    description?: string,
    /** URL of the detailed message- or component-layout in the Trade Appendix. */
    trade_layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Trade Appendix. */
    trade_layout_rows?: TradeLayoutRow[],
}


/**
 * Purpose-grouped sub-section inside a category's Messages sub-section (e.g. "New Order Single", "Execution Reports", "Order Cancel Requests" under Single/General Order Handling).
 */
export interface TradeMessageGroup {
    /** Purpose-group heading inside a category's Messages sub-section. */
    trade_group_title: string,
    /** Description of the purpose-group's role within the category. */
    description?: string,
    /** Messages bundled under the purpose-group heading. */
    messages: TradeMessageDetail[],
    /** Rows of the OrdStatus(39) precedence table that appears inside the Execution Reports purpose-group of the Single/General Order Handling category. */
    trade_ord_status_precedence_entries?: TradeOrdStatusPrecedenceEntry[],
}


/**
 * Per-common-component description from the chapter's final "Common Components" section.
 */
export interface TradeCommonComponentDetail {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    trade_repetition?: string,
    /** Description of the common component's purpose. */
    description?: string,
    /** URL of the detailed message- or component-layout in the Trade Appendix. */
    trade_layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Trade Appendix. */
    trade_layout_rows?: TradeLayoutRow[],
}


/**
 * One row of the layout table published in the Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
 */
export interface TradeLayoutRow {
    /** Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table). */
    trade_layout_kind: string,
    /** FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows. */
    trade_layout_field_tag?: number,
    /** Element name as printed in the Name column — either the FIX field name or the component name. */
    trade_layout_element_name: string,
    /** Whether the field or component is required, as printed in the Req'd column of the source layout table ("Y" / "N"). */
    trade_layout_required?: boolean,
    /** Free-text content of the Description column of the row (may be empty). */
    trade_layout_description?: string,
    /** Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table). */
    trade_layout_nested?: boolean,
}


/**
 * One row of the OrdStatus(39) precedence table published in the Execution Reports purpose-group of the Single/General Order Handling category. Defines the precedence ranking used to resolve simultaneous state transitions on an order, paired with the human-readable OrdStatus label and its descriptive prose.
 */
export interface TradeOrdStatusPrecedenceEntry {
    /** Precedence rank (1 = lowest, higher numbers take precedence) of an OrdStatus(39) value used to resolve simultaneous state transitions on an order. */
    trade_ord_status_precedence: number,
    /** Human-readable OrdStatus(39) label as printed in the Execution Reports precedence table (e.g. "Pending Cancel", "Done for Day", "Filled"). */
    trade_ord_status_label: string,
    /** Verbatim OrdStatus description from the table. */
    description?: string,
}


/**
 * One row of a fragmentation table published in a Trade category (currently only List/Program/Basket Trading) identifying a message that may be fragmented, the "Total Entries" field used to indicate the total count across all fragments of the batch, and the verbatim description of the repeating group that may be fragmented.
 */
export interface TradeFragmentationEntry {
    /** Message that may be fragmented — verbatim text from the Message column of the fragmentation table (e.g. "NewOrderList(35=E)"). */
    trade_fragmentation_message: string,
    /** Name and tag of the "Total Entries" field used to indicate the total count across all fragments of the batch (e.g. "TotNoOrders(68)"). */
    trade_fragmentation_total_entries_field: string,
    /** Verbatim description of the repeating group that may be fragmented — from the table's third column. */
    trade_fragmentation_repeating_group: string,
}


/**
 * Tree-root container for the Trade Appendix — the spec companion document that publishes the full message- and component-layout tables for every message and component used in the Trade business area, organized into one "Appendix – <X> Category" sub-section per Trade category plus a final "Appendix – Common Category" sub-section covering the layouts of the chapter's common components.
 */
export interface TradeAppendix {
    /** Display title. */
    title?: string,
    /** Version stamp from the document header. */
    published_version?: string,
    /** Publishing body of the FIX Latest specification. */
    publisher?: string,
    /** Optional preface prose for the Trade Appendix as a whole. */
    description?: string,
    /** Per-category sub-sections of the Trade Appendix — one "Appendix – <X> Category" section per Trade category, plus a synthetic "Common Category" section that lists layouts of the chapter's common components. */
    trade_appendix_sections?: TradeAppendixSection[],
}


/**
 * One "Appendix – <X> Category" sub-section of the Trade Appendix. Bundles the per-message layout tables (TradeMessageDetail) and per-component layout tables (TradeComponentDetail) for messages and components that belong to one Trade category — or, for the synthetic "Common" section, the layouts of the chapter's common components.
 */
export interface TradeAppendixSection {
    /** Identifier for an appendix section — either the Trade category name as printed in the heading (e.g. "CrossOrders", "MultilegOrders", "OrderMassHandling", "ProgramTrading", "SingleGeneralOrderHandling") or the literal "Common" for the common-components appendix. */
    trade_appendix_category: string,
    /** Section heading exactly as printed in the Trade Appendix (e.g. "Appendix – CrossOrders Category"). */
    title?: string,
    /** Free-text description. */
    description?: string,
    /** Layout tables for the messages that belong to the appendix section. Empty for the "Common" section. */
    messages?: TradeMessageDetail[],
    /** Layout tables for the components that belong to the appendix section. */
    components?: TradeComponentDetailComponentName[],
}


/**
 * Tree-root container for the Post-Trade business area of FIX Latest.
 */
export interface PostTradeBusinessArea {
    /** Identity of the business area. */
    area: string,
    /** Display title. */
    title?: string,
    /** Version stamp from the document header. */
    published_version?: string,
    /** Publishing body of the FIX Latest specification. */
    publisher?: string,
    /** Prose introduction of the Post-Trade chapter. */
    post_introduction?: string,
    /** Sentence describing diagram conventions used in the chapter. */
    diagram_conventions?: string,
    /** Common Components declared at the top of the Post-Trade chapter. */
    post_common_components?: string,
    /** Messages defined within the enclosing element. */
    messages: PostTradeMessageEntry[],
    /** Components referenced by the enclosing element. */
    components: PostTradeComponentEntry[],
    /** Footnotes attached to the area-wide components table. */
    post_footnotes?: PostTradeComponentTableFootnote[],
    /** Per-category sub-sections of the Post-Trade chapter. */
    post_category_sections?: PostTradeCategorySection[],
    /** Per-common-component descriptions from the chapter's final Common Components section. */
    post_common_component_details?: PostTradeCommonComponentDetail[],
    /** Intro prose of the area-wide Messages sub-section. */
    messages_overview_note?: string,
    /** Intro prose of the area-wide Components sub-section. */
    components_overview_note?: string,
    /** Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name. */
    referenced_global_components?: GlobalComponentComponentName[],
}


/**
 * One row of the area-wide "Messages for Post-Trade Business Area" table.
 */
export interface PostTradeMessageEntry {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Message category. */
    category: string,
}


/**
 * One row of the area-wide "Components for Post-Trade Business Area" table.
 */
export interface PostTradeComponentEntry {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    repetition: string,
    /** Category label as printed in the component table; the token "Common Components" is allowed in addition to the PostTradeCategoryEnum values. */
    category: string,
    /** True when the component is declared as a Common Component. */
    is_common?: boolean,
    /** Footnote indicator on a component-table row. */
    footnote_number?: number,
}


/**
 * A footnote attached to a row of the area-wide Post-Trade components table.
 */
export interface PostTradeComponentTableFootnote {
    /** Footnote indicator on a component-table row. */
    footnote_number: number,
    /** PascalCase name of the component. */
    component_name: string,
    /** FIX version or Extension Pack that introduced the component. */
    introduced_in: string,
    /** Single Post-Trade category that actually uses the component (per footnote). */
    post_sole_category: string,
    /** Footnote text. */
    text?: string,
}


/**
 * A "Category – <name>" sub-section of the Post-Trade chapter.
 */
export interface PostTradeCategorySection {
    /** Message category. */
    category: string,
    /** Display title. */
    title?: string,
    /** Free-text description. */
    description?: string,
    /** Intro prose of a category's Components sub-section. */
    category_components_note?: string,
    /** Purpose-grouped message descriptions inside a Post-Trade category. */
    post_message_groups?: PostTradeMessageGroup[],
    /** Messages defined within the enclosing element. */
    messages?: PostTradeMessageDetail[],
    /** Components used exclusively by messages within a category. */
    post_category_specific_components?: PostTradeComponentDetail[],
    /** Communication options supported by the Allocation category for conveying allocation instructions. */
    allocation_scenarios?: string,
    /** Role labels used throughout the Allocation category prose. */
    allocation_roles?: string,
    /** Methods supported for computing post-trade allocations. */
    post_trade_allocation_pricing_methods?: string,
    /** Descriptions tied to AllocStatus(87) values as listed in the Allocation Instruction Acknowledgements section. */
    allocation_status_descriptions?: AllocationStatusDescription[],
    /** Per-message mapping of fragmentation-related fields used by the Allocation messages. */
    fragmentation_field_map?: AllocationFragmentationFieldMap[],
    /** Usages described in the "Trade Capture Report Usages" sub-section of the Trade Capture Reporting category. */
    trade_capture_report_usages?: TradeCaptureReportUsage[],
    /** Rules governing TradeCaptureReport(35=AE) identifier fields. */
    trade_capture_report_identifier_rules?: TradeCaptureReportIdentifierRule[],
    /** Descriptions tied to RegistStatus(506) values. */
    registration_status_descriptions?: RegistrationStatusDescription[],
    /** Business functions exposed by the Position Management Clearing Services. */
    clearing_services_for_position_management?: string,
    /** Per-format action sets exposed by the Post-Trade Processing Clearing Services. */
    clearing_services_for_post_trade_processing?: ClearingServicePostTradeProcessingFormat[],
    /** Documented usages for the Collateral Management messages. */
    collateral_management_usages?: string,
    /** Documented purposes for the CollateralAssignment(35=AY) message. */
    collateral_assignment_purposes?: string,
}


/**
 * A purpose-themed grouping of messages within a Post-Trade category (e.g. "Allocation Instructions").
 */
export interface PostTradeMessageGroup {
    /** Purpose-group heading inside a category's Messages sub-section. */
    group_title: string,
    /** Messages defined within the enclosing element. */
    messages: PostTradeMessageDetail[],
}


/**
 * Per-message description block from a Post-Trade category section.
 */
export interface PostTradeMessageDetail {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Free-text description. */
    description?: string,
    /** URL of the detailed message- or component-layout. */
    layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Post-Trade Appendix. */
    post_layout_rows?: PostTradeLayoutRow[],
}


/**
 * Per-component description block from a Post-Trade category section's Components sub-section.
 */
export interface PostTradeComponentDetail {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    repetition?: string,
    /** Free-text description. */
    description?: string,
    /** URL of the detailed message- or component-layout. */
    layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Post-Trade Appendix. */
    post_layout_rows?: PostTradeLayoutRow[],
}


/**
 * Per-common-component description block from the chapter's final "Common Components" section.
 */
export interface PostTradeCommonComponentDetail {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    repetition?: string,
    /** Free-text description. */
    description?: string,
    /** URL of the detailed message- or component-layout. */
    layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Post-Trade Appendix. */
    post_layout_rows?: PostTradeLayoutRow[],
}


/**
 * One row of the AllocStatus(87) value/description table.
 */
export interface AllocationStatusDescription {
    /** Wire status code as referenced in the chapter. */
    status_code: string,
    /** Human-readable label of the status code. */
    status_label: string,
    /** Free-text description. */
    description?: string,
}


/**
 * One row of the table mapping an allocation message to its fragmentation-related fields.
 */
export interface AllocationFragmentationFieldMap {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Field carrying the total number of repeating-group entries across all fragments (e.g. TotNoAllocs). */
    total_count_field: string,
    /** Field carrying the number of entries in the current message fragment (e.g. NoAllocs). */
    fragment_count_field: string,
    /** Principal message reference field used to bind allocation message fragments together (e.g. AllocID, AllocReportID). */
    principal_message_reference: string,
}


/**
 * One documented usage of the TradeCaptureReport(35=AE) message.
 */
export interface TradeCaptureReportUsage {
    /** Short label for the usage. */
    status_label: string,
    /** Free-text description. */
    description?: string,
    /** Role of the trade-capture-report identifier field. */
    identifier_role?: string,
}


/**
 * A rule governing one of the TradeCaptureReport(35=AE) identifier fields.
 */
export interface TradeCaptureReportIdentifierRule {
    /** Role of the trade-capture-report identifier field. */
    identifier_role: string,
    /** Free-text description. */
    description?: string,
}


/**
 * One row of the RegistStatus(506) value/description table.
 */
export interface RegistrationStatusDescription {
    /** Wire status code as referenced in the chapter. */
    status_code: string,
    /** Human-readable label of the status code. */
    status_label: string,
    /** Free-text description. */
    description?: string,
}


/**
 * One message-format row from the Post-Trade Processing Clearing Services section, with its supported actions.
 */
export interface ClearingServicePostTradeProcessingFormat {
    /** Clearing-service message format family referenced in the chapter. */
    message_format: string,
    /** Action labels (e.g. Allocation, Accept, Reject, Release, Change, Delete) supported by a clearing-service message format. */
    supported_actions: string[],
}


/**
 * One row of the layout table published in the Post-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
 */
export interface PostTradeLayoutRow {
    /** Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table). */
    post_layout_kind: string,
    /** FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows. */
    post_layout_field_tag?: number,
    /** Element name as printed in the Name column — either the FIX field name or the component name. */
    post_layout_element_name: string,
    /** Whether the field or component is required, as printed in the Req’d column of the source layout table ("Y" / "N"). */
    post_layout_required?: boolean,
    /** Free-text content of the Description column of the row (may be empty). */
    post_layout_description?: string,
    /** Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table). */
    post_layout_nested?: boolean,
}


/**
 * Tree-root container for the Infrastructure business area of FIX Latest.
 */
export interface InfrastructureBusinessArea {
    /** Identity of the business area. */
    area: string,
    /** Display title. */
    title?: string,
    /** Version stamp from the document header. */
    published_version?: string,
    /** Publishing body of the FIX Latest specification. */
    publisher?: string,
    /** Prose introduction of the Infrastructure chapter. */
    infra_introduction?: string,
    /** Sentence describing diagram conventions used in the chapter. */
    diagram_conventions?: string,
    /** Component names declared in the area-wide components listing. Per the chapter prose, none of these are shared across categories within the area. */
    infra_common_components?: string,
    /** Messages defined within the enclosing element. */
    messages: InfrastructureMessageEntry[],
    /** Intro prose of the area-wide Messages sub-section. */
    messages_overview_note?: string,
    /** Components referenced by the enclosing element. */
    components: InfrastructureComponentEntry[],
    /** Intro prose of the area-wide Components sub-section. */
    components_overview_note?: string,
    /** Footnotes attached to the area-wide Infrastructure components table. */
    infra_footnotes?: InfrastructureComponentTableFootnote[],
    /** Per-category sub-sections of the Infrastructure chapter. */
    infra_category_sections?: InfrastructureCategorySection[],
    /** "Standard Responses for Pre-Trade Messages" table rows. */
    standard_responses_pre_trade?: StandardResponseMapping[],
    /** "Standard Responses for Trade Messages" table rows. */
    standard_responses_trade?: StandardResponseMapping[],
    /** "Standard Responses for Post-Trade Messages" table rows. */
    standard_responses_post_trade?: StandardResponseMapping[],
    /** "Key Fields for Pre-Trade Application Message References" table rows. */
    key_fields_pre_trade?: ApplicationMessageReferenceKey[],
    /** "Key Fields for Trade Application Message References" table rows. */
    key_fields_trade?: ApplicationMessageReferenceKey[],
    /** "Key Fields for Post-Trade Application Message References" table rows. */
    key_fields_post_trade?: ApplicationMessageReferenceKey[],
    /** Descriptions tied to BusinessRejectReason(380) values. */
    business_reject_reason_descriptions?: BusinessRejectReasonDescription[],
    /** Global Components (from the FIX Latest "Global Components" page) that are explicitly referenced by messages in the Infrastructure business area, together with their tag set and usage scope. */
    infra_global_components?: InfrastructureGlobalComponentReference[],
    /** Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name. */
    referenced_global_components?: GlobalComponentComponentName[],
}


/**
 * One row of the area-wide "Messages for Infrastructure Business Area" table.
 */
export interface InfrastructureMessageEntry {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Message category. */
    category: string,
}


/**
 * One row of the area-wide "Components for Infrastructure Business Area" table.
 */
export interface InfrastructureComponentEntry {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    repetition: string,
    /** Message category. */
    category: string,
    /** Footnote indicator on a component-table row. */
    footnote_number?: number,
}


/**
 * A footnote attached to a row of the area-wide Infrastructure components table.
 */
export interface InfrastructureComponentTableFootnote {
    /** Footnote indicator on a component-table row. */
    footnote_number: number,
    /** PascalCase name of the component. */
    component_name: string,
    /** FIX version or Extension Pack that introduced the component. */
    introduced_in: string,
    /** Single Infrastructure category that actually uses the footnoted component. */
    infra_sole_category: string,
    /** Footnote text. */
    text?: string,
}


/**
 * A "Category – <name>" sub-section of the Infrastructure chapter.
 */
export interface InfrastructureCategorySection {
    /** Message category. */
    category: string,
    /** Display title. */
    title?: string,
    /** Free-text description. */
    description?: string,
    /** Intro prose of a category's Components sub-section. */
    category_components_note?: string,
    /** Messages defined within the enclosing element. */
    messages?: InfrastructureMessageDetail[],
    /** Per-component descriptions appearing in a category's Components sub-section. */
    infra_category_specific_components?: InfrastructureComponentDetail[],
    /** Network Status Communication usage scenarios. */
    network_status_scenarios?: string,
    /** NetworkRequestType(935) values explicitly cited in the Network Status Communication category prose. */
    network_request_types_referenced?: string,
    /** Documented uses of ApplicationMessageReport(35=BY). */
    application_message_report_uses?: string,
}


/**
 * Per-message description appearing in a category's Messages sub-section.
 */
export interface InfrastructureMessageDetail {
    /** MsgType(35) wire value identifying the message. */
    msg_type: string,
    /** PascalCase name of the message. */
    message_name: string,
    /** Free-text description. */
    description?: string,
    /** URL of the detailed message- or component-layout. */
    layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Infrastructure Appendix. */
    infra_layout_rows?: InfrastructureLayoutRow[],
}


/**
 * Per-component description appearing in a category's Components sub-section.
 */
export interface InfrastructureComponentDetail {
    /** PascalCase name of the component. */
    component_name: string,
    /** REPEATING or NON_REPEATING. */
    repetition?: string,
    /** Free-text description. */
    description?: string,
    /** URL of the detailed message- or component-layout. */
    layout_url?: string,
    /** Ordered rows of the layout table published for the message or component in the Infrastructure Appendix. */
    infra_layout_rows?: InfrastructureLayoutRow[],
}


/**
 * One row of the layout table published in the Infrastructure Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
 */
export interface InfrastructureLayoutRow {
    /** Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table). */
    infra_layout_kind: string,
    /** FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows. */
    infra_layout_field_tag?: number,
    /** Element name as printed in the Name column — either the FIX field name (e.g. ApplReqID) or the component name (e.g. StandardHeader, ApplIDRequestGrp). */
    infra_layout_element_name: string,
    /** Whether the field or component is required, as printed in the Req’d column of the source layout table ("Y" / "N"). */
    infra_layout_required?: boolean,
    /** Free-text content of the Description column of the row (may be empty). */
    infra_layout_description?: string,
    /** Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table). */
    infra_layout_nested?: boolean,
}


/**
 * One row of a "Standard Responses for <area> Messages" table mapping a request message to its appropriate response(s).
 */
export interface StandardResponseMapping {
    /** Category label as printed in the source table (free text; may include parenthesised sub-categories such as "Single General Order Handling"). */
    category_label: string,
    /** FIX message name with MsgType in parentheses, e.g. AllocationInstruction(35=J). */
    fix_message: string,
    /** Free-text appropriate-response cell from the Standard Responses tables. */
    appropriate_responses: string,
}


/**
 * One row of a "Key Fields for <area> Application Message References" table identifying the field whose value is copied into BusinessRejectRefID(379).
 */
export interface ApplicationMessageReferenceKey {
    /** Category label as printed in the source table (free text; may include parenthesised sub-categories such as "Single General Order Handling"). */
    category_label: string,
    /** FIX message name with MsgType in parentheses, e.g. AllocationInstruction(35=J). */
    fix_message: string,
    /** Source field copied into BusinessRejectRefID(379) when the target message lacks its own reject. May enumerate several alternatives joined by "or". */
    business_reject_ref_id_value: string,
}


/**
 * One entry of the BusinessRejectReason(380) code table.
 */
export interface BusinessRejectReasonDescription {
    /** Numeric code value of BusinessRejectReason(380). */
    reject_reason_code: number,
    /** Human-readable label of a BusinessRejectReason(380) code. */
    reject_reason_label: string,
}


/**
 * A reference from the Infrastructure business area to a Global Component declared on the FIX Latest "Global Components" page. Records the component name, the FIX tags it contributes, and the Infrastructure categories and messages that embed it.
 */
export interface InfrastructureGlobalComponentReference {
    /** Name of a Global Component referenced from within the Infrastructure business area. */
    infra_global_component_name: string,
    /** Repetition indicator for the Global Component as it appears in the referenced Infrastructure messages. */
    infra_global_component_repetition?: string,
    /** FIX tag numbers contributed by the referenced Global Component (as listed on the Global Components page). */
    infra_global_component_field_tags?: number[],
    /** Human-readable field names of the tags contributed by the referenced Global Component. */
    infra_global_component_field_names?: string[],
    /** Infrastructure categories that reference the Global Component. */
    infra_global_component_used_in: string,
    /** MsgType values within the Infrastructure business area that embed the referenced Global Component. */
    infra_global_component_msg_types?: string[],
}



