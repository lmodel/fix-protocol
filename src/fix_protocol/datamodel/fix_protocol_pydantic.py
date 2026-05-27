from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'fix_protocol',
     'default_range': 'string',
     'description': 'FIX Protocol - LinkML Schema',
     'id': 'https://w3id.org/lmodel/fix-protocol',
     'imports': ['linkml:types',
                 './fix_base',
                 './fix_pre_trade',
                 './fix_trade',
                 './fix_post_trade',
                 './fix_infrastructure',
                 './fix_global_components'],
     'license': 'Apache-2.0',
     'name': 'fix-protocol',
     'prefixes': {'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'biolink': {'prefix_prefix': 'biolink',
                              'prefix_reference': 'https://w3id.org/biolink/vocab/'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'http://www.example.org/rdf#'},
                  'fix_protocol': {'prefix_prefix': 'fix_protocol',
                                   'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/'},
                  'iso10383': {'prefix_prefix': 'iso10383',
                               'prefix_reference': 'https://www.iso.org/standard/61067.html#'},
                  'iso11404': {'prefix_prefix': 'iso11404',
                               'prefix_reference': 'https://www.iso.org/standard/39479.html#'},
                  'iso17442': {'prefix_prefix': 'iso17442',
                               'prefix_reference': 'https://www.iso.org/standard/78829.html#'},
                  'iso3166': {'prefix_prefix': 'iso3166',
                              'prefix_reference': 'https://www.iso.org/iso-3166-country-codes.html#'},
                  'iso4217': {'prefix_prefix': 'iso4217',
                              'prefix_reference': 'https://www.iso.org/iso-4217-currency-codes.html#'},
                  'iso639': {'prefix_prefix': 'iso639',
                             'prefix_reference': 'https://www.iso.org/iso-639-language-codes.html#'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/fix-protocol'],
     'source_file': 'src/fix_protocol/schema/fix_protocol.yaml',
     'title': 'fix-protocol'} )

class StandardLayer(str, Enum):
    """
    Layer of the FIX Technical Standard Stack.
    """
    APPLICATION = "APPLICATION"
    ENCODING = "ENCODING"
    SESSION = "SESSION"


class ExtensionPackSize(str, Enum):
    """
    Qualitative size indicator for an Extension Pack.
    """
    XXS = "XXS"
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"


class GlobalComponentBusinessAreaEnum(str, Enum):
    """
    FIX business areas that may reference a Global Component from the FIX Latest "Global Components" page.
    """
    PRE_TRADE = "PRE_TRADE"
    TRADE = "TRADE"
    POST_TRADE = "POST_TRADE"
    INFRASTRUCTURE = "INFRASTRUCTURE"


class BusinessAreaEnum(str, Enum):
    """
    Top-level business areas of the FIX Latest specification.
    """
    INTRODUCTION = "INTRODUCTION"
    PRE_TRADE = "PRE_TRADE"
    TRADE = "TRADE"
    POST_TRADE = "POST_TRADE"
    INFRASTRUCTURE = "INFRASTRUCTURE"


class MessageCategoryEnum(str, Enum):
    """
    Message categories defined within FIX Latest business areas.
    """
    INDICATION = "INDICATION"
    EVENT_COMMUNICATION = "EVENT_COMMUNICATION"
    QUOTATION_NEGOTIATION = "QUOTATION_NEGOTIATION"
    MARKET_DATA = "MARKET_DATA"
    MARKET_STRUCTURE_REFERENCE_DATA = "MARKET_STRUCTURE_REFERENCE_DATA"
    SECURITIES_REFERENCE_DATA = "SECURITIES_REFERENCE_DATA"
    PARTIES_REFERENCE_DATA = "PARTIES_REFERENCE_DATA"
    PARTIES_ACTION = "PARTIES_ACTION"
    SINGLE_GENERAL_ORDER_HANDLING = "SINGLE_GENERAL_ORDER_HANDLING"
    ORDER_MASS_HANDLING = "ORDER_MASS_HANDLING"
    CROSS_ORDERS = "CROSS_ORDERS"
    MULTILEG_ORDERS = "MULTILEG_ORDERS"
    LIST_PROGRAM_BASKET_TRADING = "LIST_PROGRAM_BASKET_TRADING"
    ALLOCATION_AND_READY_TO_BOOK = "ALLOCATION_AND_READY_TO_BOOK"
    CONFIRMATION = "CONFIRMATION"
    SETTLEMENT_INSTRUCTIONS = "SETTLEMENT_INSTRUCTIONS"
    TRADE_CAPTURE_REPORTING = "TRADE_CAPTURE_REPORTING"
    REGISTRATION_INSTRUCTIONS = "REGISTRATION_INSTRUCTIONS"
    POSITIONS_MAINTENANCE = "POSITIONS_MAINTENANCE"
    COLLATERAL_MANAGEMENT = "COLLATERAL_MANAGEMENT"
    MARGIN_REQUIREMENT_MANAGEMENT = "MARGIN_REQUIREMENT_MANAGEMENT"
    ACCOUNT_REPORTING = "ACCOUNT_REPORTING"
    TRADE_MANAGEMENT = "TRADE_MANAGEMENT"
    PAY_MANAGEMENT = "PAY_MANAGEMENT"
    SETTLEMENT_STATUS_MANAGEMENT = "SETTLEMENT_STATUS_MANAGEMENT"
    BUSINESS_MESSAGE_REJECTS = "BUSINESS_MESSAGE_REJECTS"
    NETWORK_STATUS_COMMUNICATION = "NETWORK_STATUS_COMMUNICATION"
    USER_MANAGEMENT = "USER_MANAGEMENT"
    APPLICATION_SEQUENCING = "APPLICATION_SEQUENCING"


class ComponentScope(str, Enum):
    """
    Sharing scope of a FIX component.
    """
    GLOBAL = "GLOBAL"
    COMMON = "COMMON"
    SPECIFIC = "SPECIFIC"


class ComponentGroup(str, Enum):
    """
    Thematic grouping under which a Global Component is presented.
    """
    SECURITIES = "SECURITIES"
    LEG_SECURITIES = "LEG_SECURITIES"
    UNDERLYING_SECURITIES = "UNDERLYING_SECURITIES"
    PARTIES = "PARTIES"
    ORDERS_AND_QUOTES = "ORDERS_AND_QUOTES"
    TRADES = "TRADES"
    COMMISSIONS_AND_FEES = "COMMISSIONS_AND_FEES"
    FINANCING = "FINANCING"
    PAYMENTS = "PAYMENTS"
    STIPULATIONS = "STIPULATIONS"
    HEADER_AND_TRAILER = "HEADER_AND_TRAILER"
    MISCELLANEOUS = "MISCELLANEOUS"


class FieldRequirement(str, Enum):
    """
    Required-status of a field within a message or component.
    """
    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"
    CONDITIONALLY_REQUIRED = "CONDITIONALLY_REQUIRED"


class ProductCoverage(str, Enum):
    """
    Product/asset classes covered by FIX at the application layer.
    """
    EQUITIES = "EQUITIES"
    CIV = "CIV"
    DERIVATIVES = "DERIVATIVES"
    FIXED_INCOME = "FIXED_INCOME"
    FOREIGN_EXCHANGE = "FOREIGN_EXCHANGE"


class FIXDatatypeName(str, Enum):
    """
    Names of FIX Protocol datatypes.
    """
    int = "int"
    TagNum = "TagNum"
    SeqNum = "SeqNum"
    NumInGroup = "NumInGroup"
    DayOfMonth = "DayOfMonth"
    float = "float"
    Qty = "Qty"
    Price = "Price"
    PriceOffset = "PriceOffset"
    Amt = "Amt"
    Percentage = "Percentage"
    char = "char"
    Boolean = "Boolean"
    String = "String"
    MultipleCharValue = "MultipleCharValue"
    MultipleStringValue = "MultipleStringValue"
    Country = "Country"
    Currency = "Currency"
    Exchange = "Exchange"
    MonthYear = "MonthYear"
    UTCTimestamp = "UTCTimestamp"
    UTCTimeOnly = "UTCTimeOnly"
    UTCDateOnly = "UTCDateOnly"
    LocalMktDate = "LocalMktDate"
    TZTimeOnly = "TZTimeOnly"
    TZTimestamp = "TZTimestamp"
    Length = "Length"
    data = "data"
    Tenor = "Tenor"
    Reserved100Plus = "Reserved100Plus"
    Reserved1000Plus = "Reserved1000Plus"
    Reserved4000Plus = "Reserved4000Plus"
    XMLData = "XMLData"
    Language = "Language"
    LocalMktTime = "LocalMktTime"


class ISO11404ValueSpace(str, Enum):
    """
    ISO/IEC 11404:2007 General-Purpose Datatypes value space.
    """
    integer = "integer"
    ordinal = "ordinal"
    size = "size"
    real = "real"
    scaled = "scaled"
    character = "character"
    characterstring = "characterstring"
    boolean = "boolean"
    set = "set"
    array = "array"
    time = "time"
    union = "union"


class TenorUnit(str, Enum):
    """
    Time unit used in a FIX Tenor expression.
    """
    D = "D"
    W = "W"
    M = "M"
    Y = "Y"


class StandardEncodingName(str, Enum):
    """
    Named encodings of the FIX Family of Standards.
    """
    TAGVALUE = "TAGVALUE"
    FIXML = "FIXML"
    FAST = "FAST"
    SBE = "SBE"
    GPB = "GPB"
    JSON = "JSON"
    ASN_1 = "ASN_1"


class SessionProtocolName(str, Enum):
    """
    Named session-layer protocols in the FIX Family of Standards.
    """
    FIX_4_2 = "FIX_4_2"
    FIX4 = "FIX4"
    FIXT = "FIXT"
    LFIXT = "LFIXT"
    FIXP = "FIXP"
    SOFH = "SOFH"
    FIXS = "FIXS"
    AMQP = "AMQP"


class TimePrecision(str, Enum):
    """
    Time-unit precision for FIX time-bearing datatypes.
    """
    SECOND = "SECOND"
    MILLISECOND = "MILLISECOND"
    MICROSECOND = "MICROSECOND"
    NANOSECOND = "NANOSECOND"
    PICOSECOND = "PICOSECOND"
    DAY = "DAY"


class FPLCommitteeRole(str, Enum):
    """
    Organizational bodies of FIX Protocol Limited.
    """
    GLOBAL_STEERING_COMMITTEE = "GLOBAL_STEERING_COMMITTEE"
    GLOBAL_TECHNICAL_COMMITTEE = "GLOBAL_TECHNICAL_COMMITTEE"
    GLOBAL_PRODUCT_COMMITTEE = "GLOBAL_PRODUCT_COMMITTEE"
    GLOBAL_BUY_SIDE_COMMITTEE = "GLOBAL_BUY_SIDE_COMMITTEE"
    GLOBAL_MEMBER_SERVICES_COMMITTEE = "GLOBAL_MEMBER_SERVICES_COMMITTEE"
    REGIONAL_COMMITTEE = "REGIONAL_COMMITTEE"


class FPLRegion(str, Enum):
    """
    Geographic regions for FPL Regional Committees.
    """
    AMERICAS = "AMERICAS"
    ASIA_PACIFIC = "ASIA_PACIFIC"
    EMEA = "EMEA"
    JAPAN = "JAPAN"


class FPLProductGroup(str, Enum):
    """
    Global Product Committees maintained by FIX Protocol Limited.
    """
    FIXED_INCOME_AND_CURRENCIES = "FIXED_INCOME_AND_CURRENCIES"
    LISTED_PRODUCTS_AND_EXCHANGES = "LISTED_PRODUCTS_AND_EXCHANGES"


class FPLMemberType(str, Enum):
    """
    Categories of organizations represented in FPL membership.
    """
    BUY_SIDE_FIRM = "BUY_SIDE_FIRM"
    SELL_SIDE_FIRM = "SELL_SIDE_FIRM"
    EXCHANGE = "EXCHANGE"
    ECN_ATS = "ECN_ATS"
    UTILITY = "UTILITY"
    VENDOR = "VENDOR"
    OTHER_ASSOCIATION = "OTHER_ASSOCIATION"


class UDFTagRangeUsage(str, Enum):
    """
    Usage policy assigned to a reserved range of UDF tag numbers.
    """
    INTER_FIRM_REGISTERED = "INTER_FIRM_REGISTERED"
    INTER_FIRM_BILATERAL = "INTER_FIRM_BILATERAL"
    GTC_REGULATORY_LEGACY = "GTC_REGULATORY_LEGACY"
    WIP_CHINA = "WIP_CHINA"
    INTERNAL_FIRM = "INTERNAL_FIRM"
    GTC_OTC_DERIVATIVES = "GTC_OTC_DERIVATIVES"
    GTC_RESERVED = "GTC_RESERVED"


class PreTradeCategoryEnum(str, Enum):
    """
    The eight message categories of the FIX Latest Pre-Trade business area. Subset of MessageCategoryEnum.
    """
    INDICATION = "INDICATION"
    EVENT_COMMUNICATION = "EVENT_COMMUNICATION"
    QUOTATION_NEGOTIATION = "QUOTATION_NEGOTIATION"
    MARKET_DATA = "MARKET_DATA"
    MARKET_STRUCTURE_REFERENCE_DATA = "MARKET_STRUCTURE_REFERENCE_DATA"
    SECURITIES_REFERENCE_DATA = "SECURITIES_REFERENCE_DATA"
    PARTIES_REFERENCE_DATA = "PARTIES_REFERENCE_DATA"
    PARTIES_ACTION = "PARTIES_ACTION"


class ComponentRepetition(str, Enum):
    """
    Whether a FIX component is repeating or non-repeating.
    """
    REPEATING = "REPEATING"
    NON_REPEATING = "NON_REPEATING"


class PreTradeCommonComponentName(str, Enum):
    """
    Names of the Common Components declared at the top of the Pre-Trade business-area chapter.
    """
    AuctionTypeRuleGrp = "AuctionTypeRuleGrp"
    BaseTradingRules = "BaseTradingRules"
    ExecInstRules = "ExecInstRules"
    InstrumentScope = "InstrumentScope"
    InstrumentScopeGrp = "InstrumentScopeGrp"
    InstrumentScopeSecurityAltIDGrp = "InstrumentScopeSecurityAltIDGrp"
    LotTypeRules = "LotTypeRules"
    MarketDataFeedTypes = "MarketDataFeedTypes"
    MarketSegmentScopeGrp = "MarketSegmentScopeGrp"
    MatchRules = "MatchRules"
    OrdTypeRules = "OrdTypeRules"
    PriceLimits = "PriceLimits"
    PriceRangeRuleGrp = "PriceRangeRuleGrp"
    QuoteSizeRuleGrp = "QuoteSizeRuleGrp"
    RequestedPartyRoleGrp = "RequestedPartyRoleGrp"
    RequestingPartyGrp = "RequestingPartyGrp"
    RequestingPartySubGrp = "RequestingPartySubGrp"
    RoutingGrp = "RoutingGrp"
    TickRules = "TickRules"
    TimeInForceRules = "TimeInForceRules"
    TradingSessionRules = "TradingSessionRules"


class QuoteModelEnum(str, Enum):
    """
    Quoting business models referenced in the Quotation / Negotiation category.
    """
    INDICATIVE = "INDICATIVE"
    TRADEABLE = "TRADEABLE"
    RESTRICTED_TRADEABLE = "RESTRICTED_TRADEABLE"
    NEGOTIATION = "NEGOTIATION"


class PreTradeLayoutRowKindEnum(str, Enum):
    """
    Discriminator for a row in a Pre-Trade message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal "Component" in the Tag column).
    """
    FIELD = "FIELD"
    COMPONENT = "COMPONENT"


class TradeCategoryEnum(str, Enum):
    """
    The five message categories of the FIX Latest Trade (Orders and Executions) business area. Subset of MessageCategoryEnum.
    """
    SINGLE_GENERAL_ORDER_HANDLING = "SINGLE_GENERAL_ORDER_HANDLING"
    ORDER_MASS_HANDLING = "ORDER_MASS_HANDLING"
    CROSS_ORDER_HANDLING = "CROSS_ORDER_HANDLING"
    MULTILEG_ORDER_HANDLING = "MULTILEG_ORDER_HANDLING"
    LIST_PROGRAM_BASKET_TRADING = "LIST_PROGRAM_BASKET_TRADING"


class TradeComponentRepetition(str, Enum):
    """
    Whether a FIX component is repeating or non-repeating.
    """
    REPEATING = "REPEATING"
    NON_REPEATING = "NON_REPEATING"


class TradeCommonComponentName(str, Enum):
    """
    Names of the Common Components declared at the bottom of the Trade business-area chapter — components used by messages across more than one Trade category.
    """
    DisclosureInstructionGrp = "DisclosureInstructionGrp"
    DiscretionInstructions = "DiscretionInstructions"
    PegInstructions = "PegInstructions"
    PreAllocGrp = "PreAllocGrp"
    StrategyParametersGrp = "StrategyParametersGrp"
    TriggeringInstruction = "TriggeringInstruction"


class TradeLayoutRowKindEnum(str, Enum):
    """
    Discriminator for a row in a Trade message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal "Component" in the Tag column).
    """
    FIELD = "FIELD"
    COMPONENT = "COMPONENT"


class PostTradeCategoryEnum(str, Enum):
    """
    The twelve message categories of the FIX Latest Post-Trade business area. Subset of MessageCategoryEnum.
    """
    ALLOCATION = "ALLOCATION"
    CONFIRMATION = "CONFIRMATION"
    SETTLEMENT_INSTRUCTION = "SETTLEMENT_INSTRUCTION"
    TRADE_CAPTURE_REPORTING = "TRADE_CAPTURE_REPORTING"
    REGISTRATION_INSTRUCTION = "REGISTRATION_INSTRUCTION"
    POSITION_MAINTENANCE = "POSITION_MAINTENANCE"
    COLLATERAL_MANAGEMENT = "COLLATERAL_MANAGEMENT"
    MARGIN_REQUIREMENT_MANAGEMENT = "MARGIN_REQUIREMENT_MANAGEMENT"
    ACCOUNT_REPORTING = "ACCOUNT_REPORTING"
    TRADE_MANAGEMENT = "TRADE_MANAGEMENT"
    PAY_MANAGEMENT = "PAY_MANAGEMENT"
    SETTLEMENT_STATUS_MANAGEMENT = "SETTLEMENT_STATUS_MANAGEMENT"


class PostTradeCommonComponentName(str, Enum):
    """
    Names of the Common Components declared at the top of the Post-Trade business-area chapter.
    """
    AllocCommissionDataGrp = "AllocCommissionDataGrp"
    AllocRegulatoryTradeIDGrp = "AllocRegulatoryTradeIDGrp"
    ClrInstGrp = "ClrInstGrp"
    CollateralAmountGrp = "CollateralAmountGrp"
    CollateralReinvestmentGrp = "CollateralReinvestmentGrp"
    DlvyInstGrp = "DlvyInstGrp"
    ExecAllocGrp = "ExecAllocGrp"
    MarginAmount = "MarginAmount"
    OrdAllocGrp = "OrdAllocGrp"
    PositionAmountData = "PositionAmountData"
    SettlDetails = "SettlDetails"
    SettlInstructionsData = "SettlInstructionsData"
    SettlParties = "SettlParties"
    SettlPtysSubGrp = "SettlPtysSubGrp"
    TradeAllocAmtGrp = "TradeAllocAmtGrp"
    TransactionAttributeGrp = "TransactionAttributeGrp"


class AllocationScenarioEnum(str, Enum):
    """
    Communication options by which an Initiator may convey allocation instructions to a Respondent.
    """
    PRE_ALLOCATED_ORDER = "PRE_ALLOCATED_ORDER"
    PRE_TRADE_ALLOCATION = "PRE_TRADE_ALLOCATION"
    POST_TRADE_ALLOCATION = "POST_TRADE_ALLOCATION"
    READY_TO_BOOK = "READY_TO_BOOK"


class AllocationStatusEnum(str, Enum):
    """
    AllocStatus(87) values used in allocation acknowledgement messages.
    """
    ACCEPTED = "ACCEPTED"
    BLOCK_LEVEL_REJECT = "BLOCK_LEVEL_REJECT"
    ACCOUNT_LEVEL_REJECT = "ACCOUNT_LEVEL_REJECT"
    RECEIVED_NOT_YET_PROCESSED = "RECEIVED_NOT_YET_PROCESSED"


class AllocationTransactionTypeEnum(str, Enum):
    """
    AllocTransType(71) values.
    """
    NEW = "NEW"
    REPLACE = "REPLACE"
    CANCEL = "CANCEL"


class PostTradeAllocationPricingMethodEnum(str, Enum):
    """
    Methods by which post-trade allocations may be computed.
    """
    AVERAGE_PRICE = "AVERAGE_PRICE"
    EXECUTED_PRICE = "EXECUTED_PRICE"


class TradeCaptureReportDirectionEnum(str, Enum):
    """
    Direction of a TradeCaptureReport relative to the marketplace.
    """
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"


class TradeCaptureReportUsageEnum(str, Enum):
    """
    Documented usages of the TradeCaptureReport(35=AE) message.
    """
    RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS = "RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS"
    RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES = "RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES"
    REPORTING_PRIVATELY_NEGOTIATED_TRADES = "REPORTING_PRIVATELY_NEGOTIATED_TRADES"
    REPORTING_FLOOR_OR_ROUTED_EXECUTIONS = "REPORTING_FLOOR_OR_ROUTED_EXECUTIONS"
    REQUEST_TRADE_CANCEL_OR_AMENDMENT = "REQUEST_TRADE_CANCEL_OR_AMENDMENT"


class TradeCaptureReportIdentifierRoleEnum(str, Enum):
    """
    Roles played by trade-capture-report identifier fields.
    """
    TRADE_REPORT_ID = "TRADE_REPORT_ID"
    TRADE_ID = "TRADE_ID"
    TRADE_REPORT_REF_ID = "TRADE_REPORT_REF_ID"
    SECONDARY_TRADE_ID = "SECONDARY_TRADE_ID"


class RegistrationTransactionTypeEnum(str, Enum):
    """
    RegistTransType(514) values.
    """
    NEW = "NEW"
    REPLACE = "REPLACE"
    CANCEL = "CANCEL"


class RegistrationStatusEnum(str, Enum):
    """
    RegistStatus(506) values.
    """
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    HELD = "HELD"
    REMINDER = "REMINDER"


class SettlementInstructionModeEnum(str, Enum):
    """
    SettlInstMode(160) values relevant in Post-Trade.
    """
    STANDING_INSTRUCTIONS = "STANDING_INSTRUCTIONS"
    SPECIFIC_ORDER = "SPECIFIC_ORDER"
    REQUEST_REJECT = "REQUEST_REJECT"


class SettlementObligationModeEnum(str, Enum):
    """
    SettlObligMode(1159) values.
    """
    PRELIMINARY = "PRELIMINARY"
    FINAL = "FINAL"


class PositionMaintenanceActionEnum(str, Enum):
    """
    PosMaintAction(712) values.
    """
    NEW = "NEW"
    REPLACE = "REPLACE"
    CANCEL = "CANCEL"
    REVERSE = "REVERSE"


class ClearingServiceForPositionManagementEnum(str, Enum):
    """
    Business functions invokable via the Position Management Clearing Services.
    """
    POSITION_CHANGE_SUBMISSION = "POSITION_CHANGE_SUBMISSION"
    POSITION_ADJUSTMENT = "POSITION_ADJUSTMENT"
    EXERCISE_NOTICE = "EXERCISE_NOTICE"
    ABANDONMENT_NOTICE = "ABANDONMENT_NOTICE"
    MARGIN_DISPOSITION = "MARGIN_DISPOSITION"
    POSITION_PLEDGE = "POSITION_PLEDGE"
    REQUEST_FOR_POSITION = "REQUEST_FOR_POSITION"


class ClearingServiceForPostTradeProcessingEnum(str, Enum):
    """
    Message-format families used by the Post-Trade Processing Clearing Services.
    """
    ETP = "ETP"
    GIVE_UP = "GIVE_UP"
    EXCHANGE_FOR_PHYSICAL = "EXCHANGE_FOR_PHYSICAL"
    AVERAGE_PRICE_SYSTEM = "AVERAGE_PRICE_SYSTEM"
    MUTUAL_OFFSET_SYSTEM = "MUTUAL_OFFSET_SYSTEM"
    TRADE_ENTRY_EDIT = "TRADE_ENTRY_EDIT"


class CollateralManagementUsageEnum(str, Enum):
    """
    Documented uses of the Collateral Management messages.
    """
    SECURITIES_FINANCING_COLLATERALIZATION = "SECURITIES_FINANCING_COLLATERALIZATION"
    CLEARING_HOUSE_COLLATERALIZATION = "CLEARING_HOUSE_COLLATERALIZATION"


class CollateralAssignmentPurposeEnum(str, Enum):
    """
    Purposes for which a CollateralAssignment may be sent.
    """
    ASSIGN_INITIAL_COLLATERAL = "ASSIGN_INITIAL_COLLATERAL"
    REPLENISH_COLLATERAL = "REPLENISH_COLLATERAL"
    REPLACE_OR_SUBSTITUTE_COLLATERAL = "REPLACE_OR_SUBSTITUTE_COLLATERAL"


class AllocationRoleEnum(str, Enum):
    """
    Role labels used throughout the Allocation category prose to designate the sender and receiver of an AllocationInstruction.
    """
    INITIATOR = "INITIATOR"
    RESPONDENT = "RESPONDENT"


class MatchStatusEnum(str, Enum):
    """
    MatchStatus(573) values referenced in Post-Trade prose.
    """
    COMPARED_MATCHED_OR_AFFIRMED = "COMPARED_MATCHED_OR_AFFIRMED"
    UNCOMPARED_UNMATCHED_OR_UNAFFIRMED = "UNCOMPARED_UNMATCHED_OR_UNAFFIRMED"


class PostTradeLayoutRowKindEnum(str, Enum):
    """
    Discriminator for a row in a Post-Trade message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal "Component" in the Tag column).
    """
    FIELD = "FIELD"
    COMPONENT = "COMPONENT"


class InfrastructureCategoryEnum(str, Enum):
    """
    The four message categories of the FIX Latest Infrastructure business area. Subset of MessageCategoryEnum.
    """
    BUSINESS_MESSAGE_REJECTS = "BUSINESS_MESSAGE_REJECTS"
    NETWORK_STATUS_COMMUNICATION = "NETWORK_STATUS_COMMUNICATION"
    USER_MANAGEMENT = "USER_MANAGEMENT"
    APPLICATION_SEQUENCING = "APPLICATION_SEQUENCING"


class InfrastructureComponentName(str, Enum):
    """
    Names of the components defined in the Infrastructure business-area chapter. None of these are shared across categories within the area; footnotes 1–4 record that four of them were historically declared as common components.
    """
    ApplIDReportGrp = "ApplIDReportGrp"
    ApplIDRequestAckGrp = "ApplIDRequestAckGrp"
    ApplIDRequestGrp = "ApplIDRequestGrp"
    CompIDReqGrp = "CompIDReqGrp"
    CompIDStatGrp = "CompIDStatGrp"
    ThrottleMsgTypeGrp = "ThrottleMsgTypeGrp"
    ThrottleParamsGrp = "ThrottleParamsGrp"
    UsernameGrp = "UsernameGrp"


class BusinessRejectReasonEnum(str, Enum):
    """
    Permissible values of BusinessRejectReason(380) on the BusinessMessageReject(35=j) message.
    """
    OTHER = "OTHER"
    UNKNOWN_ID = "UNKNOWN_ID"
    UNKNOWN_SECURITY = "UNKNOWN_SECURITY"
    UNSUPPORTED_MESSAGE_TYPE = "UNSUPPORTED_MESSAGE_TYPE"
    APPLICATION_NOT_AVAILABLE = "APPLICATION_NOT_AVAILABLE"
    CONDITIONALLY_REQUIRED_FIELD_MISSING = "CONDITIONALLY_REQUIRED_FIELD_MISSING"
    NOT_AUTHORISED = "NOT_AUTHORISED"
    DELIVER_TO_FIRM_NOT_AVAILABLE = "DELIVER_TO_FIRM_NOT_AVAILABLE"
    THROTTLE_LIMIT_EXCEEDED = "THROTTLE_LIMIT_EXCEEDED"
    THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT = "THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT"
    THROTTLED_MESSAGES_REJECTED_ON_REQUEST = "THROTTLED_MESSAGES_REJECTED_ON_REQUEST"
    INVALID_PRICE_INCREMENT = "INVALID_PRICE_INCREMENT"


class NetworkStatusScenarioEnum(str, Enum):
    """
    Network Status Communication usage scenarios documented in the chapter (Scenario A: hub-and-spoke; Scenario B: global brokerage region availability).
    """
    SCENARIO_A = "SCENARIO_A"
    SCENARIO_B = "SCENARIO_B"


class ApplicationMessageReportTypeEnum(str, Enum):
    """
    Documented uses of ApplicationMessageReport(35=BY) selected via ApplReportType(1426).
    """
    RESET = "RESET"
    LAST_MESSAGE = "LAST_MESSAGE"
    KEEP_ALIVE = "KEEP_ALIVE"
    RESEND_COMPLETED = "RESEND_COMPLETED"


class NetworkRequestTypeEnum(str, Enum):
    """
    Values of NetworkRequestType(935) explicitly cited in the NetworkCounterpartySystemStatusRequest(35=BC) prose.
    """
    SNAPSHOT = "SNAPSHOT"
    STOP_SUBSCRIBING = "STOP_SUBSCRIBING"


class StandardResponseDirectionEnum(str, Enum):
    """
    Direction of a "Standard Response" mapping — which area the requesting message belongs to.
    """
    PRE_TRADE = "PRE_TRADE"
    TRADE = "TRADE"
    POST_TRADE = "POST_TRADE"


class BusinessMessageReferenceDirectionEnum(str, Enum):
    """
    Direction of an "application message reference" key-field mapping — which area the referenced message belongs to.
    """
    PRE_TRADE = "PRE_TRADE"
    TRADE = "TRADE"
    POST_TRADE = "POST_TRADE"


class InfrastructureGlobalComponentName(str, Enum):
    """
    Names of the Global Components (declared in the FIX Latest "Global Components" page) that the Infrastructure business-area messages explicitly reference. Global Components are reusable component blocks used across two or more business areas.
    """
    ApplicationSequenceControl = "ApplicationSequenceControl"


class ApplicationSequenceControlFieldName(str, Enum):
    """
    Tags contributed by the ApplicationSequenceControl global component (used by Application Sequencing messages and by all FIX messages representing reports).
    """
    ApplID = "ApplID"
    ApplSeqNum = "ApplSeqNum"
    ApplLastSeqNum = "ApplLastSeqNum"
    ApplResendFlag = "ApplResendFlag"


class InfrastructureLayoutRowKindEnum(str, Enum):
    """
    Discriminator for a row in an Infrastructure message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal "Component" in the Tag column).
    """
    FIELD = "FIELD"
    COMPONENT = "COMPONENT"



class FIXIntroduction(ConfiguredBaseModel):
    """
    Container for the structural elements of the FIX Latest Introduction section. Tree root for instance data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['FIX Latest Introduction'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'related_mappings': ['fix_orchestra:Repository'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/introduction-to-fix-protocol/'],
         'tree_root': True})

    published_version: Optional[str] = Field(default=None, description="""Version stamp from the document header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'slot_uri': 'schema:version'} })
    published_date: Optional[date] = Field(default=None, description="""Publication date of the document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction'], 'slot_uri': 'dcterms:issued'} })
    publisher: Optional[str] = Field(default="FIX Global Technical Committee", description="""Publishing body of the FIX Latest specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'ifabsent': 'string(FIX Global Technical Committee)',
         'slot_uri': 'dcterms:publisher'} })
    preface: Optional[str] = Field(default=None, description="""The Preface text of the specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })
    introduction_text: Optional[str] = Field(default=None, description="""The Introduction prose section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })
    utc_leap_seconds_note: Optional[str] = Field(default=None, description="""Prose note on UTC leap-second handling for UTCTimestamp.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction'],
         'see_also': ['https://maia.usno.navy.mil/information/what-is-a-leap-second']} })
    about_fpl: Optional[FIXProtocolLimited] = Field(default=None, description="""Information about FIX Protocol Limited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })
    standards: Optional[list[FIXFamilyStandard]] = Field(default=None, description="""The FIX Family of Standards.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })
    extension_packs: Optional[list[ExtensionPack]] = Field(default=None, description="""The list of Extension Packs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })
    datatypes: Optional[list[FIXDatatype]] = Field(default=None, description="""FIX Protocol datatype definitions and value spaces.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })
    business_areas: Optional[list[BusinessArea]] = Field(default=None, description="""Top-level business areas of FIX Latest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })
    global_components: Optional[list[GlobalComponent]] = Field(default=None, description="""Global Components defined in the Introduction.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })
    udf_ranges: Optional[list[UDFTagRange]] = Field(default=None, description="""Reserved ranges of user-defined-field tag numbers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })
    product_coverage: Optional[list[ProductCoverage]] = Field(default=None, description="""Product/asset classes covered by FIX at the application layer.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction']} })


class FIXProtocolLimited(ConfiguredBaseModel):
    """
    The organization that maintains the FIX Protocol specification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['FPL', 'FIX Trading Community'],
         'class_uri': 'fix_base:FIXProtocolLimited',
         'close_mappings': ['iso27001:Organization'],
         'exact_mappings': ['schema:Organization'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['governance'],
         'related_mappings': ['common_domain_model:Organization'],
         'see_also': ['https://www.fixtrading.org/about-fix/corporate-structure/'],
         'slot_usage': {'brand_name': {'ifabsent': 'string(FIX Trading Community)',
                                       'name': 'brand_name'},
                        'legal_name': {'ifabsent': 'string(FIX Protocol Limited)',
                                       'name': 'legal_name'},
                        'website': {'ifabsent': 'string(https://www.fixtrading.org)',
                                    'name': 'website'}}})

    brand_name: Optional[str] = Field(default="FIX Trading Community", description="""Brand name used by the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited'],
         'ifabsent': 'string(FIX Trading Community)'} })
    legal_name: Optional[str] = Field(default="FIX Protocol Limited", description="""Legal name of the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited'],
         'ifabsent': 'string(FIX Protocol Limited)',
         'slot_uri': 'schema:legalName'} })
    website: Optional[str] = Field(default="https://www.fixtrading.org", description="""Main website URL of the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited'],
         'ifabsent': 'string(https://www.fixtrading.org)',
         'slot_uri': 'schema:url'} })
    member_firms_url: Optional[str] = Field(default=None, description="""URL listing current FPL Member firms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited']} })
    working_groups_url: Optional[str] = Field(default=None, description="""URL listing currently active FPL Working Groups.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited']} })
    committees_url: Optional[str] = Field(default=None, description="""URL listing Product and Regional Committees.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited']} })
    member_types: Optional[list[FPLMemberType]] = Field(default=None, description="""Organization categories represented in FPL membership.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited']} })
    governance_bodies: Optional[list[FPLCommitteeRole]] = Field(default=None, description="""High-level governance bodies that represent FPL.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited']} })
    product_committees: Optional[list[FPLProductGroup]] = Field(default=None, description="""Global Product Committees maintained by FPL.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited']} })
    regional_committees: Optional[list[FPLRegion]] = Field(default=None, description="""Regional Committees maintained by FPL.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXProtocolLimited']} })


class FIXFamilyStandard(ConfiguredBaseModel):
    """
    A member standard of the FIX Family of Standards.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:FIXFamilyStandard',
         'exact_mappings': ['schema:Specification'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'related_mappings': ['fix_orchestra:ProtocolEnum'],
         'see_also': ['https://www.fixtrading.org/standards/'],
         'slot_usage': {'acronym': {'description': 'Short acronym used to refer to the '
                                                   'standard.',
                                    'name': 'acronym'},
                        'layer': {'name': 'layer', 'required': True}}})

    id: str = Field(default=..., description="""Unique identifier (CURIE or local name) of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard'],
         'exact_mappings': ['schema:identifier', 'dcterms:identifier']} })
    name: str = Field(default=..., description="""Display name of the element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    acronym: Optional[str] = Field(default=None, description="""Short acronym used to refer to the standard.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard'], 'slot_uri': 'schema:alternateName'} })
    see_also: Optional[list[str]] = Field(default=None, description="""Related external resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard'], 'slot_uri': 'rdfs:seeAlso'} })
    layer: StandardLayer = Field(default=..., description="""The layer the standard belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard']} })
    version: Optional[str] = Field(default=None, description="""Version of the standard, if applicable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard'], 'slot_uri': 'schema:version'} })
    session_profile: Optional[SessionProtocolName] = Field(default=None, description="""Name of the session profile for session-layer variants.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard']} })
    encoding_name: Optional[StandardEncodingName] = Field(default=None, description="""Named encoding, when layer is ENCODING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard']} })


class ExtensionPack(ConfiguredBaseModel):
    """
    A unit of change to FIX Latest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['EP'],
         'annotations': {'wire_tag': {'tag': 'wire_tag',
                                      'value': {'field_name': 'ApplExtID',
                                                'field_number': 1156}}},
         'class_uri': 'fix_base:ExtensionPack',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'related_mappings': ['fix_orchestra:Repository',
                              'iso27001:DocumentedInformation'],
         'see_also': ['https://www.fixtrading.org/standards/extension-packs/'],
         'slot_usage': {'number': {'identifier': True,
                                   'name': 'number',
                                   'required': True},
                        'title': {'description': 'Short descriptive title.',
                                  'name': 'title',
                                  'required': True}}})

    number: int = Field(default=..., description="""Sequential identifier of the Extension Pack.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack']} })
    title: str = Field(default=..., description="""Short descriptive title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'slot_uri': 'dcterms:title'} })
    size: Optional[ExtensionPackSize] = Field(default=None, description="""Qualitative size indicator (XXS..XXL).""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack']} })
    enhancement_summary: Optional[str] = Field(default=None, description="""Narrative summary of what the EP introduces.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack']} })
    applies_to_session_layer_only: Optional[bool] = Field(default=False, description="""True when the EP applies only to the FIX Session Layer.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack'], 'ifabsent': 'string(False)'} })
    applies_to_fixml_only: Optional[bool] = Field(default=False, description="""True when the EP applies only to the FIXML encoding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack'], 'ifabsent': 'string(False)'} })


class FIXDatatype(ConfiguredBaseModel):
    """
    A FIX Protocol datatype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:FIXDatatype',
         'close_mappings': ['fix_sbe:SemanticAttributes'],
         'exact_mappings': ['fix_orchestra:Datatype'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['datatypes'],
         'see_also': ['https://www.iso.org/standard/39479.html'],
         'slot_usage': {'datatype_name': {'identifier': True,
                                          'name': 'datatype_name',
                                          'required': True},
                        'definition': {'name': 'definition', 'required': True}}})

    datatype_name: FIXDatatypeName = Field(default=..., description="""Canonical FIX datatype name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    definition: str = Field(default=..., description="""Prose definition of the datatype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    value_space: Optional[list[ISO11404ValueSpace]] = Field(default=None, description="""ISO/IEC 11404:2007 GPD value space assigned to the datatype.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    value_space_notes: Optional[str] = Field(default=None, description="""Additional value-space constraints.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    deprecated_for_new_designs: Optional[bool] = Field(default=False, description="""True for datatypes not permitted in new designs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype'], 'ifabsent': 'string(False)'} })
    external_code_set: Optional[str] = Field(default=None, description="""Reference standard for datatypes backed by an external code set.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype'], 'slot_uri': 'dcterms:conformsTo'} })
    time_unit: Optional[list[TimePrecision]] = Field(default=None, description="""Time-unit precision for time-bearing datatypes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    radix: Optional[int] = Field(default=None, description="""Numeric radix for scaled value-space datatypes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    repertoire: Optional[str] = Field(default=None, description="""Character repertoire for character/string datatypes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    index_lower_bound: Optional[int] = Field(default=None, description="""Inclusive lower bound of a bounded-array index.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    index_upper_bound: Optional[int] = Field(default=None, description="""Inclusive upper bound of a bounded-array index.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    minimum_value: Optional[int] = Field(default=None, description="""Inclusive lower bound on the integer value space.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    maximum_value: Optional[int] = Field(default=None, description="""Inclusive upper bound on the integer value space.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })
    footnote_numbers: Optional[list[int]] = Field(default=None, description="""Footnote indicators attached to a datatype row.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXDatatype']} })


class BusinessArea(ConfiguredBaseModel):
    """
    A top-level business area of the FIX Latest specification.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:BusinessArea',
         'close_mappings': ['fix_orchestra:CategoryType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['organization'],
         'slot_usage': {'area': {'identifier': True, 'name': 'area', 'required': True},
                        'description': {'description': 'Description of the area.',
                                        'name': 'description'},
                        'title': {'description': 'Display title of the area.',
                                  'name': 'title'}}})

    area: BusinessAreaEnum = Field(default=..., description="""Identity of the business area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BusinessArea',
                       'PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'slot_uri': 'schema:identifier'} })
    title: Optional[str] = Field(default=None, description="""Display title of the area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Description of the area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    categories: Optional[list[MessageCategory]] = Field(default=None, description="""Message categories defined within a business area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BusinessArea']} })


class MessageCategory(ConfiguredBaseModel):
    """
    A message category within a business area.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:MessageCategory',
         'close_mappings': ['fix_orchestra:CategoryType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['organization'],
         'slot_usage': {'business_area': {'name': 'business_area', 'required': True},
                        'category': {'description': 'Identity of the message category.',
                                     'identifier': True,
                                     'name': 'category',
                                     'required': True},
                        'description': {'description': 'Description of the category.',
                                        'name': 'description'},
                        'title': {'description': 'Display title of the category.',
                                  'name': 'title'}}})

    category: MessageCategoryEnum = Field(default=..., description="""Identity of the message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    title: Optional[str] = Field(default=None, description="""Display title of the category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Description of the category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    business_area: BusinessAreaEnum = Field(default=..., description="""Business area the element belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory', 'CommonComponent', 'SpecificComponent']} })
    messages: Optional[list[Message]] = Field(default=None, description="""Messages defined within the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })


class Field(ConfiguredBaseModel):
    """
    A FIX field — a uniquely tagged data element with a FIX datatype.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:Field',
         'exact_mappings': ['fix_orchestra:FieldType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'related_mappings': ['fix_sbe:SemanticAttributes'],
         'slot_usage': {'datatype': {'name': 'datatype', 'required': True},
                        'description': {'description': "Description of the field's "
                                                       'purpose.',
                                        'name': 'description'},
                        'field_name': {'name': 'field_name', 'required': True},
                        'tag': {'identifier': True, 'name': 'tag', 'required': True}}})

    tag: int = Field(default=..., description="""Numeric tag of the field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Field']} })
    field_name: str = Field(default=..., description="""PascalCase name of the field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Field'], 'slot_uri': 'schema:name'} })
    datatype: FIXDatatypeName = Field(default=..., description="""FIX datatype of the field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Field']} })
    description: Optional[str] = Field(default=None, description="""Description of the field's purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    requirement: Optional[FieldRequirement] = Field(default=None, description="""Required-status of the field within the enclosing context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Field']} })
    is_user_defined: Optional[bool] = Field(default=False, description="""True when the field is a User Defined Field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Field'], 'ifabsent': 'string(False)'} })


class Component(ConfiguredBaseModel):
    """
    A FIX component — a named set of related fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'fix_base:Component',
         'close_mappings': ['fix_orchestra:ComponentType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'slot_usage': {'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'required': True},
                        'description': {'description': 'Description of the component.',
                                        'name': 'description'},
                        'scope': {'name': 'scope', 'required': True}}})

    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    scope: ComponentScope = Field(default=..., description="""Sharing scope of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })
    is_repeating_group: Optional[bool] = Field(default=False, description="""True when the component is a repeating group.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'ifabsent': 'string(False)'} })
    fields: Optional[list[Field]] = Field(default=None, description="""Fields directly contained by the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Message']} })
    nested_components: Optional[list[str]] = Field(default=None, description="""Components nested within this component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })


class GlobalComponent(Component):
    """
    A component shared by messages of two or more business areas.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:GlobalComponent',
         'close_mappings': ['fix_orchestra:ComponentType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'slot_usage': {'component_group': {'name': 'component_group',
                                            'required': True},
                        'scope': {'ifabsent': 'string(GLOBAL)', 'name': 'scope'}}})

    component_group: ComponentGroup = Field(default=..., description="""Thematic group under which the component is presented.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GlobalComponent']} })
    applies_to_instrument: Optional[bool] = Field(default=None, description="""Applicable at the Instrument level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GlobalComponent']} })
    applies_to_leg: Optional[bool] = Field(default=None, description="""Applicable at the InstrumentLeg level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GlobalComponent']} })
    applies_to_underlying: Optional[bool] = Field(default=None, description="""Applicable at the UnderlyingInstrument level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GlobalComponent']} })
    conceptually_identical_to: Optional[list[str]] = Field(default=None, description="""Names of other components conceptually identical to this one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GlobalComponent']} })
    gc_id: Optional[int] = Field(default=None, description="""Numeric component identifier extracted from the FIX Latest \"Global Components\" page anchor ID (e.g. \"comp1057-1\" → 1057). Stable across Extension Packs and shared with the FIX Orchestra repository.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['GlobalComponent']} })
    gc_referenced_in: Optional[list[GlobalComponentBusinessAreaEnum]] = Field(default=None, description="""FIX business areas whose messages embed the Global Component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GlobalComponent']} })
    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    scope: ComponentScope = Field(default=ComponentScope.GLOBAL, description="""Sharing scope of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'ifabsent': 'string(GLOBAL)'} })
    is_repeating_group: Optional[bool] = Field(default=False, description="""True when the component is a repeating group.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'ifabsent': 'string(False)'} })
    fields: Optional[list[Field]] = Field(default=None, description="""Fields directly contained by the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Message']} })
    nested_components: Optional[list[str]] = Field(default=None, description="""Components nested within this component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })


class CommonComponent(Component):
    """
    A component used only by messages within a single business area.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:CommonComponent',
         'close_mappings': ['fix_orchestra:ComponentType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'slot_usage': {'business_area': {'name': 'business_area', 'required': True},
                        'scope': {'ifabsent': 'string(COMMON)', 'name': 'scope'}}})

    business_area: BusinessAreaEnum = Field(default=..., description="""Business area the element belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory', 'CommonComponent', 'SpecificComponent']} })
    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    scope: ComponentScope = Field(default=ComponentScope.COMMON, description="""Sharing scope of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'ifabsent': 'string(COMMON)'} })
    is_repeating_group: Optional[bool] = Field(default=False, description="""True when the component is a repeating group.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'ifabsent': 'string(False)'} })
    fields: Optional[list[Field]] = Field(default=None, description="""Fields directly contained by the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Message']} })
    nested_components: Optional[list[str]] = Field(default=None, description="""Components nested within this component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })


class SpecificComponent(Component):
    """
    A component used only by messages within a single category.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:SpecificComponent',
         'close_mappings': ['fix_orchestra:ComponentType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'slot_usage': {'business_area': {'name': 'business_area', 'required': True},
                        'category': {'name': 'category', 'required': True},
                        'scope': {'ifabsent': 'string(SPECIFIC)', 'name': 'scope'}}})

    business_area: BusinessAreaEnum = Field(default=..., description="""Business area the element belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory', 'CommonComponent', 'SpecificComponent']} })
    category: MessageCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    scope: ComponentScope = Field(default=ComponentScope.SPECIFIC, description="""Sharing scope of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'ifabsent': 'string(SPECIFIC)'} })
    is_repeating_group: Optional[bool] = Field(default=False, description="""True when the component is a repeating group.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component'], 'ifabsent': 'string(False)'} })
    fields: Optional[list[Field]] = Field(default=None, description="""Fields directly contained by the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Message']} })
    nested_components: Optional[list[str]] = Field(default=None, description="""Components nested within this component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component']} })


class Message(ConfiguredBaseModel):
    """
    A FIX application message.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:Message',
         'exact_mappings': ['fix_orchestra:MessageType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'slot_usage': {'description': {'description': "Description of the message's "
                                                       'purpose.',
                                        'name': 'description'},
                        'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'identifier': True,
                                     'name': 'msg_type',
                                     'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the message's purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    category: Optional[MessageCategoryEnum] = Field(default=None, description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    fields: Optional[list[Field]] = Field(default=None, description="""Fields directly contained by the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component', 'Message']} })
    components: Optional[list[str]] = Field(default=None, description="""Components referenced by the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class UDFTagRange(ConfiguredBaseModel):
    """
    A reserved range of tag numbers for User Defined Fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_base:UDFTagRange',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-base',
         'in_subset': ['introduction'],
         'slot_usage': {'description': {'description': "Notes on the range's intended "
                                                       'use.',
                                        'name': 'description'},
                        'high_tag': {'description': 'Upper bound of the tag range. '
                                                    'Required for all ``usage`` values '
                                                    'except ``GTC_RESERVED`` (which is '
                                                    'open-ended, 50000+). Downstream '
                                                    'validators should enforce this; '
                                                    'the constraint cannot be '
                                                    "expressed here because LinkML's "
                                                    '``equals_string`` operator only '
                                                    'accepts string-ranged slots and '
                                                    '``usage`` is an enum.',
                                     'name': 'high_tag'},
                        'low_tag': {'name': 'low_tag', 'required': True},
                        'range_id': {'identifier': True,
                                     'name': 'range_id',
                                     'required': True},
                        'usage': {'name': 'usage', 'required': True}}})

    range_id: str = Field(default=..., description="""Identifier of the range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UDFTagRange']} })
    low_tag: int = Field(default=..., description="""Inclusive lower bound of the range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UDFTagRange']} })
    high_tag: Optional[int] = Field(default=None, description="""Upper bound of the tag range. Required for all ``usage`` values except ``GTC_RESERVED`` (which is open-ended, 50000+). Downstream validators should enforce this; the constraint cannot be expressed here because LinkML's ``equals_string`` operator only accepts string-ranged slots and ``usage`` is an enum.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UDFTagRange']} })
    usage: UDFTagRangeUsage = Field(default=..., description="""Usage policy assigned to the range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UDFTagRange']} })
    description: Optional[str] = Field(default=None, description="""Notes on the range's intended use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    requires_registration: Optional[bool] = Field(default=False, description="""True when tags in the range must be registered.""", json_schema_extra = { "linkml_meta": {'domain_of': ['UDFTagRange'], 'ifabsent': 'string(False)'} })


class PreTradeBusinessArea(ConfiguredBaseModel):
    """
    Tree-root container for the Pre-Trade business area of FIX Latest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Pre-Trade'],
         'class_uri': 'fix_pre_trade:PreTradeBusinessArea',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/business-area-pre-trade/'],
         'slot_usage': {'area': {'ifabsent': 'string(PRE_TRADE)',
                                 'name': 'area',
                                 'required': True},
                        'components': {'description': 'Area-wide pre-trade components '
                                                      'table.',
                                       'inlined': True,
                                       'inlined_as_list': True,
                                       'name': 'components',
                                       'range': 'PreTradeComponentEntry'},
                        'messages': {'description': 'Area-wide pre-trade messages '
                                                    'table.',
                                     'name': 'messages',
                                     'range': 'PreTradeMessageEntry'},
                        'publisher': {'ifabsent': 'string(FIX Global Technical '
                                                  'Committee)',
                                      'name': 'publisher'},
                        'title': {'ifabsent': 'string(Business Area Pre-Trade)',
                                  'name': 'title'}},
         'tree_root': True})

    area: BusinessAreaEnum = Field(default=BusinessAreaEnum.PRE_TRADE, description="""Identity of the business area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BusinessArea',
                       'PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'ifabsent': 'string(PRE_TRADE)',
         'slot_uri': 'schema:identifier'} })
    title: Optional[str] = Field(default="Business Area Pre-Trade", description="""Display title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'ifabsent': 'string(Business Area Pre-Trade)',
         'slot_uri': 'dcterms:title'} })
    published_version: Optional[str] = Field(default=None, description="""Version stamp from the document header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'slot_uri': 'schema:version'} })
    publisher: Optional[str] = Field(default="FIX Global Technical Committee", description="""Publishing body of the FIX Latest specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'ifabsent': 'string(FIX Global Technical Committee)',
         'slot_uri': 'dcterms:publisher'} })
    introduction: Optional[str] = Field(default=None, description="""Prose introduction of the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea']} })
    diagram_conventions: Optional[str] = Field(default=None, description="""Sentence describing diagram conventions used in the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    messages_overview_note: Optional[str] = Field(default=None, description="""Intro prose of the area-wide Messages sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    messages: Optional[list[PreTradeMessageEntry]] = Field(default=None, description="""Area-wide pre-trade messages table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    components_overview_note: Optional[str] = Field(default=None, description="""Intro prose of the area-wide Components sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    components: Optional[list[PreTradeComponentEntry]] = Field(default=None, description="""Area-wide pre-trade components table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    common_components: Optional[list[PreTradeCommonComponentName]] = Field(default=None, description="""Common Components declared at the top of the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea']} })
    common_component_details: Optional[list[CommonComponentDetail]] = Field(default=None, description="""Per-common-component descriptions from the chapter's final section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea']} })
    footnotes: Optional[list[ComponentTableFootnote]] = Field(default=None, description="""Footnotes attached to the area-wide components table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea']} })
    category_sections: Optional[list[PreTradeCategorySection]] = Field(default=None, description="""Per-category sub-sections of the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea']} })
    referenced_global_components: Optional[list[str]] = Field(default=None, description="""Names of Global Components from the FIX Latest \"Global Components\" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })


class PreTradeMessageEntry(ConfiguredBaseModel):
    """
    One row of the area-wide pre-trade messages table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_pre_trade:PreTradeMessageEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade_organization'],
         'slot_usage': {'category': {'name': 'category',
                                     'range': 'PreTradeCategoryEnum',
                                     'required': True},
                        'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'identifier': True,
                                     'name': 'msg_type',
                                     'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    category: PreTradeCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class PreTradeComponentEntry(ConfiguredBaseModel):
    """
    One row of the area-wide pre-trade components table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_pre_trade:PreTradeComponentEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade_organization'],
         'slot_usage': {'category': {'description': 'Category the component is listed '
                                                    'under. Common Components are '
                                                    'listed under the synthetic '
                                                    '"Common Components" value.',
                                     'name': 'category',
                                     'range': 'string',
                                     'required': True},
                        'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'required': True},
                        'is_common': {'ifabsent': 'string(False)', 'name': 'is_common'},
                        'repetition': {'name': 'repetition', 'required': True}}})

    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    repetition: ComponentRepetition = Field(default=..., description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentDetail']} })
    category: str = Field(default=..., description="""Category the component is listed under. Common Components are listed under the synthetic \"Common Components\" value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    is_common: Optional[bool] = Field(default=False, description="""True when the component is declared as a Common Component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry', 'PostTradeComponentEntry'],
         'ifabsent': 'string(False)'} })
    footnote_number: Optional[int] = Field(default=None, description="""Footnote indicator on a component-table row.""", ge=1, le=25, json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote']} })


class ComponentTableFootnote(ConfiguredBaseModel):
    """
    A footnote on the area-wide components table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_pre_trade:ComponentTableFootnote',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade_organization'],
         'slot_usage': {'component_name': {'name': 'component_name', 'required': True},
                        'footnote_number': {'identifier': True,
                                            'name': 'footnote_number',
                                            'required': True},
                        'introduced_in': {'name': 'introduced_in', 'required': True},
                        'sole_category': {'name': 'sole_category', 'required': True}}})

    footnote_number: int = Field(default=..., description="""Footnote indicator on a component-table row.""", ge=1, le=25, json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote']} })
    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    introduced_in: str = Field(default=..., description="""FIX version or Extension Pack that introduced the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentTableFootnote',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentTableFootnote']} })
    sole_category: PreTradeCategoryEnum = Field(default=..., description="""Single category that actually uses the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentTableFootnote']} })
    text: Optional[str] = Field(default=None, description="""Footnote text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentTableFootnote',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentTableFootnote']} })


class PreTradeCategorySection(ConfiguredBaseModel):
    """
    A per-category sub-section of the Pre-Trade chapter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_pre_trade:PreTradeCategorySection',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade'],
         'slot_usage': {'category': {'identifier': True,
                                     'name': 'category',
                                     'range': 'PreTradeCategoryEnum',
                                     'required': True},
                        'messages': {'description': 'Messages defined in this '
                                                    'category.',
                                     'name': 'messages',
                                     'range': 'PreTradeMessageDetail'}}})

    category: PreTradeCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    title: Optional[str] = Field(default=None, description="""Display title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    quote_models: Optional[list[QuoteModelEnum]] = Field(default=None, description="""Quoting business models referenced in the Quotation / Negotiation category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeCategorySection']} })
    message_groups: Optional[list[MessageGroup]] = Field(default=None, description="""Purpose-grouped message descriptions inside a category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeCategorySection']} })
    messages: Optional[list[PreTradeMessageDetail]] = Field(default=None, description="""Messages defined in this category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    category_components_note: Optional[str] = Field(default=None, description="""Intro prose of a category's Components sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeCategorySection',
                       'PostTradeCategorySection',
                       'InfrastructureCategorySection']} })
    category_specific_components: Optional[list[PreTradeComponentDetail]] = Field(default=None, description="""Components used exclusively by messages within a category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeCategorySection']} })


class PreTradeMessageDetail(ConfiguredBaseModel):
    """
    Per-category message description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_pre_trade:PreTradeMessageDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade'],
         'slot_usage': {'description': {'description': "Description of the message's "
                                                       'purpose and usage.',
                                        'name': 'description'},
                        'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'identifier': True,
                                     'name': 'msg_type',
                                     'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the message's purpose and usage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:url'} })
    pre_layout_rows: Optional[list[PreTradeLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Pre-Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class PreTradeComponentDetail(ConfiguredBaseModel):
    """
    Per-category component description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_pre_trade:PreTradeComponentDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade'],
         'slot_usage': {'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'required': True},
                        'description': {'description': "Description of the component's "
                                                       'purpose.',
                                        'name': 'description'}}})

    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    repetition: Optional[ComponentRepetition] = Field(default=None, description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentDetail']} })
    description: Optional[str] = Field(default=None, description="""Description of the component's purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:url'} })
    pre_layout_rows: Optional[list[PreTradeLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Pre-Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail']} })


class MessageGroup(ConfiguredBaseModel):
    """
    Purpose-grouped sub-section inside a category's Messages section.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_pre_trade:MessageGroup',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade'],
         'slot_usage': {'description': {'description': 'Description of the '
                                                       "purpose-group's role within "
                                                       'the category.',
                                        'name': 'description'},
                        'group_title': {'identifier': True,
                                        'name': 'group_title',
                                        'required': True},
                        'messages': {'description': 'Messages bundled under the '
                                                    'purpose-group heading.',
                                     'name': 'messages',
                                     'range': 'PreTradeMessageDetail',
                                     'required': True}}})

    group_title: str = Field(default=..., description="""Purpose-group heading inside a category's Messages sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageGroup', 'PostTradeMessageGroup'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the purpose-group's role within the category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    messages: list[PreTradeMessageDetail] = Field(default=..., description="""Messages bundled under the purpose-group heading.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })


class CommonComponentDetail(ConfiguredBaseModel):
    """
    Per-common-component description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_pre_trade:CommonComponentDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade'],
         'slot_usage': {'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'range': 'PreTradeCommonComponentName',
                                           'required': True},
                        'description': {'description': 'Description of the common '
                                                       "component's purpose.",
                                        'name': 'description'}}})

    component_name: PreTradeCommonComponentName = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    repetition: Optional[ComponentRepetition] = Field(default=None, description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentDetail']} })
    description: Optional[str] = Field(default=None, description="""Description of the common component's purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:url'} })
    pre_layout_rows: Optional[list[PreTradeLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Pre-Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail']} })


class PreTradeLayoutRow(ConfiguredBaseModel):
    """
    One row of the layout table published in the Pre-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_pre_trade:PreTradeLayoutRow',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade',
         'in_subset': ['pre_trade'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/pre-trade-appendix/'],
         'slot_usage': {'pre_layout_element_name': {'name': 'pre_layout_element_name',
                                                    'required': True},
                        'pre_layout_kind': {'name': 'pre_layout_kind',
                                            'required': True}}})

    pre_layout_kind: PreTradeLayoutRowKindEnum = Field(default=..., description="""Row kind — either a FIX field (numeric Tag) or an embedded component (literal \"Component\" in the Tag column of the source table).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeLayoutRow']} })
    pre_layout_field_tag: Optional[int] = Field(default=None, description="""FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeLayoutRow']} })
    pre_layout_element_name: str = Field(default=..., description="""Element name as printed in the Name column — either the FIX field name or the component name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeLayoutRow']} })
    pre_layout_required: Optional[bool] = Field(default=None, description="""Whether the field or component is required, as printed in the Req’d column of the source layout table (\"Y\" / \"N\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeLayoutRow']} })
    pre_layout_description: Optional[str] = Field(default=None, description="""Free-text content of the Description column of the row (may be empty).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeLayoutRow']} })
    pre_layout_nested: Optional[bool] = Field(default=False, description="""Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the \"→\" arrow in the source table).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeLayoutRow'], 'ifabsent': 'False'} })


class TradeBusinessArea(ConfiguredBaseModel):
    """
    Tree-root container for the Trade (Orders and Executions) business area of FIX Latest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Trade', 'Orders and Executions'],
         'class_uri': 'fix_trade:TradeBusinessArea',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/business-area-trade/'],
         'slot_usage': {'components': {'description': 'Area-wide trade components '
                                                      'table.',
                                       'inlined': True,
                                       'inlined_as_list': True,
                                       'name': 'components',
                                       'range': 'TradeComponentEntry'},
                        'messages': {'description': 'Area-wide trade messages table.',
                                     'name': 'messages',
                                     'range': 'TradeMessageEntry'},
                        'publisher': {'ifabsent': 'string(FIX Global Technical '
                                                  'Committee)',
                                      'name': 'publisher'},
                        'title': {'ifabsent': 'string(Business Area Trade)',
                                  'name': 'title'},
                        'trade_area': {'ifabsent': 'string(TRADE)',
                                       'name': 'trade_area',
                                       'required': True}},
         'tree_root': True})

    trade_area: BusinessAreaEnum = Field(default=BusinessAreaEnum.TRADE, description="""Identity of the business area the chapter describes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea'],
         'ifabsent': 'string(TRADE)',
         'slot_uri': 'schema:identifier'} })
    title: Optional[str] = Field(default="Business Area Trade", description="""Display title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'ifabsent': 'string(Business Area Trade)',
         'slot_uri': 'dcterms:title'} })
    published_version: Optional[str] = Field(default=None, description="""Version stamp from the document header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'slot_uri': 'schema:version'} })
    publisher: Optional[str] = Field(default="FIX Global Technical Committee", description="""Publishing body of the FIX Latest specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'ifabsent': 'string(FIX Global Technical Committee)',
         'slot_uri': 'dcterms:publisher'} })
    trade_introduction: Optional[str] = Field(default=None, description="""Prose introduction of the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea']} })
    trade_diagram_conventions: Optional[str] = Field(default=None, description="""Sentence describing diagram conventions used in the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea']} })
    trade_message_diagram_template_url: Optional[str] = Field(default=None, description="""URL of the \"Message Diagram Templates\" page referenced by the chapter introduction.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea'], 'slot_uri': 'schema:url'} })
    trade_messages_overview_note: Optional[str] = Field(default=None, description="""Intro prose of the area-wide Messages sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea']} })
    messages: Optional[list[TradeMessageEntry]] = Field(default=None, description="""Area-wide trade messages table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    trade_components_overview_note: Optional[str] = Field(default=None, description="""Intro prose of the area-wide Components sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea']} })
    components: Optional[list[TradeComponentEntry]] = Field(default=None, description="""Area-wide trade components table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    trade_common_components: Optional[list[TradeCommonComponentName]] = Field(default=None, description="""Common Components declared at the bottom of the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea']} })
    trade_common_component_details: Optional[list[TradeCommonComponentDetail]] = Field(default=None, description="""Per-common-component descriptions from the chapter's final section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea']} })
    trade_footnotes: Optional[list[TradeComponentTableFootnote]] = Field(default=None, description="""Footnotes attached to the area-wide components table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea']} })
    trade_category_sections: Optional[list[TradeCategorySection]] = Field(default=None, description="""Per-category sub-sections of the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeBusinessArea']} })
    referenced_global_components: Optional[list[str]] = Field(default=None, description="""Names of Global Components from the FIX Latest \"Global Components\" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })


class TradeMessageEntry(ConfiguredBaseModel):
    """
    One row of the area-wide trade messages table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeMessageEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade_organization'],
         'slot_usage': {'category': {'name': 'category',
                                     'range': 'TradeCategoryEnum',
                                     'required': True},
                        'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'identifier': True,
                                     'name': 'msg_type',
                                     'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    category: TradeCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class TradeComponentEntry(ConfiguredBaseModel):
    """
    One row of the area-wide trade components table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeComponentEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade_organization'],
         'slot_usage': {'category': {'description': 'Category the component is listed '
                                                    'under. Common Components are '
                                                    'listed under the synthetic '
                                                    '"Common Components" value.',
                                     'name': 'category',
                                     'range': 'string',
                                     'required': True},
                        'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'required': True},
                        'trade_is_common': {'ifabsent': 'string(False)',
                                            'name': 'trade_is_common'},
                        'trade_repetition': {'name': 'trade_repetition',
                                             'required': True}}})

    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    trade_repetition: TradeComponentRepetition = Field(default=..., description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeComponentEntry',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail']} })
    category: str = Field(default=..., description="""Category the component is listed under. Common Components are listed under the synthetic \"Common Components\" value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    trade_is_common: Optional[bool] = Field(default=False, description="""True when the component is declared as a Common Component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeComponentEntry'], 'ifabsent': 'string(False)'} })
    trade_footnote_number: Optional[int] = Field(default=None, description="""Footnote indicator on a component-table row.""", ge=1, le=25, json_schema_extra = { "linkml_meta": {'domain_of': ['TradeComponentEntry', 'TradeComponentTableFootnote']} })


class TradeComponentTableFootnote(ConfiguredBaseModel):
    """
    A footnote on the area-wide components table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeComponentTableFootnote',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade_organization'],
         'slot_usage': {'component_name': {'name': 'component_name', 'required': True},
                        'trade_footnote_number': {'identifier': True,
                                                  'name': 'trade_footnote_number',
                                                  'required': True},
                        'trade_introduced_in': {'name': 'trade_introduced_in',
                                                'required': True},
                        'trade_sole_category': {'name': 'trade_sole_category',
                                                'required': True}}})

    trade_footnote_number: int = Field(default=..., description="""Footnote indicator on a component-table row.""", ge=1, le=25, json_schema_extra = { "linkml_meta": {'domain_of': ['TradeComponentEntry', 'TradeComponentTableFootnote']} })
    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    trade_introduced_in: str = Field(default=..., description="""FIX version or Extension Pack that introduced the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeComponentTableFootnote']} })
    trade_sole_category: TradeCategoryEnum = Field(default=..., description="""Single category that actually uses the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeComponentTableFootnote']} })
    trade_footnote_text: Optional[str] = Field(default=None, description="""Footnote text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeComponentTableFootnote']} })


class TradeCategorySection(ConfiguredBaseModel):
    """
    A per-category sub-section of the Trade chapter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeCategorySection',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'slot_usage': {'category': {'identifier': True,
                                     'name': 'category',
                                     'range': 'TradeCategoryEnum',
                                     'required': True},
                        'messages': {'description': 'Messages defined in this '
                                                    'category.',
                                     'name': 'messages',
                                     'range': 'TradeMessageDetail'}}})

    category: TradeCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    title: Optional[str] = Field(default=None, description="""Display title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    trade_category_background: Optional[str] = Field(default=None, description="""Optional \"Background\" prose preceding a category's message descriptions (e.g. the Cross Order Handling chapter's cross-trade overview).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeCategorySection']} })
    trade_message_groups: Optional[list[TradeMessageGroup]] = Field(default=None, description="""Purpose-grouped message descriptions inside a category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeCategorySection']} })
    messages: Optional[list[TradeMessageDetail]] = Field(default=None, description="""Messages defined in this category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    trade_category_components_note: Optional[str] = Field(default=None, description="""Intro prose of a category's Components sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeCategorySection']} })
    trade_category_specific_components: Optional[list[TradeComponentDetail]] = Field(default=None, description="""Components used exclusively by messages within a single category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeCategorySection']} })
    trade_fragmentation_entries: Optional[list[TradeFragmentationEntry]] = Field(default=None, description="""Rows of the fragmentation table listed in a Trade category that documents which messages may be fragmented and which repeating group is fragmentable (currently published only for List/Program/Basket Trading).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeCategorySection']} })


class TradeMessageDetail(ConfiguredBaseModel):
    """
    Per-category message description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeMessageDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'slot_usage': {'description': {'description': "Description of the message's "
                                                       'purpose and usage.',
                                        'name': 'description'},
                        'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'identifier': True,
                                     'name': 'msg_type',
                                     'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the message's purpose and usage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    trade_layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout in the Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail'],
         'slot_uri': 'schema:url'} })
    trade_layout_rows: Optional[list[TradeLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class TradeComponentDetail(ConfiguredBaseModel):
    """
    Per-category component description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeComponentDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'slot_usage': {'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'required': True},
                        'description': {'description': "Description of the component's "
                                                       'purpose.',
                                        'name': 'description'}}})

    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    trade_repetition: Optional[TradeComponentRepetition] = Field(default=None, description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeComponentEntry',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail']} })
    description: Optional[str] = Field(default=None, description="""Description of the component's purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    trade_layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout in the Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail'],
         'slot_uri': 'schema:url'} })
    trade_layout_rows: Optional[list[TradeLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail']} })


class TradeMessageGroup(ConfiguredBaseModel):
    """
    Purpose-grouped sub-section inside a category's Messages sub-section (e.g. \"New Order Single\", \"Execution Reports\", \"Order Cancel Requests\" under Single/General Order Handling).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeMessageGroup',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'slot_usage': {'description': {'description': 'Description of the '
                                                       "purpose-group's role within "
                                                       'the category.',
                                        'name': 'description'},
                        'messages': {'description': 'Messages bundled under the '
                                                    'purpose-group heading.',
                                     'name': 'messages',
                                     'range': 'TradeMessageDetail',
                                     'required': True},
                        'trade_group_title': {'identifier': True,
                                              'name': 'trade_group_title',
                                              'required': True}}})

    trade_group_title: str = Field(default=..., description="""Purpose-group heading inside a category's Messages sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeMessageGroup'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Description of the purpose-group's role within the category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    messages: list[TradeMessageDetail] = Field(default=..., description="""Messages bundled under the purpose-group heading.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    trade_ord_status_precedence_entries: Optional[list[TradeOrdStatusPrecedenceEntry]] = Field(default=None, description="""Rows of the OrdStatus(39) precedence table that appears inside the Execution Reports purpose-group of the Single/General Order Handling category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeMessageGroup']} })


class TradeCommonComponentDetail(ConfiguredBaseModel):
    """
    Per-common-component description from the chapter's final \"Common Components\" section.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeCommonComponentDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'slot_usage': {'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'range': 'TradeCommonComponentName',
                                           'required': True},
                        'description': {'description': 'Description of the common '
                                                       "component's purpose.",
                                        'name': 'description'}}})

    component_name: TradeCommonComponentName = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    trade_repetition: Optional[TradeComponentRepetition] = Field(default=None, description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeComponentEntry',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail']} })
    description: Optional[str] = Field(default=None, description="""Description of the common component's purpose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    trade_layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout in the Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail'],
         'slot_uri': 'schema:url'} })
    trade_layout_rows: Optional[list[TradeLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail']} })


class TradeLayoutRow(ConfiguredBaseModel):
    """
    One row of the layout table published in the Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeLayoutRow',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/trade-appendix/'],
         'slot_usage': {'trade_layout_element_name': {'name': 'trade_layout_element_name',
                                                      'required': True},
                        'trade_layout_kind': {'name': 'trade_layout_kind',
                                              'required': True}}})

    trade_layout_kind: TradeLayoutRowKindEnum = Field(default=..., description="""Row kind — either a FIX field (numeric Tag) or an embedded component (literal \"Component\" in the Tag column of the source table).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeLayoutRow']} })
    trade_layout_field_tag: Optional[int] = Field(default=None, description="""FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['TradeLayoutRow']} })
    trade_layout_element_name: str = Field(default=..., description="""Element name as printed in the Name column — either the FIX field name or the component name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeLayoutRow']} })
    trade_layout_required: Optional[bool] = Field(default=None, description="""Whether the field or component is required, as printed in the Req'd column of the source layout table (\"Y\" / \"N\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeLayoutRow']} })
    trade_layout_description: Optional[str] = Field(default=None, description="""Free-text content of the Description column of the row (may be empty).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeLayoutRow']} })
    trade_layout_nested: Optional[bool] = Field(default=False, description="""Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the \"→\" arrow in the source table).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeLayoutRow'], 'ifabsent': 'False'} })


class TradeOrdStatusPrecedenceEntry(ConfiguredBaseModel):
    """
    One row of the OrdStatus(39) precedence table published in the Execution Reports purpose-group of the Single/General Order Handling category. Defines the precedence ranking used to resolve simultaneous state transitions on an order, paired with the human-readable OrdStatus label and its descriptive prose.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeOrdStatusPrecedenceEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'slot_usage': {'description': {'description': 'Verbatim OrdStatus description '
                                                       'from the table.',
                                        'name': 'description'},
                        'trade_ord_status_label': {'identifier': True,
                                                   'name': 'trade_ord_status_label',
                                                   'required': True},
                        'trade_ord_status_precedence': {'name': 'trade_ord_status_precedence',
                                                        'required': True}}})

    trade_ord_status_precedence: int = Field(default=..., description="""Precedence rank (1 = lowest, higher numbers take precedence) of an OrdStatus(39) value used to resolve simultaneous state transitions on an order.""", ge=1, le=11, json_schema_extra = { "linkml_meta": {'domain_of': ['TradeOrdStatusPrecedenceEntry']} })
    trade_ord_status_label: str = Field(default=..., description="""Human-readable OrdStatus(39) label as printed in the Execution Reports precedence table (e.g. \"Pending Cancel\", \"Done for Day\", \"Filled\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeOrdStatusPrecedenceEntry']} })
    description: Optional[str] = Field(default=None, description="""Verbatim OrdStatus description from the table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })


class TradeFragmentationEntry(ConfiguredBaseModel):
    """
    One row of a fragmentation table published in a Trade category (currently only List/Program/Basket Trading) identifying a message that may be fragmented, the \"Total Entries\" field used to indicate the total count across all fragments of the batch, and the verbatim description of the repeating group that may be fragmented.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeFragmentationEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'slot_usage': {'trade_fragmentation_message': {'identifier': True,
                                                        'name': 'trade_fragmentation_message',
                                                        'required': True},
                        'trade_fragmentation_repeating_group': {'name': 'trade_fragmentation_repeating_group',
                                                                'required': True},
                        'trade_fragmentation_total_entries_field': {'name': 'trade_fragmentation_total_entries_field',
                                                                    'required': True}}})

    trade_fragmentation_message: str = Field(default=..., description="""Message that may be fragmented — verbatim text from the Message column of the fragmentation table (e.g. \"NewOrderList(35=E)\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeFragmentationEntry']} })
    trade_fragmentation_total_entries_field: str = Field(default=..., description="""Name and tag of the \"Total Entries\" field used to indicate the total count across all fragments of the batch (e.g. \"TotNoOrders(68)\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeFragmentationEntry']} })
    trade_fragmentation_repeating_group: str = Field(default=..., description="""Verbatim description of the repeating group that may be fragmented — from the table's third column.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeFragmentationEntry']} })


class TradeAppendix(ConfiguredBaseModel):
    """
    Tree-root container for the Trade Appendix — the spec companion document that publishes the full message- and component-layout tables for every message and component used in the Trade business area, organized into one \"Appendix – <X> Category\" sub-section per Trade category plus a final \"Appendix – Common Category\" sub-section covering the layouts of the chapter's common components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Trade Appendix'],
         'class_uri': 'fix_trade:TradeAppendix',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/trade-appendix/'],
         'slot_usage': {'description': {'description': 'Optional preface prose for the '
                                                       'Trade Appendix as a whole.',
                                        'name': 'description'},
                        'publisher': {'ifabsent': 'string(FIX Global Technical '
                                                  'Committee)',
                                      'name': 'publisher'},
                        'title': {'ifabsent': 'string(Trade Appendix)',
                                  'name': 'title'}},
         'tree_root': True})

    title: Optional[str] = Field(default="Trade Appendix", description="""Display title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'ifabsent': 'string(Trade Appendix)',
         'slot_uri': 'dcterms:title'} })
    published_version: Optional[str] = Field(default=None, description="""Version stamp from the document header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'slot_uri': 'schema:version'} })
    publisher: Optional[str] = Field(default="FIX Global Technical Committee", description="""Publishing body of the FIX Latest specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'ifabsent': 'string(FIX Global Technical Committee)',
         'slot_uri': 'dcterms:publisher'} })
    description: Optional[str] = Field(default=None, description="""Optional preface prose for the Trade Appendix as a whole.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    trade_appendix_sections: Optional[list[TradeAppendixSection]] = Field(default=None, description="""Per-category sub-sections of the Trade Appendix — one \"Appendix – <X> Category\" section per Trade category, plus a synthetic \"Common Category\" section that lists layouts of the chapter's common components.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeAppendix']} })


class TradeAppendixSection(ConfiguredBaseModel):
    """
    One \"Appendix – <X> Category\" sub-section of the Trade Appendix. Bundles the per-message layout tables (TradeMessageDetail) and per-component layout tables (TradeComponentDetail) for messages and components that belong to one Trade category — or, for the synthetic \"Common\" section, the layouts of the chapter's common components.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_trade:TradeAppendixSection',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-trade',
         'in_subset': ['trade'],
         'slot_usage': {'components': {'description': 'Layout tables for the '
                                                      'components that belong to the '
                                                      'appendix section.',
                                       'name': 'components',
                                       'range': 'TradeComponentDetail'},
                        'messages': {'description': 'Layout tables for the messages '
                                                    'that belong to the appendix '
                                                    'section. Empty for the "Common" '
                                                    'section.',
                                     'name': 'messages',
                                     'range': 'TradeMessageDetail'},
                        'title': {'description': 'Section heading exactly as printed '
                                                 'in the Trade Appendix (e.g. '
                                                 '"Appendix – CrossOrders Category").',
                                  'name': 'title'},
                        'trade_appendix_category': {'identifier': True,
                                                    'name': 'trade_appendix_category',
                                                    'required': True}}})

    trade_appendix_category: str = Field(default=..., description="""Identifier for an appendix section — either the Trade category name as printed in the heading (e.g. \"CrossOrders\", \"MultilegOrders\", \"OrderMassHandling\", \"ProgramTrading\", \"SingleGeneralOrderHandling\") or the literal \"Common\" for the common-components appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeAppendixSection']} })
    title: Optional[str] = Field(default=None, description="""Section heading exactly as printed in the Trade Appendix (e.g. \"Appendix – CrossOrders Category\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    messages: Optional[list[TradeMessageDetail]] = Field(default=None, description="""Layout tables for the messages that belong to the appendix section. Empty for the \"Common\" section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    components: Optional[list[str]] = Field(default=None, description="""Layout tables for the components that belong to the appendix section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })


class PostTradeBusinessArea(ConfiguredBaseModel):
    """
    Tree-root container for the Post-Trade business area of FIX Latest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Post-Trade'],
         'class_uri': 'fix_post_trade:PostTradeBusinessArea',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/business-area-post-trade/'],
         'slot_usage': {'area': {'ifabsent': 'string(POST_TRADE)',
                                 'name': 'area',
                                 'required': True},
                        'components': {'inlined': True,
                                       'inlined_as_list': True,
                                       'name': 'components',
                                       'range': 'PostTradeComponentEntry',
                                       'required': True},
                        'messages': {'inlined': True,
                                     'inlined_as_list': True,
                                     'name': 'messages',
                                     'range': 'PostTradeMessageEntry',
                                     'required': True},
                        'publisher': {'ifabsent': 'string(FIX Global Technical '
                                                  'Committee)',
                                      'name': 'publisher'},
                        'title': {'ifabsent': 'string(Business Area Post-Trade)',
                                  'name': 'title'}},
         'tree_root': True})

    area: BusinessAreaEnum = Field(default=BusinessAreaEnum.POST_TRADE, description="""Identity of the business area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BusinessArea',
                       'PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'ifabsent': 'string(POST_TRADE)',
         'slot_uri': 'schema:identifier'} })
    title: Optional[str] = Field(default="Business Area Post-Trade", description="""Display title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'ifabsent': 'string(Business Area Post-Trade)',
         'slot_uri': 'dcterms:title'} })
    published_version: Optional[str] = Field(default=None, description="""Version stamp from the document header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'slot_uri': 'schema:version'} })
    publisher: Optional[str] = Field(default="FIX Global Technical Committee", description="""Publishing body of the FIX Latest specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'ifabsent': 'string(FIX Global Technical Committee)',
         'slot_uri': 'dcterms:publisher'} })
    post_introduction: Optional[str] = Field(default=None, description="""Prose introduction of the Post-Trade chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeBusinessArea']} })
    diagram_conventions: Optional[str] = Field(default=None, description="""Sentence describing diagram conventions used in the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    post_common_components: Optional[list[PostTradeCommonComponentName]] = Field(default=None, description="""Common Components declared at the top of the Post-Trade chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeBusinessArea']} })
    messages: list[PostTradeMessageEntry] = Field(default=..., description="""Messages defined within the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    components: list[PostTradeComponentEntry] = Field(default=..., description="""Components referenced by the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    post_footnotes: Optional[list[PostTradeComponentTableFootnote]] = Field(default=None, description="""Footnotes attached to the area-wide components table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeBusinessArea']} })
    post_category_sections: Optional[list[PostTradeCategorySection]] = Field(default=None, description="""Per-category sub-sections of the Post-Trade chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeBusinessArea']} })
    post_common_component_details: Optional[list[PostTradeCommonComponentDetail]] = Field(default=None, description="""Per-common-component descriptions from the chapter's final Common Components section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeBusinessArea']} })
    messages_overview_note: Optional[str] = Field(default=None, description="""Intro prose of the area-wide Messages sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    components_overview_note: Optional[str] = Field(default=None, description="""Intro prose of the area-wide Components sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    referenced_global_components: Optional[list[str]] = Field(default=None, description="""Names of Global Components from the FIX Latest \"Global Components\" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })


class PostTradeMessageEntry(ConfiguredBaseModel):
    """
    One row of the area-wide \"Messages for Post-Trade Business Area\" table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:PostTradeMessageEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade_organization'],
         'slot_usage': {'category': {'name': 'category',
                                     'range': 'PostTradeCategoryEnum',
                                     'required': True},
                        'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'identifier': True,
                                     'name': 'msg_type',
                                     'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    category: PostTradeCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class PostTradeComponentEntry(ConfiguredBaseModel):
    """
    One row of the area-wide \"Components for Post-Trade Business Area\" table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:PostTradeComponentEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade_organization'],
         'slot_usage': {'category': {'description': 'Category label as printed in the '
                                                    'component table; the token '
                                                    '"Common Components" is allowed in '
                                                    'addition to the '
                                                    'PostTradeCategoryEnum values.',
                                     'name': 'category',
                                     'range': 'string',
                                     'required': True},
                        'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'required': True},
                        'is_common': {'ifabsent': 'string(False)', 'name': 'is_common'},
                        'repetition': {'name': 'repetition', 'required': True}}})

    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    repetition: ComponentRepetition = Field(default=..., description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentDetail']} })
    category: str = Field(default=..., description="""Category label as printed in the component table; the token \"Common Components\" is allowed in addition to the PostTradeCategoryEnum values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    is_common: Optional[bool] = Field(default=False, description="""True when the component is declared as a Common Component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry', 'PostTradeComponentEntry'],
         'ifabsent': 'string(False)'} })
    footnote_number: Optional[int] = Field(default=None, description="""Footnote indicator on a component-table row.""", ge=1, le=25, json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote']} })


class PostTradeComponentTableFootnote(ConfiguredBaseModel):
    """
    A footnote attached to a row of the area-wide Post-Trade components table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:PostTradeComponentTableFootnote',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade_organization'],
         'slot_usage': {'component_name': {'name': 'component_name', 'required': True},
                        'footnote_number': {'identifier': True,
                                            'name': 'footnote_number',
                                            'required': True},
                        'introduced_in': {'name': 'introduced_in', 'required': True},
                        'post_sole_category': {'name': 'post_sole_category',
                                               'required': True}}})

    footnote_number: int = Field(default=..., description="""Footnote indicator on a component-table row.""", ge=1, le=25, json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote']} })
    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    introduced_in: str = Field(default=..., description="""FIX version or Extension Pack that introduced the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentTableFootnote',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentTableFootnote']} })
    post_sole_category: PostTradeCategoryEnum = Field(default=..., description="""Single Post-Trade category that actually uses the component (per footnote).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeComponentTableFootnote']} })
    text: Optional[str] = Field(default=None, description="""Footnote text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentTableFootnote',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentTableFootnote']} })


class PostTradeCategorySection(ConfiguredBaseModel):
    """
    A \"Category – <name>\" sub-section of the Post-Trade chapter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:PostTradeCategorySection',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade'],
         'slot_usage': {'category': {'identifier': True,
                                     'name': 'category',
                                     'range': 'PostTradeCategoryEnum',
                                     'required': True},
                        'messages': {'inlined': True,
                                     'inlined_as_list': True,
                                     'name': 'messages',
                                     'range': 'PostTradeMessageDetail'}}})

    category: PostTradeCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    title: Optional[str] = Field(default=None, description="""Display title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    category_components_note: Optional[str] = Field(default=None, description="""Intro prose of a category's Components sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeCategorySection',
                       'PostTradeCategorySection',
                       'InfrastructureCategorySection']} })
    post_message_groups: Optional[list[PostTradeMessageGroup]] = Field(default=None, description="""Purpose-grouped message descriptions inside a Post-Trade category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    messages: Optional[list[PostTradeMessageDetail]] = Field(default=None, description="""Messages defined within the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    post_category_specific_components: Optional[list[PostTradeComponentDetail]] = Field(default=None, description="""Components used exclusively by messages within a category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    allocation_scenarios: Optional[list[AllocationScenarioEnum]] = Field(default=None, description="""Communication options supported by the Allocation category for conveying allocation instructions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    allocation_roles: Optional[list[AllocationRoleEnum]] = Field(default=None, description="""Role labels used throughout the Allocation category prose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    post_trade_allocation_pricing_methods: Optional[list[PostTradeAllocationPricingMethodEnum]] = Field(default=None, description="""Methods supported for computing post-trade allocations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    allocation_status_descriptions: Optional[list[AllocationStatusDescription]] = Field(default=None, description="""Descriptions tied to AllocStatus(87) values as listed in the Allocation Instruction Acknowledgements section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    fragmentation_field_map: Optional[list[AllocationFragmentationFieldMap]] = Field(default=None, description="""Per-message mapping of fragmentation-related fields used by the Allocation messages.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    trade_capture_report_usages: Optional[list[TradeCaptureReportUsage]] = Field(default=None, description="""Usages described in the \"Trade Capture Report Usages\" sub-section of the Trade Capture Reporting category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    trade_capture_report_identifier_rules: Optional[list[TradeCaptureReportIdentifierRule]] = Field(default=None, description="""Rules governing TradeCaptureReport(35=AE) identifier fields.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    registration_status_descriptions: Optional[list[RegistrationStatusDescription]] = Field(default=None, description="""Descriptions tied to RegistStatus(506) values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    clearing_services_for_position_management: Optional[list[ClearingServiceForPositionManagementEnum]] = Field(default=None, description="""Business functions exposed by the Position Management Clearing Services.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    clearing_services_for_post_trade_processing: Optional[list[ClearingServicePostTradeProcessingFormat]] = Field(default=None, description="""Per-format action sets exposed by the Post-Trade Processing Clearing Services.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    collateral_management_usages: Optional[list[CollateralManagementUsageEnum]] = Field(default=None, description="""Documented usages for the Collateral Management messages.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })
    collateral_assignment_purposes: Optional[list[CollateralAssignmentPurposeEnum]] = Field(default=None, description="""Documented purposes for the CollateralAssignment(35=AY) message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeCategorySection']} })


class PostTradeMessageGroup(ConfiguredBaseModel):
    """
    A purpose-themed grouping of messages within a Post-Trade category (e.g. \"Allocation Instructions\").
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:PostTradeMessageGroup',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade'],
         'slot_usage': {'group_title': {'identifier': True,
                                        'name': 'group_title',
                                        'required': True},
                        'messages': {'inlined': True,
                                     'inlined_as_list': True,
                                     'name': 'messages',
                                     'range': 'PostTradeMessageDetail',
                                     'required': True}}})

    group_title: str = Field(default=..., description="""Purpose-group heading inside a category's Messages sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageGroup', 'PostTradeMessageGroup'],
         'slot_uri': 'schema:name'} })
    messages: list[PostTradeMessageDetail] = Field(default=..., description="""Messages defined within the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })


class PostTradeMessageDetail(ConfiguredBaseModel):
    """
    Per-message description block from a Post-Trade category section.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:PostTradeMessageDetail',
         'close_mappings': ['fix_orchestra:MessageType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade'],
         'slot_usage': {'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'identifier': True,
                                     'name': 'msg_type',
                                     'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:url'} })
    post_layout_rows: Optional[list[PostTradeLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Post-Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class PostTradeComponentDetail(ConfiguredBaseModel):
    """
    Per-component description block from a Post-Trade category section's Components sub-section.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:PostTradeComponentDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade'],
         'slot_usage': {'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'required': True}}})

    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    repetition: Optional[ComponentRepetition] = Field(default=None, description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentDetail']} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:url'} })
    post_layout_rows: Optional[list[PostTradeLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Post-Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail']} })


class PostTradeCommonComponentDetail(ConfiguredBaseModel):
    """
    Per-common-component description block from the chapter's final \"Common Components\" section.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:PostTradeCommonComponentDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade'],
         'slot_usage': {'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'range': 'PostTradeCommonComponentName',
                                           'required': True}}})

    component_name: PostTradeCommonComponentName = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    repetition: Optional[ComponentRepetition] = Field(default=None, description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentDetail']} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:url'} })
    post_layout_rows: Optional[list[PostTradeLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Post-Trade Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail']} })


class AllocationStatusDescription(ConfiguredBaseModel):
    """
    One row of the AllocStatus(87) value/description table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:AllocationStatusDescription',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade_workflow'],
         'slot_usage': {'status_code': {'identifier': True,
                                        'name': 'status_code',
                                        'required': True},
                        'status_label': {'name': 'status_label', 'required': True}}})

    status_code: str = Field(default=..., description="""Wire status code as referenced in the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AllocationStatusDescription', 'RegistrationStatusDescription']} })
    status_label: str = Field(default=..., description="""Human-readable label of the status code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'RegistrationStatusDescription']} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })


class AllocationFragmentationFieldMap(ConfiguredBaseModel):
    """
    One row of the table mapping an allocation message to its fragmentation-related fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:AllocationFragmentationFieldMap',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade_workflow'],
         'slot_usage': {'fragment_count_field': {'name': 'fragment_count_field',
                                                 'required': True},
                        'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'identifier': True,
                                     'name': 'msg_type',
                                     'required': True},
                        'principal_message_reference': {'name': 'principal_message_reference',
                                                        'required': True},
                        'total_count_field': {'name': 'total_count_field',
                                              'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    total_count_field: str = Field(default=..., description="""Field carrying the total number of repeating-group entries across all fragments (e.g. TotNoAllocs).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AllocationFragmentationFieldMap']} })
    fragment_count_field: str = Field(default=..., description="""Field carrying the number of entries in the current message fragment (e.g. NoAllocs).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AllocationFragmentationFieldMap']} })
    principal_message_reference: str = Field(default=..., description="""Principal message reference field used to bind allocation message fragments together (e.g. AllocID, AllocReportID).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AllocationFragmentationFieldMap']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class TradeCaptureReportUsage(ConfiguredBaseModel):
    """
    One documented usage of the TradeCaptureReport(35=AE) message.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:TradeCaptureReportUsage',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade_workflow'],
         'related_mappings': ['common_domain_model:BusinessEvent',
                              'fix_orchestra:ScenarioType'],
         'slot_usage': {'status_label': {'description': 'Short label for the usage.',
                                         'identifier': True,
                                         'name': 'status_label',
                                         'required': True}}})

    status_label: str = Field(default=..., description="""Short label for the usage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'RegistrationStatusDescription']} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    identifier_role: Optional[TradeCaptureReportIdentifierRoleEnum] = Field(default=None, description="""Role of the trade-capture-report identifier field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeCaptureReportUsage', 'TradeCaptureReportIdentifierRule']} })


class TradeCaptureReportIdentifierRule(ConfiguredBaseModel):
    """
    A rule governing one of the TradeCaptureReport(35=AE) identifier fields.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:TradeCaptureReportIdentifierRule',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade_workflow'],
         'related_mappings': ['common_domain_model:Identifier'],
         'slot_usage': {'identifier_role': {'identifier': True,
                                            'name': 'identifier_role',
                                            'required': True}}})

    identifier_role: TradeCaptureReportIdentifierRoleEnum = Field(default=..., description="""Role of the trade-capture-report identifier field.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TradeCaptureReportUsage', 'TradeCaptureReportIdentifierRule']} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })


class RegistrationStatusDescription(ConfiguredBaseModel):
    """
    One row of the RegistStatus(506) value/description table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:RegistrationStatusDescription',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade_workflow'],
         'slot_usage': {'status_code': {'identifier': True,
                                        'name': 'status_code',
                                        'required': True},
                        'status_label': {'name': 'status_label', 'required': True}}})

    status_code: str = Field(default=..., description="""Wire status code as referenced in the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AllocationStatusDescription', 'RegistrationStatusDescription']} })
    status_label: str = Field(default=..., description="""Human-readable label of the status code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'RegistrationStatusDescription']} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })


class ClearingServicePostTradeProcessingFormat(ConfiguredBaseModel):
    """
    One message-format row from the Post-Trade Processing Clearing Services section, with its supported actions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:ClearingServicePostTradeProcessingFormat',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade_workflow'],
         'slot_usage': {'message_format': {'identifier': True,
                                           'name': 'message_format',
                                           'required': True},
                        'supported_actions': {'name': 'supported_actions',
                                              'required': True}}})

    message_format: ClearingServiceForPostTradeProcessingEnum = Field(default=..., description="""Clearing-service message format family referenced in the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClearingServicePostTradeProcessingFormat']} })
    supported_actions: list[str] = Field(default=..., description="""Action labels (e.g. Allocation, Accept, Reject, Release, Change, Delete) supported by a clearing-service message format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ClearingServicePostTradeProcessingFormat']} })


class PostTradeLayoutRow(ConfiguredBaseModel):
    """
    One row of the layout table published in the Post-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_post_trade:PostTradeLayoutRow',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-post-trade',
         'in_subset': ['post_trade'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/post-trade-appendix/'],
         'slot_usage': {'post_layout_element_name': {'name': 'post_layout_element_name',
                                                     'required': True},
                        'post_layout_kind': {'name': 'post_layout_kind',
                                             'required': True}}})

    post_layout_kind: PostTradeLayoutRowKindEnum = Field(default=..., description="""Row kind — either a FIX field (numeric Tag) or an embedded component (literal \"Component\" in the Tag column of the source table).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeLayoutRow']} })
    post_layout_field_tag: Optional[int] = Field(default=None, description="""FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeLayoutRow']} })
    post_layout_element_name: str = Field(default=..., description="""Element name as printed in the Name column — either the FIX field name or the component name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeLayoutRow']} })
    post_layout_required: Optional[bool] = Field(default=None, description="""Whether the field or component is required, as printed in the Req’d column of the source layout table (\"Y\" / \"N\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeLayoutRow']} })
    post_layout_description: Optional[str] = Field(default=None, description="""Free-text content of the Description column of the row (may be empty).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeLayoutRow']} })
    post_layout_nested: Optional[bool] = Field(default=False, description="""Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the \"→\" arrow in the source table).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PostTradeLayoutRow'], 'ifabsent': 'False'} })


class InfrastructureBusinessArea(ConfiguredBaseModel):
    """
    Tree-root container for the Infrastructure business area of FIX Latest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['Infrastructure'],
         'class_uri': 'fix_infrastructure:InfrastructureBusinessArea',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure'],
         'related_mappings': ['fixp:FixpSessionExchange'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/business-area-infrastructure/'],
         'slot_usage': {'area': {'ifabsent': 'string(INFRASTRUCTURE)',
                                 'name': 'area',
                                 'required': True},
                        'components': {'inlined': True,
                                       'inlined_as_list': True,
                                       'name': 'components',
                                       'range': 'InfrastructureComponentEntry',
                                       'required': True},
                        'messages': {'inlined': True,
                                     'inlined_as_list': True,
                                     'name': 'messages',
                                     'range': 'InfrastructureMessageEntry',
                                     'required': True},
                        'publisher': {'ifabsent': 'string(FIX Global Technical '
                                                  'Committee)',
                                      'name': 'publisher'},
                        'title': {'ifabsent': 'string(Business Area Infrastructure)',
                                  'name': 'title'}},
         'tree_root': True})

    area: BusinessAreaEnum = Field(default=BusinessAreaEnum.INFRASTRUCTURE, description="""Identity of the business area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BusinessArea',
                       'PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'ifabsent': 'string(INFRASTRUCTURE)',
         'slot_uri': 'schema:identifier'} })
    title: Optional[str] = Field(default="Business Area Infrastructure", description="""Display title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'ifabsent': 'string(Business Area Infrastructure)',
         'slot_uri': 'dcterms:title'} })
    published_version: Optional[str] = Field(default=None, description="""Version stamp from the document header.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'slot_uri': 'schema:version'} })
    publisher: Optional[str] = Field(default="FIX Global Technical Committee", description="""Publishing body of the FIX Latest specification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXIntroduction',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendix',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea'],
         'ifabsent': 'string(FIX Global Technical Committee)',
         'slot_uri': 'dcterms:publisher'} })
    infra_introduction: Optional[str] = Field(default=None, description="""Prose introduction of the Infrastructure chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    diagram_conventions: Optional[str] = Field(default=None, description="""Sentence describing diagram conventions used in the chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    infra_common_components: Optional[list[InfrastructureComponentName]] = Field(default=None, description="""Component names declared in the area-wide components listing. Per the chapter prose, none of these are shared across categories within the area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    messages: list[InfrastructureMessageEntry] = Field(default=..., description="""Messages defined within the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    messages_overview_note: Optional[str] = Field(default=None, description="""Intro prose of the area-wide Messages sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    components: list[InfrastructureComponentEntry] = Field(default=..., description="""Components referenced by the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    components_overview_note: Optional[str] = Field(default=None, description="""Intro prose of the area-wide Components sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })
    infra_footnotes: Optional[list[InfrastructureComponentTableFootnote]] = Field(default=None, description="""Footnotes attached to the area-wide Infrastructure components table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    infra_category_sections: Optional[list[InfrastructureCategorySection]] = Field(default=None, description="""Per-category sub-sections of the Infrastructure chapter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    standard_responses_pre_trade: Optional[list[StandardResponseMapping]] = Field(default=None, description="""\"Standard Responses for Pre-Trade Messages\" table rows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    standard_responses_trade: Optional[list[StandardResponseMapping]] = Field(default=None, description="""\"Standard Responses for Trade Messages\" table rows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    standard_responses_post_trade: Optional[list[StandardResponseMapping]] = Field(default=None, description="""\"Standard Responses for Post-Trade Messages\" table rows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    key_fields_pre_trade: Optional[list[ApplicationMessageReferenceKey]] = Field(default=None, description="""\"Key Fields for Pre-Trade Application Message References\" table rows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    key_fields_trade: Optional[list[ApplicationMessageReferenceKey]] = Field(default=None, description="""\"Key Fields for Trade Application Message References\" table rows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    key_fields_post_trade: Optional[list[ApplicationMessageReferenceKey]] = Field(default=None, description="""\"Key Fields for Post-Trade Application Message References\" table rows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    business_reject_reason_descriptions: Optional[list[BusinessRejectReasonDescription]] = Field(default=None, description="""Descriptions tied to BusinessRejectReason(380) values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    infra_global_components: Optional[list[InfrastructureGlobalComponentReference]] = Field(default=None, description="""Global Components (from the FIX Latest \"Global Components\" page) that are explicitly referenced by messages in the Infrastructure business area, together with their tag set and usage scope.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureBusinessArea']} })
    referenced_global_components: Optional[list[str]] = Field(default=None, description="""Names of Global Components from the FIX Latest \"Global Components\" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeBusinessArea',
                       'TradeBusinessArea',
                       'PostTradeBusinessArea',
                       'InfrastructureBusinessArea']} })


class InfrastructureMessageEntry(ConfiguredBaseModel):
    """
    One row of the area-wide \"Messages for Infrastructure Business Area\" table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:InfrastructureMessageEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure_organization'],
         'slot_usage': {'category': {'name': 'category',
                                     'range': 'InfrastructureCategoryEnum',
                                     'required': True},
                        'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'identifier': True,
                                     'name': 'msg_type',
                                     'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    category: InfrastructureCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class InfrastructureComponentEntry(ConfiguredBaseModel):
    """
    One row of the area-wide \"Components for Infrastructure Business Area\" table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:InfrastructureComponentEntry',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure_organization'],
         'slot_usage': {'category': {'name': 'category',
                                     'range': 'InfrastructureCategoryEnum',
                                     'required': True},
                        'component_name': {'identifier': True,
                                           'name': 'component_name',
                                           'required': True},
                        'repetition': {'name': 'repetition', 'required': True}}})

    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    repetition: ComponentRepetition = Field(default=..., description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentDetail']} })
    category: InfrastructureCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    footnote_number: Optional[int] = Field(default=None, description="""Footnote indicator on a component-table row.""", ge=1, le=25, json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote']} })


class InfrastructureComponentTableFootnote(ConfiguredBaseModel):
    """
    A footnote attached to a row of the area-wide Infrastructure components table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:InfrastructureComponentTableFootnote',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure_organization'],
         'slot_usage': {'component_name': {'name': 'component_name', 'required': True},
                        'footnote_number': {'identifier': True,
                                            'name': 'footnote_number',
                                            'required': True},
                        'infra_sole_category': {'name': 'infra_sole_category',
                                                'required': True},
                        'introduced_in': {'name': 'introduced_in', 'required': True}}})

    footnote_number: int = Field(default=..., description="""Footnote indicator on a component-table row.""", ge=1, le=25, json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote']} })
    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    introduced_in: str = Field(default=..., description="""FIX version or Extension Pack that introduced the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentTableFootnote',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentTableFootnote']} })
    infra_sole_category: InfrastructureCategoryEnum = Field(default=..., description="""Single Infrastructure category that actually uses the footnoted component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureComponentTableFootnote']} })
    text: Optional[str] = Field(default=None, description="""Footnote text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ComponentTableFootnote',
                       'PostTradeComponentTableFootnote',
                       'InfrastructureComponentTableFootnote']} })


class InfrastructureCategorySection(ConfiguredBaseModel):
    """
    A \"Category – <name>\" sub-section of the Infrastructure chapter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:InfrastructureCategorySection',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure'],
         'slot_usage': {'category': {'name': 'category',
                                     'range': 'InfrastructureCategoryEnum',
                                     'required': True},
                        'messages': {'inlined': True,
                                     'inlined_as_list': True,
                                     'name': 'messages',
                                     'range': 'InfrastructureMessageDetail'}}})

    category: InfrastructureCategoryEnum = Field(default=..., description="""Message category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'SpecificComponent',
                       'Message',
                       'PreTradeMessageEntry',
                       'PreTradeComponentEntry',
                       'PreTradeCategorySection',
                       'TradeMessageEntry',
                       'TradeComponentEntry',
                       'TradeCategorySection',
                       'PostTradeMessageEntry',
                       'PostTradeComponentEntry',
                       'PostTradeCategorySection',
                       'InfrastructureMessageEntry',
                       'InfrastructureComponentEntry',
                       'InfrastructureCategorySection']} })
    title: Optional[str] = Field(default=None, description="""Display title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ExtensionPack',
                       'BusinessArea',
                       'MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    category_components_note: Optional[str] = Field(default=None, description="""Intro prose of a category's Components sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeCategorySection',
                       'PostTradeCategorySection',
                       'InfrastructureCategorySection']} })
    messages: Optional[list[InfrastructureMessageDetail]] = Field(default=None, description="""Messages defined within the enclosing element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MessageCategory',
                       'PreTradeBusinessArea',
                       'PreTradeCategorySection',
                       'MessageGroup',
                       'TradeBusinessArea',
                       'TradeCategorySection',
                       'TradeMessageGroup',
                       'TradeAppendixSection',
                       'PostTradeBusinessArea',
                       'PostTradeCategorySection',
                       'PostTradeMessageGroup',
                       'InfrastructureBusinessArea',
                       'InfrastructureCategorySection']} })
    infra_category_specific_components: Optional[list[InfrastructureComponentDetail]] = Field(default=None, description="""Per-component descriptions appearing in a category's Components sub-section.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureCategorySection']} })
    network_status_scenarios: Optional[list[NetworkStatusScenarioEnum]] = Field(default=None, description="""Network Status Communication usage scenarios.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureCategorySection']} })
    network_request_types_referenced: Optional[list[NetworkRequestTypeEnum]] = Field(default=None, description="""NetworkRequestType(935) values explicitly cited in the Network Status Communication category prose.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureCategorySection']} })
    application_message_report_uses: Optional[list[ApplicationMessageReportTypeEnum]] = Field(default=None, description="""Documented uses of ApplicationMessageReport(35=BY).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureCategorySection']} })


class InfrastructureMessageDetail(ConfiguredBaseModel):
    """
    Per-message description appearing in a category's Messages sub-section.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:InfrastructureMessageDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure'],
         'slot_usage': {'message_name': {'name': 'message_name', 'required': True},
                        'msg_type': {'name': 'msg_type', 'required': True}}})

    msg_type: str = Field(default=..., description="""MsgType(35) wire value identifying the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail']} })
    message_name: str = Field(default=..., description="""PascalCase name of the message.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Message',
                       'PreTradeMessageEntry',
                       'PreTradeMessageDetail',
                       'TradeMessageEntry',
                       'TradeMessageDetail',
                       'PostTradeMessageEntry',
                       'PostTradeMessageDetail',
                       'AllocationFragmentationFieldMap',
                       'InfrastructureMessageEntry',
                       'InfrastructureMessageDetail'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:url'} })
    infra_layout_rows: Optional[list[InfrastructureLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Infrastructure Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureMessageDetail', 'InfrastructureComponentDetail']} })

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[A-Za-z0-9]{1,3}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v


class InfrastructureComponentDetail(ConfiguredBaseModel):
    """
    Per-component description appearing in a category's Components sub-section.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:InfrastructureComponentDetail',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure'],
         'slot_usage': {'component_name': {'name': 'component_name', 'required': True}}})

    component_name: str = Field(default=..., description="""PascalCase name of the component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Component',
                       'PreTradeComponentEntry',
                       'ComponentTableFootnote',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'TradeComponentEntry',
                       'TradeComponentTableFootnote',
                       'TradeComponentDetail',
                       'TradeCommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentTableFootnote',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentTableFootnote',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:name'} })
    repetition: Optional[ComponentRepetition] = Field(default=None, description="""REPEATING or NON_REPEATING.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeComponentEntry',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeComponentEntry',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureComponentEntry',
                       'InfrastructureComponentDetail']} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FIXFamilyStandard',
                       'BusinessArea',
                       'MessageCategory',
                       'Field',
                       'Component',
                       'Message',
                       'UDFTagRange',
                       'PreTradeCategorySection',
                       'PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'MessageGroup',
                       'CommonComponentDetail',
                       'TradeCategorySection',
                       'TradeMessageDetail',
                       'TradeComponentDetail',
                       'TradeMessageGroup',
                       'TradeCommonComponentDetail',
                       'TradeOrdStatusPrecedenceEntry',
                       'TradeAppendix',
                       'TradeAppendixSection',
                       'PostTradeCategorySection',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'AllocationStatusDescription',
                       'TradeCaptureReportUsage',
                       'TradeCaptureReportIdentifierRule',
                       'RegistrationStatusDescription',
                       'InfrastructureCategorySection',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'dcterms:description'} })
    layout_url: Optional[str] = Field(default=None, description="""URL of the detailed message- or component-layout.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PreTradeMessageDetail',
                       'PreTradeComponentDetail',
                       'CommonComponentDetail',
                       'PostTradeMessageDetail',
                       'PostTradeComponentDetail',
                       'PostTradeCommonComponentDetail',
                       'InfrastructureMessageDetail',
                       'InfrastructureComponentDetail'],
         'slot_uri': 'schema:url'} })
    infra_layout_rows: Optional[list[InfrastructureLayoutRow]] = Field(default=None, description="""Ordered rows of the layout table published for the message or component in the Infrastructure Appendix.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureMessageDetail', 'InfrastructureComponentDetail']} })


class InfrastructureLayoutRow(ConfiguredBaseModel):
    """
    One row of the layout table published in the Infrastructure Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:InfrastructureLayoutRow',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/business-area-infrastructure-appendix/'],
         'slot_usage': {'infra_layout_element_name': {'name': 'infra_layout_element_name',
                                                      'required': True},
                        'infra_layout_kind': {'name': 'infra_layout_kind',
                                              'required': True}}})

    infra_layout_kind: InfrastructureLayoutRowKindEnum = Field(default=..., description="""Row kind — either a FIX field (numeric Tag) or an embedded component (literal \"Component\" in the Tag column of the source table).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureLayoutRow']} })
    infra_layout_field_tag: Optional[int] = Field(default=None, description="""FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureLayoutRow']} })
    infra_layout_element_name: str = Field(default=..., description="""Element name as printed in the Name column — either the FIX field name (e.g. ApplReqID) or the component name (e.g. StandardHeader, ApplIDRequestGrp).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureLayoutRow']} })
    infra_layout_required: Optional[bool] = Field(default=None, description="""Whether the field or component is required, as printed in the Req’d column of the source layout table (\"Y\" / \"N\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureLayoutRow']} })
    infra_layout_description: Optional[str] = Field(default=None, description="""Free-text content of the Description column of the row (may be empty).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureLayoutRow']} })
    infra_layout_nested: Optional[bool] = Field(default=False, description="""Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the \"→\" arrow in the source table).""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureLayoutRow'], 'ifabsent': 'False'} })


class StandardResponseMapping(ConfiguredBaseModel):
    """
    One row of a \"Standard Responses for <area> Messages\" table mapping a request message to its appropriate response(s).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:StandardResponseMapping',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure_workflow'],
         'related_mappings': ['fluxnova_bpm_platform:Task'],
         'slot_usage': {'appropriate_responses': {'name': 'appropriate_responses',
                                                  'required': True},
                        'category_label': {'name': 'category_label', 'required': True},
                        'fix_message': {'name': 'fix_message', 'required': True}}})

    category_label: str = Field(default=..., description="""Category label as printed in the source table (free text; may include parenthesised sub-categories such as \"Single General Order Handling\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['StandardResponseMapping', 'ApplicationMessageReferenceKey']} })
    fix_message: str = Field(default=..., description="""FIX message name with MsgType in parentheses, e.g. AllocationInstruction(35=J).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StandardResponseMapping', 'ApplicationMessageReferenceKey']} })
    appropriate_responses: str = Field(default=..., description="""Free-text appropriate-response cell from the Standard Responses tables.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StandardResponseMapping']} })


class ApplicationMessageReferenceKey(ConfiguredBaseModel):
    """
    One row of a \"Key Fields for <area> Application Message References\" table identifying the field whose value is copied into BusinessRejectRefID(379).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:ApplicationMessageReferenceKey',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure_workflow'],
         'slot_usage': {'business_reject_ref_id_value': {'name': 'business_reject_ref_id_value',
                                                         'required': True},
                        'category_label': {'name': 'category_label', 'required': True},
                        'fix_message': {'name': 'fix_message', 'required': True}}})

    category_label: str = Field(default=..., description="""Category label as printed in the source table (free text; may include parenthesised sub-categories such as \"Single General Order Handling\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['StandardResponseMapping', 'ApplicationMessageReferenceKey']} })
    fix_message: str = Field(default=..., description="""FIX message name with MsgType in parentheses, e.g. AllocationInstruction(35=J).""", json_schema_extra = { "linkml_meta": {'domain_of': ['StandardResponseMapping', 'ApplicationMessageReferenceKey']} })
    business_reject_ref_id_value: str = Field(default=..., description="""Source field copied into BusinessRejectRefID(379) when the target message lacks its own reject. May enumerate several alternatives joined by \"or\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['ApplicationMessageReferenceKey']} })


class BusinessRejectReasonDescription(ConfiguredBaseModel):
    """
    One entry of the BusinessRejectReason(380) code table.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:BusinessRejectReasonDescription',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure_workflow'],
         'related_mappings': ['iso27001:AuditFindingType'],
         'slot_usage': {'reject_reason_code': {'identifier': True,
                                               'name': 'reject_reason_code',
                                               'required': True},
                        'reject_reason_label': {'name': 'reject_reason_label',
                                                'required': True}}})

    reject_reason_code: int = Field(default=..., description="""Numeric code value of BusinessRejectReason(380).""", ge=0, le=999, json_schema_extra = { "linkml_meta": {'domain_of': ['BusinessRejectReasonDescription']} })
    reject_reason_label: str = Field(default=..., description="""Human-readable label of a BusinessRejectReason(380) code.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BusinessRejectReasonDescription']} })


class InfrastructureGlobalComponentReference(ConfiguredBaseModel):
    """
    A reference from the Infrastructure business area to a Global Component declared on the FIX Latest \"Global Components\" page. Records the component name, the FIX tags it contributes, and the Infrastructure categories and messages that embed it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'fix_infrastructure:InfrastructureGlobalComponentReference',
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure',
         'in_subset': ['infrastructure_organization'],
         'see_also': ['https://www.fixtrading.org/standards/fix-latest-online/global-components/'],
         'slot_usage': {'infra_global_component_name': {'identifier': True,
                                                        'name': 'infra_global_component_name',
                                                        'required': True},
                        'infra_global_component_used_in': {'name': 'infra_global_component_used_in',
                                                           'required': True}}})

    infra_global_component_name: InfrastructureGlobalComponentName = Field(default=..., description="""Name of a Global Component referenced from within the Infrastructure business area.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureGlobalComponentReference']} })
    infra_global_component_repetition: Optional[str] = Field(default=None, description="""Repetition indicator for the Global Component as it appears in the referenced Infrastructure messages.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureGlobalComponentReference']} })
    infra_global_component_field_tags: Optional[list[int]] = Field(default=None, description="""FIX tag numbers contributed by the referenced Global Component (as listed on the Global Components page).""", ge=0, json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureGlobalComponentReference']} })
    infra_global_component_field_names: Optional[list[str]] = Field(default=None, description="""Human-readable field names of the tags contributed by the referenced Global Component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureGlobalComponentReference']} })
    infra_global_component_used_in: list[InfrastructureCategoryEnum] = Field(default=..., description="""Infrastructure categories that reference the Global Component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureGlobalComponentReference']} })
    infra_global_component_msg_types: Optional[list[str]] = Field(default=None, description="""MsgType values within the Infrastructure business area that embed the referenced Global Component.""", json_schema_extra = { "linkml_meta": {'domain_of': ['InfrastructureGlobalComponentReference']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
FIXIntroduction.model_rebuild()
FIXProtocolLimited.model_rebuild()
FIXFamilyStandard.model_rebuild()
ExtensionPack.model_rebuild()
FIXDatatype.model_rebuild()
BusinessArea.model_rebuild()
MessageCategory.model_rebuild()
Field.model_rebuild()
Component.model_rebuild()
GlobalComponent.model_rebuild()
CommonComponent.model_rebuild()
SpecificComponent.model_rebuild()
Message.model_rebuild()
UDFTagRange.model_rebuild()
PreTradeBusinessArea.model_rebuild()
PreTradeMessageEntry.model_rebuild()
PreTradeComponentEntry.model_rebuild()
ComponentTableFootnote.model_rebuild()
PreTradeCategorySection.model_rebuild()
PreTradeMessageDetail.model_rebuild()
PreTradeComponentDetail.model_rebuild()
MessageGroup.model_rebuild()
CommonComponentDetail.model_rebuild()
PreTradeLayoutRow.model_rebuild()
TradeBusinessArea.model_rebuild()
TradeMessageEntry.model_rebuild()
TradeComponentEntry.model_rebuild()
TradeComponentTableFootnote.model_rebuild()
TradeCategorySection.model_rebuild()
TradeMessageDetail.model_rebuild()
TradeComponentDetail.model_rebuild()
TradeMessageGroup.model_rebuild()
TradeCommonComponentDetail.model_rebuild()
TradeLayoutRow.model_rebuild()
TradeOrdStatusPrecedenceEntry.model_rebuild()
TradeFragmentationEntry.model_rebuild()
TradeAppendix.model_rebuild()
TradeAppendixSection.model_rebuild()
PostTradeBusinessArea.model_rebuild()
PostTradeMessageEntry.model_rebuild()
PostTradeComponentEntry.model_rebuild()
PostTradeComponentTableFootnote.model_rebuild()
PostTradeCategorySection.model_rebuild()
PostTradeMessageGroup.model_rebuild()
PostTradeMessageDetail.model_rebuild()
PostTradeComponentDetail.model_rebuild()
PostTradeCommonComponentDetail.model_rebuild()
AllocationStatusDescription.model_rebuild()
AllocationFragmentationFieldMap.model_rebuild()
TradeCaptureReportUsage.model_rebuild()
TradeCaptureReportIdentifierRule.model_rebuild()
RegistrationStatusDescription.model_rebuild()
ClearingServicePostTradeProcessingFormat.model_rebuild()
PostTradeLayoutRow.model_rebuild()
InfrastructureBusinessArea.model_rebuild()
InfrastructureMessageEntry.model_rebuild()
InfrastructureComponentEntry.model_rebuild()
InfrastructureComponentTableFootnote.model_rebuild()
InfrastructureCategorySection.model_rebuild()
InfrastructureMessageDetail.model_rebuild()
InfrastructureComponentDetail.model_rebuild()
InfrastructureLayoutRow.model_rebuild()
StandardResponseMapping.model_rebuild()
ApplicationMessageReferenceKey.model_rebuild()
BusinessRejectReasonDescription.model_rebuild()
InfrastructureGlobalComponentReference.model_rebuild()
