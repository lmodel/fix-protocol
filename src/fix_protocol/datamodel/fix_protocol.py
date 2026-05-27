# Auto generated from fix_protocol.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-27T23:02:59
# Schema: fix-protocol
#
# id: https://w3id.org/lmodel/fix-protocol
# description: FIX Protocol - LinkML Schema
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate

# fix-protocol patch: enum hash/eq
from linkml_runtime.linkml_model.meta import PermissibleValue as _PV
from linkml_runtime.utils.enumerations import EnumDefinitionImpl as _EDI
if not getattr(_PV, "_fix_protocol_patched", False):
    _orig_pv_eq = _PV.__eq__
    def _pv_eq(self, other):
        if isinstance(other, str):
            return self.text == other
        return _orig_pv_eq(self, other)
    _PV.__eq__ = _pv_eq
    _PV.__hash__ = lambda self: hash(self.text)
    _PV._fix_protocol_patched = True
if not getattr(_EDI, "_fix_protocol_patched", False):
    _orig_edi_eq = _EDI.__eq__
    def _edi_eq(self, other):
        if isinstance(other, str):
            return str(self) == other
        return _orig_edi_eq(self, other)
    # Bypass EnumDefinitionMeta.__setattr__, which routes assignments on
    # enum subclasses through PermissibleValue handling.
    type.__setattr__(_EDI, "__eq__", _edi_eq)
    type.__setattr__(_EDI, "__hash__", lambda self: hash(str(self)))
    type.__setattr__(_EDI, "_fix_protocol_patched", True)

metamodel_version = "1.11.0"
version = None

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
COMMON_DOMAIN_MODEL = CurieNamespace('common_domain_model', 'https://w3id.org/lmodel/common-domain-model/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EXAMPLE = CurieNamespace('example', 'http://www.example.org/rdf#')
FIX_BASE = CurieNamespace('fix_base', 'https://w3id.org/lmodel/fix-protocol/fix-base/')
FIX_GLOBAL_COMPONENTS = CurieNamespace('fix_global_components', 'https://w3id.org/lmodel/fix-protocol/fix-global-components/')
FIX_INFRASTRUCTURE = CurieNamespace('fix_infrastructure', 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure/')
FIX_ORCHESTRA = CurieNamespace('fix_orchestra', 'https://w3id.org/lmodel/fix-orchestra/')
FIX_POST_TRADE = CurieNamespace('fix_post_trade', 'https://w3id.org/lmodel/fix-protocol/fix-post-trade/')
FIX_PRE_TRADE = CurieNamespace('fix_pre_trade', 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade/')
FIX_PROTOCOL = CurieNamespace('fix_protocol', 'https://w3id.org/lmodel/fix-protocol/')
FIX_SBE = CurieNamespace('fix_sbe', 'https://w3id.org/lmodel/fix-sbe/')
FIX_TRADE = CurieNamespace('fix_trade', 'https://w3id.org/lmodel/fix-protocol/fix-trade/')
FIXP = CurieNamespace('fixp', 'https://w3id.org/lmodel/fixp/')
FLUXNOVA_BPM_PLATFORM = CurieNamespace('fluxnova_bpm_platform', 'https://w3id.org/lmodel/fluxnova-bpm-platform/')
ISO10383 = CurieNamespace('iso10383', 'https://www.iso.org/standard/61067.html#')
ISO11404 = CurieNamespace('iso11404', 'https://www.iso.org/standard/39479.html#')
ISO17442 = CurieNamespace('iso17442', 'https://www.iso.org/standard/78829.html#')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
ISO3166 = CurieNamespace('iso3166', 'https://www.iso.org/iso-3166-country-codes.html#')
ISO4217 = CurieNamespace('iso4217', 'https://www.iso.org/iso-4217-currency-codes.html#')
ISO639 = CurieNamespace('iso639', 'https://www.iso.org/iso-639-language-codes.html#')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = FIX_PROTOCOL


# Types
class TagNumber(int):
    """ A FIX field tag number (a positive integer). """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "TagNumber"
    type_model_uri = FIX_PROTOCOL.TagNumber


class ExtensionPackNumber(int):
    """ Sequential identifier of a FIX Extension Pack. Carried on the wire in ApplExtID(1156). """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "ExtensionPackNumber"
    type_model_uri = FIX_PROTOCOL.ExtensionPackNumber




# Enumerations
class StandardLayer(EnumDefinitionImpl):
    """
    Layer of the FIX Technical Standard Stack.
    """
    APPLICATION = PermissibleValue(text="APPLICATION")
    ENCODING = PermissibleValue(text="ENCODING")
    SESSION = PermissibleValue(text="SESSION")

    _defn = EnumDefinition(
        name="StandardLayer",
        description="Layer of the FIX Technical Standard Stack.",
    )

class ExtensionPackSize(EnumDefinitionImpl):
    """
    Qualitative size indicator for an Extension Pack.
    """
    XXS = PermissibleValue(text="XXS")
    XS = PermissibleValue(text="XS")
    S = PermissibleValue(text="S")
    M = PermissibleValue(text="M")
    L = PermissibleValue(text="L")
    XL = PermissibleValue(text="XL")
    XXL = PermissibleValue(text="XXL")

    _defn = EnumDefinition(
        name="ExtensionPackSize",
        description="Qualitative size indicator for an Extension Pack.",
    )

class GlobalComponentBusinessAreaEnum(EnumDefinitionImpl):
    """
    FIX business areas that may reference a Global Component from the FIX Latest "Global Components" page.
    """
    PRE_TRADE = PermissibleValue(text="PRE_TRADE")
    TRADE = PermissibleValue(text="TRADE")
    POST_TRADE = PermissibleValue(text="POST_TRADE")
    INFRASTRUCTURE = PermissibleValue(text="INFRASTRUCTURE")

    _defn = EnumDefinition(
        name="GlobalComponentBusinessAreaEnum",
        description="""FIX business areas that may reference a Global Component from the FIX Latest \"Global Components\" page.""",
    )

class BusinessAreaEnum(EnumDefinitionImpl):
    """
    Top-level business areas of the FIX Latest specification.
    """
    INTRODUCTION = PermissibleValue(text="INTRODUCTION")
    PRE_TRADE = PermissibleValue(text="PRE_TRADE")
    TRADE = PermissibleValue(text="TRADE")
    POST_TRADE = PermissibleValue(text="POST_TRADE")
    INFRASTRUCTURE = PermissibleValue(text="INFRASTRUCTURE")

    _defn = EnumDefinition(
        name="BusinessAreaEnum",
        description="Top-level business areas of the FIX Latest specification.",
    )

class MessageCategoryEnum(EnumDefinitionImpl):
    """
    Message categories defined within FIX Latest business areas.
    """
    INDICATION = PermissibleValue(text="INDICATION")
    EVENT_COMMUNICATION = PermissibleValue(text="EVENT_COMMUNICATION")
    QUOTATION_NEGOTIATION = PermissibleValue(text="QUOTATION_NEGOTIATION")
    MARKET_DATA = PermissibleValue(text="MARKET_DATA")
    MARKET_STRUCTURE_REFERENCE_DATA = PermissibleValue(text="MARKET_STRUCTURE_REFERENCE_DATA")
    SECURITIES_REFERENCE_DATA = PermissibleValue(text="SECURITIES_REFERENCE_DATA")
    PARTIES_REFERENCE_DATA = PermissibleValue(text="PARTIES_REFERENCE_DATA")
    PARTIES_ACTION = PermissibleValue(text="PARTIES_ACTION")
    SINGLE_GENERAL_ORDER_HANDLING = PermissibleValue(text="SINGLE_GENERAL_ORDER_HANDLING")
    ORDER_MASS_HANDLING = PermissibleValue(text="ORDER_MASS_HANDLING")
    CROSS_ORDERS = PermissibleValue(text="CROSS_ORDERS")
    MULTILEG_ORDERS = PermissibleValue(text="MULTILEG_ORDERS")
    LIST_PROGRAM_BASKET_TRADING = PermissibleValue(text="LIST_PROGRAM_BASKET_TRADING")
    ALLOCATION_AND_READY_TO_BOOK = PermissibleValue(text="ALLOCATION_AND_READY_TO_BOOK")
    CONFIRMATION = PermissibleValue(text="CONFIRMATION")
    SETTLEMENT_INSTRUCTIONS = PermissibleValue(text="SETTLEMENT_INSTRUCTIONS")
    TRADE_CAPTURE_REPORTING = PermissibleValue(text="TRADE_CAPTURE_REPORTING")
    REGISTRATION_INSTRUCTIONS = PermissibleValue(text="REGISTRATION_INSTRUCTIONS")
    POSITIONS_MAINTENANCE = PermissibleValue(text="POSITIONS_MAINTENANCE")
    COLLATERAL_MANAGEMENT = PermissibleValue(text="COLLATERAL_MANAGEMENT")
    MARGIN_REQUIREMENT_MANAGEMENT = PermissibleValue(text="MARGIN_REQUIREMENT_MANAGEMENT")
    ACCOUNT_REPORTING = PermissibleValue(text="ACCOUNT_REPORTING")
    TRADE_MANAGEMENT = PermissibleValue(text="TRADE_MANAGEMENT")
    PAY_MANAGEMENT = PermissibleValue(text="PAY_MANAGEMENT")
    SETTLEMENT_STATUS_MANAGEMENT = PermissibleValue(text="SETTLEMENT_STATUS_MANAGEMENT")
    BUSINESS_MESSAGE_REJECTS = PermissibleValue(text="BUSINESS_MESSAGE_REJECTS")
    NETWORK_STATUS_COMMUNICATION = PermissibleValue(text="NETWORK_STATUS_COMMUNICATION")
    USER_MANAGEMENT = PermissibleValue(text="USER_MANAGEMENT")
    APPLICATION_SEQUENCING = PermissibleValue(text="APPLICATION_SEQUENCING")

    _defn = EnumDefinition(
        name="MessageCategoryEnum",
        description="Message categories defined within FIX Latest business areas.",
    )

class ComponentScope(EnumDefinitionImpl):
    """
    Sharing scope of a FIX component.
    """
    GLOBAL = PermissibleValue(text="GLOBAL")
    COMMON = PermissibleValue(text="COMMON")
    SPECIFIC = PermissibleValue(text="SPECIFIC")

    _defn = EnumDefinition(
        name="ComponentScope",
        description="Sharing scope of a FIX component.",
    )

class ComponentGroup(EnumDefinitionImpl):
    """
    Thematic grouping under which a Global Component is presented.
    """
    SECURITIES = PermissibleValue(text="SECURITIES")
    LEG_SECURITIES = PermissibleValue(text="LEG_SECURITIES")
    UNDERLYING_SECURITIES = PermissibleValue(text="UNDERLYING_SECURITIES")
    PARTIES = PermissibleValue(text="PARTIES")
    ORDERS_AND_QUOTES = PermissibleValue(text="ORDERS_AND_QUOTES")
    TRADES = PermissibleValue(text="TRADES")
    COMMISSIONS_AND_FEES = PermissibleValue(text="COMMISSIONS_AND_FEES")
    FINANCING = PermissibleValue(text="FINANCING")
    PAYMENTS = PermissibleValue(text="PAYMENTS")
    STIPULATIONS = PermissibleValue(text="STIPULATIONS")
    HEADER_AND_TRAILER = PermissibleValue(text="HEADER_AND_TRAILER")
    MISCELLANEOUS = PermissibleValue(text="MISCELLANEOUS")

    _defn = EnumDefinition(
        name="ComponentGroup",
        description="Thematic grouping under which a Global Component is presented.",
    )

class FieldRequirement(EnumDefinitionImpl):
    """
    Required-status of a field within a message or component.
    """
    REQUIRED = PermissibleValue(text="REQUIRED")
    OPTIONAL = PermissibleValue(text="OPTIONAL")
    CONDITIONALLY_REQUIRED = PermissibleValue(text="CONDITIONALLY_REQUIRED")

    _defn = EnumDefinition(
        name="FieldRequirement",
        description="Required-status of a field within a message or component.",
    )

class ProductCoverage(EnumDefinitionImpl):
    """
    Product/asset classes covered by FIX at the application layer.
    """
    EQUITIES = PermissibleValue(text="EQUITIES")
    CIV = PermissibleValue(text="CIV")
    DERIVATIVES = PermissibleValue(text="DERIVATIVES")
    FIXED_INCOME = PermissibleValue(text="FIXED_INCOME")
    FOREIGN_EXCHANGE = PermissibleValue(text="FOREIGN_EXCHANGE")

    _defn = EnumDefinition(
        name="ProductCoverage",
        description="Product/asset classes covered by FIX at the application layer.",
    )

class FIXDatatypeName(EnumDefinitionImpl):
    """
    Names of FIX Protocol datatypes.
    """
    int = PermissibleValue(text="int")
    TagNum = PermissibleValue(text="TagNum")
    SeqNum = PermissibleValue(text="SeqNum")
    NumInGroup = PermissibleValue(text="NumInGroup")
    DayOfMonth = PermissibleValue(text="DayOfMonth")
    float = PermissibleValue(text="float")
    Qty = PermissibleValue(text="Qty")
    Price = PermissibleValue(text="Price")
    PriceOffset = PermissibleValue(text="PriceOffset")
    Amt = PermissibleValue(text="Amt")
    Percentage = PermissibleValue(text="Percentage")
    char = PermissibleValue(text="char")
    Boolean = PermissibleValue(text="Boolean")
    String = PermissibleValue(text="String")
    MultipleCharValue = PermissibleValue(text="MultipleCharValue")
    MultipleStringValue = PermissibleValue(text="MultipleStringValue")
    Country = PermissibleValue(
        text="Country",
        meaning=URIRef(str(ISO3166)))
    Currency = PermissibleValue(
        text="Currency",
        meaning=URIRef(str(ISO4217)))
    Exchange = PermissibleValue(
        text="Exchange",
        meaning=URIRef(str(ISO10383)))
    MonthYear = PermissibleValue(text="MonthYear")
    UTCTimestamp = PermissibleValue(text="UTCTimestamp")
    UTCTimeOnly = PermissibleValue(text="UTCTimeOnly")
    UTCDateOnly = PermissibleValue(text="UTCDateOnly")
    LocalMktDate = PermissibleValue(text="LocalMktDate")
    TZTimeOnly = PermissibleValue(text="TZTimeOnly")
    TZTimestamp = PermissibleValue(text="TZTimestamp")
    Length = PermissibleValue(text="Length")
    data = PermissibleValue(text="data")
    Tenor = PermissibleValue(text="Tenor")
    Reserved100Plus = PermissibleValue(text="Reserved100Plus")
    Reserved1000Plus = PermissibleValue(text="Reserved1000Plus")
    Reserved4000Plus = PermissibleValue(text="Reserved4000Plus")
    XMLData = PermissibleValue(text="XMLData")
    Language = PermissibleValue(
        text="Language",
        meaning=URIRef(str(ISO639)))
    LocalMktTime = PermissibleValue(text="LocalMktTime")

    _defn = EnumDefinition(
        name="FIXDatatypeName",
        description="Names of FIX Protocol datatypes.",
    )

class ISO11404ValueSpace(EnumDefinitionImpl):
    """
    ISO/IEC 11404:2007 General-Purpose Datatypes value space.
    """
    integer = PermissibleValue(text="integer")
    ordinal = PermissibleValue(text="ordinal")
    size = PermissibleValue(text="size")
    real = PermissibleValue(text="real")
    scaled = PermissibleValue(text="scaled")
    character = PermissibleValue(text="character")
    characterstring = PermissibleValue(text="characterstring")
    boolean = PermissibleValue(text="boolean")
    set = PermissibleValue(text="set")
    array = PermissibleValue(text="array")
    time = PermissibleValue(text="time")
    union = PermissibleValue(text="union")

    _defn = EnumDefinition(
        name="ISO11404ValueSpace",
        description="ISO/IEC 11404:2007 General-Purpose Datatypes value space.",
    )

class TenorUnit(EnumDefinitionImpl):
    """
    Time unit used in a FIX Tenor expression.
    """
    D = PermissibleValue(text="D")
    W = PermissibleValue(text="W")
    M = PermissibleValue(text="M")
    Y = PermissibleValue(text="Y")

    _defn = EnumDefinition(
        name="TenorUnit",
        description="Time unit used in a FIX Tenor expression.",
    )

class StandardEncodingName(EnumDefinitionImpl):
    """
    Named encodings of the FIX Family of Standards.
    """
    TAGVALUE = PermissibleValue(text="TAGVALUE")
    FIXML = PermissibleValue(text="FIXML")
    FAST = PermissibleValue(text="FAST")
    SBE = PermissibleValue(text="SBE")
    GPB = PermissibleValue(text="GPB")
    JSON = PermissibleValue(text="JSON")
    ASN_1 = PermissibleValue(text="ASN_1")

    _defn = EnumDefinition(
        name="StandardEncodingName",
        description="Named encodings of the FIX Family of Standards.",
    )

class SessionProtocolName(EnumDefinitionImpl):
    """
    Named session-layer protocols in the FIX Family of Standards.
    """
    FIX_4_2 = PermissibleValue(text="FIX_4_2")
    FIX4 = PermissibleValue(text="FIX4")
    FIXT = PermissibleValue(text="FIXT")
    LFIXT = PermissibleValue(text="LFIXT")
    FIXP = PermissibleValue(text="FIXP")
    SOFH = PermissibleValue(text="SOFH")
    FIXS = PermissibleValue(text="FIXS")
    AMQP = PermissibleValue(text="AMQP")

    _defn = EnumDefinition(
        name="SessionProtocolName",
        description="Named session-layer protocols in the FIX Family of Standards.",
    )

class TimePrecision(EnumDefinitionImpl):
    """
    Time-unit precision for FIX time-bearing datatypes.
    """
    SECOND = PermissibleValue(text="SECOND")
    MILLISECOND = PermissibleValue(text="MILLISECOND")
    MICROSECOND = PermissibleValue(text="MICROSECOND")
    NANOSECOND = PermissibleValue(text="NANOSECOND")
    PICOSECOND = PermissibleValue(text="PICOSECOND")
    DAY = PermissibleValue(text="DAY")

    _defn = EnumDefinition(
        name="TimePrecision",
        description="Time-unit precision for FIX time-bearing datatypes.",
    )

class FPLCommitteeRole(EnumDefinitionImpl):
    """
    Organizational bodies of FIX Protocol Limited.
    """
    GLOBAL_STEERING_COMMITTEE = PermissibleValue(text="GLOBAL_STEERING_COMMITTEE")
    GLOBAL_TECHNICAL_COMMITTEE = PermissibleValue(text="GLOBAL_TECHNICAL_COMMITTEE")
    GLOBAL_PRODUCT_COMMITTEE = PermissibleValue(text="GLOBAL_PRODUCT_COMMITTEE")
    GLOBAL_BUY_SIDE_COMMITTEE = PermissibleValue(text="GLOBAL_BUY_SIDE_COMMITTEE")
    GLOBAL_MEMBER_SERVICES_COMMITTEE = PermissibleValue(text="GLOBAL_MEMBER_SERVICES_COMMITTEE")
    REGIONAL_COMMITTEE = PermissibleValue(text="REGIONAL_COMMITTEE")

    _defn = EnumDefinition(
        name="FPLCommitteeRole",
        description="Organizational bodies of FIX Protocol Limited.",
    )

class FPLRegion(EnumDefinitionImpl):
    """
    Geographic regions for FPL Regional Committees.
    """
    AMERICAS = PermissibleValue(text="AMERICAS")
    ASIA_PACIFIC = PermissibleValue(text="ASIA_PACIFIC")
    EMEA = PermissibleValue(text="EMEA")
    JAPAN = PermissibleValue(text="JAPAN")

    _defn = EnumDefinition(
        name="FPLRegion",
        description="Geographic regions for FPL Regional Committees.",
    )

class FPLProductGroup(EnumDefinitionImpl):
    """
    Global Product Committees maintained by FIX Protocol Limited.
    """
    FIXED_INCOME_AND_CURRENCIES = PermissibleValue(text="FIXED_INCOME_AND_CURRENCIES")
    LISTED_PRODUCTS_AND_EXCHANGES = PermissibleValue(text="LISTED_PRODUCTS_AND_EXCHANGES")

    _defn = EnumDefinition(
        name="FPLProductGroup",
        description="Global Product Committees maintained by FIX Protocol Limited.",
    )

class FPLMemberType(EnumDefinitionImpl):
    """
    Categories of organizations represented in FPL membership.
    """
    BUY_SIDE_FIRM = PermissibleValue(text="BUY_SIDE_FIRM")
    SELL_SIDE_FIRM = PermissibleValue(text="SELL_SIDE_FIRM")
    EXCHANGE = PermissibleValue(text="EXCHANGE")
    ECN_ATS = PermissibleValue(text="ECN_ATS")
    UTILITY = PermissibleValue(text="UTILITY")
    VENDOR = PermissibleValue(text="VENDOR")
    OTHER_ASSOCIATION = PermissibleValue(text="OTHER_ASSOCIATION")

    _defn = EnumDefinition(
        name="FPLMemberType",
        description="Categories of organizations represented in FPL membership.",
    )

class UDFTagRangeUsage(EnumDefinitionImpl):
    """
    Usage policy assigned to a reserved range of UDF tag numbers.
    """
    INTER_FIRM_REGISTERED = PermissibleValue(text="INTER_FIRM_REGISTERED")
    INTER_FIRM_BILATERAL = PermissibleValue(text="INTER_FIRM_BILATERAL")
    GTC_REGULATORY_LEGACY = PermissibleValue(text="GTC_REGULATORY_LEGACY")
    WIP_CHINA = PermissibleValue(text="WIP_CHINA")
    INTERNAL_FIRM = PermissibleValue(text="INTERNAL_FIRM")
    GTC_OTC_DERIVATIVES = PermissibleValue(text="GTC_OTC_DERIVATIVES")
    GTC_RESERVED = PermissibleValue(text="GTC_RESERVED")

    _defn = EnumDefinition(
        name="UDFTagRangeUsage",
        description="Usage policy assigned to a reserved range of UDF tag numbers.",
    )

class PreTradeCategoryEnum(EnumDefinitionImpl):
    """
    The eight message categories of the FIX Latest Pre-Trade business area. Subset of MessageCategoryEnum.
    """
    INDICATION = PermissibleValue(text="INDICATION")
    EVENT_COMMUNICATION = PermissibleValue(text="EVENT_COMMUNICATION")
    QUOTATION_NEGOTIATION = PermissibleValue(text="QUOTATION_NEGOTIATION")
    MARKET_DATA = PermissibleValue(text="MARKET_DATA")
    MARKET_STRUCTURE_REFERENCE_DATA = PermissibleValue(text="MARKET_STRUCTURE_REFERENCE_DATA")
    SECURITIES_REFERENCE_DATA = PermissibleValue(text="SECURITIES_REFERENCE_DATA")
    PARTIES_REFERENCE_DATA = PermissibleValue(text="PARTIES_REFERENCE_DATA")
    PARTIES_ACTION = PermissibleValue(text="PARTIES_ACTION")

    _defn = EnumDefinition(
        name="PreTradeCategoryEnum",
        description="""The eight message categories of the FIX Latest Pre-Trade business area. Subset of MessageCategoryEnum.""",
    )

class ComponentRepetition(EnumDefinitionImpl):
    """
    Whether a FIX component is repeating or non-repeating.
    """
    REPEATING = PermissibleValue(text="REPEATING")
    NON_REPEATING = PermissibleValue(text="NON_REPEATING")

    _defn = EnumDefinition(
        name="ComponentRepetition",
        description="Whether a FIX component is repeating or non-repeating.",
    )

class PreTradeCommonComponentName(EnumDefinitionImpl):
    """
    Names of the Common Components declared at the top of the Pre-Trade business-area chapter.
    """
    AuctionTypeRuleGrp = PermissibleValue(text="AuctionTypeRuleGrp")
    BaseTradingRules = PermissibleValue(text="BaseTradingRules")
    ExecInstRules = PermissibleValue(text="ExecInstRules")
    InstrumentScope = PermissibleValue(text="InstrumentScope")
    InstrumentScopeGrp = PermissibleValue(text="InstrumentScopeGrp")
    InstrumentScopeSecurityAltIDGrp = PermissibleValue(text="InstrumentScopeSecurityAltIDGrp")
    LotTypeRules = PermissibleValue(text="LotTypeRules")
    MarketDataFeedTypes = PermissibleValue(text="MarketDataFeedTypes")
    MarketSegmentScopeGrp = PermissibleValue(text="MarketSegmentScopeGrp")
    MatchRules = PermissibleValue(text="MatchRules")
    OrdTypeRules = PermissibleValue(text="OrdTypeRules")
    PriceLimits = PermissibleValue(text="PriceLimits")
    PriceRangeRuleGrp = PermissibleValue(text="PriceRangeRuleGrp")
    QuoteSizeRuleGrp = PermissibleValue(text="QuoteSizeRuleGrp")
    RequestedPartyRoleGrp = PermissibleValue(text="RequestedPartyRoleGrp")
    RequestingPartyGrp = PermissibleValue(text="RequestingPartyGrp")
    RequestingPartySubGrp = PermissibleValue(text="RequestingPartySubGrp")
    RoutingGrp = PermissibleValue(text="RoutingGrp")
    TickRules = PermissibleValue(text="TickRules")
    TimeInForceRules = PermissibleValue(text="TimeInForceRules")
    TradingSessionRules = PermissibleValue(text="TradingSessionRules")

    _defn = EnumDefinition(
        name="PreTradeCommonComponentName",
        description="Names of the Common Components declared at the top of the Pre-Trade business-area chapter.",
    )

class QuoteModelEnum(EnumDefinitionImpl):
    """
    Quoting business models referenced in the Quotation / Negotiation category.
    """
    INDICATIVE = PermissibleValue(text="INDICATIVE")
    TRADEABLE = PermissibleValue(text="TRADEABLE")
    RESTRICTED_TRADEABLE = PermissibleValue(text="RESTRICTED_TRADEABLE")
    NEGOTIATION = PermissibleValue(text="NEGOTIATION")

    _defn = EnumDefinition(
        name="QuoteModelEnum",
        description="Quoting business models referenced in the Quotation / Negotiation category.",
    )

class PreTradeLayoutRowKindEnum(EnumDefinitionImpl):
    """
    Discriminator for a row in a Pre-Trade message- or component-layout table: either a FIX field (numeric Tag column)
    or an embedded component (literal "Component" in the Tag column).
    """
    FIELD = PermissibleValue(text="FIELD")
    COMPONENT = PermissibleValue(text="COMPONENT")

    _defn = EnumDefinition(
        name="PreTradeLayoutRowKindEnum",
        description="""Discriminator for a row in a Pre-Trade message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal \"Component\" in the Tag column).""",
    )

class TradeCategoryEnum(EnumDefinitionImpl):
    """
    The five message categories of the FIX Latest Trade (Orders and Executions) business area. Subset of
    MessageCategoryEnum.
    """
    SINGLE_GENERAL_ORDER_HANDLING = PermissibleValue(text="SINGLE_GENERAL_ORDER_HANDLING")
    ORDER_MASS_HANDLING = PermissibleValue(text="ORDER_MASS_HANDLING")
    CROSS_ORDER_HANDLING = PermissibleValue(text="CROSS_ORDER_HANDLING")
    MULTILEG_ORDER_HANDLING = PermissibleValue(text="MULTILEG_ORDER_HANDLING")
    LIST_PROGRAM_BASKET_TRADING = PermissibleValue(text="LIST_PROGRAM_BASKET_TRADING")

    _defn = EnumDefinition(
        name="TradeCategoryEnum",
        description="""The five message categories of the FIX Latest Trade (Orders and Executions) business area. Subset of MessageCategoryEnum.""",
    )

class TradeComponentRepetition(EnumDefinitionImpl):
    """
    Whether a FIX component is repeating or non-repeating.
    """
    REPEATING = PermissibleValue(text="REPEATING")
    NON_REPEATING = PermissibleValue(text="NON_REPEATING")

    _defn = EnumDefinition(
        name="TradeComponentRepetition",
        description="Whether a FIX component is repeating or non-repeating.",
    )

class TradeCommonComponentName(EnumDefinitionImpl):
    """
    Names of the Common Components declared at the bottom of the Trade business-area chapter — components used by
    messages across more than one Trade category.
    """
    DisclosureInstructionGrp = PermissibleValue(text="DisclosureInstructionGrp")
    DiscretionInstructions = PermissibleValue(text="DiscretionInstructions")
    PegInstructions = PermissibleValue(text="PegInstructions")
    PreAllocGrp = PermissibleValue(text="PreAllocGrp")
    StrategyParametersGrp = PermissibleValue(text="StrategyParametersGrp")
    TriggeringInstruction = PermissibleValue(text="TriggeringInstruction")

    _defn = EnumDefinition(
        name="TradeCommonComponentName",
        description="""Names of the Common Components declared at the bottom of the Trade business-area chapter — components used by messages across more than one Trade category.""",
    )

class TradeLayoutRowKindEnum(EnumDefinitionImpl):
    """
    Discriminator for a row in a Trade message- or component-layout table: either a FIX field (numeric Tag column) or
    an embedded component (literal "Component" in the Tag column).
    """
    FIELD = PermissibleValue(text="FIELD")
    COMPONENT = PermissibleValue(text="COMPONENT")

    _defn = EnumDefinition(
        name="TradeLayoutRowKindEnum",
        description="""Discriminator for a row in a Trade message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal \"Component\" in the Tag column).""",
    )

class PostTradeCategoryEnum(EnumDefinitionImpl):
    """
    The twelve message categories of the FIX Latest Post-Trade business area. Subset of MessageCategoryEnum.
    """
    ALLOCATION = PermissibleValue(text="ALLOCATION")
    CONFIRMATION = PermissibleValue(text="CONFIRMATION")
    SETTLEMENT_INSTRUCTION = PermissibleValue(text="SETTLEMENT_INSTRUCTION")
    TRADE_CAPTURE_REPORTING = PermissibleValue(text="TRADE_CAPTURE_REPORTING")
    REGISTRATION_INSTRUCTION = PermissibleValue(text="REGISTRATION_INSTRUCTION")
    POSITION_MAINTENANCE = PermissibleValue(text="POSITION_MAINTENANCE")
    COLLATERAL_MANAGEMENT = PermissibleValue(text="COLLATERAL_MANAGEMENT")
    MARGIN_REQUIREMENT_MANAGEMENT = PermissibleValue(text="MARGIN_REQUIREMENT_MANAGEMENT")
    ACCOUNT_REPORTING = PermissibleValue(text="ACCOUNT_REPORTING")
    TRADE_MANAGEMENT = PermissibleValue(text="TRADE_MANAGEMENT")
    PAY_MANAGEMENT = PermissibleValue(text="PAY_MANAGEMENT")
    SETTLEMENT_STATUS_MANAGEMENT = PermissibleValue(text="SETTLEMENT_STATUS_MANAGEMENT")

    _defn = EnumDefinition(
        name="PostTradeCategoryEnum",
        description="""The twelve message categories of the FIX Latest Post-Trade business area. Subset of MessageCategoryEnum.""",
    )

class PostTradeCommonComponentName(EnumDefinitionImpl):
    """
    Names of the Common Components declared at the top of the Post-Trade business-area chapter.
    """
    AllocCommissionDataGrp = PermissibleValue(text="AllocCommissionDataGrp")
    AllocRegulatoryTradeIDGrp = PermissibleValue(text="AllocRegulatoryTradeIDGrp")
    ClrInstGrp = PermissibleValue(text="ClrInstGrp")
    CollateralAmountGrp = PermissibleValue(text="CollateralAmountGrp")
    CollateralReinvestmentGrp = PermissibleValue(text="CollateralReinvestmentGrp")
    DlvyInstGrp = PermissibleValue(text="DlvyInstGrp")
    ExecAllocGrp = PermissibleValue(text="ExecAllocGrp")
    MarginAmount = PermissibleValue(text="MarginAmount")
    OrdAllocGrp = PermissibleValue(text="OrdAllocGrp")
    PositionAmountData = PermissibleValue(text="PositionAmountData")
    SettlDetails = PermissibleValue(text="SettlDetails")
    SettlInstructionsData = PermissibleValue(text="SettlInstructionsData")
    SettlParties = PermissibleValue(text="SettlParties")
    SettlPtysSubGrp = PermissibleValue(text="SettlPtysSubGrp")
    TradeAllocAmtGrp = PermissibleValue(text="TradeAllocAmtGrp")
    TransactionAttributeGrp = PermissibleValue(text="TransactionAttributeGrp")

    _defn = EnumDefinition(
        name="PostTradeCommonComponentName",
        description="Names of the Common Components declared at the top of the Post-Trade business-area chapter.",
    )

class AllocationScenarioEnum(EnumDefinitionImpl):
    """
    Communication options by which an Initiator may convey allocation instructions to a Respondent.
    """
    PRE_ALLOCATED_ORDER = PermissibleValue(text="PRE_ALLOCATED_ORDER")
    PRE_TRADE_ALLOCATION = PermissibleValue(text="PRE_TRADE_ALLOCATION")
    POST_TRADE_ALLOCATION = PermissibleValue(text="POST_TRADE_ALLOCATION")
    READY_TO_BOOK = PermissibleValue(text="READY_TO_BOOK")

    _defn = EnumDefinition(
        name="AllocationScenarioEnum",
        description="Communication options by which an Initiator may convey allocation instructions to a Respondent.",
    )

class AllocationStatusEnum(EnumDefinitionImpl):
    """
    AllocStatus(87) values used in allocation acknowledgement messages.
    """
    ACCEPTED = PermissibleValue(
        text="ACCEPTED",
        meaning=FIX_POST_TRADE["AllocStatus_0"])
    BLOCK_LEVEL_REJECT = PermissibleValue(
        text="BLOCK_LEVEL_REJECT",
        meaning=FIX_POST_TRADE["AllocStatus_1"])
    ACCOUNT_LEVEL_REJECT = PermissibleValue(
        text="ACCOUNT_LEVEL_REJECT",
        meaning=FIX_POST_TRADE["AllocStatus_2"])
    RECEIVED_NOT_YET_PROCESSED = PermissibleValue(
        text="RECEIVED_NOT_YET_PROCESSED",
        meaning=FIX_POST_TRADE["AllocStatus_3"])

    _defn = EnumDefinition(
        name="AllocationStatusEnum",
        description="AllocStatus(87) values used in allocation acknowledgement messages.",
    )

class AllocationTransactionTypeEnum(EnumDefinitionImpl):
    """
    AllocTransType(71) values.
    """
    NEW = PermissibleValue(
        text="NEW",
        meaning=FIX_POST_TRADE["AllocTransType_0"])
    REPLACE = PermissibleValue(
        text="REPLACE",
        meaning=FIX_POST_TRADE["AllocTransType_1"])
    CANCEL = PermissibleValue(
        text="CANCEL",
        meaning=FIX_POST_TRADE["AllocTransType_2"])

    _defn = EnumDefinition(
        name="AllocationTransactionTypeEnum",
        description="AllocTransType(71) values.",
    )

class PostTradeAllocationPricingMethodEnum(EnumDefinitionImpl):
    """
    Methods by which post-trade allocations may be computed.
    """
    AVERAGE_PRICE = PermissibleValue(text="AVERAGE_PRICE")
    EXECUTED_PRICE = PermissibleValue(text="EXECUTED_PRICE")

    _defn = EnumDefinition(
        name="PostTradeAllocationPricingMethodEnum",
        description="Methods by which post-trade allocations may be computed.",
    )

class TradeCaptureReportDirectionEnum(EnumDefinitionImpl):
    """
    Direction of a TradeCaptureReport relative to the marketplace.
    """
    INBOUND = PermissibleValue(text="INBOUND")
    OUTBOUND = PermissibleValue(text="OUTBOUND")

    _defn = EnumDefinition(
        name="TradeCaptureReportDirectionEnum",
        description="Direction of a TradeCaptureReport relative to the marketplace.",
    )

class TradeCaptureReportUsageEnum(EnumDefinitionImpl):
    """
    Documented usages of the TradeCaptureReport(35=AE) message.
    """
    RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS = PermissibleValue(text="RELAY_CONFIRMED_TRADES_TO_NON_PARTICIPANTS")
    RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES = PermissibleValue(text="RELAY_CONFIRMED_TRADES_TO_COUNTERPARTIES")
    REPORTING_PRIVATELY_NEGOTIATED_TRADES = PermissibleValue(text="REPORTING_PRIVATELY_NEGOTIATED_TRADES")
    REPORTING_FLOOR_OR_ROUTED_EXECUTIONS = PermissibleValue(text="REPORTING_FLOOR_OR_ROUTED_EXECUTIONS")
    REQUEST_TRADE_CANCEL_OR_AMENDMENT = PermissibleValue(text="REQUEST_TRADE_CANCEL_OR_AMENDMENT")

    _defn = EnumDefinition(
        name="TradeCaptureReportUsageEnum",
        description="Documented usages of the TradeCaptureReport(35=AE) message.",
    )

class TradeCaptureReportIdentifierRoleEnum(EnumDefinitionImpl):
    """
    Roles played by trade-capture-report identifier fields.
    """
    TRADE_REPORT_ID = PermissibleValue(text="TRADE_REPORT_ID")
    TRADE_ID = PermissibleValue(text="TRADE_ID")
    TRADE_REPORT_REF_ID = PermissibleValue(text="TRADE_REPORT_REF_ID")
    SECONDARY_TRADE_ID = PermissibleValue(text="SECONDARY_TRADE_ID")

    _defn = EnumDefinition(
        name="TradeCaptureReportIdentifierRoleEnum",
        description="Roles played by trade-capture-report identifier fields.",
    )

class RegistrationTransactionTypeEnum(EnumDefinitionImpl):
    """
    RegistTransType(514) values.
    """
    NEW = PermissibleValue(
        text="NEW",
        meaning=FIX_POST_TRADE["RegistTransType_0"])
    REPLACE = PermissibleValue(
        text="REPLACE",
        meaning=FIX_POST_TRADE["RegistTransType_1"])
    CANCEL = PermissibleValue(
        text="CANCEL",
        meaning=FIX_POST_TRADE["RegistTransType_2"])

    _defn = EnumDefinition(
        name="RegistrationTransactionTypeEnum",
        description="RegistTransType(514) values.",
    )

class RegistrationStatusEnum(EnumDefinitionImpl):
    """
    RegistStatus(506) values.
    """
    ACCEPTED = PermissibleValue(
        text="ACCEPTED",
        meaning=FIX_POST_TRADE["RegistStatus_A"])
    REJECTED = PermissibleValue(
        text="REJECTED",
        meaning=FIX_POST_TRADE["RegistStatus_R"])
    HELD = PermissibleValue(
        text="HELD",
        meaning=FIX_POST_TRADE["RegistStatus_H"])
    REMINDER = PermissibleValue(
        text="REMINDER",
        meaning=FIX_POST_TRADE["RegistStatus_N"])

    _defn = EnumDefinition(
        name="RegistrationStatusEnum",
        description="RegistStatus(506) values.",
    )

class SettlementInstructionModeEnum(EnumDefinitionImpl):
    """
    SettlInstMode(160) values relevant in Post-Trade.
    """
    STANDING_INSTRUCTIONS = PermissibleValue(
        text="STANDING_INSTRUCTIONS",
        meaning=FIX_POST_TRADE["SettlInstMode_1"])
    SPECIFIC_ORDER = PermissibleValue(
        text="SPECIFIC_ORDER",
        meaning=FIX_POST_TRADE["SettlInstMode_4"])
    REQUEST_REJECT = PermissibleValue(
        text="REQUEST_REJECT",
        meaning=FIX_POST_TRADE["SettlInstMode_5"])

    _defn = EnumDefinition(
        name="SettlementInstructionModeEnum",
        description="SettlInstMode(160) values relevant in Post-Trade.",
    )

class SettlementObligationModeEnum(EnumDefinitionImpl):
    """
    SettlObligMode(1159) values.
    """
    PRELIMINARY = PermissibleValue(
        text="PRELIMINARY",
        meaning=FIX_POST_TRADE["SettlObligMode_1"])
    FINAL = PermissibleValue(
        text="FINAL",
        meaning=FIX_POST_TRADE["SettlObligMode_2"])

    _defn = EnumDefinition(
        name="SettlementObligationModeEnum",
        description="SettlObligMode(1159) values.",
    )

class PositionMaintenanceActionEnum(EnumDefinitionImpl):
    """
    PosMaintAction(712) values.
    """
    NEW = PermissibleValue(
        text="NEW",
        meaning=FIX_POST_TRADE["PosMaintAction_1"])
    REPLACE = PermissibleValue(
        text="REPLACE",
        meaning=FIX_POST_TRADE["PosMaintAction_2"])
    CANCEL = PermissibleValue(
        text="CANCEL",
        meaning=FIX_POST_TRADE["PosMaintAction_3"])
    REVERSE = PermissibleValue(
        text="REVERSE",
        meaning=FIX_POST_TRADE["PosMaintAction_4"])

    _defn = EnumDefinition(
        name="PositionMaintenanceActionEnum",
        description="PosMaintAction(712) values.",
    )

class ClearingServiceForPositionManagementEnum(EnumDefinitionImpl):
    """
    Business functions invokable via the Position Management Clearing Services.
    """
    POSITION_CHANGE_SUBMISSION = PermissibleValue(text="POSITION_CHANGE_SUBMISSION")
    POSITION_ADJUSTMENT = PermissibleValue(text="POSITION_ADJUSTMENT")
    EXERCISE_NOTICE = PermissibleValue(text="EXERCISE_NOTICE")
    ABANDONMENT_NOTICE = PermissibleValue(text="ABANDONMENT_NOTICE")
    MARGIN_DISPOSITION = PermissibleValue(text="MARGIN_DISPOSITION")
    POSITION_PLEDGE = PermissibleValue(text="POSITION_PLEDGE")
    REQUEST_FOR_POSITION = PermissibleValue(text="REQUEST_FOR_POSITION")

    _defn = EnumDefinition(
        name="ClearingServiceForPositionManagementEnum",
        description="Business functions invokable via the Position Management Clearing Services.",
    )

class ClearingServiceForPostTradeProcessingEnum(EnumDefinitionImpl):
    """
    Message-format families used by the Post-Trade Processing Clearing Services.
    """
    ETP = PermissibleValue(text="ETP")
    GIVE_UP = PermissibleValue(text="GIVE_UP")
    EXCHANGE_FOR_PHYSICAL = PermissibleValue(text="EXCHANGE_FOR_PHYSICAL")
    AVERAGE_PRICE_SYSTEM = PermissibleValue(text="AVERAGE_PRICE_SYSTEM")
    MUTUAL_OFFSET_SYSTEM = PermissibleValue(text="MUTUAL_OFFSET_SYSTEM")
    TRADE_ENTRY_EDIT = PermissibleValue(text="TRADE_ENTRY_EDIT")

    _defn = EnumDefinition(
        name="ClearingServiceForPostTradeProcessingEnum",
        description="Message-format families used by the Post-Trade Processing Clearing Services.",
    )

class CollateralManagementUsageEnum(EnumDefinitionImpl):
    """
    Documented uses of the Collateral Management messages.
    """
    SECURITIES_FINANCING_COLLATERALIZATION = PermissibleValue(text="SECURITIES_FINANCING_COLLATERALIZATION")
    CLEARING_HOUSE_COLLATERALIZATION = PermissibleValue(text="CLEARING_HOUSE_COLLATERALIZATION")

    _defn = EnumDefinition(
        name="CollateralManagementUsageEnum",
        description="Documented uses of the Collateral Management messages.",
    )

class CollateralAssignmentPurposeEnum(EnumDefinitionImpl):
    """
    Purposes for which a CollateralAssignment may be sent.
    """
    ASSIGN_INITIAL_COLLATERAL = PermissibleValue(text="ASSIGN_INITIAL_COLLATERAL")
    REPLENISH_COLLATERAL = PermissibleValue(text="REPLENISH_COLLATERAL")
    REPLACE_OR_SUBSTITUTE_COLLATERAL = PermissibleValue(text="REPLACE_OR_SUBSTITUTE_COLLATERAL")

    _defn = EnumDefinition(
        name="CollateralAssignmentPurposeEnum",
        description="Purposes for which a CollateralAssignment may be sent.",
    )

class AllocationRoleEnum(EnumDefinitionImpl):
    """
    Role labels used throughout the Allocation category prose to designate the sender and receiver of an
    AllocationInstruction.
    """
    INITIATOR = PermissibleValue(text="INITIATOR")
    RESPONDENT = PermissibleValue(text="RESPONDENT")

    _defn = EnumDefinition(
        name="AllocationRoleEnum",
        description="""Role labels used throughout the Allocation category prose to designate the sender and receiver of an AllocationInstruction.""",
    )

class MatchStatusEnum(EnumDefinitionImpl):
    """
    MatchStatus(573) values referenced in Post-Trade prose.
    """
    COMPARED_MATCHED_OR_AFFIRMED = PermissibleValue(
        text="COMPARED_MATCHED_OR_AFFIRMED",
        meaning=FIX_POST_TRADE["MatchStatus_0"])
    UNCOMPARED_UNMATCHED_OR_UNAFFIRMED = PermissibleValue(
        text="UNCOMPARED_UNMATCHED_OR_UNAFFIRMED",
        meaning=FIX_POST_TRADE["MatchStatus_1"])

    _defn = EnumDefinition(
        name="MatchStatusEnum",
        description="MatchStatus(573) values referenced in Post-Trade prose.",
    )

class PostTradeLayoutRowKindEnum(EnumDefinitionImpl):
    """
    Discriminator for a row in a Post-Trade message- or component-layout table: either a FIX field (numeric Tag
    column) or an embedded component (literal "Component" in the Tag column).
    """
    FIELD = PermissibleValue(text="FIELD")
    COMPONENT = PermissibleValue(text="COMPONENT")

    _defn = EnumDefinition(
        name="PostTradeLayoutRowKindEnum",
        description="""Discriminator for a row in a Post-Trade message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal \"Component\" in the Tag column).""",
    )

class InfrastructureCategoryEnum(EnumDefinitionImpl):
    """
    The four message categories of the FIX Latest Infrastructure business area. Subset of MessageCategoryEnum.
    """
    BUSINESS_MESSAGE_REJECTS = PermissibleValue(text="BUSINESS_MESSAGE_REJECTS")
    NETWORK_STATUS_COMMUNICATION = PermissibleValue(text="NETWORK_STATUS_COMMUNICATION")
    USER_MANAGEMENT = PermissibleValue(text="USER_MANAGEMENT")
    APPLICATION_SEQUENCING = PermissibleValue(text="APPLICATION_SEQUENCING")

    _defn = EnumDefinition(
        name="InfrastructureCategoryEnum",
        description="""The four message categories of the FIX Latest Infrastructure business area. Subset of MessageCategoryEnum.""",
    )

class InfrastructureComponentName(EnumDefinitionImpl):
    """
    Names of the components defined in the Infrastructure business-area chapter. None of these are shared across
    categories within the area; footnotes 1–4 record that four of them were historically declared as common
    components.
    """
    ApplIDReportGrp = PermissibleValue(text="ApplIDReportGrp")
    ApplIDRequestAckGrp = PermissibleValue(text="ApplIDRequestAckGrp")
    ApplIDRequestGrp = PermissibleValue(text="ApplIDRequestGrp")
    CompIDReqGrp = PermissibleValue(text="CompIDReqGrp")
    CompIDStatGrp = PermissibleValue(text="CompIDStatGrp")
    ThrottleMsgTypeGrp = PermissibleValue(text="ThrottleMsgTypeGrp")
    ThrottleParamsGrp = PermissibleValue(text="ThrottleParamsGrp")
    UsernameGrp = PermissibleValue(text="UsernameGrp")

    _defn = EnumDefinition(
        name="InfrastructureComponentName",
        description="""Names of the components defined in the Infrastructure business-area chapter. None of these are shared across categories within the area; footnotes 1–4 record that four of them were historically declared as common components.""",
    )

class BusinessRejectReasonEnum(EnumDefinitionImpl):
    """
    Permissible values of BusinessRejectReason(380) on the BusinessMessageReject(35=j) message.
    """
    OTHER = PermissibleValue(
        text="OTHER",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_0"])
    UNKNOWN_ID = PermissibleValue(
        text="UNKNOWN_ID",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_1"])
    UNKNOWN_SECURITY = PermissibleValue(
        text="UNKNOWN_SECURITY",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_2"])
    UNSUPPORTED_MESSAGE_TYPE = PermissibleValue(
        text="UNSUPPORTED_MESSAGE_TYPE",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_3"])
    APPLICATION_NOT_AVAILABLE = PermissibleValue(
        text="APPLICATION_NOT_AVAILABLE",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_4"])
    CONDITIONALLY_REQUIRED_FIELD_MISSING = PermissibleValue(
        text="CONDITIONALLY_REQUIRED_FIELD_MISSING",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_5"])
    NOT_AUTHORISED = PermissibleValue(
        text="NOT_AUTHORISED",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_6"])
    DELIVER_TO_FIRM_NOT_AVAILABLE = PermissibleValue(
        text="DELIVER_TO_FIRM_NOT_AVAILABLE",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_7"])
    THROTTLE_LIMIT_EXCEEDED = PermissibleValue(
        text="THROTTLE_LIMIT_EXCEEDED",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_8"])
    THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT = PermissibleValue(
        text="THROTTLE_LIMIT_EXCEEDED_SESSION_DISCONNECT",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_9"])
    THROTTLED_MESSAGES_REJECTED_ON_REQUEST = PermissibleValue(
        text="THROTTLED_MESSAGES_REJECTED_ON_REQUEST",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_10"])
    INVALID_PRICE_INCREMENT = PermissibleValue(
        text="INVALID_PRICE_INCREMENT",
        meaning=FIX_INFRASTRUCTURE["BusinessRejectReason_18"])

    _defn = EnumDefinition(
        name="BusinessRejectReasonEnum",
        description="Permissible values of BusinessRejectReason(380) on the BusinessMessageReject(35=j) message.",
    )

class NetworkStatusScenarioEnum(EnumDefinitionImpl):
    """
    Network Status Communication usage scenarios documented in the chapter (Scenario A: hub-and-spoke; Scenario B:
    global brokerage region availability).
    """
    SCENARIO_A = PermissibleValue(text="SCENARIO_A")
    SCENARIO_B = PermissibleValue(text="SCENARIO_B")

    _defn = EnumDefinition(
        name="NetworkStatusScenarioEnum",
        description="""Network Status Communication usage scenarios documented in the chapter (Scenario A: hub-and-spoke; Scenario B: global brokerage region availability).""",
    )

class ApplicationMessageReportTypeEnum(EnumDefinitionImpl):
    """
    Documented uses of ApplicationMessageReport(35=BY) selected via ApplReportType(1426).
    """
    RESET = PermissibleValue(
        text="RESET",
        meaning=FIX_INFRASTRUCTURE["ApplReportType_0"])
    LAST_MESSAGE = PermissibleValue(
        text="LAST_MESSAGE",
        meaning=FIX_INFRASTRUCTURE["ApplReportType_1"])
    KEEP_ALIVE = PermissibleValue(text="KEEP_ALIVE")
    RESEND_COMPLETED = PermissibleValue(
        text="RESEND_COMPLETED",
        meaning=FIX_INFRASTRUCTURE["ApplReportType_3"])

    _defn = EnumDefinition(
        name="ApplicationMessageReportTypeEnum",
        description="Documented uses of ApplicationMessageReport(35=BY) selected via ApplReportType(1426).",
    )

class NetworkRequestTypeEnum(EnumDefinitionImpl):
    """
    Values of NetworkRequestType(935) explicitly cited in the NetworkCounterpartySystemStatusRequest(35=BC) prose.
    """
    SNAPSHOT = PermissibleValue(
        text="SNAPSHOT",
        meaning=FIX_INFRASTRUCTURE["NetworkRequestType_1"])
    STOP_SUBSCRIBING = PermissibleValue(
        text="STOP_SUBSCRIBING",
        meaning=FIX_INFRASTRUCTURE["NetworkRequestType_4"])

    _defn = EnumDefinition(
        name="NetworkRequestTypeEnum",
        description="""Values of NetworkRequestType(935) explicitly cited in the NetworkCounterpartySystemStatusRequest(35=BC) prose.""",
    )

class StandardResponseDirectionEnum(EnumDefinitionImpl):
    """
    Direction of a "Standard Response" mapping — which area the requesting message belongs to.
    """
    PRE_TRADE = PermissibleValue(text="PRE_TRADE")
    TRADE = PermissibleValue(text="TRADE")
    POST_TRADE = PermissibleValue(text="POST_TRADE")

    _defn = EnumDefinition(
        name="StandardResponseDirectionEnum",
        description="Direction of a \"Standard Response\" mapping — which area the requesting message belongs to.",
    )

class BusinessMessageReferenceDirectionEnum(EnumDefinitionImpl):
    """
    Direction of an "application message reference" key-field mapping — which area the referenced message belongs to.
    """
    PRE_TRADE = PermissibleValue(text="PRE_TRADE")
    TRADE = PermissibleValue(text="TRADE")
    POST_TRADE = PermissibleValue(text="POST_TRADE")

    _defn = EnumDefinition(
        name="BusinessMessageReferenceDirectionEnum",
        description="""Direction of an \"application message reference\" key-field mapping — which area the referenced message belongs to.""",
    )

class InfrastructureGlobalComponentName(EnumDefinitionImpl):
    """
    Names of the Global Components (declared in the FIX Latest "Global Components" page) that the Infrastructure
    business-area messages explicitly reference. Global Components are reusable component blocks used across two or
    more business areas.
    """
    ApplicationSequenceControl = PermissibleValue(text="ApplicationSequenceControl")

    _defn = EnumDefinition(
        name="InfrastructureGlobalComponentName",
        description="""Names of the Global Components (declared in the FIX Latest \"Global Components\" page) that the Infrastructure business-area messages explicitly reference. Global Components are reusable component blocks used across two or more business areas.""",
    )

class ApplicationSequenceControlFieldName(EnumDefinitionImpl):
    """
    Tags contributed by the ApplicationSequenceControl global component (used by Application Sequencing messages and
    by all FIX messages representing reports).
    """
    ApplID = PermissibleValue(text="ApplID")
    ApplSeqNum = PermissibleValue(text="ApplSeqNum")
    ApplLastSeqNum = PermissibleValue(text="ApplLastSeqNum")
    ApplResendFlag = PermissibleValue(text="ApplResendFlag")

    _defn = EnumDefinition(
        name="ApplicationSequenceControlFieldName",
        description="""Tags contributed by the ApplicationSequenceControl global component (used by Application Sequencing messages and by all FIX messages representing reports).""",
    )

class InfrastructureLayoutRowKindEnum(EnumDefinitionImpl):
    """
    Discriminator for a row in an Infrastructure message- or component-layout table: either a FIX field (numeric Tag
    column) or an embedded component (literal "Component" in the Tag column).
    """
    FIELD = PermissibleValue(text="FIELD")
    COMPONENT = PermissibleValue(text="COMPONENT")

    _defn = EnumDefinition(
        name="InfrastructureLayoutRowKindEnum",
        description="""Discriminator for a row in an Infrastructure message- or component-layout table: either a FIX field (numeric Tag column) or an embedded component (literal \"Component\" in the Tag column).""",
    )


# Class references
class FIXFamilyStandardId(extended_str):
    pass


class ExtensionPackNumber(extended_int):
    pass


FIXDatatypeDatatypeName = FIXDatatypeName
BusinessAreaArea = BusinessAreaEnum
MessageCategoryCategory = MessageCategoryEnum
class FieldTag(extended_int):
    pass


class ComponentComponentName(extended_str):
    pass


class GlobalComponentComponentName(ComponentComponentName):
    pass


class CommonComponentComponentName(ComponentComponentName):
    pass


class SpecificComponentComponentName(ComponentComponentName):
    pass


class MessageMsgType(extended_str):
    pass


class UDFTagRangeRangeId(extended_str):
    pass


class PreTradeMessageEntryMsgType(extended_str):
    pass


class PreTradeComponentEntryComponentName(extended_str):
    pass


class ComponentTableFootnoteFootnoteNumber(extended_int):
    pass


PreTradeCategorySectionCategory = PreTradeCategoryEnum
class PreTradeMessageDetailMsgType(extended_str):
    pass


class PreTradeComponentDetailComponentName(extended_str):
    pass


class MessageGroupGroupTitle(extended_str):
    pass


CommonComponentDetailComponentName = PreTradeCommonComponentName
class TradeMessageEntryMsgType(extended_str):
    pass


class TradeComponentEntryComponentName(extended_str):
    pass


class TradeComponentTableFootnoteTradeFootnoteNumber(extended_int):
    pass


TradeCategorySectionCategory = TradeCategoryEnum
class TradeMessageDetailMsgType(extended_str):
    pass


class TradeComponentDetailComponentName(extended_str):
    pass


class TradeMessageGroupTradeGroupTitle(extended_str):
    pass


TradeCommonComponentDetailComponentName = TradeCommonComponentName
class TradeOrdStatusPrecedenceEntryTradeOrdStatusLabel(extended_str):
    pass


class TradeFragmentationEntryTradeFragmentationMessage(extended_str):
    pass


class TradeAppendixSectionTradeAppendixCategory(extended_str):
    pass


class PostTradeMessageEntryMsgType(extended_str):
    pass


class PostTradeComponentEntryComponentName(extended_str):
    pass


class PostTradeComponentTableFootnoteFootnoteNumber(extended_int):
    pass


PostTradeCategorySectionCategory = PostTradeCategoryEnum
class PostTradeMessageGroupGroupTitle(extended_str):
    pass


class PostTradeMessageDetailMsgType(extended_str):
    pass


class PostTradeComponentDetailComponentName(extended_str):
    pass


PostTradeCommonComponentDetailComponentName = PostTradeCommonComponentName
class AllocationStatusDescriptionStatusCode(extended_str):
    pass


class AllocationFragmentationFieldMapMsgType(extended_str):
    pass


class TradeCaptureReportUsageStatusLabel(extended_str):
    pass


TradeCaptureReportIdentifierRuleIdentifierRole = TradeCaptureReportIdentifierRoleEnum
class RegistrationStatusDescriptionStatusCode(extended_str):
    pass


ClearingServicePostTradeProcessingFormatMessageFormat = ClearingServiceForPostTradeProcessingEnum
class InfrastructureMessageEntryMsgType(extended_str):
    pass


class InfrastructureComponentEntryComponentName(extended_str):
    pass


class InfrastructureComponentTableFootnoteFootnoteNumber(extended_int):
    pass


class BusinessRejectReasonDescriptionRejectReasonCode(extended_int):
    pass


InfrastructureGlobalComponentReferenceInfraGlobalComponentName = InfrastructureGlobalComponentName
@dataclass(repr=False)
class FIXIntroduction(YAMLRoot):
    """
    Container for the structural elements of the FIX Latest Introduction section. Tree root for instance data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["FIXIntroduction"]
    class_class_curie: ClassVar[str] = "fix_base:FIXIntroduction"
    class_name: ClassVar[str] = "FIXIntroduction"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FIXIntroduction

    published_version: Optional[str] = None
    published_date: Optional[Union[str, XSDDate]] = None
    publisher: Optional[str] = "FIX Global Technical Committee"
    preface: Optional[str] = None
    introduction_text: Optional[str] = None
    utc_leap_seconds_note: Optional[str] = None
    about_fpl: Optional[Union[dict, "FIXProtocolLimited"]] = None
    standards: Optional[Union[dict[Union[str, FIXFamilyStandardId], Union[dict, "FIXFamilyStandard"]], list[Union[dict, "FIXFamilyStandard"]]]] = empty_dict()
    extension_packs: Optional[Union[dict[Union[int, ExtensionPackNumber], Union[dict, "ExtensionPack"]], list[Union[dict, "ExtensionPack"]]]] = empty_dict()
    datatypes: Optional[Union[dict[Union[str, FIXDatatypeDatatypeName], Union[dict, "FIXDatatype"]], list[Union[dict, "FIXDatatype"]]]] = empty_dict()
    business_areas: Optional[Union[dict[Union[str, BusinessAreaArea], Union[dict, "BusinessArea"]], list[Union[dict, "BusinessArea"]]]] = empty_dict()
    global_components: Optional[Union[dict[Union[str, GlobalComponentComponentName], Union[dict, "GlobalComponent"]], list[Union[dict, "GlobalComponent"]]]] = empty_dict()
    udf_ranges: Optional[Union[dict[Union[str, UDFTagRangeRangeId], Union[dict, "UDFTagRange"]], list[Union[dict, "UDFTagRange"]]]] = empty_dict()
    product_coverage: Optional[Union[Union[str, "ProductCoverage"], list[Union[str, "ProductCoverage"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.published_version is not None and not isinstance(self.published_version, str):
            self.published_version = str(self.published_version)

        if self.published_date is not None and not isinstance(self.published_date, XSDDate):
            self.published_date = XSDDate(self.published_date)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.preface is not None and not isinstance(self.preface, str):
            self.preface = str(self.preface)

        if self.introduction_text is not None and not isinstance(self.introduction_text, str):
            self.introduction_text = str(self.introduction_text)

        if self.utc_leap_seconds_note is not None and not isinstance(self.utc_leap_seconds_note, str):
            self.utc_leap_seconds_note = str(self.utc_leap_seconds_note)

        if self.about_fpl is not None and not isinstance(self.about_fpl, FIXProtocolLimited):
            self.about_fpl = FIXProtocolLimited(**as_dict(self.about_fpl))

        self._normalize_inlined_as_list(slot_name="standards", slot_type=FIXFamilyStandard, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="extension_packs", slot_type=ExtensionPack, key_name="number", keyed=True)

        self._normalize_inlined_as_list(slot_name="datatypes", slot_type=FIXDatatype, key_name="datatype_name", keyed=True)

        self._normalize_inlined_as_list(slot_name="business_areas", slot_type=BusinessArea, key_name="area", keyed=True)

        self._normalize_inlined_as_list(slot_name="global_components", slot_type=GlobalComponent, key_name="component_name", keyed=True)

        self._normalize_inlined_as_list(slot_name="udf_ranges", slot_type=UDFTagRange, key_name="range_id", keyed=True)

        if not isinstance(self.product_coverage, list):
            self.product_coverage = [self.product_coverage] if self.product_coverage is not None else []
        self.product_coverage = [v if isinstance(v, ProductCoverage) else ProductCoverage(v) for v in self.product_coverage]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FIXProtocolLimited(YAMLRoot):
    """
    The organization that maintains the FIX Protocol specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["FIXProtocolLimited"]
    class_class_curie: ClassVar[str] = "fix_base:FIXProtocolLimited"
    class_name: ClassVar[str] = "FIXProtocolLimited"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FIXProtocolLimited

    brand_name: Optional[str] = "FIX Trading Community"
    legal_name: Optional[str] = "FIX Protocol Limited"
    website: Optional[Union[str, URI]] = "https://www.fixtrading.org"
    member_firms_url: Optional[Union[str, URI]] = None
    working_groups_url: Optional[Union[str, URI]] = None
    committees_url: Optional[Union[str, URI]] = None
    member_types: Optional[Union[Union[str, "FPLMemberType"], list[Union[str, "FPLMemberType"]]]] = empty_list()
    governance_bodies: Optional[Union[Union[str, "FPLCommitteeRole"], list[Union[str, "FPLCommitteeRole"]]]] = empty_list()
    product_committees: Optional[Union[Union[str, "FPLProductGroup"], list[Union[str, "FPLProductGroup"]]]] = empty_list()
    regional_committees: Optional[Union[Union[str, "FPLRegion"], list[Union[str, "FPLRegion"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.brand_name is not None and not isinstance(self.brand_name, str):
            self.brand_name = str(self.brand_name)

        if self.legal_name is not None and not isinstance(self.legal_name, str):
            self.legal_name = str(self.legal_name)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if self.member_firms_url is not None and not isinstance(self.member_firms_url, URI):
            self.member_firms_url = URI(self.member_firms_url)

        if self.working_groups_url is not None and not isinstance(self.working_groups_url, URI):
            self.working_groups_url = URI(self.working_groups_url)

        if self.committees_url is not None and not isinstance(self.committees_url, URI):
            self.committees_url = URI(self.committees_url)

        if not isinstance(self.member_types, list):
            self.member_types = [self.member_types] if self.member_types is not None else []
        self.member_types = [v if isinstance(v, FPLMemberType) else FPLMemberType(v) for v in self.member_types]

        if not isinstance(self.governance_bodies, list):
            self.governance_bodies = [self.governance_bodies] if self.governance_bodies is not None else []
        self.governance_bodies = [v if isinstance(v, FPLCommitteeRole) else FPLCommitteeRole(v) for v in self.governance_bodies]

        if not isinstance(self.product_committees, list):
            self.product_committees = [self.product_committees] if self.product_committees is not None else []
        self.product_committees = [v if isinstance(v, FPLProductGroup) else FPLProductGroup(v) for v in self.product_committees]

        if not isinstance(self.regional_committees, list):
            self.regional_committees = [self.regional_committees] if self.regional_committees is not None else []
        self.regional_committees = [v if isinstance(v, FPLRegion) else FPLRegion(v) for v in self.regional_committees]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FIXFamilyStandard(YAMLRoot):
    """
    A member standard of the FIX Family of Standards.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["FIXFamilyStandard"]
    class_class_curie: ClassVar[str] = "fix_base:FIXFamilyStandard"
    class_name: ClassVar[str] = "FIXFamilyStandard"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FIXFamilyStandard

    id: Union[str, FIXFamilyStandardId] = None
    name: str = None
    layer: Union[str, "StandardLayer"] = None
    description: Optional[str] = None
    acronym: Optional[str] = None
    see_also: Optional[Union[Union[str, URI], list[Union[str, URI]]]] = empty_list()
    version: Optional[str] = None
    session_profile: Optional[Union[str, "SessionProtocolName"]] = None
    encoding_name: Optional[Union[str, "StandardEncodingName"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FIXFamilyStandardId):
            self.id = FIXFamilyStandardId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.layer):
            self.MissingRequiredField("layer")
        if not isinstance(self.layer, StandardLayer):
            self.layer = StandardLayer(self.layer)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, URI) else URI(v) for v in self.see_also]

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.session_profile is not None and not isinstance(self.session_profile, SessionProtocolName):
            self.session_profile = SessionProtocolName(self.session_profile)

        if self.encoding_name is not None and not isinstance(self.encoding_name, StandardEncodingName):
            self.encoding_name = StandardEncodingName(self.encoding_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExtensionPack(YAMLRoot):
    """
    A unit of change to FIX Latest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["ExtensionPack"]
    class_class_curie: ClassVar[str] = "fix_base:ExtensionPack"
    class_name: ClassVar[str] = "ExtensionPack"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.ExtensionPack

    number: Union[int, ExtensionPackNumber] = None
    title: str = None
    size: Optional[Union[str, "ExtensionPackSize"]] = None
    enhancement_summary: Optional[str] = None
    applies_to_session_layer_only: Optional[Union[bool, Bool]] = False
    applies_to_fixml_only: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.number):
            self.MissingRequiredField("number")
        if not isinstance(self.number, ExtensionPackNumber):
            self.number = ExtensionPackNumber(self.number)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.size is not None and not isinstance(self.size, ExtensionPackSize):
            self.size = ExtensionPackSize(self.size)

        if self.enhancement_summary is not None and not isinstance(self.enhancement_summary, str):
            self.enhancement_summary = str(self.enhancement_summary)

        if self.applies_to_session_layer_only is not None and not isinstance(self.applies_to_session_layer_only, Bool):
            self.applies_to_session_layer_only = Bool(self.applies_to_session_layer_only)

        if self.applies_to_fixml_only is not None and not isinstance(self.applies_to_fixml_only, Bool):
            self.applies_to_fixml_only = Bool(self.applies_to_fixml_only)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FIXDatatype(YAMLRoot):
    """
    A FIX Protocol datatype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["FIXDatatype"]
    class_class_curie: ClassVar[str] = "fix_base:FIXDatatype"
    class_name: ClassVar[str] = "FIXDatatype"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FIXDatatype

    datatype_name: Union[str, "FIXDatatypeDatatypeName"] = None
    definition: str = None
    value_space: Optional[Union[Union[str, "ISO11404ValueSpace"], list[Union[str, "ISO11404ValueSpace"]]]] = empty_list()
    value_space_notes: Optional[str] = None
    deprecated_for_new_designs: Optional[Union[bool, Bool]] = False
    external_code_set: Optional[str] = None
    time_unit: Optional[Union[Union[str, "TimePrecision"], list[Union[str, "TimePrecision"]]]] = empty_list()
    radix: Optional[int] = None
    repertoire: Optional[str] = None
    index_lower_bound: Optional[int] = None
    index_upper_bound: Optional[int] = None
    minimum_value: Optional[int] = None
    maximum_value: Optional[int] = None
    footnote_numbers: Optional[Union[int, list[int]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.datatype_name):
            self.MissingRequiredField("datatype_name")
        if not isinstance(self.datatype_name, FIXDatatypeDatatypeName):
            self.datatype_name = FIXDatatypeDatatypeName(self.datatype_name)

        if self._is_empty(self.definition):
            self.MissingRequiredField("definition")
        if not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if not isinstance(self.value_space, list):
            self.value_space = [self.value_space] if self.value_space is not None else []
        self.value_space = [v if isinstance(v, ISO11404ValueSpace) else ISO11404ValueSpace(v) for v in self.value_space]

        if self.value_space_notes is not None and not isinstance(self.value_space_notes, str):
            self.value_space_notes = str(self.value_space_notes)

        if self.deprecated_for_new_designs is not None and not isinstance(self.deprecated_for_new_designs, Bool):
            self.deprecated_for_new_designs = Bool(self.deprecated_for_new_designs)

        if self.external_code_set is not None and not isinstance(self.external_code_set, str):
            self.external_code_set = str(self.external_code_set)

        if not isinstance(self.time_unit, list):
            self.time_unit = [self.time_unit] if self.time_unit is not None else []
        self.time_unit = [v if isinstance(v, TimePrecision) else TimePrecision(v) for v in self.time_unit]

        if self.radix is not None and not isinstance(self.radix, int):
            self.radix = int(self.radix)

        if self.repertoire is not None and not isinstance(self.repertoire, str):
            self.repertoire = str(self.repertoire)

        if self.index_lower_bound is not None and not isinstance(self.index_lower_bound, int):
            self.index_lower_bound = int(self.index_lower_bound)

        if self.index_upper_bound is not None and not isinstance(self.index_upper_bound, int):
            self.index_upper_bound = int(self.index_upper_bound)

        if self.minimum_value is not None and not isinstance(self.minimum_value, int):
            self.minimum_value = int(self.minimum_value)

        if self.maximum_value is not None and not isinstance(self.maximum_value, int):
            self.maximum_value = int(self.maximum_value)

        if not isinstance(self.footnote_numbers, list):
            self.footnote_numbers = [self.footnote_numbers] if self.footnote_numbers is not None else []
        self.footnote_numbers = [v if isinstance(v, int) else int(v) for v in self.footnote_numbers]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BusinessArea(YAMLRoot):
    """
    A top-level business area of the FIX Latest specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["BusinessArea"]
    class_class_curie: ClassVar[str] = "fix_base:BusinessArea"
    class_name: ClassVar[str] = "BusinessArea"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.BusinessArea

    area: Union[str, "BusinessAreaArea"] = None
    title: Optional[str] = None
    description: Optional[str] = None
    categories: Optional[Union[dict[Union[str, MessageCategoryCategory], Union[dict, "MessageCategory"]], list[Union[dict, "MessageCategory"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.area):
            self.MissingRequiredField("area")
        if not isinstance(self.area, BusinessAreaArea):
            self.area = BusinessAreaArea(self.area)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="categories", slot_type=MessageCategory, key_name="category", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MessageCategory(YAMLRoot):
    """
    A message category within a business area.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["MessageCategory"]
    class_class_curie: ClassVar[str] = "fix_base:MessageCategory"
    class_name: ClassVar[str] = "MessageCategory"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.MessageCategory

    category: Union[str, "MessageCategoryCategory"] = None
    business_area: Union[str, "BusinessAreaEnum"] = None
    title: Optional[str] = None
    description: Optional[str] = None
    messages: Optional[Union[dict[Union[str, MessageMsgType], Union[dict, "Message"]], list[Union[dict, "Message"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, MessageCategoryCategory):
            self.category = MessageCategoryCategory(self.category)

        if self._is_empty(self.business_area):
            self.MissingRequiredField("business_area")
        if not isinstance(self.business_area, BusinessAreaEnum):
            self.business_area = BusinessAreaEnum(self.business_area)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="messages", slot_type=Message, key_name="msg_type", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Field(YAMLRoot):
    """
    A FIX field — a uniquely tagged data element with a FIX datatype.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["Field"]
    class_class_curie: ClassVar[str] = "fix_base:Field"
    class_name: ClassVar[str] = "Field"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.Field

    tag: Union[int, FieldTag] = None
    field_name: str = None
    datatype: Union[str, "FIXDatatypeName"] = None
    description: Optional[str] = None
    requirement: Optional[Union[str, "FieldRequirement"]] = None
    is_user_defined: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.tag):
            self.MissingRequiredField("tag")
        if not isinstance(self.tag, FieldTag):
            self.tag = FieldTag(self.tag)

        if self._is_empty(self.field_name):
            self.MissingRequiredField("field_name")
        if not isinstance(self.field_name, str):
            self.field_name = str(self.field_name)

        if self._is_empty(self.datatype):
            self.MissingRequiredField("datatype")
        if not isinstance(self.datatype, FIXDatatypeName):
            self.datatype = FIXDatatypeName(self.datatype)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.requirement is not None and not isinstance(self.requirement, FieldRequirement):
            self.requirement = FieldRequirement(self.requirement)

        if self.is_user_defined is not None and not isinstance(self.is_user_defined, Bool):
            self.is_user_defined = Bool(self.is_user_defined)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Component(YAMLRoot):
    """
    A FIX component — a named set of related fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["Component"]
    class_class_curie: ClassVar[str] = "fix_base:Component"
    class_name: ClassVar[str] = "Component"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.Component

    component_name: Union[str, ComponentComponentName] = None
    scope: Union[str, "ComponentScope"] = None
    description: Optional[str] = None
    is_repeating_group: Optional[Union[bool, Bool]] = False
    fields: Optional[Union[dict[Union[int, FieldTag], Union[dict, Field]], list[Union[dict, Field]]]] = empty_dict()
    nested_components: Optional[Union[Union[str, ComponentComponentName], list[Union[str, ComponentComponentName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, ComponentComponentName):
            self.component_name = ComponentComponentName(self.component_name)

        if self._is_empty(self.scope):
            self.MissingRequiredField("scope")
        if not isinstance(self.scope, ComponentScope):
            self.scope = ComponentScope(self.scope)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.is_repeating_group is not None and not isinstance(self.is_repeating_group, Bool):
            self.is_repeating_group = Bool(self.is_repeating_group)

        self._normalize_inlined_as_list(slot_name="fields", slot_type=Field, key_name="tag", keyed=True)

        if not isinstance(self.nested_components, list):
            self.nested_components = [self.nested_components] if self.nested_components is not None else []
        self.nested_components = [v if isinstance(v, ComponentComponentName) else ComponentComponentName(v) for v in self.nested_components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GlobalComponent(Component):
    """
    A component shared by messages of two or more business areas.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["GlobalComponent"]
    class_class_curie: ClassVar[str] = "fix_base:GlobalComponent"
    class_name: ClassVar[str] = "GlobalComponent"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.GlobalComponent

    component_name: Union[str, GlobalComponentComponentName] = None
    component_group: Union[str, "ComponentGroup"] = None
    scope: Union[str, "ComponentScope"] = 'GLOBAL'
    applies_to_instrument: Optional[Union[bool, Bool]] = None
    applies_to_leg: Optional[Union[bool, Bool]] = None
    applies_to_underlying: Optional[Union[bool, Bool]] = None
    conceptually_identical_to: Optional[Union[str, list[str]]] = empty_list()
    gc_id: Optional[int] = None
    gc_referenced_in: Optional[Union[Union[str, "GlobalComponentBusinessAreaEnum"], list[Union[str, "GlobalComponentBusinessAreaEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, GlobalComponentComponentName):
            self.component_name = GlobalComponentComponentName(self.component_name)

        if self._is_empty(self.component_group):
            self.MissingRequiredField("component_group")
        if not isinstance(self.component_group, ComponentGroup):
            self.component_group = ComponentGroup(self.component_group)

        if self._is_empty(self.scope):
            self.MissingRequiredField("scope")
        if not isinstance(self.scope, ComponentScope):
            self.scope = ComponentScope(self.scope)

        if self.applies_to_instrument is not None and not isinstance(self.applies_to_instrument, Bool):
            self.applies_to_instrument = Bool(self.applies_to_instrument)

        if self.applies_to_leg is not None and not isinstance(self.applies_to_leg, Bool):
            self.applies_to_leg = Bool(self.applies_to_leg)

        if self.applies_to_underlying is not None and not isinstance(self.applies_to_underlying, Bool):
            self.applies_to_underlying = Bool(self.applies_to_underlying)

        if not isinstance(self.conceptually_identical_to, list):
            self.conceptually_identical_to = [self.conceptually_identical_to] if self.conceptually_identical_to is not None else []
        self.conceptually_identical_to = [v if isinstance(v, str) else str(v) for v in self.conceptually_identical_to]

        if self.gc_id is not None and not isinstance(self.gc_id, int):
            self.gc_id = int(self.gc_id)

        if not isinstance(self.gc_referenced_in, list):
            self.gc_referenced_in = [self.gc_referenced_in] if self.gc_referenced_in is not None else []
        self.gc_referenced_in = [v if isinstance(v, GlobalComponentBusinessAreaEnum) else GlobalComponentBusinessAreaEnum(v) for v in self.gc_referenced_in]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommonComponent(Component):
    """
    A component used only by messages within a single business area.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["CommonComponent"]
    class_class_curie: ClassVar[str] = "fix_base:CommonComponent"
    class_name: ClassVar[str] = "CommonComponent"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.CommonComponent

    component_name: Union[str, CommonComponentComponentName] = None
    business_area: Union[str, "BusinessAreaEnum"] = None
    scope: Union[str, "ComponentScope"] = 'COMMON'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, CommonComponentComponentName):
            self.component_name = CommonComponentComponentName(self.component_name)

        if self._is_empty(self.business_area):
            self.MissingRequiredField("business_area")
        if not isinstance(self.business_area, BusinessAreaEnum):
            self.business_area = BusinessAreaEnum(self.business_area)

        if self._is_empty(self.scope):
            self.MissingRequiredField("scope")
        if not isinstance(self.scope, ComponentScope):
            self.scope = ComponentScope(self.scope)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpecificComponent(Component):
    """
    A component used only by messages within a single category.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["SpecificComponent"]
    class_class_curie: ClassVar[str] = "fix_base:SpecificComponent"
    class_name: ClassVar[str] = "SpecificComponent"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.SpecificComponent

    component_name: Union[str, SpecificComponentComponentName] = None
    business_area: Union[str, "BusinessAreaEnum"] = None
    category: Union[str, "MessageCategoryEnum"] = None
    scope: Union[str, "ComponentScope"] = 'SPECIFIC'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, SpecificComponentComponentName):
            self.component_name = SpecificComponentComponentName(self.component_name)

        if self._is_empty(self.business_area):
            self.MissingRequiredField("business_area")
        if not isinstance(self.business_area, BusinessAreaEnum):
            self.business_area = BusinessAreaEnum(self.business_area)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, MessageCategoryEnum):
            self.category = MessageCategoryEnum(self.category)

        if self._is_empty(self.scope):
            self.MissingRequiredField("scope")
        if not isinstance(self.scope, ComponentScope):
            self.scope = ComponentScope(self.scope)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Message(YAMLRoot):
    """
    A FIX application message.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["Message"]
    class_class_curie: ClassVar[str] = "fix_base:Message"
    class_name: ClassVar[str] = "Message"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.Message

    msg_type: Union[str, MessageMsgType] = None
    message_name: str = None
    description: Optional[str] = None
    category: Optional[Union[str, "MessageCategoryEnum"]] = None
    fields: Optional[Union[dict[Union[int, FieldTag], Union[dict, Field]], list[Union[dict, Field]]]] = empty_dict()
    components: Optional[Union[Union[str, ComponentComponentName], list[Union[str, ComponentComponentName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, MessageMsgType):
            self.msg_type = MessageMsgType(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.category is not None and not isinstance(self.category, MessageCategoryEnum):
            self.category = MessageCategoryEnum(self.category)

        self._normalize_inlined_as_list(slot_name="fields", slot_type=Field, key_name="tag", keyed=True)

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, ComponentComponentName) else ComponentComponentName(v) for v in self.components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class UDFTagRange(YAMLRoot):
    """
    A reserved range of tag numbers for User Defined Fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_BASE["UDFTagRange"]
    class_class_curie: ClassVar[str] = "fix_base:UDFTagRange"
    class_name: ClassVar[str] = "UDFTagRange"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.UDFTagRange

    range_id: Union[str, UDFTagRangeRangeId] = None
    low_tag: int = None
    usage: Union[str, "UDFTagRangeUsage"] = None
    high_tag: Optional[int] = None
    description: Optional[str] = None
    requires_registration: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.range_id):
            self.MissingRequiredField("range_id")
        if not isinstance(self.range_id, UDFTagRangeRangeId):
            self.range_id = UDFTagRangeRangeId(self.range_id)

        if self._is_empty(self.low_tag):
            self.MissingRequiredField("low_tag")
        if not isinstance(self.low_tag, int):
            self.low_tag = int(self.low_tag)

        if self._is_empty(self.usage):
            self.MissingRequiredField("usage")
        if not isinstance(self.usage, UDFTagRangeUsage):
            self.usage = UDFTagRangeUsage(self.usage)

        if self.high_tag is not None and not isinstance(self.high_tag, int):
            self.high_tag = int(self.high_tag)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.requires_registration is not None and not isinstance(self.requires_registration, Bool):
            self.requires_registration = Bool(self.requires_registration)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreTradeBusinessArea(YAMLRoot):
    """
    Tree-root container for the Pre-Trade business area of FIX Latest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["PreTradeBusinessArea"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:PreTradeBusinessArea"
    class_name: ClassVar[str] = "PreTradeBusinessArea"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PreTradeBusinessArea

    area: Union[str, "BusinessAreaEnum"] = 'PRE_TRADE'
    title: Optional[str] = "Business Area Pre-Trade"
    published_version: Optional[str] = None
    publisher: Optional[str] = "FIX Global Technical Committee"
    introduction: Optional[str] = None
    diagram_conventions: Optional[str] = None
    messages_overview_note: Optional[str] = None
    messages: Optional[Union[dict[Union[str, PreTradeMessageEntryMsgType], Union[dict, "PreTradeMessageEntry"]], list[Union[dict, "PreTradeMessageEntry"]]]] = empty_dict()
    components_overview_note: Optional[str] = None
    components: Optional[Union[dict[Union[str, PreTradeComponentEntryComponentName], Union[dict, "PreTradeComponentEntry"]], list[Union[dict, "PreTradeComponentEntry"]]]] = empty_dict()
    common_components: Optional[Union[Union[str, "PreTradeCommonComponentName"], list[Union[str, "PreTradeCommonComponentName"]]]] = empty_list()
    common_component_details: Optional[Union[dict[Union[str, CommonComponentDetailComponentName], Union[dict, "CommonComponentDetail"]], list[Union[dict, "CommonComponentDetail"]]]] = empty_dict()
    footnotes: Optional[Union[dict[Union[int, ComponentTableFootnoteFootnoteNumber], Union[dict, "ComponentTableFootnote"]], list[Union[dict, "ComponentTableFootnote"]]]] = empty_dict()
    category_sections: Optional[Union[dict[Union[str, PreTradeCategorySectionCategory], Union[dict, "PreTradeCategorySection"]], list[Union[dict, "PreTradeCategorySection"]]]] = empty_dict()
    referenced_global_components: Optional[Union[Union[str, GlobalComponentComponentName], list[Union[str, GlobalComponentComponentName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.area):
            self.MissingRequiredField("area")
        if not isinstance(self.area, BusinessAreaEnum):
            self.area = BusinessAreaEnum(self.area)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.published_version is not None and not isinstance(self.published_version, str):
            self.published_version = str(self.published_version)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.introduction is not None and not isinstance(self.introduction, str):
            self.introduction = str(self.introduction)

        if self.diagram_conventions is not None and not isinstance(self.diagram_conventions, str):
            self.diagram_conventions = str(self.diagram_conventions)

        if self.messages_overview_note is not None and not isinstance(self.messages_overview_note, str):
            self.messages_overview_note = str(self.messages_overview_note)

        self._normalize_inlined_as_list(slot_name="messages", slot_type=PreTradeMessageEntry, key_name="msg_type", keyed=True)

        if self.components_overview_note is not None and not isinstance(self.components_overview_note, str):
            self.components_overview_note = str(self.components_overview_note)

        self._normalize_inlined_as_list(slot_name="components", slot_type=PreTradeComponentEntry, key_name="component_name", keyed=True)

        if not isinstance(self.common_components, list):
            self.common_components = [self.common_components] if self.common_components is not None else []
        self.common_components = [v if isinstance(v, PreTradeCommonComponentName) else PreTradeCommonComponentName(v) for v in self.common_components]

        self._normalize_inlined_as_list(slot_name="common_component_details", slot_type=CommonComponentDetail, key_name="component_name", keyed=True)

        self._normalize_inlined_as_list(slot_name="footnotes", slot_type=ComponentTableFootnote, key_name="footnote_number", keyed=True)

        self._normalize_inlined_as_list(slot_name="category_sections", slot_type=PreTradeCategorySection, key_name="category", keyed=True)

        if not isinstance(self.referenced_global_components, list):
            self.referenced_global_components = [self.referenced_global_components] if self.referenced_global_components is not None else []
        self.referenced_global_components = [v if isinstance(v, GlobalComponentComponentName) else GlobalComponentComponentName(v) for v in self.referenced_global_components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreTradeMessageEntry(YAMLRoot):
    """
    One row of the area-wide pre-trade messages table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["PreTradeMessageEntry"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:PreTradeMessageEntry"
    class_name: ClassVar[str] = "PreTradeMessageEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PreTradeMessageEntry

    msg_type: Union[str, PreTradeMessageEntryMsgType] = None
    message_name: str = None
    category: Union[str, "PreTradeCategoryEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, PreTradeMessageEntryMsgType):
            self.msg_type = PreTradeMessageEntryMsgType(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, PreTradeCategoryEnum):
            self.category = PreTradeCategoryEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreTradeComponentEntry(YAMLRoot):
    """
    One row of the area-wide pre-trade components table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["PreTradeComponentEntry"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:PreTradeComponentEntry"
    class_name: ClassVar[str] = "PreTradeComponentEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PreTradeComponentEntry

    component_name: Union[str, PreTradeComponentEntryComponentName] = None
    repetition: Union[str, "ComponentRepetition"] = None
    category: str = None
    is_common: Optional[Union[bool, Bool]] = False
    footnote_number: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, PreTradeComponentEntryComponentName):
            self.component_name = PreTradeComponentEntryComponentName(self.component_name)

        if self._is_empty(self.repetition):
            self.MissingRequiredField("repetition")
        if not isinstance(self.repetition, ComponentRepetition):
            self.repetition = ComponentRepetition(self.repetition)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, str):
            self.category = str(self.category)

        if self.is_common is not None and not isinstance(self.is_common, Bool):
            self.is_common = Bool(self.is_common)

        if self.footnote_number is not None and not isinstance(self.footnote_number, int):
            self.footnote_number = int(self.footnote_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComponentTableFootnote(YAMLRoot):
    """
    A footnote on the area-wide components table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["ComponentTableFootnote"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:ComponentTableFootnote"
    class_name: ClassVar[str] = "ComponentTableFootnote"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.ComponentTableFootnote

    footnote_number: Union[int, ComponentTableFootnoteFootnoteNumber] = None
    component_name: str = None
    introduced_in: str = None
    sole_category: Union[str, "PreTradeCategoryEnum"] = None
    text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.footnote_number):
            self.MissingRequiredField("footnote_number")
        if not isinstance(self.footnote_number, ComponentTableFootnoteFootnoteNumber):
            self.footnote_number = ComponentTableFootnoteFootnoteNumber(self.footnote_number)

        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, str):
            self.component_name = str(self.component_name)

        if self._is_empty(self.introduced_in):
            self.MissingRequiredField("introduced_in")
        if not isinstance(self.introduced_in, str):
            self.introduced_in = str(self.introduced_in)

        if self._is_empty(self.sole_category):
            self.MissingRequiredField("sole_category")
        if not isinstance(self.sole_category, PreTradeCategoryEnum):
            self.sole_category = PreTradeCategoryEnum(self.sole_category)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreTradeCategorySection(YAMLRoot):
    """
    A per-category sub-section of the Pre-Trade chapter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["PreTradeCategorySection"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:PreTradeCategorySection"
    class_name: ClassVar[str] = "PreTradeCategorySection"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PreTradeCategorySection

    category: Union[str, "PreTradeCategorySectionCategory"] = None
    title: Optional[str] = None
    description: Optional[str] = None
    quote_models: Optional[Union[Union[str, "QuoteModelEnum"], list[Union[str, "QuoteModelEnum"]]]] = empty_list()
    message_groups: Optional[Union[dict[Union[str, MessageGroupGroupTitle], Union[dict, "MessageGroup"]], list[Union[dict, "MessageGroup"]]]] = empty_dict()
    messages: Optional[Union[dict[Union[str, PreTradeMessageDetailMsgType], Union[dict, "PreTradeMessageDetail"]], list[Union[dict, "PreTradeMessageDetail"]]]] = empty_dict()
    category_components_note: Optional[str] = None
    category_specific_components: Optional[Union[dict[Union[str, PreTradeComponentDetailComponentName], Union[dict, "PreTradeComponentDetail"]], list[Union[dict, "PreTradeComponentDetail"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, PreTradeCategorySectionCategory):
            self.category = PreTradeCategorySectionCategory(self.category)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.quote_models, list):
            self.quote_models = [self.quote_models] if self.quote_models is not None else []
        self.quote_models = [v if isinstance(v, QuoteModelEnum) else QuoteModelEnum(v) for v in self.quote_models]

        self._normalize_inlined_as_list(slot_name="message_groups", slot_type=MessageGroup, key_name="group_title", keyed=True)

        self._normalize_inlined_as_list(slot_name="messages", slot_type=PreTradeMessageDetail, key_name="msg_type", keyed=True)

        if self.category_components_note is not None and not isinstance(self.category_components_note, str):
            self.category_components_note = str(self.category_components_note)

        self._normalize_inlined_as_list(slot_name="category_specific_components", slot_type=PreTradeComponentDetail, key_name="component_name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreTradeMessageDetail(YAMLRoot):
    """
    Per-category message description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["PreTradeMessageDetail"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:PreTradeMessageDetail"
    class_name: ClassVar[str] = "PreTradeMessageDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PreTradeMessageDetail

    msg_type: Union[str, PreTradeMessageDetailMsgType] = None
    message_name: str = None
    description: Optional[str] = None
    layout_url: Optional[Union[str, URI]] = None
    pre_layout_rows: Optional[Union[Union[dict, "PreTradeLayoutRow"], list[Union[dict, "PreTradeLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, PreTradeMessageDetailMsgType):
            self.msg_type = PreTradeMessageDetailMsgType(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.layout_url is not None and not isinstance(self.layout_url, URI):
            self.layout_url = URI(self.layout_url)

        self._normalize_inlined_as_list(slot_name="pre_layout_rows", slot_type=PreTradeLayoutRow, key_name="pre_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreTradeComponentDetail(YAMLRoot):
    """
    Per-category component description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["PreTradeComponentDetail"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:PreTradeComponentDetail"
    class_name: ClassVar[str] = "PreTradeComponentDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PreTradeComponentDetail

    component_name: Union[str, PreTradeComponentDetailComponentName] = None
    repetition: Optional[Union[str, "ComponentRepetition"]] = None
    description: Optional[str] = None
    layout_url: Optional[Union[str, URI]] = None
    pre_layout_rows: Optional[Union[Union[dict, "PreTradeLayoutRow"], list[Union[dict, "PreTradeLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, PreTradeComponentDetailComponentName):
            self.component_name = PreTradeComponentDetailComponentName(self.component_name)

        if self.repetition is not None and not isinstance(self.repetition, ComponentRepetition):
            self.repetition = ComponentRepetition(self.repetition)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.layout_url is not None and not isinstance(self.layout_url, URI):
            self.layout_url = URI(self.layout_url)

        self._normalize_inlined_as_list(slot_name="pre_layout_rows", slot_type=PreTradeLayoutRow, key_name="pre_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MessageGroup(YAMLRoot):
    """
    Purpose-grouped sub-section inside a category's Messages section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["MessageGroup"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:MessageGroup"
    class_name: ClassVar[str] = "MessageGroup"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.MessageGroup

    group_title: Union[str, MessageGroupGroupTitle] = None
    messages: Union[dict[Union[str, PreTradeMessageDetailMsgType], Union[dict, PreTradeMessageDetail]], list[Union[dict, PreTradeMessageDetail]]] = empty_dict()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.group_title):
            self.MissingRequiredField("group_title")
        if not isinstance(self.group_title, MessageGroupGroupTitle):
            self.group_title = MessageGroupGroupTitle(self.group_title)

        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        self._normalize_inlined_as_list(slot_name="messages", slot_type=PreTradeMessageDetail, key_name="msg_type", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CommonComponentDetail(YAMLRoot):
    """
    Per-common-component description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["CommonComponentDetail"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:CommonComponentDetail"
    class_name: ClassVar[str] = "CommonComponentDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.CommonComponentDetail

    component_name: Union[str, "CommonComponentDetailComponentName"] = None
    repetition: Optional[Union[str, "ComponentRepetition"]] = None
    description: Optional[str] = None
    layout_url: Optional[Union[str, URI]] = None
    pre_layout_rows: Optional[Union[Union[dict, "PreTradeLayoutRow"], list[Union[dict, "PreTradeLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, CommonComponentDetailComponentName):
            self.component_name = CommonComponentDetailComponentName(self.component_name)

        if self.repetition is not None and not isinstance(self.repetition, ComponentRepetition):
            self.repetition = ComponentRepetition(self.repetition)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.layout_url is not None and not isinstance(self.layout_url, URI):
            self.layout_url = URI(self.layout_url)

        self._normalize_inlined_as_list(slot_name="pre_layout_rows", slot_type=PreTradeLayoutRow, key_name="pre_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PreTradeLayoutRow(YAMLRoot):
    """
    One row of the layout table published in the Pre-Trade Appendix for a message or component. Each row identifies
    either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required,
    carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PRE_TRADE["PreTradeLayoutRow"]
    class_class_curie: ClassVar[str] = "fix_pre_trade:PreTradeLayoutRow"
    class_name: ClassVar[str] = "PreTradeLayoutRow"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PreTradeLayoutRow

    pre_layout_kind: Union[str, "PreTradeLayoutRowKindEnum"] = None
    pre_layout_element_name: str = None
    pre_layout_field_tag: Optional[int] = None
    pre_layout_required: Optional[Union[bool, Bool]] = None
    pre_layout_description: Optional[str] = None
    pre_layout_nested: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.pre_layout_kind):
            self.MissingRequiredField("pre_layout_kind")
        if not isinstance(self.pre_layout_kind, PreTradeLayoutRowKindEnum):
            self.pre_layout_kind = PreTradeLayoutRowKindEnum(self.pre_layout_kind)

        if self._is_empty(self.pre_layout_element_name):
            self.MissingRequiredField("pre_layout_element_name")
        if not isinstance(self.pre_layout_element_name, str):
            self.pre_layout_element_name = str(self.pre_layout_element_name)

        if self.pre_layout_field_tag is not None and not isinstance(self.pre_layout_field_tag, int):
            self.pre_layout_field_tag = int(self.pre_layout_field_tag)

        if self.pre_layout_required is not None and not isinstance(self.pre_layout_required, Bool):
            self.pre_layout_required = Bool(self.pre_layout_required)

        if self.pre_layout_description is not None and not isinstance(self.pre_layout_description, str):
            self.pre_layout_description = str(self.pre_layout_description)

        if self.pre_layout_nested is not None and not isinstance(self.pre_layout_nested, Bool):
            self.pre_layout_nested = Bool(self.pre_layout_nested)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeBusinessArea(YAMLRoot):
    """
    Tree-root container for the Trade (Orders and Executions) business area of FIX Latest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeBusinessArea"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeBusinessArea"
    class_name: ClassVar[str] = "TradeBusinessArea"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeBusinessArea

    trade_area: Union[str, "BusinessAreaEnum"] = 'TRADE'
    title: Optional[str] = "Business Area Trade"
    published_version: Optional[str] = None
    publisher: Optional[str] = "FIX Global Technical Committee"
    trade_introduction: Optional[str] = None
    trade_diagram_conventions: Optional[str] = None
    trade_message_diagram_template_url: Optional[Union[str, URI]] = None
    trade_messages_overview_note: Optional[str] = None
    messages: Optional[Union[dict[Union[str, TradeMessageEntryMsgType], Union[dict, "TradeMessageEntry"]], list[Union[dict, "TradeMessageEntry"]]]] = empty_dict()
    trade_components_overview_note: Optional[str] = None
    components: Optional[Union[dict[Union[str, TradeComponentEntryComponentName], Union[dict, "TradeComponentEntry"]], list[Union[dict, "TradeComponentEntry"]]]] = empty_dict()
    trade_common_components: Optional[Union[Union[str, "TradeCommonComponentName"], list[Union[str, "TradeCommonComponentName"]]]] = empty_list()
    trade_common_component_details: Optional[Union[dict[Union[str, TradeCommonComponentDetailComponentName], Union[dict, "TradeCommonComponentDetail"]], list[Union[dict, "TradeCommonComponentDetail"]]]] = empty_dict()
    trade_footnotes: Optional[Union[dict[Union[int, TradeComponentTableFootnoteTradeFootnoteNumber], Union[dict, "TradeComponentTableFootnote"]], list[Union[dict, "TradeComponentTableFootnote"]]]] = empty_dict()
    trade_category_sections: Optional[Union[dict[Union[str, TradeCategorySectionCategory], Union[dict, "TradeCategorySection"]], list[Union[dict, "TradeCategorySection"]]]] = empty_dict()
    referenced_global_components: Optional[Union[Union[str, GlobalComponentComponentName], list[Union[str, GlobalComponentComponentName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trade_area):
            self.MissingRequiredField("trade_area")
        if not isinstance(self.trade_area, BusinessAreaEnum):
            self.trade_area = BusinessAreaEnum(self.trade_area)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.published_version is not None and not isinstance(self.published_version, str):
            self.published_version = str(self.published_version)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.trade_introduction is not None and not isinstance(self.trade_introduction, str):
            self.trade_introduction = str(self.trade_introduction)

        if self.trade_diagram_conventions is not None and not isinstance(self.trade_diagram_conventions, str):
            self.trade_diagram_conventions = str(self.trade_diagram_conventions)

        if self.trade_message_diagram_template_url is not None and not isinstance(self.trade_message_diagram_template_url, URI):
            self.trade_message_diagram_template_url = URI(self.trade_message_diagram_template_url)

        if self.trade_messages_overview_note is not None and not isinstance(self.trade_messages_overview_note, str):
            self.trade_messages_overview_note = str(self.trade_messages_overview_note)

        self._normalize_inlined_as_list(slot_name="messages", slot_type=TradeMessageEntry, key_name="msg_type", keyed=True)

        if self.trade_components_overview_note is not None and not isinstance(self.trade_components_overview_note, str):
            self.trade_components_overview_note = str(self.trade_components_overview_note)

        self._normalize_inlined_as_list(slot_name="components", slot_type=TradeComponentEntry, key_name="component_name", keyed=True)

        if not isinstance(self.trade_common_components, list):
            self.trade_common_components = [self.trade_common_components] if self.trade_common_components is not None else []
        self.trade_common_components = [v if isinstance(v, TradeCommonComponentName) else TradeCommonComponentName(v) for v in self.trade_common_components]

        self._normalize_inlined_as_list(slot_name="trade_common_component_details", slot_type=TradeCommonComponentDetail, key_name="component_name", keyed=True)

        self._normalize_inlined_as_list(slot_name="trade_footnotes", slot_type=TradeComponentTableFootnote, key_name="trade_footnote_number", keyed=True)

        self._normalize_inlined_as_list(slot_name="trade_category_sections", slot_type=TradeCategorySection, key_name="category", keyed=True)

        if not isinstance(self.referenced_global_components, list):
            self.referenced_global_components = [self.referenced_global_components] if self.referenced_global_components is not None else []
        self.referenced_global_components = [v if isinstance(v, GlobalComponentComponentName) else GlobalComponentComponentName(v) for v in self.referenced_global_components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeMessageEntry(YAMLRoot):
    """
    One row of the area-wide trade messages table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeMessageEntry"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeMessageEntry"
    class_name: ClassVar[str] = "TradeMessageEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeMessageEntry

    msg_type: Union[str, TradeMessageEntryMsgType] = None
    message_name: str = None
    category: Union[str, "TradeCategoryEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, TradeMessageEntryMsgType):
            self.msg_type = TradeMessageEntryMsgType(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, TradeCategoryEnum):
            self.category = TradeCategoryEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeComponentEntry(YAMLRoot):
    """
    One row of the area-wide trade components table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeComponentEntry"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeComponentEntry"
    class_name: ClassVar[str] = "TradeComponentEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeComponentEntry

    component_name: Union[str, TradeComponentEntryComponentName] = None
    trade_repetition: Union[str, "TradeComponentRepetition"] = None
    category: str = None
    trade_is_common: Optional[Union[bool, Bool]] = False
    trade_footnote_number: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, TradeComponentEntryComponentName):
            self.component_name = TradeComponentEntryComponentName(self.component_name)

        if self._is_empty(self.trade_repetition):
            self.MissingRequiredField("trade_repetition")
        if not isinstance(self.trade_repetition, TradeComponentRepetition):
            self.trade_repetition = TradeComponentRepetition(self.trade_repetition)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, str):
            self.category = str(self.category)

        if self.trade_is_common is not None and not isinstance(self.trade_is_common, Bool):
            self.trade_is_common = Bool(self.trade_is_common)

        if self.trade_footnote_number is not None and not isinstance(self.trade_footnote_number, int):
            self.trade_footnote_number = int(self.trade_footnote_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeComponentTableFootnote(YAMLRoot):
    """
    A footnote on the area-wide components table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeComponentTableFootnote"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeComponentTableFootnote"
    class_name: ClassVar[str] = "TradeComponentTableFootnote"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeComponentTableFootnote

    trade_footnote_number: Union[int, TradeComponentTableFootnoteTradeFootnoteNumber] = None
    component_name: str = None
    trade_introduced_in: str = None
    trade_sole_category: Union[str, "TradeCategoryEnum"] = None
    trade_footnote_text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trade_footnote_number):
            self.MissingRequiredField("trade_footnote_number")
        if not isinstance(self.trade_footnote_number, TradeComponentTableFootnoteTradeFootnoteNumber):
            self.trade_footnote_number = TradeComponentTableFootnoteTradeFootnoteNumber(self.trade_footnote_number)

        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, str):
            self.component_name = str(self.component_name)

        if self._is_empty(self.trade_introduced_in):
            self.MissingRequiredField("trade_introduced_in")
        if not isinstance(self.trade_introduced_in, str):
            self.trade_introduced_in = str(self.trade_introduced_in)

        if self._is_empty(self.trade_sole_category):
            self.MissingRequiredField("trade_sole_category")
        if not isinstance(self.trade_sole_category, TradeCategoryEnum):
            self.trade_sole_category = TradeCategoryEnum(self.trade_sole_category)

        if self.trade_footnote_text is not None and not isinstance(self.trade_footnote_text, str):
            self.trade_footnote_text = str(self.trade_footnote_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeCategorySection(YAMLRoot):
    """
    A per-category sub-section of the Trade chapter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeCategorySection"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeCategorySection"
    class_name: ClassVar[str] = "TradeCategorySection"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeCategorySection

    category: Union[str, "TradeCategorySectionCategory"] = None
    title: Optional[str] = None
    description: Optional[str] = None
    trade_category_background: Optional[str] = None
    trade_message_groups: Optional[Union[dict[Union[str, TradeMessageGroupTradeGroupTitle], Union[dict, "TradeMessageGroup"]], list[Union[dict, "TradeMessageGroup"]]]] = empty_dict()
    messages: Optional[Union[dict[Union[str, TradeMessageDetailMsgType], Union[dict, "TradeMessageDetail"]], list[Union[dict, "TradeMessageDetail"]]]] = empty_dict()
    trade_category_components_note: Optional[str] = None
    trade_category_specific_components: Optional[Union[dict[Union[str, TradeComponentDetailComponentName], Union[dict, "TradeComponentDetail"]], list[Union[dict, "TradeComponentDetail"]]]] = empty_dict()
    trade_fragmentation_entries: Optional[Union[dict[Union[str, TradeFragmentationEntryTradeFragmentationMessage], Union[dict, "TradeFragmentationEntry"]], list[Union[dict, "TradeFragmentationEntry"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, TradeCategorySectionCategory):
            self.category = TradeCategorySectionCategory(self.category)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.trade_category_background is not None and not isinstance(self.trade_category_background, str):
            self.trade_category_background = str(self.trade_category_background)

        self._normalize_inlined_as_list(slot_name="trade_message_groups", slot_type=TradeMessageGroup, key_name="trade_group_title", keyed=True)

        self._normalize_inlined_as_list(slot_name="messages", slot_type=TradeMessageDetail, key_name="msg_type", keyed=True)

        if self.trade_category_components_note is not None and not isinstance(self.trade_category_components_note, str):
            self.trade_category_components_note = str(self.trade_category_components_note)

        self._normalize_inlined_as_list(slot_name="trade_category_specific_components", slot_type=TradeComponentDetail, key_name="component_name", keyed=True)

        self._normalize_inlined_as_list(slot_name="trade_fragmentation_entries", slot_type=TradeFragmentationEntry, key_name="trade_fragmentation_message", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeMessageDetail(YAMLRoot):
    """
    Per-category message description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeMessageDetail"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeMessageDetail"
    class_name: ClassVar[str] = "TradeMessageDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeMessageDetail

    msg_type: Union[str, TradeMessageDetailMsgType] = None
    message_name: str = None
    description: Optional[str] = None
    trade_layout_url: Optional[Union[str, URI]] = None
    trade_layout_rows: Optional[Union[Union[dict, "TradeLayoutRow"], list[Union[dict, "TradeLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, TradeMessageDetailMsgType):
            self.msg_type = TradeMessageDetailMsgType(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.trade_layout_url is not None and not isinstance(self.trade_layout_url, URI):
            self.trade_layout_url = URI(self.trade_layout_url)

        self._normalize_inlined_as_list(slot_name="trade_layout_rows", slot_type=TradeLayoutRow, key_name="trade_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeComponentDetail(YAMLRoot):
    """
    Per-category component description.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeComponentDetail"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeComponentDetail"
    class_name: ClassVar[str] = "TradeComponentDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeComponentDetail

    component_name: Union[str, TradeComponentDetailComponentName] = None
    trade_repetition: Optional[Union[str, "TradeComponentRepetition"]] = None
    description: Optional[str] = None
    trade_layout_url: Optional[Union[str, URI]] = None
    trade_layout_rows: Optional[Union[Union[dict, "TradeLayoutRow"], list[Union[dict, "TradeLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, TradeComponentDetailComponentName):
            self.component_name = TradeComponentDetailComponentName(self.component_name)

        if self.trade_repetition is not None and not isinstance(self.trade_repetition, TradeComponentRepetition):
            self.trade_repetition = TradeComponentRepetition(self.trade_repetition)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.trade_layout_url is not None and not isinstance(self.trade_layout_url, URI):
            self.trade_layout_url = URI(self.trade_layout_url)

        self._normalize_inlined_as_list(slot_name="trade_layout_rows", slot_type=TradeLayoutRow, key_name="trade_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeMessageGroup(YAMLRoot):
    """
    Purpose-grouped sub-section inside a category's Messages sub-section (e.g. "New Order Single", "Execution
    Reports", "Order Cancel Requests" under Single/General Order Handling).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeMessageGroup"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeMessageGroup"
    class_name: ClassVar[str] = "TradeMessageGroup"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeMessageGroup

    trade_group_title: Union[str, TradeMessageGroupTradeGroupTitle] = None
    messages: Union[dict[Union[str, TradeMessageDetailMsgType], Union[dict, TradeMessageDetail]], list[Union[dict, TradeMessageDetail]]] = empty_dict()
    description: Optional[str] = None
    trade_ord_status_precedence_entries: Optional[Union[dict[Union[str, TradeOrdStatusPrecedenceEntryTradeOrdStatusLabel], Union[dict, "TradeOrdStatusPrecedenceEntry"]], list[Union[dict, "TradeOrdStatusPrecedenceEntry"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trade_group_title):
            self.MissingRequiredField("trade_group_title")
        if not isinstance(self.trade_group_title, TradeMessageGroupTradeGroupTitle):
            self.trade_group_title = TradeMessageGroupTradeGroupTitle(self.trade_group_title)

        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        self._normalize_inlined_as_list(slot_name="messages", slot_type=TradeMessageDetail, key_name="msg_type", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="trade_ord_status_precedence_entries", slot_type=TradeOrdStatusPrecedenceEntry, key_name="trade_ord_status_label", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeCommonComponentDetail(YAMLRoot):
    """
    Per-common-component description from the chapter's final "Common Components" section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeCommonComponentDetail"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeCommonComponentDetail"
    class_name: ClassVar[str] = "TradeCommonComponentDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeCommonComponentDetail

    component_name: Union[str, "TradeCommonComponentDetailComponentName"] = None
    trade_repetition: Optional[Union[str, "TradeComponentRepetition"]] = None
    description: Optional[str] = None
    trade_layout_url: Optional[Union[str, URI]] = None
    trade_layout_rows: Optional[Union[Union[dict, "TradeLayoutRow"], list[Union[dict, "TradeLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, TradeCommonComponentDetailComponentName):
            self.component_name = TradeCommonComponentDetailComponentName(self.component_name)

        if self.trade_repetition is not None and not isinstance(self.trade_repetition, TradeComponentRepetition):
            self.trade_repetition = TradeComponentRepetition(self.trade_repetition)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.trade_layout_url is not None and not isinstance(self.trade_layout_url, URI):
            self.trade_layout_url = URI(self.trade_layout_url)

        self._normalize_inlined_as_list(slot_name="trade_layout_rows", slot_type=TradeLayoutRow, key_name="trade_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeLayoutRow(YAMLRoot):
    """
    One row of the layout table published in the Trade Appendix for a message or component. Each row identifies either
    a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the
    Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeLayoutRow"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeLayoutRow"
    class_name: ClassVar[str] = "TradeLayoutRow"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeLayoutRow

    trade_layout_kind: Union[str, "TradeLayoutRowKindEnum"] = None
    trade_layout_element_name: str = None
    trade_layout_field_tag: Optional[int] = None
    trade_layout_required: Optional[Union[bool, Bool]] = None
    trade_layout_description: Optional[str] = None
    trade_layout_nested: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trade_layout_kind):
            self.MissingRequiredField("trade_layout_kind")
        if not isinstance(self.trade_layout_kind, TradeLayoutRowKindEnum):
            self.trade_layout_kind = TradeLayoutRowKindEnum(self.trade_layout_kind)

        if self._is_empty(self.trade_layout_element_name):
            self.MissingRequiredField("trade_layout_element_name")
        if not isinstance(self.trade_layout_element_name, str):
            self.trade_layout_element_name = str(self.trade_layout_element_name)

        if self.trade_layout_field_tag is not None and not isinstance(self.trade_layout_field_tag, int):
            self.trade_layout_field_tag = int(self.trade_layout_field_tag)

        if self.trade_layout_required is not None and not isinstance(self.trade_layout_required, Bool):
            self.trade_layout_required = Bool(self.trade_layout_required)

        if self.trade_layout_description is not None and not isinstance(self.trade_layout_description, str):
            self.trade_layout_description = str(self.trade_layout_description)

        if self.trade_layout_nested is not None and not isinstance(self.trade_layout_nested, Bool):
            self.trade_layout_nested = Bool(self.trade_layout_nested)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeOrdStatusPrecedenceEntry(YAMLRoot):
    """
    One row of the OrdStatus(39) precedence table published in the Execution Reports purpose-group of the
    Single/General Order Handling category. Defines the precedence ranking used to resolve simultaneous state
    transitions on an order, paired with the human-readable OrdStatus label and its descriptive prose.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeOrdStatusPrecedenceEntry"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeOrdStatusPrecedenceEntry"
    class_name: ClassVar[str] = "TradeOrdStatusPrecedenceEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeOrdStatusPrecedenceEntry

    trade_ord_status_label: Union[str, TradeOrdStatusPrecedenceEntryTradeOrdStatusLabel] = None
    trade_ord_status_precedence: int = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trade_ord_status_label):
            self.MissingRequiredField("trade_ord_status_label")
        if not isinstance(self.trade_ord_status_label, TradeOrdStatusPrecedenceEntryTradeOrdStatusLabel):
            self.trade_ord_status_label = TradeOrdStatusPrecedenceEntryTradeOrdStatusLabel(self.trade_ord_status_label)

        if self._is_empty(self.trade_ord_status_precedence):
            self.MissingRequiredField("trade_ord_status_precedence")
        if not isinstance(self.trade_ord_status_precedence, int):
            self.trade_ord_status_precedence = int(self.trade_ord_status_precedence)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeFragmentationEntry(YAMLRoot):
    """
    One row of a fragmentation table published in a Trade category (currently only List/Program/Basket Trading)
    identifying a message that may be fragmented, the "Total Entries" field used to indicate the total count across
    all fragments of the batch, and the verbatim description of the repeating group that may be fragmented.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeFragmentationEntry"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeFragmentationEntry"
    class_name: ClassVar[str] = "TradeFragmentationEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeFragmentationEntry

    trade_fragmentation_message: Union[str, TradeFragmentationEntryTradeFragmentationMessage] = None
    trade_fragmentation_total_entries_field: str = None
    trade_fragmentation_repeating_group: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trade_fragmentation_message):
            self.MissingRequiredField("trade_fragmentation_message")
        if not isinstance(self.trade_fragmentation_message, TradeFragmentationEntryTradeFragmentationMessage):
            self.trade_fragmentation_message = TradeFragmentationEntryTradeFragmentationMessage(self.trade_fragmentation_message)

        if self._is_empty(self.trade_fragmentation_total_entries_field):
            self.MissingRequiredField("trade_fragmentation_total_entries_field")
        if not isinstance(self.trade_fragmentation_total_entries_field, str):
            self.trade_fragmentation_total_entries_field = str(self.trade_fragmentation_total_entries_field)

        if self._is_empty(self.trade_fragmentation_repeating_group):
            self.MissingRequiredField("trade_fragmentation_repeating_group")
        if not isinstance(self.trade_fragmentation_repeating_group, str):
            self.trade_fragmentation_repeating_group = str(self.trade_fragmentation_repeating_group)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeAppendix(YAMLRoot):
    """
    Tree-root container for the Trade Appendix — the spec companion document that publishes the full message- and
    component-layout tables for every message and component used in the Trade business area, organized into one
    "Appendix – <X> Category" sub-section per Trade category plus a final "Appendix – Common Category" sub-section
    covering the layouts of the chapter's common components.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeAppendix"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeAppendix"
    class_name: ClassVar[str] = "TradeAppendix"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeAppendix

    title: Optional[str] = "Trade Appendix"
    published_version: Optional[str] = None
    publisher: Optional[str] = "FIX Global Technical Committee"
    description: Optional[str] = None
    trade_appendix_sections: Optional[Union[dict[Union[str, TradeAppendixSectionTradeAppendixCategory], Union[dict, "TradeAppendixSection"]], list[Union[dict, "TradeAppendixSection"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.published_version is not None and not isinstance(self.published_version, str):
            self.published_version = str(self.published_version)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="trade_appendix_sections", slot_type=TradeAppendixSection, key_name="trade_appendix_category", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeAppendixSection(YAMLRoot):
    """
    One "Appendix – <X> Category" sub-section of the Trade Appendix. Bundles the per-message layout tables
    (TradeMessageDetail) and per-component layout tables (TradeComponentDetail) for messages and components that
    belong to one Trade category — or, for the synthetic "Common" section, the layouts of the chapter's common
    components.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_TRADE["TradeAppendixSection"]
    class_class_curie: ClassVar[str] = "fix_trade:TradeAppendixSection"
    class_name: ClassVar[str] = "TradeAppendixSection"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeAppendixSection

    trade_appendix_category: Union[str, TradeAppendixSectionTradeAppendixCategory] = None
    title: Optional[str] = None
    description: Optional[str] = None
    messages: Optional[Union[dict[Union[str, TradeMessageDetailMsgType], Union[dict, TradeMessageDetail]], list[Union[dict, TradeMessageDetail]]]] = empty_dict()
    components: Optional[Union[Union[str, TradeComponentDetailComponentName], list[Union[str, TradeComponentDetailComponentName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trade_appendix_category):
            self.MissingRequiredField("trade_appendix_category")
        if not isinstance(self.trade_appendix_category, TradeAppendixSectionTradeAppendixCategory):
            self.trade_appendix_category = TradeAppendixSectionTradeAppendixCategory(self.trade_appendix_category)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="messages", slot_type=TradeMessageDetail, key_name="msg_type", keyed=True)

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, TradeComponentDetailComponentName) else TradeComponentDetailComponentName(v) for v in self.components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeBusinessArea(YAMLRoot):
    """
    Tree-root container for the Post-Trade business area of FIX Latest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeBusinessArea"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeBusinessArea"
    class_name: ClassVar[str] = "PostTradeBusinessArea"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeBusinessArea

    messages: Union[dict[Union[str, PostTradeMessageEntryMsgType], Union[dict, "PostTradeMessageEntry"]], list[Union[dict, "PostTradeMessageEntry"]]] = empty_dict()
    components: Union[dict[Union[str, PostTradeComponentEntryComponentName], Union[dict, "PostTradeComponentEntry"]], list[Union[dict, "PostTradeComponentEntry"]]] = empty_dict()
    area: Union[str, "BusinessAreaEnum"] = 'POST_TRADE'
    title: Optional[str] = "Business Area Post-Trade"
    published_version: Optional[str] = None
    publisher: Optional[str] = "FIX Global Technical Committee"
    post_introduction: Optional[str] = None
    diagram_conventions: Optional[str] = None
    post_common_components: Optional[Union[Union[str, "PostTradeCommonComponentName"], list[Union[str, "PostTradeCommonComponentName"]]]] = empty_list()
    post_footnotes: Optional[Union[dict[Union[int, PostTradeComponentTableFootnoteFootnoteNumber], Union[dict, "PostTradeComponentTableFootnote"]], list[Union[dict, "PostTradeComponentTableFootnote"]]]] = empty_dict()
    post_category_sections: Optional[Union[dict[Union[str, PostTradeCategorySectionCategory], Union[dict, "PostTradeCategorySection"]], list[Union[dict, "PostTradeCategorySection"]]]] = empty_dict()
    post_common_component_details: Optional[Union[dict[Union[str, PostTradeCommonComponentDetailComponentName], Union[dict, "PostTradeCommonComponentDetail"]], list[Union[dict, "PostTradeCommonComponentDetail"]]]] = empty_dict()
    messages_overview_note: Optional[str] = None
    components_overview_note: Optional[str] = None
    referenced_global_components: Optional[Union[Union[str, GlobalComponentComponentName], list[Union[str, GlobalComponentComponentName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.area):
            self.MissingRequiredField("area")
        if not isinstance(self.area, BusinessAreaEnum):
            self.area = BusinessAreaEnum(self.area)

        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        self._normalize_inlined_as_list(slot_name="messages", slot_type=PostTradeMessageEntry, key_name="msg_type", keyed=True)

        if self._is_empty(self.components):
            self.MissingRequiredField("components")
        self._normalize_inlined_as_list(slot_name="components", slot_type=PostTradeComponentEntry, key_name="component_name", keyed=True)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.published_version is not None and not isinstance(self.published_version, str):
            self.published_version = str(self.published_version)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.post_introduction is not None and not isinstance(self.post_introduction, str):
            self.post_introduction = str(self.post_introduction)

        if self.diagram_conventions is not None and not isinstance(self.diagram_conventions, str):
            self.diagram_conventions = str(self.diagram_conventions)

        if not isinstance(self.post_common_components, list):
            self.post_common_components = [self.post_common_components] if self.post_common_components is not None else []
        self.post_common_components = [v if isinstance(v, PostTradeCommonComponentName) else PostTradeCommonComponentName(v) for v in self.post_common_components]

        self._normalize_inlined_as_list(slot_name="post_footnotes", slot_type=PostTradeComponentTableFootnote, key_name="footnote_number", keyed=True)

        self._normalize_inlined_as_list(slot_name="post_category_sections", slot_type=PostTradeCategorySection, key_name="category", keyed=True)

        self._normalize_inlined_as_list(slot_name="post_common_component_details", slot_type=PostTradeCommonComponentDetail, key_name="component_name", keyed=True)

        if self.messages_overview_note is not None and not isinstance(self.messages_overview_note, str):
            self.messages_overview_note = str(self.messages_overview_note)

        if self.components_overview_note is not None and not isinstance(self.components_overview_note, str):
            self.components_overview_note = str(self.components_overview_note)

        if not isinstance(self.referenced_global_components, list):
            self.referenced_global_components = [self.referenced_global_components] if self.referenced_global_components is not None else []
        self.referenced_global_components = [v if isinstance(v, GlobalComponentComponentName) else GlobalComponentComponentName(v) for v in self.referenced_global_components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeMessageEntry(YAMLRoot):
    """
    One row of the area-wide "Messages for Post-Trade Business Area" table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeMessageEntry"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeMessageEntry"
    class_name: ClassVar[str] = "PostTradeMessageEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeMessageEntry

    msg_type: Union[str, PostTradeMessageEntryMsgType] = None
    message_name: str = None
    category: Union[str, "PostTradeCategoryEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, PostTradeMessageEntryMsgType):
            self.msg_type = PostTradeMessageEntryMsgType(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, PostTradeCategoryEnum):
            self.category = PostTradeCategoryEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeComponentEntry(YAMLRoot):
    """
    One row of the area-wide "Components for Post-Trade Business Area" table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeComponentEntry"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeComponentEntry"
    class_name: ClassVar[str] = "PostTradeComponentEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeComponentEntry

    component_name: Union[str, PostTradeComponentEntryComponentName] = None
    repetition: Union[str, "ComponentRepetition"] = None
    category: str = None
    is_common: Optional[Union[bool, Bool]] = False
    footnote_number: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, PostTradeComponentEntryComponentName):
            self.component_name = PostTradeComponentEntryComponentName(self.component_name)

        if self._is_empty(self.repetition):
            self.MissingRequiredField("repetition")
        if not isinstance(self.repetition, ComponentRepetition):
            self.repetition = ComponentRepetition(self.repetition)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, str):
            self.category = str(self.category)

        if self.is_common is not None and not isinstance(self.is_common, Bool):
            self.is_common = Bool(self.is_common)

        if self.footnote_number is not None and not isinstance(self.footnote_number, int):
            self.footnote_number = int(self.footnote_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeComponentTableFootnote(YAMLRoot):
    """
    A footnote attached to a row of the area-wide Post-Trade components table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeComponentTableFootnote"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeComponentTableFootnote"
    class_name: ClassVar[str] = "PostTradeComponentTableFootnote"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeComponentTableFootnote

    footnote_number: Union[int, PostTradeComponentTableFootnoteFootnoteNumber] = None
    component_name: str = None
    introduced_in: str = None
    post_sole_category: Union[str, "PostTradeCategoryEnum"] = None
    text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.footnote_number):
            self.MissingRequiredField("footnote_number")
        if not isinstance(self.footnote_number, PostTradeComponentTableFootnoteFootnoteNumber):
            self.footnote_number = PostTradeComponentTableFootnoteFootnoteNumber(self.footnote_number)

        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, str):
            self.component_name = str(self.component_name)

        if self._is_empty(self.introduced_in):
            self.MissingRequiredField("introduced_in")
        if not isinstance(self.introduced_in, str):
            self.introduced_in = str(self.introduced_in)

        if self._is_empty(self.post_sole_category):
            self.MissingRequiredField("post_sole_category")
        if not isinstance(self.post_sole_category, PostTradeCategoryEnum):
            self.post_sole_category = PostTradeCategoryEnum(self.post_sole_category)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeCategorySection(YAMLRoot):
    """
    A "Category – <name>" sub-section of the Post-Trade chapter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeCategorySection"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeCategorySection"
    class_name: ClassVar[str] = "PostTradeCategorySection"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeCategorySection

    category: Union[str, "PostTradeCategorySectionCategory"] = None
    title: Optional[str] = None
    description: Optional[str] = None
    category_components_note: Optional[str] = None
    post_message_groups: Optional[Union[dict[Union[str, PostTradeMessageGroupGroupTitle], Union[dict, "PostTradeMessageGroup"]], list[Union[dict, "PostTradeMessageGroup"]]]] = empty_dict()
    messages: Optional[Union[dict[Union[str, PostTradeMessageDetailMsgType], Union[dict, "PostTradeMessageDetail"]], list[Union[dict, "PostTradeMessageDetail"]]]] = empty_dict()
    post_category_specific_components: Optional[Union[dict[Union[str, PostTradeComponentDetailComponentName], Union[dict, "PostTradeComponentDetail"]], list[Union[dict, "PostTradeComponentDetail"]]]] = empty_dict()
    allocation_scenarios: Optional[Union[Union[str, "AllocationScenarioEnum"], list[Union[str, "AllocationScenarioEnum"]]]] = empty_list()
    allocation_roles: Optional[Union[Union[str, "AllocationRoleEnum"], list[Union[str, "AllocationRoleEnum"]]]] = empty_list()
    post_trade_allocation_pricing_methods: Optional[Union[Union[str, "PostTradeAllocationPricingMethodEnum"], list[Union[str, "PostTradeAllocationPricingMethodEnum"]]]] = empty_list()
    allocation_status_descriptions: Optional[Union[dict[Union[str, AllocationStatusDescriptionStatusCode], Union[dict, "AllocationStatusDescription"]], list[Union[dict, "AllocationStatusDescription"]]]] = empty_dict()
    fragmentation_field_map: Optional[Union[dict[Union[str, AllocationFragmentationFieldMapMsgType], Union[dict, "AllocationFragmentationFieldMap"]], list[Union[dict, "AllocationFragmentationFieldMap"]]]] = empty_dict()
    trade_capture_report_usages: Optional[Union[dict[Union[str, TradeCaptureReportUsageStatusLabel], Union[dict, "TradeCaptureReportUsage"]], list[Union[dict, "TradeCaptureReportUsage"]]]] = empty_dict()
    trade_capture_report_identifier_rules: Optional[Union[dict[Union[str, TradeCaptureReportIdentifierRuleIdentifierRole], Union[dict, "TradeCaptureReportIdentifierRule"]], list[Union[dict, "TradeCaptureReportIdentifierRule"]]]] = empty_dict()
    registration_status_descriptions: Optional[Union[dict[Union[str, RegistrationStatusDescriptionStatusCode], Union[dict, "RegistrationStatusDescription"]], list[Union[dict, "RegistrationStatusDescription"]]]] = empty_dict()
    clearing_services_for_position_management: Optional[Union[Union[str, "ClearingServiceForPositionManagementEnum"], list[Union[str, "ClearingServiceForPositionManagementEnum"]]]] = empty_list()
    clearing_services_for_post_trade_processing: Optional[Union[dict[Union[str, ClearingServicePostTradeProcessingFormatMessageFormat], Union[dict, "ClearingServicePostTradeProcessingFormat"]], list[Union[dict, "ClearingServicePostTradeProcessingFormat"]]]] = empty_dict()
    collateral_management_usages: Optional[Union[Union[str, "CollateralManagementUsageEnum"], list[Union[str, "CollateralManagementUsageEnum"]]]] = empty_list()
    collateral_assignment_purposes: Optional[Union[Union[str, "CollateralAssignmentPurposeEnum"], list[Union[str, "CollateralAssignmentPurposeEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, PostTradeCategorySectionCategory):
            self.category = PostTradeCategorySectionCategory(self.category)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.category_components_note is not None and not isinstance(self.category_components_note, str):
            self.category_components_note = str(self.category_components_note)

        self._normalize_inlined_as_list(slot_name="post_message_groups", slot_type=PostTradeMessageGroup, key_name="group_title", keyed=True)

        self._normalize_inlined_as_list(slot_name="messages", slot_type=PostTradeMessageDetail, key_name="msg_type", keyed=True)

        self._normalize_inlined_as_list(slot_name="post_category_specific_components", slot_type=PostTradeComponentDetail, key_name="component_name", keyed=True)

        if not isinstance(self.allocation_scenarios, list):
            self.allocation_scenarios = [self.allocation_scenarios] if self.allocation_scenarios is not None else []
        self.allocation_scenarios = [v if isinstance(v, AllocationScenarioEnum) else AllocationScenarioEnum(v) for v in self.allocation_scenarios]

        if not isinstance(self.allocation_roles, list):
            self.allocation_roles = [self.allocation_roles] if self.allocation_roles is not None else []
        self.allocation_roles = [v if isinstance(v, AllocationRoleEnum) else AllocationRoleEnum(v) for v in self.allocation_roles]

        if not isinstance(self.post_trade_allocation_pricing_methods, list):
            self.post_trade_allocation_pricing_methods = [self.post_trade_allocation_pricing_methods] if self.post_trade_allocation_pricing_methods is not None else []
        self.post_trade_allocation_pricing_methods = [v if isinstance(v, PostTradeAllocationPricingMethodEnum) else PostTradeAllocationPricingMethodEnum(v) for v in self.post_trade_allocation_pricing_methods]

        self._normalize_inlined_as_list(slot_name="allocation_status_descriptions", slot_type=AllocationStatusDescription, key_name="status_code", keyed=True)

        self._normalize_inlined_as_list(slot_name="fragmentation_field_map", slot_type=AllocationFragmentationFieldMap, key_name="msg_type", keyed=True)

        self._normalize_inlined_as_list(slot_name="trade_capture_report_usages", slot_type=TradeCaptureReportUsage, key_name="status_label", keyed=True)

        self._normalize_inlined_as_list(slot_name="trade_capture_report_identifier_rules", slot_type=TradeCaptureReportIdentifierRule, key_name="identifier_role", keyed=True)

        self._normalize_inlined_as_list(slot_name="registration_status_descriptions", slot_type=RegistrationStatusDescription, key_name="status_code", keyed=True)

        if not isinstance(self.clearing_services_for_position_management, list):
            self.clearing_services_for_position_management = [self.clearing_services_for_position_management] if self.clearing_services_for_position_management is not None else []
        self.clearing_services_for_position_management = [v if isinstance(v, ClearingServiceForPositionManagementEnum) else ClearingServiceForPositionManagementEnum(v) for v in self.clearing_services_for_position_management]

        self._normalize_inlined_as_list(slot_name="clearing_services_for_post_trade_processing", slot_type=ClearingServicePostTradeProcessingFormat, key_name="message_format", keyed=True)

        if not isinstance(self.collateral_management_usages, list):
            self.collateral_management_usages = [self.collateral_management_usages] if self.collateral_management_usages is not None else []
        self.collateral_management_usages = [v if isinstance(v, CollateralManagementUsageEnum) else CollateralManagementUsageEnum(v) for v in self.collateral_management_usages]

        if not isinstance(self.collateral_assignment_purposes, list):
            self.collateral_assignment_purposes = [self.collateral_assignment_purposes] if self.collateral_assignment_purposes is not None else []
        self.collateral_assignment_purposes = [v if isinstance(v, CollateralAssignmentPurposeEnum) else CollateralAssignmentPurposeEnum(v) for v in self.collateral_assignment_purposes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeMessageGroup(YAMLRoot):
    """
    A purpose-themed grouping of messages within a Post-Trade category (e.g. "Allocation Instructions").
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeMessageGroup"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeMessageGroup"
    class_name: ClassVar[str] = "PostTradeMessageGroup"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeMessageGroup

    group_title: Union[str, PostTradeMessageGroupGroupTitle] = None
    messages: Union[dict[Union[str, PostTradeMessageDetailMsgType], Union[dict, "PostTradeMessageDetail"]], list[Union[dict, "PostTradeMessageDetail"]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.group_title):
            self.MissingRequiredField("group_title")
        if not isinstance(self.group_title, PostTradeMessageGroupGroupTitle):
            self.group_title = PostTradeMessageGroupGroupTitle(self.group_title)

        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        self._normalize_inlined_as_list(slot_name="messages", slot_type=PostTradeMessageDetail, key_name="msg_type", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeMessageDetail(YAMLRoot):
    """
    Per-message description block from a Post-Trade category section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeMessageDetail"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeMessageDetail"
    class_name: ClassVar[str] = "PostTradeMessageDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeMessageDetail

    msg_type: Union[str, PostTradeMessageDetailMsgType] = None
    message_name: str = None
    description: Optional[str] = None
    layout_url: Optional[Union[str, URI]] = None
    post_layout_rows: Optional[Union[Union[dict, "PostTradeLayoutRow"], list[Union[dict, "PostTradeLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, PostTradeMessageDetailMsgType):
            self.msg_type = PostTradeMessageDetailMsgType(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.layout_url is not None and not isinstance(self.layout_url, URI):
            self.layout_url = URI(self.layout_url)

        self._normalize_inlined_as_list(slot_name="post_layout_rows", slot_type=PostTradeLayoutRow, key_name="post_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeComponentDetail(YAMLRoot):
    """
    Per-component description block from a Post-Trade category section's Components sub-section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeComponentDetail"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeComponentDetail"
    class_name: ClassVar[str] = "PostTradeComponentDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeComponentDetail

    component_name: Union[str, PostTradeComponentDetailComponentName] = None
    repetition: Optional[Union[str, "ComponentRepetition"]] = None
    description: Optional[str] = None
    layout_url: Optional[Union[str, URI]] = None
    post_layout_rows: Optional[Union[Union[dict, "PostTradeLayoutRow"], list[Union[dict, "PostTradeLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, PostTradeComponentDetailComponentName):
            self.component_name = PostTradeComponentDetailComponentName(self.component_name)

        if self.repetition is not None and not isinstance(self.repetition, ComponentRepetition):
            self.repetition = ComponentRepetition(self.repetition)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.layout_url is not None and not isinstance(self.layout_url, URI):
            self.layout_url = URI(self.layout_url)

        self._normalize_inlined_as_list(slot_name="post_layout_rows", slot_type=PostTradeLayoutRow, key_name="post_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeCommonComponentDetail(YAMLRoot):
    """
    Per-common-component description block from the chapter's final "Common Components" section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeCommonComponentDetail"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeCommonComponentDetail"
    class_name: ClassVar[str] = "PostTradeCommonComponentDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeCommonComponentDetail

    component_name: Union[str, "PostTradeCommonComponentDetailComponentName"] = None
    repetition: Optional[Union[str, "ComponentRepetition"]] = None
    description: Optional[str] = None
    layout_url: Optional[Union[str, URI]] = None
    post_layout_rows: Optional[Union[Union[dict, "PostTradeLayoutRow"], list[Union[dict, "PostTradeLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, PostTradeCommonComponentDetailComponentName):
            self.component_name = PostTradeCommonComponentDetailComponentName(self.component_name)

        if self.repetition is not None and not isinstance(self.repetition, ComponentRepetition):
            self.repetition = ComponentRepetition(self.repetition)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.layout_url is not None and not isinstance(self.layout_url, URI):
            self.layout_url = URI(self.layout_url)

        self._normalize_inlined_as_list(slot_name="post_layout_rows", slot_type=PostTradeLayoutRow, key_name="post_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AllocationStatusDescription(YAMLRoot):
    """
    One row of the AllocStatus(87) value/description table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["AllocationStatusDescription"]
    class_class_curie: ClassVar[str] = "fix_post_trade:AllocationStatusDescription"
    class_name: ClassVar[str] = "AllocationStatusDescription"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.AllocationStatusDescription

    status_code: Union[str, AllocationStatusDescriptionStatusCode] = None
    status_label: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.status_code):
            self.MissingRequiredField("status_code")
        if not isinstance(self.status_code, AllocationStatusDescriptionStatusCode):
            self.status_code = AllocationStatusDescriptionStatusCode(self.status_code)

        if self._is_empty(self.status_label):
            self.MissingRequiredField("status_label")
        if not isinstance(self.status_label, str):
            self.status_label = str(self.status_label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AllocationFragmentationFieldMap(YAMLRoot):
    """
    One row of the table mapping an allocation message to its fragmentation-related fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["AllocationFragmentationFieldMap"]
    class_class_curie: ClassVar[str] = "fix_post_trade:AllocationFragmentationFieldMap"
    class_name: ClassVar[str] = "AllocationFragmentationFieldMap"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.AllocationFragmentationFieldMap

    msg_type: Union[str, AllocationFragmentationFieldMapMsgType] = None
    message_name: str = None
    total_count_field: str = None
    fragment_count_field: str = None
    principal_message_reference: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, AllocationFragmentationFieldMapMsgType):
            self.msg_type = AllocationFragmentationFieldMapMsgType(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self._is_empty(self.total_count_field):
            self.MissingRequiredField("total_count_field")
        if not isinstance(self.total_count_field, str):
            self.total_count_field = str(self.total_count_field)

        if self._is_empty(self.fragment_count_field):
            self.MissingRequiredField("fragment_count_field")
        if not isinstance(self.fragment_count_field, str):
            self.fragment_count_field = str(self.fragment_count_field)

        if self._is_empty(self.principal_message_reference):
            self.MissingRequiredField("principal_message_reference")
        if not isinstance(self.principal_message_reference, str):
            self.principal_message_reference = str(self.principal_message_reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeCaptureReportUsage(YAMLRoot):
    """
    One documented usage of the TradeCaptureReport(35=AE) message.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["TradeCaptureReportUsage"]
    class_class_curie: ClassVar[str] = "fix_post_trade:TradeCaptureReportUsage"
    class_name: ClassVar[str] = "TradeCaptureReportUsage"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeCaptureReportUsage

    status_label: Union[str, TradeCaptureReportUsageStatusLabel] = None
    description: Optional[str] = None
    identifier_role: Optional[Union[str, "TradeCaptureReportIdentifierRoleEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.status_label):
            self.MissingRequiredField("status_label")
        if not isinstance(self.status_label, TradeCaptureReportUsageStatusLabel):
            self.status_label = TradeCaptureReportUsageStatusLabel(self.status_label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.identifier_role is not None and not isinstance(self.identifier_role, TradeCaptureReportIdentifierRoleEnum):
            self.identifier_role = TradeCaptureReportIdentifierRoleEnum(self.identifier_role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TradeCaptureReportIdentifierRule(YAMLRoot):
    """
    A rule governing one of the TradeCaptureReport(35=AE) identifier fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["TradeCaptureReportIdentifierRule"]
    class_class_curie: ClassVar[str] = "fix_post_trade:TradeCaptureReportIdentifierRule"
    class_name: ClassVar[str] = "TradeCaptureReportIdentifierRule"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.TradeCaptureReportIdentifierRule

    identifier_role: Union[str, "TradeCaptureReportIdentifierRuleIdentifierRole"] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.identifier_role):
            self.MissingRequiredField("identifier_role")
        if not isinstance(self.identifier_role, TradeCaptureReportIdentifierRuleIdentifierRole):
            self.identifier_role = TradeCaptureReportIdentifierRuleIdentifierRole(self.identifier_role)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RegistrationStatusDescription(YAMLRoot):
    """
    One row of the RegistStatus(506) value/description table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["RegistrationStatusDescription"]
    class_class_curie: ClassVar[str] = "fix_post_trade:RegistrationStatusDescription"
    class_name: ClassVar[str] = "RegistrationStatusDescription"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.RegistrationStatusDescription

    status_code: Union[str, RegistrationStatusDescriptionStatusCode] = None
    status_label: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.status_code):
            self.MissingRequiredField("status_code")
        if not isinstance(self.status_code, RegistrationStatusDescriptionStatusCode):
            self.status_code = RegistrationStatusDescriptionStatusCode(self.status_code)

        if self._is_empty(self.status_label):
            self.MissingRequiredField("status_label")
        if not isinstance(self.status_label, str):
            self.status_label = str(self.status_label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClearingServicePostTradeProcessingFormat(YAMLRoot):
    """
    One message-format row from the Post-Trade Processing Clearing Services section, with its supported actions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["ClearingServicePostTradeProcessingFormat"]
    class_class_curie: ClassVar[str] = "fix_post_trade:ClearingServicePostTradeProcessingFormat"
    class_name: ClassVar[str] = "ClearingServicePostTradeProcessingFormat"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.ClearingServicePostTradeProcessingFormat

    message_format: Union[str, "ClearingServicePostTradeProcessingFormatMessageFormat"] = None
    supported_actions: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.message_format):
            self.MissingRequiredField("message_format")
        if not isinstance(self.message_format, ClearingServicePostTradeProcessingFormatMessageFormat):
            self.message_format = ClearingServicePostTradeProcessingFormatMessageFormat(self.message_format)

        if self._is_empty(self.supported_actions):
            self.MissingRequiredField("supported_actions")
        if not isinstance(self.supported_actions, list):
            self.supported_actions = [self.supported_actions] if self.supported_actions is not None else []
        self.supported_actions = [v if isinstance(v, str) else str(v) for v in self.supported_actions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTradeLayoutRow(YAMLRoot):
    """
    One row of the layout table published in the Post-Trade Appendix for a message or component. Each row identifies
    either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required,
    carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_POST_TRADE["PostTradeLayoutRow"]
    class_class_curie: ClassVar[str] = "fix_post_trade:PostTradeLayoutRow"
    class_name: ClassVar[str] = "PostTradeLayoutRow"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.PostTradeLayoutRow

    post_layout_kind: Union[str, "PostTradeLayoutRowKindEnum"] = None
    post_layout_element_name: str = None
    post_layout_field_tag: Optional[int] = None
    post_layout_required: Optional[Union[bool, Bool]] = None
    post_layout_description: Optional[str] = None
    post_layout_nested: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.post_layout_kind):
            self.MissingRequiredField("post_layout_kind")
        if not isinstance(self.post_layout_kind, PostTradeLayoutRowKindEnum):
            self.post_layout_kind = PostTradeLayoutRowKindEnum(self.post_layout_kind)

        if self._is_empty(self.post_layout_element_name):
            self.MissingRequiredField("post_layout_element_name")
        if not isinstance(self.post_layout_element_name, str):
            self.post_layout_element_name = str(self.post_layout_element_name)

        if self.post_layout_field_tag is not None and not isinstance(self.post_layout_field_tag, int):
            self.post_layout_field_tag = int(self.post_layout_field_tag)

        if self.post_layout_required is not None and not isinstance(self.post_layout_required, Bool):
            self.post_layout_required = Bool(self.post_layout_required)

        if self.post_layout_description is not None and not isinstance(self.post_layout_description, str):
            self.post_layout_description = str(self.post_layout_description)

        if self.post_layout_nested is not None and not isinstance(self.post_layout_nested, Bool):
            self.post_layout_nested = Bool(self.post_layout_nested)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfrastructureBusinessArea(YAMLRoot):
    """
    Tree-root container for the Infrastructure business area of FIX Latest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["InfrastructureBusinessArea"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:InfrastructureBusinessArea"
    class_name: ClassVar[str] = "InfrastructureBusinessArea"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.InfrastructureBusinessArea

    messages: Union[dict[Union[str, InfrastructureMessageEntryMsgType], Union[dict, "InfrastructureMessageEntry"]], list[Union[dict, "InfrastructureMessageEntry"]]] = empty_dict()
    components: Union[dict[Union[str, InfrastructureComponentEntryComponentName], Union[dict, "InfrastructureComponentEntry"]], list[Union[dict, "InfrastructureComponentEntry"]]] = empty_dict()
    area: Union[str, "BusinessAreaEnum"] = 'INFRASTRUCTURE'
    title: Optional[str] = "Business Area Infrastructure"
    published_version: Optional[str] = None
    publisher: Optional[str] = "FIX Global Technical Committee"
    infra_introduction: Optional[str] = None
    diagram_conventions: Optional[str] = None
    infra_common_components: Optional[Union[Union[str, "InfrastructureComponentName"], list[Union[str, "InfrastructureComponentName"]]]] = empty_list()
    messages_overview_note: Optional[str] = None
    components_overview_note: Optional[str] = None
    infra_footnotes: Optional[Union[dict[Union[int, InfrastructureComponentTableFootnoteFootnoteNumber], Union[dict, "InfrastructureComponentTableFootnote"]], list[Union[dict, "InfrastructureComponentTableFootnote"]]]] = empty_dict()
    infra_category_sections: Optional[Union[Union[dict, "InfrastructureCategorySection"], list[Union[dict, "InfrastructureCategorySection"]]]] = empty_list()
    standard_responses_pre_trade: Optional[Union[Union[dict, "StandardResponseMapping"], list[Union[dict, "StandardResponseMapping"]]]] = empty_list()
    standard_responses_trade: Optional[Union[Union[dict, "StandardResponseMapping"], list[Union[dict, "StandardResponseMapping"]]]] = empty_list()
    standard_responses_post_trade: Optional[Union[Union[dict, "StandardResponseMapping"], list[Union[dict, "StandardResponseMapping"]]]] = empty_list()
    key_fields_pre_trade: Optional[Union[Union[dict, "ApplicationMessageReferenceKey"], list[Union[dict, "ApplicationMessageReferenceKey"]]]] = empty_list()
    key_fields_trade: Optional[Union[Union[dict, "ApplicationMessageReferenceKey"], list[Union[dict, "ApplicationMessageReferenceKey"]]]] = empty_list()
    key_fields_post_trade: Optional[Union[Union[dict, "ApplicationMessageReferenceKey"], list[Union[dict, "ApplicationMessageReferenceKey"]]]] = empty_list()
    business_reject_reason_descriptions: Optional[Union[dict[Union[int, BusinessRejectReasonDescriptionRejectReasonCode], Union[dict, "BusinessRejectReasonDescription"]], list[Union[dict, "BusinessRejectReasonDescription"]]]] = empty_dict()
    infra_global_components: Optional[Union[dict[Union[str, InfrastructureGlobalComponentReferenceInfraGlobalComponentName], Union[dict, "InfrastructureGlobalComponentReference"]], list[Union[dict, "InfrastructureGlobalComponentReference"]]]] = empty_dict()
    referenced_global_components: Optional[Union[Union[str, GlobalComponentComponentName], list[Union[str, GlobalComponentComponentName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.area):
            self.MissingRequiredField("area")
        if not isinstance(self.area, BusinessAreaEnum):
            self.area = BusinessAreaEnum(self.area)

        if self._is_empty(self.messages):
            self.MissingRequiredField("messages")
        self._normalize_inlined_as_list(slot_name="messages", slot_type=InfrastructureMessageEntry, key_name="msg_type", keyed=True)

        if self._is_empty(self.components):
            self.MissingRequiredField("components")
        self._normalize_inlined_as_list(slot_name="components", slot_type=InfrastructureComponentEntry, key_name="component_name", keyed=True)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.published_version is not None and not isinstance(self.published_version, str):
            self.published_version = str(self.published_version)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.infra_introduction is not None and not isinstance(self.infra_introduction, str):
            self.infra_introduction = str(self.infra_introduction)

        if self.diagram_conventions is not None and not isinstance(self.diagram_conventions, str):
            self.diagram_conventions = str(self.diagram_conventions)

        if not isinstance(self.infra_common_components, list):
            self.infra_common_components = [self.infra_common_components] if self.infra_common_components is not None else []
        self.infra_common_components = [v if isinstance(v, InfrastructureComponentName) else InfrastructureComponentName(v) for v in self.infra_common_components]

        if self.messages_overview_note is not None and not isinstance(self.messages_overview_note, str):
            self.messages_overview_note = str(self.messages_overview_note)

        if self.components_overview_note is not None and not isinstance(self.components_overview_note, str):
            self.components_overview_note = str(self.components_overview_note)

        self._normalize_inlined_as_list(slot_name="infra_footnotes", slot_type=InfrastructureComponentTableFootnote, key_name="footnote_number", keyed=True)

        self._normalize_inlined_as_list(slot_name="infra_category_sections", slot_type=InfrastructureCategorySection, key_name="category", keyed=False)

        self._normalize_inlined_as_list(slot_name="standard_responses_pre_trade", slot_type=StandardResponseMapping, key_name="category_label", keyed=False)

        self._normalize_inlined_as_list(slot_name="standard_responses_trade", slot_type=StandardResponseMapping, key_name="category_label", keyed=False)

        self._normalize_inlined_as_list(slot_name="standard_responses_post_trade", slot_type=StandardResponseMapping, key_name="category_label", keyed=False)

        self._normalize_inlined_as_list(slot_name="key_fields_pre_trade", slot_type=ApplicationMessageReferenceKey, key_name="category_label", keyed=False)

        self._normalize_inlined_as_list(slot_name="key_fields_trade", slot_type=ApplicationMessageReferenceKey, key_name="category_label", keyed=False)

        self._normalize_inlined_as_list(slot_name="key_fields_post_trade", slot_type=ApplicationMessageReferenceKey, key_name="category_label", keyed=False)

        self._normalize_inlined_as_list(slot_name="business_reject_reason_descriptions", slot_type=BusinessRejectReasonDescription, key_name="reject_reason_code", keyed=True)

        self._normalize_inlined_as_list(slot_name="infra_global_components", slot_type=InfrastructureGlobalComponentReference, key_name="infra_global_component_name", keyed=True)

        if not isinstance(self.referenced_global_components, list):
            self.referenced_global_components = [self.referenced_global_components] if self.referenced_global_components is not None else []
        self.referenced_global_components = [v if isinstance(v, GlobalComponentComponentName) else GlobalComponentComponentName(v) for v in self.referenced_global_components]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfrastructureMessageEntry(YAMLRoot):
    """
    One row of the area-wide "Messages for Infrastructure Business Area" table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["InfrastructureMessageEntry"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:InfrastructureMessageEntry"
    class_name: ClassVar[str] = "InfrastructureMessageEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.InfrastructureMessageEntry

    msg_type: Union[str, InfrastructureMessageEntryMsgType] = None
    message_name: str = None
    category: Union[str, "InfrastructureCategoryEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, InfrastructureMessageEntryMsgType):
            self.msg_type = InfrastructureMessageEntryMsgType(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, InfrastructureCategoryEnum):
            self.category = InfrastructureCategoryEnum(self.category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfrastructureComponentEntry(YAMLRoot):
    """
    One row of the area-wide "Components for Infrastructure Business Area" table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["InfrastructureComponentEntry"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:InfrastructureComponentEntry"
    class_name: ClassVar[str] = "InfrastructureComponentEntry"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.InfrastructureComponentEntry

    component_name: Union[str, InfrastructureComponentEntryComponentName] = None
    repetition: Union[str, "ComponentRepetition"] = None
    category: Union[str, "InfrastructureCategoryEnum"] = None
    footnote_number: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, InfrastructureComponentEntryComponentName):
            self.component_name = InfrastructureComponentEntryComponentName(self.component_name)

        if self._is_empty(self.repetition):
            self.MissingRequiredField("repetition")
        if not isinstance(self.repetition, ComponentRepetition):
            self.repetition = ComponentRepetition(self.repetition)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, InfrastructureCategoryEnum):
            self.category = InfrastructureCategoryEnum(self.category)

        if self.footnote_number is not None and not isinstance(self.footnote_number, int):
            self.footnote_number = int(self.footnote_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfrastructureComponentTableFootnote(YAMLRoot):
    """
    A footnote attached to a row of the area-wide Infrastructure components table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["InfrastructureComponentTableFootnote"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:InfrastructureComponentTableFootnote"
    class_name: ClassVar[str] = "InfrastructureComponentTableFootnote"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.InfrastructureComponentTableFootnote

    footnote_number: Union[int, InfrastructureComponentTableFootnoteFootnoteNumber] = None
    component_name: str = None
    introduced_in: str = None
    infra_sole_category: Union[str, "InfrastructureCategoryEnum"] = None
    text: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.footnote_number):
            self.MissingRequiredField("footnote_number")
        if not isinstance(self.footnote_number, InfrastructureComponentTableFootnoteFootnoteNumber):
            self.footnote_number = InfrastructureComponentTableFootnoteFootnoteNumber(self.footnote_number)

        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, str):
            self.component_name = str(self.component_name)

        if self._is_empty(self.introduced_in):
            self.MissingRequiredField("introduced_in")
        if not isinstance(self.introduced_in, str):
            self.introduced_in = str(self.introduced_in)

        if self._is_empty(self.infra_sole_category):
            self.MissingRequiredField("infra_sole_category")
        if not isinstance(self.infra_sole_category, InfrastructureCategoryEnum):
            self.infra_sole_category = InfrastructureCategoryEnum(self.infra_sole_category)

        if self.text is not None and not isinstance(self.text, str):
            self.text = str(self.text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfrastructureCategorySection(YAMLRoot):
    """
    A "Category – <name>" sub-section of the Infrastructure chapter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["InfrastructureCategorySection"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:InfrastructureCategorySection"
    class_name: ClassVar[str] = "InfrastructureCategorySection"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.InfrastructureCategorySection

    category: Union[str, "InfrastructureCategoryEnum"] = None
    title: Optional[str] = None
    description: Optional[str] = None
    category_components_note: Optional[str] = None
    messages: Optional[Union[Union[dict, "InfrastructureMessageDetail"], list[Union[dict, "InfrastructureMessageDetail"]]]] = empty_list()
    infra_category_specific_components: Optional[Union[Union[dict, "InfrastructureComponentDetail"], list[Union[dict, "InfrastructureComponentDetail"]]]] = empty_list()
    network_status_scenarios: Optional[Union[Union[str, "NetworkStatusScenarioEnum"], list[Union[str, "NetworkStatusScenarioEnum"]]]] = empty_list()
    network_request_types_referenced: Optional[Union[Union[str, "NetworkRequestTypeEnum"], list[Union[str, "NetworkRequestTypeEnum"]]]] = empty_list()
    application_message_report_uses: Optional[Union[Union[str, "ApplicationMessageReportTypeEnum"], list[Union[str, "ApplicationMessageReportTypeEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, InfrastructureCategoryEnum):
            self.category = InfrastructureCategoryEnum(self.category)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.category_components_note is not None and not isinstance(self.category_components_note, str):
            self.category_components_note = str(self.category_components_note)

        self._normalize_inlined_as_list(slot_name="messages", slot_type=InfrastructureMessageDetail, key_name="msg_type", keyed=False)

        self._normalize_inlined_as_list(slot_name="infra_category_specific_components", slot_type=InfrastructureComponentDetail, key_name="component_name", keyed=False)

        if not isinstance(self.network_status_scenarios, list):
            self.network_status_scenarios = [self.network_status_scenarios] if self.network_status_scenarios is not None else []
        self.network_status_scenarios = [v if isinstance(v, NetworkStatusScenarioEnum) else NetworkStatusScenarioEnum(v) for v in self.network_status_scenarios]

        if not isinstance(self.network_request_types_referenced, list):
            self.network_request_types_referenced = [self.network_request_types_referenced] if self.network_request_types_referenced is not None else []
        self.network_request_types_referenced = [v if isinstance(v, NetworkRequestTypeEnum) else NetworkRequestTypeEnum(v) for v in self.network_request_types_referenced]

        if not isinstance(self.application_message_report_uses, list):
            self.application_message_report_uses = [self.application_message_report_uses] if self.application_message_report_uses is not None else []
        self.application_message_report_uses = [v if isinstance(v, ApplicationMessageReportTypeEnum) else ApplicationMessageReportTypeEnum(v) for v in self.application_message_report_uses]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfrastructureMessageDetail(YAMLRoot):
    """
    Per-message description appearing in a category's Messages sub-section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["InfrastructureMessageDetail"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:InfrastructureMessageDetail"
    class_name: ClassVar[str] = "InfrastructureMessageDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.InfrastructureMessageDetail

    msg_type: str = None
    message_name: str = None
    description: Optional[str] = None
    layout_url: Optional[Union[str, URI]] = None
    infra_layout_rows: Optional[Union[Union[dict, "InfrastructureLayoutRow"], list[Union[dict, "InfrastructureLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, str):
            self.msg_type = str(self.msg_type)

        if self._is_empty(self.message_name):
            self.MissingRequiredField("message_name")
        if not isinstance(self.message_name, str):
            self.message_name = str(self.message_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.layout_url is not None and not isinstance(self.layout_url, URI):
            self.layout_url = URI(self.layout_url)

        self._normalize_inlined_as_list(slot_name="infra_layout_rows", slot_type=InfrastructureLayoutRow, key_name="infra_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfrastructureComponentDetail(YAMLRoot):
    """
    Per-component description appearing in a category's Components sub-section.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["InfrastructureComponentDetail"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:InfrastructureComponentDetail"
    class_name: ClassVar[str] = "InfrastructureComponentDetail"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.InfrastructureComponentDetail

    component_name: str = None
    repetition: Optional[Union[str, "ComponentRepetition"]] = None
    description: Optional[str] = None
    layout_url: Optional[Union[str, URI]] = None
    infra_layout_rows: Optional[Union[Union[dict, "InfrastructureLayoutRow"], list[Union[dict, "InfrastructureLayoutRow"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.component_name):
            self.MissingRequiredField("component_name")
        if not isinstance(self.component_name, str):
            self.component_name = str(self.component_name)

        if self.repetition is not None and not isinstance(self.repetition, ComponentRepetition):
            self.repetition = ComponentRepetition(self.repetition)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.layout_url is not None and not isinstance(self.layout_url, URI):
            self.layout_url = URI(self.layout_url)

        self._normalize_inlined_as_list(slot_name="infra_layout_rows", slot_type=InfrastructureLayoutRow, key_name="infra_layout_kind", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfrastructureLayoutRow(YAMLRoot):
    """
    One row of the layout table published in the Infrastructure Appendix for a message or component. Each row
    identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is
    required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group
    counter.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["InfrastructureLayoutRow"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:InfrastructureLayoutRow"
    class_name: ClassVar[str] = "InfrastructureLayoutRow"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.InfrastructureLayoutRow

    infra_layout_kind: Union[str, "InfrastructureLayoutRowKindEnum"] = None
    infra_layout_element_name: str = None
    infra_layout_field_tag: Optional[int] = None
    infra_layout_required: Optional[Union[bool, Bool]] = None
    infra_layout_description: Optional[str] = None
    infra_layout_nested: Optional[Union[bool, Bool]] = False

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.infra_layout_kind):
            self.MissingRequiredField("infra_layout_kind")
        if not isinstance(self.infra_layout_kind, InfrastructureLayoutRowKindEnum):
            self.infra_layout_kind = InfrastructureLayoutRowKindEnum(self.infra_layout_kind)

        if self._is_empty(self.infra_layout_element_name):
            self.MissingRequiredField("infra_layout_element_name")
        if not isinstance(self.infra_layout_element_name, str):
            self.infra_layout_element_name = str(self.infra_layout_element_name)

        if self.infra_layout_field_tag is not None and not isinstance(self.infra_layout_field_tag, int):
            self.infra_layout_field_tag = int(self.infra_layout_field_tag)

        if self.infra_layout_required is not None and not isinstance(self.infra_layout_required, Bool):
            self.infra_layout_required = Bool(self.infra_layout_required)

        if self.infra_layout_description is not None and not isinstance(self.infra_layout_description, str):
            self.infra_layout_description = str(self.infra_layout_description)

        if self.infra_layout_nested is not None and not isinstance(self.infra_layout_nested, Bool):
            self.infra_layout_nested = Bool(self.infra_layout_nested)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StandardResponseMapping(YAMLRoot):
    """
    One row of a "Standard Responses for <area> Messages" table mapping a request message to its appropriate
    response(s).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["StandardResponseMapping"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:StandardResponseMapping"
    class_name: ClassVar[str] = "StandardResponseMapping"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.StandardResponseMapping

    category_label: str = None
    fix_message: str = None
    appropriate_responses: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.category_label):
            self.MissingRequiredField("category_label")
        if not isinstance(self.category_label, str):
            self.category_label = str(self.category_label)

        if self._is_empty(self.fix_message):
            self.MissingRequiredField("fix_message")
        if not isinstance(self.fix_message, str):
            self.fix_message = str(self.fix_message)

        if self._is_empty(self.appropriate_responses):
            self.MissingRequiredField("appropriate_responses")
        if not isinstance(self.appropriate_responses, str):
            self.appropriate_responses = str(self.appropriate_responses)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ApplicationMessageReferenceKey(YAMLRoot):
    """
    One row of a "Key Fields for <area> Application Message References" table identifying the field whose value is
    copied into BusinessRejectRefID(379).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["ApplicationMessageReferenceKey"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:ApplicationMessageReferenceKey"
    class_name: ClassVar[str] = "ApplicationMessageReferenceKey"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.ApplicationMessageReferenceKey

    category_label: str = None
    fix_message: str = None
    business_reject_ref_id_value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.category_label):
            self.MissingRequiredField("category_label")
        if not isinstance(self.category_label, str):
            self.category_label = str(self.category_label)

        if self._is_empty(self.fix_message):
            self.MissingRequiredField("fix_message")
        if not isinstance(self.fix_message, str):
            self.fix_message = str(self.fix_message)

        if self._is_empty(self.business_reject_ref_id_value):
            self.MissingRequiredField("business_reject_ref_id_value")
        if not isinstance(self.business_reject_ref_id_value, str):
            self.business_reject_ref_id_value = str(self.business_reject_ref_id_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BusinessRejectReasonDescription(YAMLRoot):
    """
    One entry of the BusinessRejectReason(380) code table.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["BusinessRejectReasonDescription"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:BusinessRejectReasonDescription"
    class_name: ClassVar[str] = "BusinessRejectReasonDescription"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.BusinessRejectReasonDescription

    reject_reason_code: Union[int, BusinessRejectReasonDescriptionRejectReasonCode] = None
    reject_reason_label: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.reject_reason_code):
            self.MissingRequiredField("reject_reason_code")
        if not isinstance(self.reject_reason_code, BusinessRejectReasonDescriptionRejectReasonCode):
            self.reject_reason_code = BusinessRejectReasonDescriptionRejectReasonCode(self.reject_reason_code)

        if self._is_empty(self.reject_reason_label):
            self.MissingRequiredField("reject_reason_label")
        if not isinstance(self.reject_reason_label, str):
            self.reject_reason_label = str(self.reject_reason_label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class InfrastructureGlobalComponentReference(YAMLRoot):
    """
    A reference from the Infrastructure business area to a Global Component declared on the FIX Latest "Global
    Components" page. Records the component name, the FIX tags it contributes, and the Infrastructure categories and
    messages that embed it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_INFRASTRUCTURE["InfrastructureGlobalComponentReference"]
    class_class_curie: ClassVar[str] = "fix_infrastructure:InfrastructureGlobalComponentReference"
    class_name: ClassVar[str] = "InfrastructureGlobalComponentReference"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.InfrastructureGlobalComponentReference

    infra_global_component_name: Union[str, "InfrastructureGlobalComponentReferenceInfraGlobalComponentName"] = None
    infra_global_component_used_in: Union[Union[str, "InfrastructureCategoryEnum"], list[Union[str, "InfrastructureCategoryEnum"]]] = None
    infra_global_component_repetition: Optional[str] = None
    infra_global_component_field_tags: Optional[Union[int, list[int]]] = empty_list()
    infra_global_component_field_names: Optional[Union[str, list[str]]] = empty_list()
    infra_global_component_msg_types: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.infra_global_component_name):
            self.MissingRequiredField("infra_global_component_name")
        if not isinstance(self.infra_global_component_name, InfrastructureGlobalComponentReferenceInfraGlobalComponentName):
            self.infra_global_component_name = InfrastructureGlobalComponentReferenceInfraGlobalComponentName(self.infra_global_component_name)

        if self._is_empty(self.infra_global_component_used_in):
            self.MissingRequiredField("infra_global_component_used_in")
        if not isinstance(self.infra_global_component_used_in, list):
            self.infra_global_component_used_in = [self.infra_global_component_used_in] if self.infra_global_component_used_in is not None else []
        self.infra_global_component_used_in = [v if isinstance(v, InfrastructureCategoryEnum) else InfrastructureCategoryEnum(v) for v in self.infra_global_component_used_in]

        if self.infra_global_component_repetition is not None and not isinstance(self.infra_global_component_repetition, str):
            self.infra_global_component_repetition = str(self.infra_global_component_repetition)

        if not isinstance(self.infra_global_component_field_tags, list):
            self.infra_global_component_field_tags = [self.infra_global_component_field_tags] if self.infra_global_component_field_tags is not None else []
        self.infra_global_component_field_tags = [v if isinstance(v, int) else int(v) for v in self.infra_global_component_field_tags]

        if not isinstance(self.infra_global_component_field_names, list):
            self.infra_global_component_field_names = [self.infra_global_component_field_names] if self.infra_global_component_field_names is not None else []
        self.infra_global_component_field_names = [v if isinstance(v, str) else str(v) for v in self.infra_global_component_field_names]

        if not isinstance(self.infra_global_component_msg_types, list):
            self.infra_global_component_msg_types = [self.infra_global_component_msg_types] if self.infra_global_component_msg_types is not None else []
        self.infra_global_component_msg_types = [v if isinstance(v, str) else str(v) for v in self.infra_global_component_msg_types]

        super().__post_init__(**kwargs)

# Slots
class slots:
    pass

slots.id = Slot(uri=FIX_BASE.id, name="id", curie=FIX_BASE.curie('id'),
                   model_uri=FIX_PROTOCOL.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.name, domain=None, range=str)

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.description, domain=None, range=Optional[str])

slots.acronym = Slot(uri=SCHEMA.alternateName, name="acronym", curie=SCHEMA.curie('alternateName'),
                   model_uri=FIX_PROTOCOL.acronym, domain=None, range=Optional[str])

slots.see_also = Slot(uri=RDFS.seeAlso, name="see_also", curie=RDFS.curie('seeAlso'),
                   model_uri=FIX_PROTOCOL.see_also, domain=None, range=Optional[Union[Union[str, URI], list[Union[str, URI]]]])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.title, domain=None, range=Optional[str])

slots.published_version = Slot(uri=SCHEMA.version, name="published_version", curie=SCHEMA.curie('version'),
                   model_uri=FIX_PROTOCOL.published_version, domain=None, range=Optional[str])

slots.published_date = Slot(uri=DCTERMS.issued, name="published_date", curie=DCTERMS.curie('issued'),
                   model_uri=FIX_PROTOCOL.published_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.publisher = Slot(uri=DCTERMS.publisher, name="publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=FIX_PROTOCOL.publisher, domain=None, range=Optional[str])

slots.preface = Slot(uri=FIX_BASE.preface, name="preface", curie=FIX_BASE.curie('preface'),
                   model_uri=FIX_PROTOCOL.preface, domain=None, range=Optional[str])

slots.introduction_text = Slot(uri=FIX_BASE.introduction_text, name="introduction_text", curie=FIX_BASE.curie('introduction_text'),
                   model_uri=FIX_PROTOCOL.introduction_text, domain=None, range=Optional[str])

slots.utc_leap_seconds_note = Slot(uri=FIX_BASE.utc_leap_seconds_note, name="utc_leap_seconds_note", curie=FIX_BASE.curie('utc_leap_seconds_note'),
                   model_uri=FIX_PROTOCOL.utc_leap_seconds_note, domain=None, range=Optional[str])

slots.about_fpl = Slot(uri=FIX_BASE.about_fpl, name="about_fpl", curie=FIX_BASE.curie('about_fpl'),
                   model_uri=FIX_PROTOCOL.about_fpl, domain=None, range=Optional[Union[dict, FIXProtocolLimited]])

slots.standards = Slot(uri=FIX_BASE.standards, name="standards", curie=FIX_BASE.curie('standards'),
                   model_uri=FIX_PROTOCOL.standards, domain=None, range=Optional[Union[dict[Union[str, FIXFamilyStandardId], Union[dict, FIXFamilyStandard]], list[Union[dict, FIXFamilyStandard]]]])

slots.extension_packs = Slot(uri=FIX_BASE.extension_packs, name="extension_packs", curie=FIX_BASE.curie('extension_packs'),
                   model_uri=FIX_PROTOCOL.extension_packs, domain=None, range=Optional[Union[dict[Union[int, ExtensionPackNumber], Union[dict, ExtensionPack]], list[Union[dict, ExtensionPack]]]])

slots.datatypes = Slot(uri=FIX_BASE.datatypes, name="datatypes", curie=FIX_BASE.curie('datatypes'),
                   model_uri=FIX_PROTOCOL.datatypes, domain=None, range=Optional[Union[dict[Union[str, FIXDatatypeDatatypeName], Union[dict, FIXDatatype]], list[Union[dict, FIXDatatype]]]])

slots.business_areas = Slot(uri=FIX_BASE.business_areas, name="business_areas", curie=FIX_BASE.curie('business_areas'),
                   model_uri=FIX_PROTOCOL.business_areas, domain=None, range=Optional[Union[dict[Union[str, BusinessAreaArea], Union[dict, BusinessArea]], list[Union[dict, BusinessArea]]]])

slots.global_components = Slot(uri=FIX_BASE.global_components, name="global_components", curie=FIX_BASE.curie('global_components'),
                   model_uri=FIX_PROTOCOL.global_components, domain=None, range=Optional[Union[dict[Union[str, GlobalComponentComponentName], Union[dict, GlobalComponent]], list[Union[dict, GlobalComponent]]]])

slots.udf_ranges = Slot(uri=FIX_BASE.udf_ranges, name="udf_ranges", curie=FIX_BASE.curie('udf_ranges'),
                   model_uri=FIX_PROTOCOL.udf_ranges, domain=None, range=Optional[Union[dict[Union[str, UDFTagRangeRangeId], Union[dict, UDFTagRange]], list[Union[dict, UDFTagRange]]]])

slots.product_coverage = Slot(uri=FIX_BASE.product_coverage, name="product_coverage", curie=FIX_BASE.curie('product_coverage'),
                   model_uri=FIX_PROTOCOL.product_coverage, domain=None, range=Optional[Union[Union[str, "ProductCoverage"], list[Union[str, "ProductCoverage"]]]])

slots.brand_name = Slot(uri=FIX_BASE.brand_name, name="brand_name", curie=FIX_BASE.curie('brand_name'),
                   model_uri=FIX_PROTOCOL.brand_name, domain=None, range=Optional[str])

slots.legal_name = Slot(uri=SCHEMA.legalName, name="legal_name", curie=SCHEMA.curie('legalName'),
                   model_uri=FIX_PROTOCOL.legal_name, domain=None, range=Optional[str])

slots.website = Slot(uri=SCHEMA.url, name="website", curie=SCHEMA.curie('url'),
                   model_uri=FIX_PROTOCOL.website, domain=None, range=Optional[Union[str, URI]])

slots.member_firms_url = Slot(uri=FIX_BASE.member_firms_url, name="member_firms_url", curie=FIX_BASE.curie('member_firms_url'),
                   model_uri=FIX_PROTOCOL.member_firms_url, domain=None, range=Optional[Union[str, URI]])

slots.working_groups_url = Slot(uri=FIX_BASE.working_groups_url, name="working_groups_url", curie=FIX_BASE.curie('working_groups_url'),
                   model_uri=FIX_PROTOCOL.working_groups_url, domain=None, range=Optional[Union[str, URI]])

slots.committees_url = Slot(uri=FIX_BASE.committees_url, name="committees_url", curie=FIX_BASE.curie('committees_url'),
                   model_uri=FIX_PROTOCOL.committees_url, domain=None, range=Optional[Union[str, URI]])

slots.member_types = Slot(uri=FIX_BASE.member_types, name="member_types", curie=FIX_BASE.curie('member_types'),
                   model_uri=FIX_PROTOCOL.member_types, domain=None, range=Optional[Union[Union[str, "FPLMemberType"], list[Union[str, "FPLMemberType"]]]])

slots.governance_bodies = Slot(uri=FIX_BASE.governance_bodies, name="governance_bodies", curie=FIX_BASE.curie('governance_bodies'),
                   model_uri=FIX_PROTOCOL.governance_bodies, domain=None, range=Optional[Union[Union[str, "FPLCommitteeRole"], list[Union[str, "FPLCommitteeRole"]]]])

slots.product_committees = Slot(uri=FIX_BASE.product_committees, name="product_committees", curie=FIX_BASE.curie('product_committees'),
                   model_uri=FIX_PROTOCOL.product_committees, domain=None, range=Optional[Union[Union[str, "FPLProductGroup"], list[Union[str, "FPLProductGroup"]]]])

slots.regional_committees = Slot(uri=FIX_BASE.regional_committees, name="regional_committees", curie=FIX_BASE.curie('regional_committees'),
                   model_uri=FIX_PROTOCOL.regional_committees, domain=None, range=Optional[Union[Union[str, "FPLRegion"], list[Union[str, "FPLRegion"]]]])

slots.layer = Slot(uri=FIX_BASE.layer, name="layer", curie=FIX_BASE.curie('layer'),
                   model_uri=FIX_PROTOCOL.layer, domain=None, range=Optional[Union[str, "StandardLayer"]])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=FIX_PROTOCOL.version, domain=None, range=Optional[str])

slots.session_profile = Slot(uri=FIX_BASE.session_profile, name="session_profile", curie=FIX_BASE.curie('session_profile'),
                   model_uri=FIX_PROTOCOL.session_profile, domain=None, range=Optional[Union[str, "SessionProtocolName"]])

slots.encoding_name = Slot(uri=FIX_BASE.encoding_name, name="encoding_name", curie=FIX_BASE.curie('encoding_name'),
                   model_uri=FIX_PROTOCOL.encoding_name, domain=None, range=Optional[Union[str, "StandardEncodingName"]])

slots.number = Slot(uri=FIX_BASE.number, name="number", curie=FIX_BASE.curie('number'),
                   model_uri=FIX_PROTOCOL.number, domain=None, range=Optional[int])

slots.size = Slot(uri=FIX_BASE.size, name="size", curie=FIX_BASE.curie('size'),
                   model_uri=FIX_PROTOCOL.size, domain=None, range=Optional[Union[str, "ExtensionPackSize"]])

slots.enhancement_summary = Slot(uri=FIX_BASE.enhancement_summary, name="enhancement_summary", curie=FIX_BASE.curie('enhancement_summary'),
                   model_uri=FIX_PROTOCOL.enhancement_summary, domain=None, range=Optional[str])

slots.applies_to_session_layer_only = Slot(uri=FIX_BASE.applies_to_session_layer_only, name="applies_to_session_layer_only", curie=FIX_BASE.curie('applies_to_session_layer_only'),
                   model_uri=FIX_PROTOCOL.applies_to_session_layer_only, domain=None, range=Optional[Union[bool, Bool]])

slots.applies_to_fixml_only = Slot(uri=FIX_BASE.applies_to_fixml_only, name="applies_to_fixml_only", curie=FIX_BASE.curie('applies_to_fixml_only'),
                   model_uri=FIX_PROTOCOL.applies_to_fixml_only, domain=None, range=Optional[Union[bool, Bool]])

slots.datatype_name = Slot(uri=FIX_BASE.datatype_name, name="datatype_name", curie=FIX_BASE.curie('datatype_name'),
                   model_uri=FIX_PROTOCOL.datatype_name, domain=None, range=Optional[Union[str, "FIXDatatypeName"]])

slots.definition = Slot(uri=FIX_BASE.definition, name="definition", curie=FIX_BASE.curie('definition'),
                   model_uri=FIX_PROTOCOL.definition, domain=None, range=Optional[str])

slots.value_space = Slot(uri=FIX_BASE.value_space, name="value_space", curie=FIX_BASE.curie('value_space'),
                   model_uri=FIX_PROTOCOL.value_space, domain=None, range=Optional[Union[Union[str, "ISO11404ValueSpace"], list[Union[str, "ISO11404ValueSpace"]]]])

slots.value_space_notes = Slot(uri=FIX_BASE.value_space_notes, name="value_space_notes", curie=FIX_BASE.curie('value_space_notes'),
                   model_uri=FIX_PROTOCOL.value_space_notes, domain=None, range=Optional[str])

slots.deprecated_for_new_designs = Slot(uri=FIX_BASE.deprecated_for_new_designs, name="deprecated_for_new_designs", curie=FIX_BASE.curie('deprecated_for_new_designs'),
                   model_uri=FIX_PROTOCOL.deprecated_for_new_designs, domain=None, range=Optional[Union[bool, Bool]])

slots.external_code_set = Slot(uri=DCTERMS.conformsTo, name="external_code_set", curie=DCTERMS.curie('conformsTo'),
                   model_uri=FIX_PROTOCOL.external_code_set, domain=None, range=Optional[str])

slots.time_unit = Slot(uri=FIX_BASE.time_unit, name="time_unit", curie=FIX_BASE.curie('time_unit'),
                   model_uri=FIX_PROTOCOL.time_unit, domain=None, range=Optional[Union[Union[str, "TimePrecision"], list[Union[str, "TimePrecision"]]]])

slots.radix = Slot(uri=FIX_BASE.radix, name="radix", curie=FIX_BASE.curie('radix'),
                   model_uri=FIX_PROTOCOL.radix, domain=None, range=Optional[int])

slots.repertoire = Slot(uri=FIX_BASE.repertoire, name="repertoire", curie=FIX_BASE.curie('repertoire'),
                   model_uri=FIX_PROTOCOL.repertoire, domain=None, range=Optional[str])

slots.index_lower_bound = Slot(uri=FIX_BASE.index_lower_bound, name="index_lower_bound", curie=FIX_BASE.curie('index_lower_bound'),
                   model_uri=FIX_PROTOCOL.index_lower_bound, domain=None, range=Optional[int])

slots.index_upper_bound = Slot(uri=FIX_BASE.index_upper_bound, name="index_upper_bound", curie=FIX_BASE.curie('index_upper_bound'),
                   model_uri=FIX_PROTOCOL.index_upper_bound, domain=None, range=Optional[int])

slots.minimum_value = Slot(uri=FIX_BASE.minimum_value, name="minimum_value", curie=FIX_BASE.curie('minimum_value'),
                   model_uri=FIX_PROTOCOL.minimum_value, domain=None, range=Optional[int])

slots.maximum_value = Slot(uri=FIX_BASE.maximum_value, name="maximum_value", curie=FIX_BASE.curie('maximum_value'),
                   model_uri=FIX_PROTOCOL.maximum_value, domain=None, range=Optional[int])

slots.footnote_numbers = Slot(uri=FIX_BASE.footnote_numbers, name="footnote_numbers", curie=FIX_BASE.curie('footnote_numbers'),
                   model_uri=FIX_PROTOCOL.footnote_numbers, domain=None, range=Optional[Union[int, list[int]]])

slots.area = Slot(uri=SCHEMA.identifier, name="area", curie=SCHEMA.curie('identifier'),
                   model_uri=FIX_PROTOCOL.area, domain=None, range=Optional[Union[str, "BusinessAreaEnum"]])

slots.categories = Slot(uri=FIX_BASE.categories, name="categories", curie=FIX_BASE.curie('categories'),
                   model_uri=FIX_PROTOCOL.categories, domain=None, range=Optional[Union[dict[Union[str, MessageCategoryCategory], Union[dict, MessageCategory]], list[Union[dict, MessageCategory]]]])

slots.category = Slot(uri=FIX_BASE.category, name="category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.category, domain=None, range=Optional[Union[str, "MessageCategoryEnum"]])

slots.business_area = Slot(uri=FIX_BASE.business_area, name="business_area", curie=FIX_BASE.curie('business_area'),
                   model_uri=FIX_PROTOCOL.business_area, domain=None, range=Optional[Union[str, "BusinessAreaEnum"]])

slots.messages = Slot(uri=FIX_BASE.messages, name="messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.messages, domain=None, range=Optional[Union[dict[Union[str, MessageMsgType], Union[dict, Message]], list[Union[dict, Message]]]])

slots.tag = Slot(uri=FIX_BASE.tag, name="tag", curie=FIX_BASE.curie('tag'),
                   model_uri=FIX_PROTOCOL.tag, domain=None, range=Optional[int])

slots.field_name = Slot(uri=SCHEMA.name, name="field_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.field_name, domain=None, range=Optional[str])

slots.datatype = Slot(uri=FIX_BASE.datatype, name="datatype", curie=FIX_BASE.curie('datatype'),
                   model_uri=FIX_PROTOCOL.datatype, domain=None, range=Optional[Union[str, "FIXDatatypeName"]])

slots.requirement = Slot(uri=FIX_BASE.requirement, name="requirement", curie=FIX_BASE.curie('requirement'),
                   model_uri=FIX_PROTOCOL.requirement, domain=None, range=Optional[Union[str, "FieldRequirement"]])

slots.is_user_defined = Slot(uri=FIX_BASE.is_user_defined, name="is_user_defined", curie=FIX_BASE.curie('is_user_defined'),
                   model_uri=FIX_PROTOCOL.is_user_defined, domain=None, range=Optional[Union[bool, Bool]])

slots.component_name = Slot(uri=SCHEMA.name, name="component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.component_name, domain=None, range=Optional[str])

slots.scope = Slot(uri=FIX_BASE.scope, name="scope", curie=FIX_BASE.curie('scope'),
                   model_uri=FIX_PROTOCOL.scope, domain=None, range=Optional[Union[str, "ComponentScope"]])

slots.is_repeating_group = Slot(uri=FIX_BASE.is_repeating_group, name="is_repeating_group", curie=FIX_BASE.curie('is_repeating_group'),
                   model_uri=FIX_PROTOCOL.is_repeating_group, domain=None, range=Optional[Union[bool, Bool]])

slots.fields = Slot(uri=FIX_BASE.fields, name="fields", curie=FIX_BASE.curie('fields'),
                   model_uri=FIX_PROTOCOL.fields, domain=None, range=Optional[Union[dict[Union[int, FieldTag], Union[dict, Field]], list[Union[dict, Field]]]])

slots.nested_components = Slot(uri=FIX_BASE.nested_components, name="nested_components", curie=FIX_BASE.curie('nested_components'),
                   model_uri=FIX_PROTOCOL.nested_components, domain=None, range=Optional[Union[Union[str, ComponentComponentName], list[Union[str, ComponentComponentName]]]])

slots.components = Slot(uri=FIX_BASE.components, name="components", curie=FIX_BASE.curie('components'),
                   model_uri=FIX_PROTOCOL.components, domain=None, range=Optional[Union[Union[str, ComponentComponentName], list[Union[str, ComponentComponentName]]]])

slots.component_group = Slot(uri=FIX_BASE.component_group, name="component_group", curie=FIX_BASE.curie('component_group'),
                   model_uri=FIX_PROTOCOL.component_group, domain=None, range=Optional[Union[str, "ComponentGroup"]])

slots.applies_to_instrument = Slot(uri=FIX_BASE.applies_to_instrument, name="applies_to_instrument", curie=FIX_BASE.curie('applies_to_instrument'),
                   model_uri=FIX_PROTOCOL.applies_to_instrument, domain=None, range=Optional[Union[bool, Bool]])

slots.applies_to_leg = Slot(uri=FIX_BASE.applies_to_leg, name="applies_to_leg", curie=FIX_BASE.curie('applies_to_leg'),
                   model_uri=FIX_PROTOCOL.applies_to_leg, domain=None, range=Optional[Union[bool, Bool]])

slots.applies_to_underlying = Slot(uri=FIX_BASE.applies_to_underlying, name="applies_to_underlying", curie=FIX_BASE.curie('applies_to_underlying'),
                   model_uri=FIX_PROTOCOL.applies_to_underlying, domain=None, range=Optional[Union[bool, Bool]])

slots.conceptually_identical_to = Slot(uri=FIX_BASE.conceptually_identical_to, name="conceptually_identical_to", curie=FIX_BASE.curie('conceptually_identical_to'),
                   model_uri=FIX_PROTOCOL.conceptually_identical_to, domain=None, range=Optional[Union[str, list[str]]])

slots.msg_type = Slot(uri=FIX_BASE.msg_type, name="msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.msg_type, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.message_name = Slot(uri=SCHEMA.name, name="message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.message_name, domain=None, range=Optional[str])

slots.range_id = Slot(uri=FIX_BASE.range_id, name="range_id", curie=FIX_BASE.curie('range_id'),
                   model_uri=FIX_PROTOCOL.range_id, domain=None, range=Optional[str])

slots.low_tag = Slot(uri=FIX_BASE.low_tag, name="low_tag", curie=FIX_BASE.curie('low_tag'),
                   model_uri=FIX_PROTOCOL.low_tag, domain=None, range=Optional[int])

slots.high_tag = Slot(uri=FIX_BASE.high_tag, name="high_tag", curie=FIX_BASE.curie('high_tag'),
                   model_uri=FIX_PROTOCOL.high_tag, domain=None, range=Optional[int])

slots.usage = Slot(uri=FIX_BASE.usage, name="usage", curie=FIX_BASE.curie('usage'),
                   model_uri=FIX_PROTOCOL.usage, domain=None, range=Optional[Union[str, "UDFTagRangeUsage"]])

slots.requires_registration = Slot(uri=FIX_BASE.requires_registration, name="requires_registration", curie=FIX_BASE.curie('requires_registration'),
                   model_uri=FIX_PROTOCOL.requires_registration, domain=None, range=Optional[Union[bool, Bool]])

slots.gc_id = Slot(uri=FIX_BASE.gc_id, name="gc_id", curie=FIX_BASE.curie('gc_id'),
                   model_uri=FIX_PROTOCOL.gc_id, domain=None, range=Optional[int])

slots.gc_referenced_in = Slot(uri=FIX_BASE.gc_referenced_in, name="gc_referenced_in", curie=FIX_BASE.curie('gc_referenced_in'),
                   model_uri=FIX_PROTOCOL.gc_referenced_in, domain=None, range=Optional[Union[Union[str, "GlobalComponentBusinessAreaEnum"], list[Union[str, "GlobalComponentBusinessAreaEnum"]]]])

slots.introduction = Slot(uri=FIX_PRE_TRADE.introduction, name="introduction", curie=FIX_PRE_TRADE.curie('introduction'),
                   model_uri=FIX_PROTOCOL.introduction, domain=None, range=Optional[str])

slots.common_components = Slot(uri=FIX_PRE_TRADE.common_components, name="common_components", curie=FIX_PRE_TRADE.curie('common_components'),
                   model_uri=FIX_PROTOCOL.common_components, domain=None, range=Optional[Union[Union[str, "PreTradeCommonComponentName"], list[Union[str, "PreTradeCommonComponentName"]]]])

slots.footnotes = Slot(uri=FIX_PRE_TRADE.footnotes, name="footnotes", curie=FIX_PRE_TRADE.curie('footnotes'),
                   model_uri=FIX_PROTOCOL.footnotes, domain=None, range=Optional[Union[dict[Union[int, ComponentTableFootnoteFootnoteNumber], Union[dict, ComponentTableFootnote]], list[Union[dict, ComponentTableFootnote]]]])

slots.category_sections = Slot(uri=FIX_PRE_TRADE.category_sections, name="category_sections", curie=FIX_PRE_TRADE.curie('category_sections'),
                   model_uri=FIX_PROTOCOL.category_sections, domain=None, range=Optional[Union[dict[Union[str, PreTradeCategorySectionCategory], Union[dict, PreTradeCategorySection]], list[Union[dict, PreTradeCategorySection]]]])

slots.category_specific_components = Slot(uri=FIX_PRE_TRADE.category_specific_components, name="category_specific_components", curie=FIX_PRE_TRADE.curie('category_specific_components'),
                   model_uri=FIX_PROTOCOL.category_specific_components, domain=None, range=Optional[Union[dict[Union[str, PreTradeComponentDetailComponentName], Union[dict, PreTradeComponentDetail]], list[Union[dict, PreTradeComponentDetail]]]])

slots.repetition = Slot(uri=FIX_PRE_TRADE.repetition, name="repetition", curie=FIX_PRE_TRADE.curie('repetition'),
                   model_uri=FIX_PROTOCOL.repetition, domain=None, range=Optional[Union[str, "ComponentRepetition"]])

slots.is_common = Slot(uri=FIX_PRE_TRADE.is_common, name="is_common", curie=FIX_PRE_TRADE.curie('is_common'),
                   model_uri=FIX_PROTOCOL.is_common, domain=None, range=Optional[Union[bool, Bool]])

slots.footnote_number = Slot(uri=FIX_PRE_TRADE.footnote_number, name="footnote_number", curie=FIX_PRE_TRADE.curie('footnote_number'),
                   model_uri=FIX_PROTOCOL.footnote_number, domain=None, range=Optional[int])

slots.introduced_in = Slot(uri=FIX_PRE_TRADE.introduced_in, name="introduced_in", curie=FIX_PRE_TRADE.curie('introduced_in'),
                   model_uri=FIX_PROTOCOL.introduced_in, domain=None, range=Optional[str])

slots.sole_category = Slot(uri=FIX_PRE_TRADE.sole_category, name="sole_category", curie=FIX_PRE_TRADE.curie('sole_category'),
                   model_uri=FIX_PROTOCOL.sole_category, domain=None, range=Optional[Union[str, "PreTradeCategoryEnum"]])

slots.text = Slot(uri=FIX_PRE_TRADE.text, name="text", curie=FIX_PRE_TRADE.curie('text'),
                   model_uri=FIX_PROTOCOL.text, domain=None, range=Optional[str])

slots.layout_url = Slot(uri=SCHEMA.url, name="layout_url", curie=SCHEMA.curie('url'),
                   model_uri=FIX_PROTOCOL.layout_url, domain=None, range=Optional[Union[str, URI]])

slots.diagram_conventions = Slot(uri=FIX_PRE_TRADE.diagram_conventions, name="diagram_conventions", curie=FIX_PRE_TRADE.curie('diagram_conventions'),
                   model_uri=FIX_PROTOCOL.diagram_conventions, domain=None, range=Optional[str])

slots.messages_overview_note = Slot(uri=FIX_PRE_TRADE.messages_overview_note, name="messages_overview_note", curie=FIX_PRE_TRADE.curie('messages_overview_note'),
                   model_uri=FIX_PROTOCOL.messages_overview_note, domain=None, range=Optional[str])

slots.components_overview_note = Slot(uri=FIX_PRE_TRADE.components_overview_note, name="components_overview_note", curie=FIX_PRE_TRADE.curie('components_overview_note'),
                   model_uri=FIX_PROTOCOL.components_overview_note, domain=None, range=Optional[str])

slots.category_components_note = Slot(uri=FIX_PRE_TRADE.category_components_note, name="category_components_note", curie=FIX_PRE_TRADE.curie('category_components_note'),
                   model_uri=FIX_PROTOCOL.category_components_note, domain=None, range=Optional[str])

slots.group_title = Slot(uri=SCHEMA.name, name="group_title", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.group_title, domain=None, range=Optional[str])

slots.message_groups = Slot(uri=FIX_PRE_TRADE.message_groups, name="message_groups", curie=FIX_PRE_TRADE.curie('message_groups'),
                   model_uri=FIX_PROTOCOL.message_groups, domain=None, range=Optional[Union[dict[Union[str, MessageGroupGroupTitle], Union[dict, MessageGroup]], list[Union[dict, MessageGroup]]]])

slots.common_component_details = Slot(uri=FIX_PRE_TRADE.common_component_details, name="common_component_details", curie=FIX_PRE_TRADE.curie('common_component_details'),
                   model_uri=FIX_PROTOCOL.common_component_details, domain=None, range=Optional[Union[dict[Union[str, CommonComponentDetailComponentName], Union[dict, CommonComponentDetail]], list[Union[dict, CommonComponentDetail]]]])

slots.quote_models = Slot(uri=FIX_PRE_TRADE.quote_models, name="quote_models", curie=FIX_PRE_TRADE.curie('quote_models'),
                   model_uri=FIX_PROTOCOL.quote_models, domain=None, range=Optional[Union[Union[str, "QuoteModelEnum"], list[Union[str, "QuoteModelEnum"]]]])

slots.pre_layout_rows = Slot(uri=FIX_PRE_TRADE.pre_layout_rows, name="pre_layout_rows", curie=FIX_PRE_TRADE.curie('pre_layout_rows'),
                   model_uri=FIX_PROTOCOL.pre_layout_rows, domain=None, range=Optional[Union[Union[dict, PreTradeLayoutRow], list[Union[dict, PreTradeLayoutRow]]]])

slots.pre_layout_kind = Slot(uri=FIX_PRE_TRADE.pre_layout_kind, name="pre_layout_kind", curie=FIX_PRE_TRADE.curie('pre_layout_kind'),
                   model_uri=FIX_PROTOCOL.pre_layout_kind, domain=None, range=Optional[Union[str, "PreTradeLayoutRowKindEnum"]])

slots.pre_layout_field_tag = Slot(uri=FIX_PRE_TRADE.pre_layout_field_tag, name="pre_layout_field_tag", curie=FIX_PRE_TRADE.curie('pre_layout_field_tag'),
                   model_uri=FIX_PROTOCOL.pre_layout_field_tag, domain=None, range=Optional[int])

slots.pre_layout_element_name = Slot(uri=FIX_PRE_TRADE.pre_layout_element_name, name="pre_layout_element_name", curie=FIX_PRE_TRADE.curie('pre_layout_element_name'),
                   model_uri=FIX_PROTOCOL.pre_layout_element_name, domain=None, range=Optional[str])

slots.pre_layout_required = Slot(uri=FIX_PRE_TRADE.pre_layout_required, name="pre_layout_required", curie=FIX_PRE_TRADE.curie('pre_layout_required'),
                   model_uri=FIX_PROTOCOL.pre_layout_required, domain=None, range=Optional[Union[bool, Bool]])

slots.pre_layout_description = Slot(uri=FIX_PRE_TRADE.pre_layout_description, name="pre_layout_description", curie=FIX_PRE_TRADE.curie('pre_layout_description'),
                   model_uri=FIX_PROTOCOL.pre_layout_description, domain=None, range=Optional[str])

slots.pre_layout_nested = Slot(uri=FIX_PRE_TRADE.pre_layout_nested, name="pre_layout_nested", curie=FIX_PRE_TRADE.curie('pre_layout_nested'),
                   model_uri=FIX_PROTOCOL.pre_layout_nested, domain=None, range=Optional[Union[bool, Bool]])

slots.trade_area = Slot(uri=SCHEMA.identifier, name="trade_area", curie=SCHEMA.curie('identifier'),
                   model_uri=FIX_PROTOCOL.trade_area, domain=None, range=Optional[Union[str, "BusinessAreaEnum"]])

slots.trade_introduction = Slot(uri=FIX_TRADE.trade_introduction, name="trade_introduction", curie=FIX_TRADE.curie('trade_introduction'),
                   model_uri=FIX_PROTOCOL.trade_introduction, domain=None, range=Optional[str])

slots.trade_common_components = Slot(uri=FIX_TRADE.trade_common_components, name="trade_common_components", curie=FIX_TRADE.curie('trade_common_components'),
                   model_uri=FIX_PROTOCOL.trade_common_components, domain=None, range=Optional[Union[Union[str, "TradeCommonComponentName"], list[Union[str, "TradeCommonComponentName"]]]])

slots.trade_footnotes = Slot(uri=FIX_TRADE.trade_footnotes, name="trade_footnotes", curie=FIX_TRADE.curie('trade_footnotes'),
                   model_uri=FIX_PROTOCOL.trade_footnotes, domain=None, range=Optional[Union[dict[Union[int, TradeComponentTableFootnoteTradeFootnoteNumber], Union[dict, TradeComponentTableFootnote]], list[Union[dict, TradeComponentTableFootnote]]]])

slots.trade_category_sections = Slot(uri=FIX_TRADE.trade_category_sections, name="trade_category_sections", curie=FIX_TRADE.curie('trade_category_sections'),
                   model_uri=FIX_PROTOCOL.trade_category_sections, domain=None, range=Optional[Union[dict[Union[str, TradeCategorySectionCategory], Union[dict, TradeCategorySection]], list[Union[dict, TradeCategorySection]]]])

slots.trade_category_specific_components = Slot(uri=FIX_TRADE.trade_category_specific_components, name="trade_category_specific_components", curie=FIX_TRADE.curie('trade_category_specific_components'),
                   model_uri=FIX_PROTOCOL.trade_category_specific_components, domain=None, range=Optional[Union[dict[Union[str, TradeComponentDetailComponentName], Union[dict, TradeComponentDetail]], list[Union[dict, TradeComponentDetail]]]])

slots.trade_repetition = Slot(uri=FIX_TRADE.trade_repetition, name="trade_repetition", curie=FIX_TRADE.curie('trade_repetition'),
                   model_uri=FIX_PROTOCOL.trade_repetition, domain=None, range=Optional[Union[str, "TradeComponentRepetition"]])

slots.trade_is_common = Slot(uri=FIX_TRADE.trade_is_common, name="trade_is_common", curie=FIX_TRADE.curie('trade_is_common'),
                   model_uri=FIX_PROTOCOL.trade_is_common, domain=None, range=Optional[Union[bool, Bool]])

slots.trade_footnote_number = Slot(uri=FIX_TRADE.trade_footnote_number, name="trade_footnote_number", curie=FIX_TRADE.curie('trade_footnote_number'),
                   model_uri=FIX_PROTOCOL.trade_footnote_number, domain=None, range=Optional[int])

slots.trade_introduced_in = Slot(uri=FIX_TRADE.trade_introduced_in, name="trade_introduced_in", curie=FIX_TRADE.curie('trade_introduced_in'),
                   model_uri=FIX_PROTOCOL.trade_introduced_in, domain=None, range=Optional[str])

slots.trade_sole_category = Slot(uri=FIX_TRADE.trade_sole_category, name="trade_sole_category", curie=FIX_TRADE.curie('trade_sole_category'),
                   model_uri=FIX_PROTOCOL.trade_sole_category, domain=None, range=Optional[Union[str, "TradeCategoryEnum"]])

slots.trade_footnote_text = Slot(uri=FIX_TRADE.trade_footnote_text, name="trade_footnote_text", curie=FIX_TRADE.curie('trade_footnote_text'),
                   model_uri=FIX_PROTOCOL.trade_footnote_text, domain=None, range=Optional[str])

slots.trade_layout_url = Slot(uri=SCHEMA.url, name="trade_layout_url", curie=SCHEMA.curie('url'),
                   model_uri=FIX_PROTOCOL.trade_layout_url, domain=None, range=Optional[Union[str, URI]])

slots.trade_diagram_conventions = Slot(uri=FIX_TRADE.trade_diagram_conventions, name="trade_diagram_conventions", curie=FIX_TRADE.curie('trade_diagram_conventions'),
                   model_uri=FIX_PROTOCOL.trade_diagram_conventions, domain=None, range=Optional[str])

slots.trade_messages_overview_note = Slot(uri=FIX_TRADE.trade_messages_overview_note, name="trade_messages_overview_note", curie=FIX_TRADE.curie('trade_messages_overview_note'),
                   model_uri=FIX_PROTOCOL.trade_messages_overview_note, domain=None, range=Optional[str])

slots.trade_components_overview_note = Slot(uri=FIX_TRADE.trade_components_overview_note, name="trade_components_overview_note", curie=FIX_TRADE.curie('trade_components_overview_note'),
                   model_uri=FIX_PROTOCOL.trade_components_overview_note, domain=None, range=Optional[str])

slots.trade_category_components_note = Slot(uri=FIX_TRADE.trade_category_components_note, name="trade_category_components_note", curie=FIX_TRADE.curie('trade_category_components_note'),
                   model_uri=FIX_PROTOCOL.trade_category_components_note, domain=None, range=Optional[str])

slots.trade_group_title = Slot(uri=SCHEMA.name, name="trade_group_title", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.trade_group_title, domain=None, range=Optional[str])

slots.trade_message_groups = Slot(uri=FIX_TRADE.trade_message_groups, name="trade_message_groups", curie=FIX_TRADE.curie('trade_message_groups'),
                   model_uri=FIX_PROTOCOL.trade_message_groups, domain=None, range=Optional[Union[dict[Union[str, TradeMessageGroupTradeGroupTitle], Union[dict, TradeMessageGroup]], list[Union[dict, TradeMessageGroup]]]])

slots.trade_common_component_details = Slot(uri=FIX_TRADE.trade_common_component_details, name="trade_common_component_details", curie=FIX_TRADE.curie('trade_common_component_details'),
                   model_uri=FIX_PROTOCOL.trade_common_component_details, domain=None, range=Optional[Union[dict[Union[str, TradeCommonComponentDetailComponentName], Union[dict, TradeCommonComponentDetail]], list[Union[dict, TradeCommonComponentDetail]]]])

slots.trade_message_diagram_template_url = Slot(uri=SCHEMA.url, name="trade_message_diagram_template_url", curie=SCHEMA.curie('url'),
                   model_uri=FIX_PROTOCOL.trade_message_diagram_template_url, domain=None, range=Optional[Union[str, URI]])

slots.trade_category_background = Slot(uri=FIX_TRADE.trade_category_background, name="trade_category_background", curie=FIX_TRADE.curie('trade_category_background'),
                   model_uri=FIX_PROTOCOL.trade_category_background, domain=None, range=Optional[str])

slots.trade_layout_rows = Slot(uri=FIX_TRADE.trade_layout_rows, name="trade_layout_rows", curie=FIX_TRADE.curie('trade_layout_rows'),
                   model_uri=FIX_PROTOCOL.trade_layout_rows, domain=None, range=Optional[Union[Union[dict, TradeLayoutRow], list[Union[dict, TradeLayoutRow]]]])

slots.trade_layout_kind = Slot(uri=FIX_TRADE.trade_layout_kind, name="trade_layout_kind", curie=FIX_TRADE.curie('trade_layout_kind'),
                   model_uri=FIX_PROTOCOL.trade_layout_kind, domain=None, range=Optional[Union[str, "TradeLayoutRowKindEnum"]])

slots.trade_layout_field_tag = Slot(uri=FIX_TRADE.trade_layout_field_tag, name="trade_layout_field_tag", curie=FIX_TRADE.curie('trade_layout_field_tag'),
                   model_uri=FIX_PROTOCOL.trade_layout_field_tag, domain=None, range=Optional[int])

slots.trade_layout_element_name = Slot(uri=FIX_TRADE.trade_layout_element_name, name="trade_layout_element_name", curie=FIX_TRADE.curie('trade_layout_element_name'),
                   model_uri=FIX_PROTOCOL.trade_layout_element_name, domain=None, range=Optional[str])

slots.trade_layout_required = Slot(uri=FIX_TRADE.trade_layout_required, name="trade_layout_required", curie=FIX_TRADE.curie('trade_layout_required'),
                   model_uri=FIX_PROTOCOL.trade_layout_required, domain=None, range=Optional[Union[bool, Bool]])

slots.trade_layout_description = Slot(uri=FIX_TRADE.trade_layout_description, name="trade_layout_description", curie=FIX_TRADE.curie('trade_layout_description'),
                   model_uri=FIX_PROTOCOL.trade_layout_description, domain=None, range=Optional[str])

slots.trade_layout_nested = Slot(uri=FIX_TRADE.trade_layout_nested, name="trade_layout_nested", curie=FIX_TRADE.curie('trade_layout_nested'),
                   model_uri=FIX_PROTOCOL.trade_layout_nested, domain=None, range=Optional[Union[bool, Bool]])

slots.trade_ord_status_precedence_entries = Slot(uri=FIX_TRADE.trade_ord_status_precedence_entries, name="trade_ord_status_precedence_entries", curie=FIX_TRADE.curie('trade_ord_status_precedence_entries'),
                   model_uri=FIX_PROTOCOL.trade_ord_status_precedence_entries, domain=None, range=Optional[Union[dict[Union[str, TradeOrdStatusPrecedenceEntryTradeOrdStatusLabel], Union[dict, TradeOrdStatusPrecedenceEntry]], list[Union[dict, TradeOrdStatusPrecedenceEntry]]]])

slots.trade_ord_status_precedence = Slot(uri=FIX_TRADE.trade_ord_status_precedence, name="trade_ord_status_precedence", curie=FIX_TRADE.curie('trade_ord_status_precedence'),
                   model_uri=FIX_PROTOCOL.trade_ord_status_precedence, domain=None, range=Optional[int])

slots.trade_ord_status_label = Slot(uri=FIX_TRADE.trade_ord_status_label, name="trade_ord_status_label", curie=FIX_TRADE.curie('trade_ord_status_label'),
                   model_uri=FIX_PROTOCOL.trade_ord_status_label, domain=None, range=Optional[str])

slots.trade_fragmentation_entries = Slot(uri=FIX_TRADE.trade_fragmentation_entries, name="trade_fragmentation_entries", curie=FIX_TRADE.curie('trade_fragmentation_entries'),
                   model_uri=FIX_PROTOCOL.trade_fragmentation_entries, domain=None, range=Optional[Union[dict[Union[str, TradeFragmentationEntryTradeFragmentationMessage], Union[dict, TradeFragmentationEntry]], list[Union[dict, TradeFragmentationEntry]]]])

slots.trade_fragmentation_message = Slot(uri=FIX_TRADE.trade_fragmentation_message, name="trade_fragmentation_message", curie=FIX_TRADE.curie('trade_fragmentation_message'),
                   model_uri=FIX_PROTOCOL.trade_fragmentation_message, domain=None, range=Optional[str])

slots.trade_fragmentation_total_entries_field = Slot(uri=FIX_TRADE.trade_fragmentation_total_entries_field, name="trade_fragmentation_total_entries_field", curie=FIX_TRADE.curie('trade_fragmentation_total_entries_field'),
                   model_uri=FIX_PROTOCOL.trade_fragmentation_total_entries_field, domain=None, range=Optional[str])

slots.trade_fragmentation_repeating_group = Slot(uri=FIX_TRADE.trade_fragmentation_repeating_group, name="trade_fragmentation_repeating_group", curie=FIX_TRADE.curie('trade_fragmentation_repeating_group'),
                   model_uri=FIX_PROTOCOL.trade_fragmentation_repeating_group, domain=None, range=Optional[str])

slots.trade_appendix_sections = Slot(uri=FIX_TRADE.trade_appendix_sections, name="trade_appendix_sections", curie=FIX_TRADE.curie('trade_appendix_sections'),
                   model_uri=FIX_PROTOCOL.trade_appendix_sections, domain=None, range=Optional[Union[dict[Union[str, TradeAppendixSectionTradeAppendixCategory], Union[dict, TradeAppendixSection]], list[Union[dict, TradeAppendixSection]]]])

slots.trade_appendix_category = Slot(uri=FIX_TRADE.trade_appendix_category, name="trade_appendix_category", curie=FIX_TRADE.curie('trade_appendix_category'),
                   model_uri=FIX_PROTOCOL.trade_appendix_category, domain=None, range=Optional[str])

slots.post_introduction = Slot(uri=FIX_POST_TRADE.post_introduction, name="post_introduction", curie=FIX_POST_TRADE.curie('post_introduction'),
                   model_uri=FIX_PROTOCOL.post_introduction, domain=None, range=Optional[str])

slots.post_common_components = Slot(uri=FIX_POST_TRADE.post_common_components, name="post_common_components", curie=FIX_POST_TRADE.curie('post_common_components'),
                   model_uri=FIX_PROTOCOL.post_common_components, domain=None, range=Optional[Union[Union[str, "PostTradeCommonComponentName"], list[Union[str, "PostTradeCommonComponentName"]]]])

slots.post_footnotes = Slot(uri=FIX_POST_TRADE.post_footnotes, name="post_footnotes", curie=FIX_POST_TRADE.curie('post_footnotes'),
                   model_uri=FIX_PROTOCOL.post_footnotes, domain=None, range=Optional[Union[dict[Union[int, PostTradeComponentTableFootnoteFootnoteNumber], Union[dict, PostTradeComponentTableFootnote]], list[Union[dict, PostTradeComponentTableFootnote]]]])

slots.post_category_sections = Slot(uri=FIX_POST_TRADE.post_category_sections, name="post_category_sections", curie=FIX_POST_TRADE.curie('post_category_sections'),
                   model_uri=FIX_PROTOCOL.post_category_sections, domain=None, range=Optional[Union[dict[Union[str, PostTradeCategorySectionCategory], Union[dict, PostTradeCategorySection]], list[Union[dict, PostTradeCategorySection]]]])

slots.post_category_specific_components = Slot(uri=FIX_POST_TRADE.post_category_specific_components, name="post_category_specific_components", curie=FIX_POST_TRADE.curie('post_category_specific_components'),
                   model_uri=FIX_PROTOCOL.post_category_specific_components, domain=None, range=Optional[Union[dict[Union[str, PostTradeComponentDetailComponentName], Union[dict, PostTradeComponentDetail]], list[Union[dict, PostTradeComponentDetail]]]])

slots.post_sole_category = Slot(uri=FIX_POST_TRADE.post_sole_category, name="post_sole_category", curie=FIX_POST_TRADE.curie('post_sole_category'),
                   model_uri=FIX_PROTOCOL.post_sole_category, domain=None, range=Optional[Union[str, "PostTradeCategoryEnum"]])

slots.post_message_groups = Slot(uri=FIX_POST_TRADE.post_message_groups, name="post_message_groups", curie=FIX_POST_TRADE.curie('post_message_groups'),
                   model_uri=FIX_PROTOCOL.post_message_groups, domain=None, range=Optional[Union[dict[Union[str, PostTradeMessageGroupGroupTitle], Union[dict, PostTradeMessageGroup]], list[Union[dict, PostTradeMessageGroup]]]])

slots.post_common_component_details = Slot(uri=FIX_POST_TRADE.post_common_component_details, name="post_common_component_details", curie=FIX_POST_TRADE.curie('post_common_component_details'),
                   model_uri=FIX_PROTOCOL.post_common_component_details, domain=None, range=Optional[Union[dict[Union[str, PostTradeCommonComponentDetailComponentName], Union[dict, PostTradeCommonComponentDetail]], list[Union[dict, PostTradeCommonComponentDetail]]]])

slots.allocation_scenarios = Slot(uri=FIX_POST_TRADE.allocation_scenarios, name="allocation_scenarios", curie=FIX_POST_TRADE.curie('allocation_scenarios'),
                   model_uri=FIX_PROTOCOL.allocation_scenarios, domain=None, range=Optional[Union[Union[str, "AllocationScenarioEnum"], list[Union[str, "AllocationScenarioEnum"]]]])

slots.post_trade_allocation_pricing_methods = Slot(uri=FIX_POST_TRADE.post_trade_allocation_pricing_methods, name="post_trade_allocation_pricing_methods", curie=FIX_POST_TRADE.curie('post_trade_allocation_pricing_methods'),
                   model_uri=FIX_PROTOCOL.post_trade_allocation_pricing_methods, domain=None, range=Optional[Union[Union[str, "PostTradeAllocationPricingMethodEnum"], list[Union[str, "PostTradeAllocationPricingMethodEnum"]]]])

slots.allocation_status_descriptions = Slot(uri=FIX_POST_TRADE.allocation_status_descriptions, name="allocation_status_descriptions", curie=FIX_POST_TRADE.curie('allocation_status_descriptions'),
                   model_uri=FIX_PROTOCOL.allocation_status_descriptions, domain=None, range=Optional[Union[dict[Union[str, AllocationStatusDescriptionStatusCode], Union[dict, AllocationStatusDescription]], list[Union[dict, AllocationStatusDescription]]]])

slots.fragmentation_field_map = Slot(uri=FIX_POST_TRADE.fragmentation_field_map, name="fragmentation_field_map", curie=FIX_POST_TRADE.curie('fragmentation_field_map'),
                   model_uri=FIX_PROTOCOL.fragmentation_field_map, domain=None, range=Optional[Union[dict[Union[str, AllocationFragmentationFieldMapMsgType], Union[dict, AllocationFragmentationFieldMap]], list[Union[dict, AllocationFragmentationFieldMap]]]])

slots.trade_capture_report_usages = Slot(uri=FIX_POST_TRADE.trade_capture_report_usages, name="trade_capture_report_usages", curie=FIX_POST_TRADE.curie('trade_capture_report_usages'),
                   model_uri=FIX_PROTOCOL.trade_capture_report_usages, domain=None, range=Optional[Union[dict[Union[str, TradeCaptureReportUsageStatusLabel], Union[dict, TradeCaptureReportUsage]], list[Union[dict, TradeCaptureReportUsage]]]])

slots.trade_capture_report_identifier_rules = Slot(uri=FIX_POST_TRADE.trade_capture_report_identifier_rules, name="trade_capture_report_identifier_rules", curie=FIX_POST_TRADE.curie('trade_capture_report_identifier_rules'),
                   model_uri=FIX_PROTOCOL.trade_capture_report_identifier_rules, domain=None, range=Optional[Union[dict[Union[str, TradeCaptureReportIdentifierRuleIdentifierRole], Union[dict, TradeCaptureReportIdentifierRule]], list[Union[dict, TradeCaptureReportIdentifierRule]]]])

slots.registration_status_descriptions = Slot(uri=FIX_POST_TRADE.registration_status_descriptions, name="registration_status_descriptions", curie=FIX_POST_TRADE.curie('registration_status_descriptions'),
                   model_uri=FIX_PROTOCOL.registration_status_descriptions, domain=None, range=Optional[Union[dict[Union[str, RegistrationStatusDescriptionStatusCode], Union[dict, RegistrationStatusDescription]], list[Union[dict, RegistrationStatusDescription]]]])

slots.clearing_services_for_position_management = Slot(uri=FIX_POST_TRADE.clearing_services_for_position_management, name="clearing_services_for_position_management", curie=FIX_POST_TRADE.curie('clearing_services_for_position_management'),
                   model_uri=FIX_PROTOCOL.clearing_services_for_position_management, domain=None, range=Optional[Union[Union[str, "ClearingServiceForPositionManagementEnum"], list[Union[str, "ClearingServiceForPositionManagementEnum"]]]])

slots.clearing_services_for_post_trade_processing = Slot(uri=FIX_POST_TRADE.clearing_services_for_post_trade_processing, name="clearing_services_for_post_trade_processing", curie=FIX_POST_TRADE.curie('clearing_services_for_post_trade_processing'),
                   model_uri=FIX_PROTOCOL.clearing_services_for_post_trade_processing, domain=None, range=Optional[Union[dict[Union[str, ClearingServicePostTradeProcessingFormatMessageFormat], Union[dict, ClearingServicePostTradeProcessingFormat]], list[Union[dict, ClearingServicePostTradeProcessingFormat]]]])

slots.allocation_roles = Slot(uri=FIX_POST_TRADE.allocation_roles, name="allocation_roles", curie=FIX_POST_TRADE.curie('allocation_roles'),
                   model_uri=FIX_PROTOCOL.allocation_roles, domain=None, range=Optional[Union[Union[str, "AllocationRoleEnum"], list[Union[str, "AllocationRoleEnum"]]]])

slots.collateral_management_usages = Slot(uri=FIX_POST_TRADE.collateral_management_usages, name="collateral_management_usages", curie=FIX_POST_TRADE.curie('collateral_management_usages'),
                   model_uri=FIX_PROTOCOL.collateral_management_usages, domain=None, range=Optional[Union[Union[str, "CollateralManagementUsageEnum"], list[Union[str, "CollateralManagementUsageEnum"]]]])

slots.collateral_assignment_purposes = Slot(uri=FIX_POST_TRADE.collateral_assignment_purposes, name="collateral_assignment_purposes", curie=FIX_POST_TRADE.curie('collateral_assignment_purposes'),
                   model_uri=FIX_PROTOCOL.collateral_assignment_purposes, domain=None, range=Optional[Union[Union[str, "CollateralAssignmentPurposeEnum"], list[Union[str, "CollateralAssignmentPurposeEnum"]]]])

slots.identifier_role = Slot(uri=FIX_POST_TRADE.identifier_role, name="identifier_role", curie=FIX_POST_TRADE.curie('identifier_role'),
                   model_uri=FIX_PROTOCOL.identifier_role, domain=None, range=Optional[Union[str, "TradeCaptureReportIdentifierRoleEnum"]])

slots.status_code = Slot(uri=FIX_POST_TRADE.status_code, name="status_code", curie=FIX_POST_TRADE.curie('status_code'),
                   model_uri=FIX_PROTOCOL.status_code, domain=None, range=Optional[str])

slots.status_label = Slot(uri=FIX_POST_TRADE.status_label, name="status_label", curie=FIX_POST_TRADE.curie('status_label'),
                   model_uri=FIX_PROTOCOL.status_label, domain=None, range=Optional[str])

slots.message_format = Slot(uri=FIX_POST_TRADE.message_format, name="message_format", curie=FIX_POST_TRADE.curie('message_format'),
                   model_uri=FIX_PROTOCOL.message_format, domain=None, range=Optional[Union[str, "ClearingServiceForPostTradeProcessingEnum"]])

slots.supported_actions = Slot(uri=FIX_POST_TRADE.supported_actions, name="supported_actions", curie=FIX_POST_TRADE.curie('supported_actions'),
                   model_uri=FIX_PROTOCOL.supported_actions, domain=None, range=Optional[Union[str, list[str]]])

slots.principal_message_reference = Slot(uri=FIX_POST_TRADE.principal_message_reference, name="principal_message_reference", curie=FIX_POST_TRADE.curie('principal_message_reference'),
                   model_uri=FIX_PROTOCOL.principal_message_reference, domain=None, range=Optional[str])

slots.total_count_field = Slot(uri=FIX_POST_TRADE.total_count_field, name="total_count_field", curie=FIX_POST_TRADE.curie('total_count_field'),
                   model_uri=FIX_PROTOCOL.total_count_field, domain=None, range=Optional[str])

slots.fragment_count_field = Slot(uri=FIX_POST_TRADE.fragment_count_field, name="fragment_count_field", curie=FIX_POST_TRADE.curie('fragment_count_field'),
                   model_uri=FIX_PROTOCOL.fragment_count_field, domain=None, range=Optional[str])

slots.post_layout_rows = Slot(uri=FIX_POST_TRADE.post_layout_rows, name="post_layout_rows", curie=FIX_POST_TRADE.curie('post_layout_rows'),
                   model_uri=FIX_PROTOCOL.post_layout_rows, domain=None, range=Optional[Union[Union[dict, PostTradeLayoutRow], list[Union[dict, PostTradeLayoutRow]]]])

slots.post_layout_kind = Slot(uri=FIX_POST_TRADE.post_layout_kind, name="post_layout_kind", curie=FIX_POST_TRADE.curie('post_layout_kind'),
                   model_uri=FIX_PROTOCOL.post_layout_kind, domain=None, range=Optional[Union[str, "PostTradeLayoutRowKindEnum"]])

slots.post_layout_field_tag = Slot(uri=FIX_POST_TRADE.post_layout_field_tag, name="post_layout_field_tag", curie=FIX_POST_TRADE.curie('post_layout_field_tag'),
                   model_uri=FIX_PROTOCOL.post_layout_field_tag, domain=None, range=Optional[int])

slots.post_layout_element_name = Slot(uri=FIX_POST_TRADE.post_layout_element_name, name="post_layout_element_name", curie=FIX_POST_TRADE.curie('post_layout_element_name'),
                   model_uri=FIX_PROTOCOL.post_layout_element_name, domain=None, range=Optional[str])

slots.post_layout_required = Slot(uri=FIX_POST_TRADE.post_layout_required, name="post_layout_required", curie=FIX_POST_TRADE.curie('post_layout_required'),
                   model_uri=FIX_PROTOCOL.post_layout_required, domain=None, range=Optional[Union[bool, Bool]])

slots.post_layout_description = Slot(uri=FIX_POST_TRADE.post_layout_description, name="post_layout_description", curie=FIX_POST_TRADE.curie('post_layout_description'),
                   model_uri=FIX_PROTOCOL.post_layout_description, domain=None, range=Optional[str])

slots.post_layout_nested = Slot(uri=FIX_POST_TRADE.post_layout_nested, name="post_layout_nested", curie=FIX_POST_TRADE.curie('post_layout_nested'),
                   model_uri=FIX_PROTOCOL.post_layout_nested, domain=None, range=Optional[Union[bool, Bool]])

slots.infra_introduction = Slot(uri=FIX_INFRASTRUCTURE.infra_introduction, name="infra_introduction", curie=FIX_INFRASTRUCTURE.curie('infra_introduction'),
                   model_uri=FIX_PROTOCOL.infra_introduction, domain=None, range=Optional[str])

slots.infra_common_components = Slot(uri=FIX_INFRASTRUCTURE.infra_common_components, name="infra_common_components", curie=FIX_INFRASTRUCTURE.curie('infra_common_components'),
                   model_uri=FIX_PROTOCOL.infra_common_components, domain=None, range=Optional[Union[Union[str, "InfrastructureComponentName"], list[Union[str, "InfrastructureComponentName"]]]])

slots.infra_footnotes = Slot(uri=FIX_INFRASTRUCTURE.infra_footnotes, name="infra_footnotes", curie=FIX_INFRASTRUCTURE.curie('infra_footnotes'),
                   model_uri=FIX_PROTOCOL.infra_footnotes, domain=None, range=Optional[Union[dict[Union[int, InfrastructureComponentTableFootnoteFootnoteNumber], Union[dict, InfrastructureComponentTableFootnote]], list[Union[dict, InfrastructureComponentTableFootnote]]]])

slots.infra_category_sections = Slot(uri=FIX_INFRASTRUCTURE.infra_category_sections, name="infra_category_sections", curie=FIX_INFRASTRUCTURE.curie('infra_category_sections'),
                   model_uri=FIX_PROTOCOL.infra_category_sections, domain=None, range=Optional[Union[Union[dict, InfrastructureCategorySection], list[Union[dict, InfrastructureCategorySection]]]])

slots.infra_category_specific_components = Slot(uri=FIX_INFRASTRUCTURE.infra_category_specific_components, name="infra_category_specific_components", curie=FIX_INFRASTRUCTURE.curie('infra_category_specific_components'),
                   model_uri=FIX_PROTOCOL.infra_category_specific_components, domain=None, range=Optional[Union[Union[dict, InfrastructureComponentDetail], list[Union[dict, InfrastructureComponentDetail]]]])

slots.infra_sole_category = Slot(uri=FIX_INFRASTRUCTURE.infra_sole_category, name="infra_sole_category", curie=FIX_INFRASTRUCTURE.curie('infra_sole_category'),
                   model_uri=FIX_PROTOCOL.infra_sole_category, domain=None, range=Optional[Union[str, "InfrastructureCategoryEnum"]])

slots.standard_responses_pre_trade = Slot(uri=FIX_INFRASTRUCTURE.standard_responses_pre_trade, name="standard_responses_pre_trade", curie=FIX_INFRASTRUCTURE.curie('standard_responses_pre_trade'),
                   model_uri=FIX_PROTOCOL.standard_responses_pre_trade, domain=None, range=Optional[Union[Union[dict, StandardResponseMapping], list[Union[dict, StandardResponseMapping]]]])

slots.standard_responses_trade = Slot(uri=FIX_INFRASTRUCTURE.standard_responses_trade, name="standard_responses_trade", curie=FIX_INFRASTRUCTURE.curie('standard_responses_trade'),
                   model_uri=FIX_PROTOCOL.standard_responses_trade, domain=None, range=Optional[Union[Union[dict, StandardResponseMapping], list[Union[dict, StandardResponseMapping]]]])

slots.standard_responses_post_trade = Slot(uri=FIX_INFRASTRUCTURE.standard_responses_post_trade, name="standard_responses_post_trade", curie=FIX_INFRASTRUCTURE.curie('standard_responses_post_trade'),
                   model_uri=FIX_PROTOCOL.standard_responses_post_trade, domain=None, range=Optional[Union[Union[dict, StandardResponseMapping], list[Union[dict, StandardResponseMapping]]]])

slots.key_fields_pre_trade = Slot(uri=FIX_INFRASTRUCTURE.key_fields_pre_trade, name="key_fields_pre_trade", curie=FIX_INFRASTRUCTURE.curie('key_fields_pre_trade'),
                   model_uri=FIX_PROTOCOL.key_fields_pre_trade, domain=None, range=Optional[Union[Union[dict, ApplicationMessageReferenceKey], list[Union[dict, ApplicationMessageReferenceKey]]]])

slots.key_fields_trade = Slot(uri=FIX_INFRASTRUCTURE.key_fields_trade, name="key_fields_trade", curie=FIX_INFRASTRUCTURE.curie('key_fields_trade'),
                   model_uri=FIX_PROTOCOL.key_fields_trade, domain=None, range=Optional[Union[Union[dict, ApplicationMessageReferenceKey], list[Union[dict, ApplicationMessageReferenceKey]]]])

slots.key_fields_post_trade = Slot(uri=FIX_INFRASTRUCTURE.key_fields_post_trade, name="key_fields_post_trade", curie=FIX_INFRASTRUCTURE.curie('key_fields_post_trade'),
                   model_uri=FIX_PROTOCOL.key_fields_post_trade, domain=None, range=Optional[Union[Union[dict, ApplicationMessageReferenceKey], list[Union[dict, ApplicationMessageReferenceKey]]]])

slots.business_reject_reason_descriptions = Slot(uri=FIX_INFRASTRUCTURE.business_reject_reason_descriptions, name="business_reject_reason_descriptions", curie=FIX_INFRASTRUCTURE.curie('business_reject_reason_descriptions'),
                   model_uri=FIX_PROTOCOL.business_reject_reason_descriptions, domain=None, range=Optional[Union[dict[Union[int, BusinessRejectReasonDescriptionRejectReasonCode], Union[dict, BusinessRejectReasonDescription]], list[Union[dict, BusinessRejectReasonDescription]]]])

slots.network_status_scenarios = Slot(uri=FIX_INFRASTRUCTURE.network_status_scenarios, name="network_status_scenarios", curie=FIX_INFRASTRUCTURE.curie('network_status_scenarios'),
                   model_uri=FIX_PROTOCOL.network_status_scenarios, domain=None, range=Optional[Union[Union[str, "NetworkStatusScenarioEnum"], list[Union[str, "NetworkStatusScenarioEnum"]]]])

slots.network_request_types_referenced = Slot(uri=FIX_INFRASTRUCTURE.network_request_types_referenced, name="network_request_types_referenced", curie=FIX_INFRASTRUCTURE.curie('network_request_types_referenced'),
                   model_uri=FIX_PROTOCOL.network_request_types_referenced, domain=None, range=Optional[Union[Union[str, "NetworkRequestTypeEnum"], list[Union[str, "NetworkRequestTypeEnum"]]]])

slots.application_message_report_uses = Slot(uri=FIX_INFRASTRUCTURE.application_message_report_uses, name="application_message_report_uses", curie=FIX_INFRASTRUCTURE.curie('application_message_report_uses'),
                   model_uri=FIX_PROTOCOL.application_message_report_uses, domain=None, range=Optional[Union[Union[str, "ApplicationMessageReportTypeEnum"], list[Union[str, "ApplicationMessageReportTypeEnum"]]]])

slots.category_label = Slot(uri=FIX_INFRASTRUCTURE.category_label, name="category_label", curie=FIX_INFRASTRUCTURE.curie('category_label'),
                   model_uri=FIX_PROTOCOL.category_label, domain=None, range=Optional[str])

slots.fix_message = Slot(uri=FIX_INFRASTRUCTURE.fix_message, name="fix_message", curie=FIX_INFRASTRUCTURE.curie('fix_message'),
                   model_uri=FIX_PROTOCOL.fix_message, domain=None, range=Optional[str])

slots.appropriate_responses = Slot(uri=FIX_INFRASTRUCTURE.appropriate_responses, name="appropriate_responses", curie=FIX_INFRASTRUCTURE.curie('appropriate_responses'),
                   model_uri=FIX_PROTOCOL.appropriate_responses, domain=None, range=Optional[str])

slots.business_reject_ref_id_value = Slot(uri=FIX_INFRASTRUCTURE.business_reject_ref_id_value, name="business_reject_ref_id_value", curie=FIX_INFRASTRUCTURE.curie('business_reject_ref_id_value'),
                   model_uri=FIX_PROTOCOL.business_reject_ref_id_value, domain=None, range=Optional[str])

slots.reject_reason_code = Slot(uri=FIX_INFRASTRUCTURE.reject_reason_code, name="reject_reason_code", curie=FIX_INFRASTRUCTURE.curie('reject_reason_code'),
                   model_uri=FIX_PROTOCOL.reject_reason_code, domain=None, range=Optional[int])

slots.reject_reason_label = Slot(uri=FIX_INFRASTRUCTURE.reject_reason_label, name="reject_reason_label", curie=FIX_INFRASTRUCTURE.curie('reject_reason_label'),
                   model_uri=FIX_PROTOCOL.reject_reason_label, domain=None, range=Optional[str])

slots.infra_global_components = Slot(uri=FIX_INFRASTRUCTURE.infra_global_components, name="infra_global_components", curie=FIX_INFRASTRUCTURE.curie('infra_global_components'),
                   model_uri=FIX_PROTOCOL.infra_global_components, domain=None, range=Optional[Union[dict[Union[str, InfrastructureGlobalComponentReferenceInfraGlobalComponentName], Union[dict, InfrastructureGlobalComponentReference]], list[Union[dict, InfrastructureGlobalComponentReference]]]])

slots.infra_global_component_name = Slot(uri=FIX_INFRASTRUCTURE.infra_global_component_name, name="infra_global_component_name", curie=FIX_INFRASTRUCTURE.curie('infra_global_component_name'),
                   model_uri=FIX_PROTOCOL.infra_global_component_name, domain=None, range=Optional[Union[str, "InfrastructureGlobalComponentName"]])

slots.infra_global_component_field_tags = Slot(uri=FIX_INFRASTRUCTURE.infra_global_component_field_tags, name="infra_global_component_field_tags", curie=FIX_INFRASTRUCTURE.curie('infra_global_component_field_tags'),
                   model_uri=FIX_PROTOCOL.infra_global_component_field_tags, domain=None, range=Optional[Union[int, list[int]]])

slots.infra_global_component_field_names = Slot(uri=FIX_INFRASTRUCTURE.infra_global_component_field_names, name="infra_global_component_field_names", curie=FIX_INFRASTRUCTURE.curie('infra_global_component_field_names'),
                   model_uri=FIX_PROTOCOL.infra_global_component_field_names, domain=None, range=Optional[Union[str, list[str]]])

slots.infra_global_component_used_in = Slot(uri=FIX_INFRASTRUCTURE.infra_global_component_used_in, name="infra_global_component_used_in", curie=FIX_INFRASTRUCTURE.curie('infra_global_component_used_in'),
                   model_uri=FIX_PROTOCOL.infra_global_component_used_in, domain=None, range=Optional[Union[Union[str, "InfrastructureCategoryEnum"], list[Union[str, "InfrastructureCategoryEnum"]]]])

slots.infra_global_component_msg_types = Slot(uri=FIX_INFRASTRUCTURE.infra_global_component_msg_types, name="infra_global_component_msg_types", curie=FIX_INFRASTRUCTURE.curie('infra_global_component_msg_types'),
                   model_uri=FIX_PROTOCOL.infra_global_component_msg_types, domain=None, range=Optional[Union[str, list[str]]])

slots.infra_global_component_repetition = Slot(uri=FIX_INFRASTRUCTURE.infra_global_component_repetition, name="infra_global_component_repetition", curie=FIX_INFRASTRUCTURE.curie('infra_global_component_repetition'),
                   model_uri=FIX_PROTOCOL.infra_global_component_repetition, domain=None, range=Optional[str])

slots.infra_layout_rows = Slot(uri=FIX_INFRASTRUCTURE.infra_layout_rows, name="infra_layout_rows", curie=FIX_INFRASTRUCTURE.curie('infra_layout_rows'),
                   model_uri=FIX_PROTOCOL.infra_layout_rows, domain=None, range=Optional[Union[Union[dict, InfrastructureLayoutRow], list[Union[dict, InfrastructureLayoutRow]]]])

slots.infra_layout_kind = Slot(uri=FIX_INFRASTRUCTURE.infra_layout_kind, name="infra_layout_kind", curie=FIX_INFRASTRUCTURE.curie('infra_layout_kind'),
                   model_uri=FIX_PROTOCOL.infra_layout_kind, domain=None, range=Optional[Union[str, "InfrastructureLayoutRowKindEnum"]])

slots.infra_layout_field_tag = Slot(uri=FIX_INFRASTRUCTURE.infra_layout_field_tag, name="infra_layout_field_tag", curie=FIX_INFRASTRUCTURE.curie('infra_layout_field_tag'),
                   model_uri=FIX_PROTOCOL.infra_layout_field_tag, domain=None, range=Optional[int])

slots.infra_layout_element_name = Slot(uri=FIX_INFRASTRUCTURE.infra_layout_element_name, name="infra_layout_element_name", curie=FIX_INFRASTRUCTURE.curie('infra_layout_element_name'),
                   model_uri=FIX_PROTOCOL.infra_layout_element_name, domain=None, range=Optional[str])

slots.infra_layout_required = Slot(uri=FIX_INFRASTRUCTURE.infra_layout_required, name="infra_layout_required", curie=FIX_INFRASTRUCTURE.curie('infra_layout_required'),
                   model_uri=FIX_PROTOCOL.infra_layout_required, domain=None, range=Optional[Union[bool, Bool]])

slots.infra_layout_description = Slot(uri=FIX_INFRASTRUCTURE.infra_layout_description, name="infra_layout_description", curie=FIX_INFRASTRUCTURE.curie('infra_layout_description'),
                   model_uri=FIX_PROTOCOL.infra_layout_description, domain=None, range=Optional[str])

slots.infra_layout_nested = Slot(uri=FIX_INFRASTRUCTURE.infra_layout_nested, name="infra_layout_nested", curie=FIX_INFRASTRUCTURE.curie('infra_layout_nested'),
                   model_uri=FIX_PROTOCOL.infra_layout_nested, domain=None, range=Optional[Union[bool, Bool]])

slots.referenced_global_components = Slot(uri=FIX_GLOBAL_COMPONENTS.referenced_global_components, name="referenced_global_components", curie=FIX_GLOBAL_COMPONENTS.curie('referenced_global_components'),
                   model_uri=FIX_PROTOCOL.referenced_global_components, domain=None, range=Optional[Union[Union[str, GlobalComponentComponentName], list[Union[str, GlobalComponentComponentName]]]])

slots.FIXProtocolLimited_brand_name = Slot(uri=FIX_BASE.brand_name, name="FIXProtocolLimited_brand_name", curie=FIX_BASE.curie('brand_name'),
                   model_uri=FIX_PROTOCOL.FIXProtocolLimited_brand_name, domain=FIXProtocolLimited, range=Optional[str])

slots.FIXProtocolLimited_legal_name = Slot(uri=SCHEMA.legalName, name="FIXProtocolLimited_legal_name", curie=SCHEMA.curie('legalName'),
                   model_uri=FIX_PROTOCOL.FIXProtocolLimited_legal_name, domain=FIXProtocolLimited, range=Optional[str])

slots.FIXProtocolLimited_website = Slot(uri=SCHEMA.url, name="FIXProtocolLimited_website", curie=SCHEMA.curie('url'),
                   model_uri=FIX_PROTOCOL.FIXProtocolLimited_website, domain=FIXProtocolLimited, range=Optional[Union[str, URI]])

slots.FIXFamilyStandard_layer = Slot(uri=FIX_BASE.layer, name="FIXFamilyStandard_layer", curie=FIX_BASE.curie('layer'),
                   model_uri=FIX_PROTOCOL.FIXFamilyStandard_layer, domain=FIXFamilyStandard, range=Union[str, "StandardLayer"])

slots.FIXFamilyStandard_acronym = Slot(uri=SCHEMA.alternateName, name="FIXFamilyStandard_acronym", curie=SCHEMA.curie('alternateName'),
                   model_uri=FIX_PROTOCOL.FIXFamilyStandard_acronym, domain=FIXFamilyStandard, range=Optional[str])

slots.ExtensionPack_number = Slot(uri=FIX_BASE.number, name="ExtensionPack_number", curie=FIX_BASE.curie('number'),
                   model_uri=FIX_PROTOCOL.ExtensionPack_number, domain=ExtensionPack, range=Union[int, ExtensionPackNumber])

slots.ExtensionPack_title = Slot(uri=DCTERMS.title, name="ExtensionPack_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.ExtensionPack_title, domain=ExtensionPack, range=str)

slots.FIXDatatype_datatype_name = Slot(uri=FIX_BASE.datatype_name, name="FIXDatatype_datatype_name", curie=FIX_BASE.curie('datatype_name'),
                   model_uri=FIX_PROTOCOL.FIXDatatype_datatype_name, domain=FIXDatatype, range=Union[str, "FIXDatatypeDatatypeName"])

slots.FIXDatatype_definition = Slot(uri=FIX_BASE.definition, name="FIXDatatype_definition", curie=FIX_BASE.curie('definition'),
                   model_uri=FIX_PROTOCOL.FIXDatatype_definition, domain=FIXDatatype, range=str)

slots.BusinessArea_area = Slot(uri=SCHEMA.identifier, name="BusinessArea_area", curie=SCHEMA.curie('identifier'),
                   model_uri=FIX_PROTOCOL.BusinessArea_area, domain=BusinessArea, range=Union[str, "BusinessAreaArea"])

slots.BusinessArea_title = Slot(uri=DCTERMS.title, name="BusinessArea_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.BusinessArea_title, domain=BusinessArea, range=Optional[str])

slots.BusinessArea_description = Slot(uri=DCTERMS.description, name="BusinessArea_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.BusinessArea_description, domain=BusinessArea, range=Optional[str])

slots.MessageCategory_category = Slot(uri=FIX_BASE.category, name="MessageCategory_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.MessageCategory_category, domain=MessageCategory, range=Union[str, "MessageCategoryCategory"])

slots.MessageCategory_title = Slot(uri=DCTERMS.title, name="MessageCategory_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.MessageCategory_title, domain=MessageCategory, range=Optional[str])

slots.MessageCategory_description = Slot(uri=DCTERMS.description, name="MessageCategory_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.MessageCategory_description, domain=MessageCategory, range=Optional[str])

slots.MessageCategory_business_area = Slot(uri=FIX_BASE.business_area, name="MessageCategory_business_area", curie=FIX_BASE.curie('business_area'),
                   model_uri=FIX_PROTOCOL.MessageCategory_business_area, domain=MessageCategory, range=Union[str, "BusinessAreaEnum"])

slots.Field_tag = Slot(uri=FIX_BASE.tag, name="Field_tag", curie=FIX_BASE.curie('tag'),
                   model_uri=FIX_PROTOCOL.Field_tag, domain=Field, range=Union[int, FieldTag])

slots.Field_field_name = Slot(uri=SCHEMA.name, name="Field_field_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.Field_field_name, domain=Field, range=str)

slots.Field_datatype = Slot(uri=FIX_BASE.datatype, name="Field_datatype", curie=FIX_BASE.curie('datatype'),
                   model_uri=FIX_PROTOCOL.Field_datatype, domain=Field, range=Union[str, "FIXDatatypeName"])

slots.Field_description = Slot(uri=DCTERMS.description, name="Field_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.Field_description, domain=Field, range=Optional[str])

slots.Component_component_name = Slot(uri=SCHEMA.name, name="Component_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.Component_component_name, domain=Component, range=Union[str, ComponentComponentName])

slots.Component_scope = Slot(uri=FIX_BASE.scope, name="Component_scope", curie=FIX_BASE.curie('scope'),
                   model_uri=FIX_PROTOCOL.Component_scope, domain=Component, range=Union[str, "ComponentScope"])

slots.Component_description = Slot(uri=DCTERMS.description, name="Component_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.Component_description, domain=Component, range=Optional[str])

slots.GlobalComponent_scope = Slot(uri=FIX_BASE.scope, name="GlobalComponent_scope", curie=FIX_BASE.curie('scope'),
                   model_uri=FIX_PROTOCOL.GlobalComponent_scope, domain=GlobalComponent, range=Union[str, "ComponentScope"])

slots.GlobalComponent_component_group = Slot(uri=FIX_BASE.component_group, name="GlobalComponent_component_group", curie=FIX_BASE.curie('component_group'),
                   model_uri=FIX_PROTOCOL.GlobalComponent_component_group, domain=GlobalComponent, range=Union[str, "ComponentGroup"])

slots.CommonComponent_scope = Slot(uri=FIX_BASE.scope, name="CommonComponent_scope", curie=FIX_BASE.curie('scope'),
                   model_uri=FIX_PROTOCOL.CommonComponent_scope, domain=CommonComponent, range=Union[str, "ComponentScope"])

slots.CommonComponent_business_area = Slot(uri=FIX_BASE.business_area, name="CommonComponent_business_area", curie=FIX_BASE.curie('business_area'),
                   model_uri=FIX_PROTOCOL.CommonComponent_business_area, domain=CommonComponent, range=Union[str, "BusinessAreaEnum"])

slots.SpecificComponent_scope = Slot(uri=FIX_BASE.scope, name="SpecificComponent_scope", curie=FIX_BASE.curie('scope'),
                   model_uri=FIX_PROTOCOL.SpecificComponent_scope, domain=SpecificComponent, range=Union[str, "ComponentScope"])

slots.SpecificComponent_business_area = Slot(uri=FIX_BASE.business_area, name="SpecificComponent_business_area", curie=FIX_BASE.curie('business_area'),
                   model_uri=FIX_PROTOCOL.SpecificComponent_business_area, domain=SpecificComponent, range=Union[str, "BusinessAreaEnum"])

slots.SpecificComponent_category = Slot(uri=FIX_BASE.category, name="SpecificComponent_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.SpecificComponent_category, domain=SpecificComponent, range=Union[str, "MessageCategoryEnum"])

slots.Message_msg_type = Slot(uri=FIX_BASE.msg_type, name="Message_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.Message_msg_type, domain=Message, range=Union[str, MessageMsgType],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.Message_message_name = Slot(uri=SCHEMA.name, name="Message_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.Message_message_name, domain=Message, range=str)

slots.Message_description = Slot(uri=DCTERMS.description, name="Message_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.Message_description, domain=Message, range=Optional[str])

slots.UDFTagRange_range_id = Slot(uri=FIX_BASE.range_id, name="UDFTagRange_range_id", curie=FIX_BASE.curie('range_id'),
                   model_uri=FIX_PROTOCOL.UDFTagRange_range_id, domain=UDFTagRange, range=Union[str, UDFTagRangeRangeId])

slots.UDFTagRange_low_tag = Slot(uri=FIX_BASE.low_tag, name="UDFTagRange_low_tag", curie=FIX_BASE.curie('low_tag'),
                   model_uri=FIX_PROTOCOL.UDFTagRange_low_tag, domain=UDFTagRange, range=int)

slots.UDFTagRange_usage = Slot(uri=FIX_BASE.usage, name="UDFTagRange_usage", curie=FIX_BASE.curie('usage'),
                   model_uri=FIX_PROTOCOL.UDFTagRange_usage, domain=UDFTagRange, range=Union[str, "UDFTagRangeUsage"])

slots.UDFTagRange_description = Slot(uri=DCTERMS.description, name="UDFTagRange_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.UDFTagRange_description, domain=UDFTagRange, range=Optional[str])

slots.UDFTagRange_high_tag = Slot(uri=FIX_BASE.high_tag, name="UDFTagRange_high_tag", curie=FIX_BASE.curie('high_tag'),
                   model_uri=FIX_PROTOCOL.UDFTagRange_high_tag, domain=UDFTagRange, range=Optional[int])

slots.PreTradeBusinessArea_area = Slot(uri=SCHEMA.identifier, name="PreTradeBusinessArea_area", curie=SCHEMA.curie('identifier'),
                   model_uri=FIX_PROTOCOL.PreTradeBusinessArea_area, domain=PreTradeBusinessArea, range=Union[str, "BusinessAreaEnum"])

slots.PreTradeBusinessArea_title = Slot(uri=DCTERMS.title, name="PreTradeBusinessArea_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.PreTradeBusinessArea_title, domain=PreTradeBusinessArea, range=Optional[str])

slots.PreTradeBusinessArea_publisher = Slot(uri=DCTERMS.publisher, name="PreTradeBusinessArea_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=FIX_PROTOCOL.PreTradeBusinessArea_publisher, domain=PreTradeBusinessArea, range=Optional[str])

slots.PreTradeBusinessArea_messages = Slot(uri=FIX_BASE.messages, name="PreTradeBusinessArea_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.PreTradeBusinessArea_messages, domain=PreTradeBusinessArea, range=Optional[Union[dict[Union[str, PreTradeMessageEntryMsgType], Union[dict, "PreTradeMessageEntry"]], list[Union[dict, "PreTradeMessageEntry"]]]])

slots.PreTradeBusinessArea_components = Slot(uri=FIX_BASE.components, name="PreTradeBusinessArea_components", curie=FIX_BASE.curie('components'),
                   model_uri=FIX_PROTOCOL.PreTradeBusinessArea_components, domain=PreTradeBusinessArea, range=Optional[Union[dict[Union[str, PreTradeComponentEntryComponentName], Union[dict, "PreTradeComponentEntry"]], list[Union[dict, "PreTradeComponentEntry"]]]])

slots.PreTradeMessageEntry_msg_type = Slot(uri=FIX_BASE.msg_type, name="PreTradeMessageEntry_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.PreTradeMessageEntry_msg_type, domain=PreTradeMessageEntry, range=Union[str, PreTradeMessageEntryMsgType],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.PreTradeMessageEntry_message_name = Slot(uri=SCHEMA.name, name="PreTradeMessageEntry_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PreTradeMessageEntry_message_name, domain=PreTradeMessageEntry, range=str)

slots.PreTradeMessageEntry_category = Slot(uri=FIX_BASE.category, name="PreTradeMessageEntry_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.PreTradeMessageEntry_category, domain=PreTradeMessageEntry, range=Union[str, "PreTradeCategoryEnum"])

slots.PreTradeComponentEntry_component_name = Slot(uri=SCHEMA.name, name="PreTradeComponentEntry_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PreTradeComponentEntry_component_name, domain=PreTradeComponentEntry, range=Union[str, PreTradeComponentEntryComponentName])

slots.PreTradeComponentEntry_repetition = Slot(uri=FIX_PRE_TRADE.repetition, name="PreTradeComponentEntry_repetition", curie=FIX_PRE_TRADE.curie('repetition'),
                   model_uri=FIX_PROTOCOL.PreTradeComponentEntry_repetition, domain=PreTradeComponentEntry, range=Union[str, "ComponentRepetition"])

slots.PreTradeComponentEntry_category = Slot(uri=FIX_BASE.category, name="PreTradeComponentEntry_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.PreTradeComponentEntry_category, domain=PreTradeComponentEntry, range=str)

slots.PreTradeComponentEntry_is_common = Slot(uri=FIX_PRE_TRADE.is_common, name="PreTradeComponentEntry_is_common", curie=FIX_PRE_TRADE.curie('is_common'),
                   model_uri=FIX_PROTOCOL.PreTradeComponentEntry_is_common, domain=PreTradeComponentEntry, range=Optional[Union[bool, Bool]])

slots.ComponentTableFootnote_footnote_number = Slot(uri=FIX_PRE_TRADE.footnote_number, name="ComponentTableFootnote_footnote_number", curie=FIX_PRE_TRADE.curie('footnote_number'),
                   model_uri=FIX_PROTOCOL.ComponentTableFootnote_footnote_number, domain=ComponentTableFootnote, range=Union[int, ComponentTableFootnoteFootnoteNumber])

slots.ComponentTableFootnote_component_name = Slot(uri=SCHEMA.name, name="ComponentTableFootnote_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.ComponentTableFootnote_component_name, domain=ComponentTableFootnote, range=str)

slots.ComponentTableFootnote_introduced_in = Slot(uri=FIX_PRE_TRADE.introduced_in, name="ComponentTableFootnote_introduced_in", curie=FIX_PRE_TRADE.curie('introduced_in'),
                   model_uri=FIX_PROTOCOL.ComponentTableFootnote_introduced_in, domain=ComponentTableFootnote, range=str)

slots.ComponentTableFootnote_sole_category = Slot(uri=FIX_PRE_TRADE.sole_category, name="ComponentTableFootnote_sole_category", curie=FIX_PRE_TRADE.curie('sole_category'),
                   model_uri=FIX_PROTOCOL.ComponentTableFootnote_sole_category, domain=ComponentTableFootnote, range=Union[str, "PreTradeCategoryEnum"])

slots.PreTradeCategorySection_category = Slot(uri=FIX_BASE.category, name="PreTradeCategorySection_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.PreTradeCategorySection_category, domain=PreTradeCategorySection, range=Union[str, "PreTradeCategorySectionCategory"])

slots.PreTradeCategorySection_messages = Slot(uri=FIX_BASE.messages, name="PreTradeCategorySection_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.PreTradeCategorySection_messages, domain=PreTradeCategorySection, range=Optional[Union[dict[Union[str, PreTradeMessageDetailMsgType], Union[dict, "PreTradeMessageDetail"]], list[Union[dict, "PreTradeMessageDetail"]]]])

slots.PreTradeMessageDetail_msg_type = Slot(uri=FIX_BASE.msg_type, name="PreTradeMessageDetail_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.PreTradeMessageDetail_msg_type, domain=PreTradeMessageDetail, range=Union[str, PreTradeMessageDetailMsgType],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.PreTradeMessageDetail_message_name = Slot(uri=SCHEMA.name, name="PreTradeMessageDetail_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PreTradeMessageDetail_message_name, domain=PreTradeMessageDetail, range=str)

slots.PreTradeMessageDetail_description = Slot(uri=DCTERMS.description, name="PreTradeMessageDetail_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.PreTradeMessageDetail_description, domain=PreTradeMessageDetail, range=Optional[str])

slots.PreTradeComponentDetail_component_name = Slot(uri=SCHEMA.name, name="PreTradeComponentDetail_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PreTradeComponentDetail_component_name, domain=PreTradeComponentDetail, range=Union[str, PreTradeComponentDetailComponentName])

slots.PreTradeComponentDetail_description = Slot(uri=DCTERMS.description, name="PreTradeComponentDetail_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.PreTradeComponentDetail_description, domain=PreTradeComponentDetail, range=Optional[str])

slots.MessageGroup_group_title = Slot(uri=SCHEMA.name, name="MessageGroup_group_title", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.MessageGroup_group_title, domain=MessageGroup, range=Union[str, MessageGroupGroupTitle])

slots.MessageGroup_description = Slot(uri=DCTERMS.description, name="MessageGroup_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.MessageGroup_description, domain=MessageGroup, range=Optional[str])

slots.MessageGroup_messages = Slot(uri=FIX_BASE.messages, name="MessageGroup_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.MessageGroup_messages, domain=MessageGroup, range=Union[dict[Union[str, PreTradeMessageDetailMsgType], Union[dict, PreTradeMessageDetail]], list[Union[dict, PreTradeMessageDetail]]])

slots.CommonComponentDetail_component_name = Slot(uri=SCHEMA.name, name="CommonComponentDetail_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.CommonComponentDetail_component_name, domain=CommonComponentDetail, range=Union[str, "CommonComponentDetailComponentName"])

slots.CommonComponentDetail_description = Slot(uri=DCTERMS.description, name="CommonComponentDetail_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.CommonComponentDetail_description, domain=CommonComponentDetail, range=Optional[str])

slots.PreTradeLayoutRow_pre_layout_kind = Slot(uri=FIX_PRE_TRADE.pre_layout_kind, name="PreTradeLayoutRow_pre_layout_kind", curie=FIX_PRE_TRADE.curie('pre_layout_kind'),
                   model_uri=FIX_PROTOCOL.PreTradeLayoutRow_pre_layout_kind, domain=PreTradeLayoutRow, range=Union[str, "PreTradeLayoutRowKindEnum"])

slots.PreTradeLayoutRow_pre_layout_element_name = Slot(uri=FIX_PRE_TRADE.pre_layout_element_name, name="PreTradeLayoutRow_pre_layout_element_name", curie=FIX_PRE_TRADE.curie('pre_layout_element_name'),
                   model_uri=FIX_PROTOCOL.PreTradeLayoutRow_pre_layout_element_name, domain=PreTradeLayoutRow, range=str)

slots.TradeBusinessArea_trade_area = Slot(uri=SCHEMA.identifier, name="TradeBusinessArea_trade_area", curie=SCHEMA.curie('identifier'),
                   model_uri=FIX_PROTOCOL.TradeBusinessArea_trade_area, domain=TradeBusinessArea, range=Union[str, "BusinessAreaEnum"])

slots.TradeBusinessArea_title = Slot(uri=DCTERMS.title, name="TradeBusinessArea_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.TradeBusinessArea_title, domain=TradeBusinessArea, range=Optional[str])

slots.TradeBusinessArea_publisher = Slot(uri=DCTERMS.publisher, name="TradeBusinessArea_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=FIX_PROTOCOL.TradeBusinessArea_publisher, domain=TradeBusinessArea, range=Optional[str])

slots.TradeBusinessArea_messages = Slot(uri=FIX_BASE.messages, name="TradeBusinessArea_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.TradeBusinessArea_messages, domain=TradeBusinessArea, range=Optional[Union[dict[Union[str, TradeMessageEntryMsgType], Union[dict, "TradeMessageEntry"]], list[Union[dict, "TradeMessageEntry"]]]])

slots.TradeBusinessArea_components = Slot(uri=FIX_BASE.components, name="TradeBusinessArea_components", curie=FIX_BASE.curie('components'),
                   model_uri=FIX_PROTOCOL.TradeBusinessArea_components, domain=TradeBusinessArea, range=Optional[Union[dict[Union[str, TradeComponentEntryComponentName], Union[dict, "TradeComponentEntry"]], list[Union[dict, "TradeComponentEntry"]]]])

slots.TradeMessageEntry_msg_type = Slot(uri=FIX_BASE.msg_type, name="TradeMessageEntry_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.TradeMessageEntry_msg_type, domain=TradeMessageEntry, range=Union[str, TradeMessageEntryMsgType],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.TradeMessageEntry_message_name = Slot(uri=SCHEMA.name, name="TradeMessageEntry_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.TradeMessageEntry_message_name, domain=TradeMessageEntry, range=str)

slots.TradeMessageEntry_category = Slot(uri=FIX_BASE.category, name="TradeMessageEntry_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.TradeMessageEntry_category, domain=TradeMessageEntry, range=Union[str, "TradeCategoryEnum"])

slots.TradeComponentEntry_component_name = Slot(uri=SCHEMA.name, name="TradeComponentEntry_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.TradeComponentEntry_component_name, domain=TradeComponentEntry, range=Union[str, TradeComponentEntryComponentName])

slots.TradeComponentEntry_trade_repetition = Slot(uri=FIX_TRADE.trade_repetition, name="TradeComponentEntry_trade_repetition", curie=FIX_TRADE.curie('trade_repetition'),
                   model_uri=FIX_PROTOCOL.TradeComponentEntry_trade_repetition, domain=TradeComponentEntry, range=Union[str, "TradeComponentRepetition"])

slots.TradeComponentEntry_category = Slot(uri=FIX_BASE.category, name="TradeComponentEntry_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.TradeComponentEntry_category, domain=TradeComponentEntry, range=str)

slots.TradeComponentEntry_trade_is_common = Slot(uri=FIX_TRADE.trade_is_common, name="TradeComponentEntry_trade_is_common", curie=FIX_TRADE.curie('trade_is_common'),
                   model_uri=FIX_PROTOCOL.TradeComponentEntry_trade_is_common, domain=TradeComponentEntry, range=Optional[Union[bool, Bool]])

slots.TradeComponentTableFootnote_trade_footnote_number = Slot(uri=FIX_TRADE.trade_footnote_number, name="TradeComponentTableFootnote_trade_footnote_number", curie=FIX_TRADE.curie('trade_footnote_number'),
                   model_uri=FIX_PROTOCOL.TradeComponentTableFootnote_trade_footnote_number, domain=TradeComponentTableFootnote, range=Union[int, TradeComponentTableFootnoteTradeFootnoteNumber])

slots.TradeComponentTableFootnote_component_name = Slot(uri=SCHEMA.name, name="TradeComponentTableFootnote_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.TradeComponentTableFootnote_component_name, domain=TradeComponentTableFootnote, range=str)

slots.TradeComponentTableFootnote_trade_introduced_in = Slot(uri=FIX_TRADE.trade_introduced_in, name="TradeComponentTableFootnote_trade_introduced_in", curie=FIX_TRADE.curie('trade_introduced_in'),
                   model_uri=FIX_PROTOCOL.TradeComponentTableFootnote_trade_introduced_in, domain=TradeComponentTableFootnote, range=str)

slots.TradeComponentTableFootnote_trade_sole_category = Slot(uri=FIX_TRADE.trade_sole_category, name="TradeComponentTableFootnote_trade_sole_category", curie=FIX_TRADE.curie('trade_sole_category'),
                   model_uri=FIX_PROTOCOL.TradeComponentTableFootnote_trade_sole_category, domain=TradeComponentTableFootnote, range=Union[str, "TradeCategoryEnum"])

slots.TradeCategorySection_category = Slot(uri=FIX_BASE.category, name="TradeCategorySection_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.TradeCategorySection_category, domain=TradeCategorySection, range=Union[str, "TradeCategorySectionCategory"])

slots.TradeCategorySection_messages = Slot(uri=FIX_BASE.messages, name="TradeCategorySection_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.TradeCategorySection_messages, domain=TradeCategorySection, range=Optional[Union[dict[Union[str, TradeMessageDetailMsgType], Union[dict, "TradeMessageDetail"]], list[Union[dict, "TradeMessageDetail"]]]])

slots.TradeMessageDetail_msg_type = Slot(uri=FIX_BASE.msg_type, name="TradeMessageDetail_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.TradeMessageDetail_msg_type, domain=TradeMessageDetail, range=Union[str, TradeMessageDetailMsgType],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.TradeMessageDetail_message_name = Slot(uri=SCHEMA.name, name="TradeMessageDetail_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.TradeMessageDetail_message_name, domain=TradeMessageDetail, range=str)

slots.TradeMessageDetail_description = Slot(uri=DCTERMS.description, name="TradeMessageDetail_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.TradeMessageDetail_description, domain=TradeMessageDetail, range=Optional[str])

slots.TradeComponentDetail_component_name = Slot(uri=SCHEMA.name, name="TradeComponentDetail_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.TradeComponentDetail_component_name, domain=TradeComponentDetail, range=Union[str, TradeComponentDetailComponentName])

slots.TradeComponentDetail_description = Slot(uri=DCTERMS.description, name="TradeComponentDetail_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.TradeComponentDetail_description, domain=TradeComponentDetail, range=Optional[str])

slots.TradeMessageGroup_trade_group_title = Slot(uri=SCHEMA.name, name="TradeMessageGroup_trade_group_title", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.TradeMessageGroup_trade_group_title, domain=TradeMessageGroup, range=Union[str, TradeMessageGroupTradeGroupTitle])

slots.TradeMessageGroup_description = Slot(uri=DCTERMS.description, name="TradeMessageGroup_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.TradeMessageGroup_description, domain=TradeMessageGroup, range=Optional[str])

slots.TradeMessageGroup_messages = Slot(uri=FIX_BASE.messages, name="TradeMessageGroup_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.TradeMessageGroup_messages, domain=TradeMessageGroup, range=Union[dict[Union[str, TradeMessageDetailMsgType], Union[dict, TradeMessageDetail]], list[Union[dict, TradeMessageDetail]]])

slots.TradeCommonComponentDetail_component_name = Slot(uri=SCHEMA.name, name="TradeCommonComponentDetail_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.TradeCommonComponentDetail_component_name, domain=TradeCommonComponentDetail, range=Union[str, "TradeCommonComponentDetailComponentName"])

slots.TradeCommonComponentDetail_description = Slot(uri=DCTERMS.description, name="TradeCommonComponentDetail_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.TradeCommonComponentDetail_description, domain=TradeCommonComponentDetail, range=Optional[str])

slots.TradeLayoutRow_trade_layout_kind = Slot(uri=FIX_TRADE.trade_layout_kind, name="TradeLayoutRow_trade_layout_kind", curie=FIX_TRADE.curie('trade_layout_kind'),
                   model_uri=FIX_PROTOCOL.TradeLayoutRow_trade_layout_kind, domain=TradeLayoutRow, range=Union[str, "TradeLayoutRowKindEnum"])

slots.TradeLayoutRow_trade_layout_element_name = Slot(uri=FIX_TRADE.trade_layout_element_name, name="TradeLayoutRow_trade_layout_element_name", curie=FIX_TRADE.curie('trade_layout_element_name'),
                   model_uri=FIX_PROTOCOL.TradeLayoutRow_trade_layout_element_name, domain=TradeLayoutRow, range=str)

slots.TradeOrdStatusPrecedenceEntry_trade_ord_status_precedence = Slot(uri=FIX_TRADE.trade_ord_status_precedence, name="TradeOrdStatusPrecedenceEntry_trade_ord_status_precedence", curie=FIX_TRADE.curie('trade_ord_status_precedence'),
                   model_uri=FIX_PROTOCOL.TradeOrdStatusPrecedenceEntry_trade_ord_status_precedence, domain=TradeOrdStatusPrecedenceEntry, range=int)

slots.TradeOrdStatusPrecedenceEntry_trade_ord_status_label = Slot(uri=FIX_TRADE.trade_ord_status_label, name="TradeOrdStatusPrecedenceEntry_trade_ord_status_label", curie=FIX_TRADE.curie('trade_ord_status_label'),
                   model_uri=FIX_PROTOCOL.TradeOrdStatusPrecedenceEntry_trade_ord_status_label, domain=TradeOrdStatusPrecedenceEntry, range=Union[str, TradeOrdStatusPrecedenceEntryTradeOrdStatusLabel])

slots.TradeOrdStatusPrecedenceEntry_description = Slot(uri=DCTERMS.description, name="TradeOrdStatusPrecedenceEntry_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.TradeOrdStatusPrecedenceEntry_description, domain=TradeOrdStatusPrecedenceEntry, range=Optional[str])

slots.TradeFragmentationEntry_trade_fragmentation_message = Slot(uri=FIX_TRADE.trade_fragmentation_message, name="TradeFragmentationEntry_trade_fragmentation_message", curie=FIX_TRADE.curie('trade_fragmentation_message'),
                   model_uri=FIX_PROTOCOL.TradeFragmentationEntry_trade_fragmentation_message, domain=TradeFragmentationEntry, range=Union[str, TradeFragmentationEntryTradeFragmentationMessage])

slots.TradeFragmentationEntry_trade_fragmentation_total_entries_field = Slot(uri=FIX_TRADE.trade_fragmentation_total_entries_field, name="TradeFragmentationEntry_trade_fragmentation_total_entries_field", curie=FIX_TRADE.curie('trade_fragmentation_total_entries_field'),
                   model_uri=FIX_PROTOCOL.TradeFragmentationEntry_trade_fragmentation_total_entries_field, domain=TradeFragmentationEntry, range=str)

slots.TradeFragmentationEntry_trade_fragmentation_repeating_group = Slot(uri=FIX_TRADE.trade_fragmentation_repeating_group, name="TradeFragmentationEntry_trade_fragmentation_repeating_group", curie=FIX_TRADE.curie('trade_fragmentation_repeating_group'),
                   model_uri=FIX_PROTOCOL.TradeFragmentationEntry_trade_fragmentation_repeating_group, domain=TradeFragmentationEntry, range=str)

slots.TradeAppendix_title = Slot(uri=DCTERMS.title, name="TradeAppendix_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.TradeAppendix_title, domain=TradeAppendix, range=Optional[str])

slots.TradeAppendix_publisher = Slot(uri=DCTERMS.publisher, name="TradeAppendix_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=FIX_PROTOCOL.TradeAppendix_publisher, domain=TradeAppendix, range=Optional[str])

slots.TradeAppendix_description = Slot(uri=DCTERMS.description, name="TradeAppendix_description", curie=DCTERMS.curie('description'),
                   model_uri=FIX_PROTOCOL.TradeAppendix_description, domain=TradeAppendix, range=Optional[str])

slots.TradeAppendixSection_trade_appendix_category = Slot(uri=FIX_TRADE.trade_appendix_category, name="TradeAppendixSection_trade_appendix_category", curie=FIX_TRADE.curie('trade_appendix_category'),
                   model_uri=FIX_PROTOCOL.TradeAppendixSection_trade_appendix_category, domain=TradeAppendixSection, range=Union[str, TradeAppendixSectionTradeAppendixCategory])

slots.TradeAppendixSection_title = Slot(uri=DCTERMS.title, name="TradeAppendixSection_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.TradeAppendixSection_title, domain=TradeAppendixSection, range=Optional[str])

slots.TradeAppendixSection_messages = Slot(uri=FIX_BASE.messages, name="TradeAppendixSection_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.TradeAppendixSection_messages, domain=TradeAppendixSection, range=Optional[Union[dict[Union[str, TradeMessageDetailMsgType], Union[dict, TradeMessageDetail]], list[Union[dict, TradeMessageDetail]]]])

slots.TradeAppendixSection_components = Slot(uri=FIX_BASE.components, name="TradeAppendixSection_components", curie=FIX_BASE.curie('components'),
                   model_uri=FIX_PROTOCOL.TradeAppendixSection_components, domain=TradeAppendixSection, range=Optional[Union[Union[str, TradeComponentDetailComponentName], list[Union[str, TradeComponentDetailComponentName]]]])

slots.PostTradeBusinessArea_area = Slot(uri=SCHEMA.identifier, name="PostTradeBusinessArea_area", curie=SCHEMA.curie('identifier'),
                   model_uri=FIX_PROTOCOL.PostTradeBusinessArea_area, domain=PostTradeBusinessArea, range=Union[str, "BusinessAreaEnum"])

slots.PostTradeBusinessArea_title = Slot(uri=DCTERMS.title, name="PostTradeBusinessArea_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.PostTradeBusinessArea_title, domain=PostTradeBusinessArea, range=Optional[str])

slots.PostTradeBusinessArea_publisher = Slot(uri=DCTERMS.publisher, name="PostTradeBusinessArea_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=FIX_PROTOCOL.PostTradeBusinessArea_publisher, domain=PostTradeBusinessArea, range=Optional[str])

slots.PostTradeBusinessArea_messages = Slot(uri=FIX_BASE.messages, name="PostTradeBusinessArea_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.PostTradeBusinessArea_messages, domain=PostTradeBusinessArea, range=Union[dict[Union[str, PostTradeMessageEntryMsgType], Union[dict, "PostTradeMessageEntry"]], list[Union[dict, "PostTradeMessageEntry"]]])

slots.PostTradeBusinessArea_components = Slot(uri=FIX_BASE.components, name="PostTradeBusinessArea_components", curie=FIX_BASE.curie('components'),
                   model_uri=FIX_PROTOCOL.PostTradeBusinessArea_components, domain=PostTradeBusinessArea, range=Union[dict[Union[str, PostTradeComponentEntryComponentName], Union[dict, "PostTradeComponentEntry"]], list[Union[dict, "PostTradeComponentEntry"]]])

slots.PostTradeMessageEntry_msg_type = Slot(uri=FIX_BASE.msg_type, name="PostTradeMessageEntry_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.PostTradeMessageEntry_msg_type, domain=PostTradeMessageEntry, range=Union[str, PostTradeMessageEntryMsgType],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.PostTradeMessageEntry_message_name = Slot(uri=SCHEMA.name, name="PostTradeMessageEntry_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PostTradeMessageEntry_message_name, domain=PostTradeMessageEntry, range=str)

slots.PostTradeMessageEntry_category = Slot(uri=FIX_BASE.category, name="PostTradeMessageEntry_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.PostTradeMessageEntry_category, domain=PostTradeMessageEntry, range=Union[str, "PostTradeCategoryEnum"])

slots.PostTradeComponentEntry_component_name = Slot(uri=SCHEMA.name, name="PostTradeComponentEntry_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PostTradeComponentEntry_component_name, domain=PostTradeComponentEntry, range=Union[str, PostTradeComponentEntryComponentName])

slots.PostTradeComponentEntry_repetition = Slot(uri=FIX_PRE_TRADE.repetition, name="PostTradeComponentEntry_repetition", curie=FIX_PRE_TRADE.curie('repetition'),
                   model_uri=FIX_PROTOCOL.PostTradeComponentEntry_repetition, domain=PostTradeComponentEntry, range=Union[str, "ComponentRepetition"])

slots.PostTradeComponentEntry_category = Slot(uri=FIX_BASE.category, name="PostTradeComponentEntry_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.PostTradeComponentEntry_category, domain=PostTradeComponentEntry, range=str)

slots.PostTradeComponentEntry_is_common = Slot(uri=FIX_PRE_TRADE.is_common, name="PostTradeComponentEntry_is_common", curie=FIX_PRE_TRADE.curie('is_common'),
                   model_uri=FIX_PROTOCOL.PostTradeComponentEntry_is_common, domain=PostTradeComponentEntry, range=Optional[Union[bool, Bool]])

slots.PostTradeComponentTableFootnote_footnote_number = Slot(uri=FIX_PRE_TRADE.footnote_number, name="PostTradeComponentTableFootnote_footnote_number", curie=FIX_PRE_TRADE.curie('footnote_number'),
                   model_uri=FIX_PROTOCOL.PostTradeComponentTableFootnote_footnote_number, domain=PostTradeComponentTableFootnote, range=Union[int, PostTradeComponentTableFootnoteFootnoteNumber])

slots.PostTradeComponentTableFootnote_component_name = Slot(uri=SCHEMA.name, name="PostTradeComponentTableFootnote_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PostTradeComponentTableFootnote_component_name, domain=PostTradeComponentTableFootnote, range=str)

slots.PostTradeComponentTableFootnote_introduced_in = Slot(uri=FIX_PRE_TRADE.introduced_in, name="PostTradeComponentTableFootnote_introduced_in", curie=FIX_PRE_TRADE.curie('introduced_in'),
                   model_uri=FIX_PROTOCOL.PostTradeComponentTableFootnote_introduced_in, domain=PostTradeComponentTableFootnote, range=str)

slots.PostTradeComponentTableFootnote_post_sole_category = Slot(uri=FIX_POST_TRADE.post_sole_category, name="PostTradeComponentTableFootnote_post_sole_category", curie=FIX_POST_TRADE.curie('post_sole_category'),
                   model_uri=FIX_PROTOCOL.PostTradeComponentTableFootnote_post_sole_category, domain=PostTradeComponentTableFootnote, range=Union[str, "PostTradeCategoryEnum"])

slots.PostTradeCategorySection_category = Slot(uri=FIX_BASE.category, name="PostTradeCategorySection_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.PostTradeCategorySection_category, domain=PostTradeCategorySection, range=Union[str, "PostTradeCategorySectionCategory"])

slots.PostTradeCategorySection_messages = Slot(uri=FIX_BASE.messages, name="PostTradeCategorySection_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.PostTradeCategorySection_messages, domain=PostTradeCategorySection, range=Optional[Union[dict[Union[str, PostTradeMessageDetailMsgType], Union[dict, "PostTradeMessageDetail"]], list[Union[dict, "PostTradeMessageDetail"]]]])

slots.PostTradeMessageGroup_group_title = Slot(uri=SCHEMA.name, name="PostTradeMessageGroup_group_title", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PostTradeMessageGroup_group_title, domain=PostTradeMessageGroup, range=Union[str, PostTradeMessageGroupGroupTitle])

slots.PostTradeMessageGroup_messages = Slot(uri=FIX_BASE.messages, name="PostTradeMessageGroup_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.PostTradeMessageGroup_messages, domain=PostTradeMessageGroup, range=Union[dict[Union[str, PostTradeMessageDetailMsgType], Union[dict, "PostTradeMessageDetail"]], list[Union[dict, "PostTradeMessageDetail"]]])

slots.PostTradeMessageDetail_msg_type = Slot(uri=FIX_BASE.msg_type, name="PostTradeMessageDetail_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.PostTradeMessageDetail_msg_type, domain=PostTradeMessageDetail, range=Union[str, PostTradeMessageDetailMsgType],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.PostTradeMessageDetail_message_name = Slot(uri=SCHEMA.name, name="PostTradeMessageDetail_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PostTradeMessageDetail_message_name, domain=PostTradeMessageDetail, range=str)

slots.PostTradeComponentDetail_component_name = Slot(uri=SCHEMA.name, name="PostTradeComponentDetail_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PostTradeComponentDetail_component_name, domain=PostTradeComponentDetail, range=Union[str, PostTradeComponentDetailComponentName])

slots.PostTradeCommonComponentDetail_component_name = Slot(uri=SCHEMA.name, name="PostTradeCommonComponentDetail_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.PostTradeCommonComponentDetail_component_name, domain=PostTradeCommonComponentDetail, range=Union[str, "PostTradeCommonComponentDetailComponentName"])

slots.AllocationStatusDescription_status_code = Slot(uri=FIX_POST_TRADE.status_code, name="AllocationStatusDescription_status_code", curie=FIX_POST_TRADE.curie('status_code'),
                   model_uri=FIX_PROTOCOL.AllocationStatusDescription_status_code, domain=AllocationStatusDescription, range=Union[str, AllocationStatusDescriptionStatusCode])

slots.AllocationStatusDescription_status_label = Slot(uri=FIX_POST_TRADE.status_label, name="AllocationStatusDescription_status_label", curie=FIX_POST_TRADE.curie('status_label'),
                   model_uri=FIX_PROTOCOL.AllocationStatusDescription_status_label, domain=AllocationStatusDescription, range=str)

slots.AllocationFragmentationFieldMap_msg_type = Slot(uri=FIX_BASE.msg_type, name="AllocationFragmentationFieldMap_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.AllocationFragmentationFieldMap_msg_type, domain=AllocationFragmentationFieldMap, range=Union[str, AllocationFragmentationFieldMapMsgType],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.AllocationFragmentationFieldMap_message_name = Slot(uri=SCHEMA.name, name="AllocationFragmentationFieldMap_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.AllocationFragmentationFieldMap_message_name, domain=AllocationFragmentationFieldMap, range=str)

slots.AllocationFragmentationFieldMap_total_count_field = Slot(uri=FIX_POST_TRADE.total_count_field, name="AllocationFragmentationFieldMap_total_count_field", curie=FIX_POST_TRADE.curie('total_count_field'),
                   model_uri=FIX_PROTOCOL.AllocationFragmentationFieldMap_total_count_field, domain=AllocationFragmentationFieldMap, range=str)

slots.AllocationFragmentationFieldMap_fragment_count_field = Slot(uri=FIX_POST_TRADE.fragment_count_field, name="AllocationFragmentationFieldMap_fragment_count_field", curie=FIX_POST_TRADE.curie('fragment_count_field'),
                   model_uri=FIX_PROTOCOL.AllocationFragmentationFieldMap_fragment_count_field, domain=AllocationFragmentationFieldMap, range=str)

slots.AllocationFragmentationFieldMap_principal_message_reference = Slot(uri=FIX_POST_TRADE.principal_message_reference, name="AllocationFragmentationFieldMap_principal_message_reference", curie=FIX_POST_TRADE.curie('principal_message_reference'),
                   model_uri=FIX_PROTOCOL.AllocationFragmentationFieldMap_principal_message_reference, domain=AllocationFragmentationFieldMap, range=str)

slots.TradeCaptureReportUsage_status_label = Slot(uri=FIX_POST_TRADE.status_label, name="TradeCaptureReportUsage_status_label", curie=FIX_POST_TRADE.curie('status_label'),
                   model_uri=FIX_PROTOCOL.TradeCaptureReportUsage_status_label, domain=TradeCaptureReportUsage, range=Union[str, TradeCaptureReportUsageStatusLabel])

slots.TradeCaptureReportIdentifierRule_identifier_role = Slot(uri=FIX_POST_TRADE.identifier_role, name="TradeCaptureReportIdentifierRule_identifier_role", curie=FIX_POST_TRADE.curie('identifier_role'),
                   model_uri=FIX_PROTOCOL.TradeCaptureReportIdentifierRule_identifier_role, domain=TradeCaptureReportIdentifierRule, range=Union[str, "TradeCaptureReportIdentifierRuleIdentifierRole"])

slots.RegistrationStatusDescription_status_code = Slot(uri=FIX_POST_TRADE.status_code, name="RegistrationStatusDescription_status_code", curie=FIX_POST_TRADE.curie('status_code'),
                   model_uri=FIX_PROTOCOL.RegistrationStatusDescription_status_code, domain=RegistrationStatusDescription, range=Union[str, RegistrationStatusDescriptionStatusCode])

slots.RegistrationStatusDescription_status_label = Slot(uri=FIX_POST_TRADE.status_label, name="RegistrationStatusDescription_status_label", curie=FIX_POST_TRADE.curie('status_label'),
                   model_uri=FIX_PROTOCOL.RegistrationStatusDescription_status_label, domain=RegistrationStatusDescription, range=str)

slots.ClearingServicePostTradeProcessingFormat_message_format = Slot(uri=FIX_POST_TRADE.message_format, name="ClearingServicePostTradeProcessingFormat_message_format", curie=FIX_POST_TRADE.curie('message_format'),
                   model_uri=FIX_PROTOCOL.ClearingServicePostTradeProcessingFormat_message_format, domain=ClearingServicePostTradeProcessingFormat, range=Union[str, "ClearingServicePostTradeProcessingFormatMessageFormat"])

slots.ClearingServicePostTradeProcessingFormat_supported_actions = Slot(uri=FIX_POST_TRADE.supported_actions, name="ClearingServicePostTradeProcessingFormat_supported_actions", curie=FIX_POST_TRADE.curie('supported_actions'),
                   model_uri=FIX_PROTOCOL.ClearingServicePostTradeProcessingFormat_supported_actions, domain=ClearingServicePostTradeProcessingFormat, range=Union[str, list[str]])

slots.PostTradeLayoutRow_post_layout_kind = Slot(uri=FIX_POST_TRADE.post_layout_kind, name="PostTradeLayoutRow_post_layout_kind", curie=FIX_POST_TRADE.curie('post_layout_kind'),
                   model_uri=FIX_PROTOCOL.PostTradeLayoutRow_post_layout_kind, domain=PostTradeLayoutRow, range=Union[str, "PostTradeLayoutRowKindEnum"])

slots.PostTradeLayoutRow_post_layout_element_name = Slot(uri=FIX_POST_TRADE.post_layout_element_name, name="PostTradeLayoutRow_post_layout_element_name", curie=FIX_POST_TRADE.curie('post_layout_element_name'),
                   model_uri=FIX_PROTOCOL.PostTradeLayoutRow_post_layout_element_name, domain=PostTradeLayoutRow, range=str)

slots.InfrastructureBusinessArea_area = Slot(uri=SCHEMA.identifier, name="InfrastructureBusinessArea_area", curie=SCHEMA.curie('identifier'),
                   model_uri=FIX_PROTOCOL.InfrastructureBusinessArea_area, domain=InfrastructureBusinessArea, range=Union[str, "BusinessAreaEnum"])

slots.InfrastructureBusinessArea_title = Slot(uri=DCTERMS.title, name="InfrastructureBusinessArea_title", curie=DCTERMS.curie('title'),
                   model_uri=FIX_PROTOCOL.InfrastructureBusinessArea_title, domain=InfrastructureBusinessArea, range=Optional[str])

slots.InfrastructureBusinessArea_publisher = Slot(uri=DCTERMS.publisher, name="InfrastructureBusinessArea_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=FIX_PROTOCOL.InfrastructureBusinessArea_publisher, domain=InfrastructureBusinessArea, range=Optional[str])

slots.InfrastructureBusinessArea_messages = Slot(uri=FIX_BASE.messages, name="InfrastructureBusinessArea_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.InfrastructureBusinessArea_messages, domain=InfrastructureBusinessArea, range=Union[dict[Union[str, InfrastructureMessageEntryMsgType], Union[dict, "InfrastructureMessageEntry"]], list[Union[dict, "InfrastructureMessageEntry"]]])

slots.InfrastructureBusinessArea_components = Slot(uri=FIX_BASE.components, name="InfrastructureBusinessArea_components", curie=FIX_BASE.curie('components'),
                   model_uri=FIX_PROTOCOL.InfrastructureBusinessArea_components, domain=InfrastructureBusinessArea, range=Union[dict[Union[str, InfrastructureComponentEntryComponentName], Union[dict, "InfrastructureComponentEntry"]], list[Union[dict, "InfrastructureComponentEntry"]]])

slots.InfrastructureMessageEntry_msg_type = Slot(uri=FIX_BASE.msg_type, name="InfrastructureMessageEntry_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.InfrastructureMessageEntry_msg_type, domain=InfrastructureMessageEntry, range=Union[str, InfrastructureMessageEntryMsgType],
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.InfrastructureMessageEntry_message_name = Slot(uri=SCHEMA.name, name="InfrastructureMessageEntry_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.InfrastructureMessageEntry_message_name, domain=InfrastructureMessageEntry, range=str)

slots.InfrastructureMessageEntry_category = Slot(uri=FIX_BASE.category, name="InfrastructureMessageEntry_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.InfrastructureMessageEntry_category, domain=InfrastructureMessageEntry, range=Union[str, "InfrastructureCategoryEnum"])

slots.InfrastructureComponentEntry_component_name = Slot(uri=SCHEMA.name, name="InfrastructureComponentEntry_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.InfrastructureComponentEntry_component_name, domain=InfrastructureComponentEntry, range=Union[str, InfrastructureComponentEntryComponentName])

slots.InfrastructureComponentEntry_repetition = Slot(uri=FIX_PRE_TRADE.repetition, name="InfrastructureComponentEntry_repetition", curie=FIX_PRE_TRADE.curie('repetition'),
                   model_uri=FIX_PROTOCOL.InfrastructureComponentEntry_repetition, domain=InfrastructureComponentEntry, range=Union[str, "ComponentRepetition"])

slots.InfrastructureComponentEntry_category = Slot(uri=FIX_BASE.category, name="InfrastructureComponentEntry_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.InfrastructureComponentEntry_category, domain=InfrastructureComponentEntry, range=Union[str, "InfrastructureCategoryEnum"])

slots.InfrastructureComponentTableFootnote_footnote_number = Slot(uri=FIX_PRE_TRADE.footnote_number, name="InfrastructureComponentTableFootnote_footnote_number", curie=FIX_PRE_TRADE.curie('footnote_number'),
                   model_uri=FIX_PROTOCOL.InfrastructureComponentTableFootnote_footnote_number, domain=InfrastructureComponentTableFootnote, range=Union[int, InfrastructureComponentTableFootnoteFootnoteNumber])

slots.InfrastructureComponentTableFootnote_component_name = Slot(uri=SCHEMA.name, name="InfrastructureComponentTableFootnote_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.InfrastructureComponentTableFootnote_component_name, domain=InfrastructureComponentTableFootnote, range=str)

slots.InfrastructureComponentTableFootnote_introduced_in = Slot(uri=FIX_PRE_TRADE.introduced_in, name="InfrastructureComponentTableFootnote_introduced_in", curie=FIX_PRE_TRADE.curie('introduced_in'),
                   model_uri=FIX_PROTOCOL.InfrastructureComponentTableFootnote_introduced_in, domain=InfrastructureComponentTableFootnote, range=str)

slots.InfrastructureComponentTableFootnote_infra_sole_category = Slot(uri=FIX_INFRASTRUCTURE.infra_sole_category, name="InfrastructureComponentTableFootnote_infra_sole_category", curie=FIX_INFRASTRUCTURE.curie('infra_sole_category'),
                   model_uri=FIX_PROTOCOL.InfrastructureComponentTableFootnote_infra_sole_category, domain=InfrastructureComponentTableFootnote, range=Union[str, "InfrastructureCategoryEnum"])

slots.InfrastructureCategorySection_category = Slot(uri=FIX_BASE.category, name="InfrastructureCategorySection_category", curie=FIX_BASE.curie('category'),
                   model_uri=FIX_PROTOCOL.InfrastructureCategorySection_category, domain=InfrastructureCategorySection, range=Union[str, "InfrastructureCategoryEnum"])

slots.InfrastructureCategorySection_messages = Slot(uri=FIX_BASE.messages, name="InfrastructureCategorySection_messages", curie=FIX_BASE.curie('messages'),
                   model_uri=FIX_PROTOCOL.InfrastructureCategorySection_messages, domain=InfrastructureCategorySection, range=Optional[Union[Union[dict, "InfrastructureMessageDetail"], list[Union[dict, "InfrastructureMessageDetail"]]]])

slots.InfrastructureMessageDetail_msg_type = Slot(uri=FIX_BASE.msg_type, name="InfrastructureMessageDetail_msg_type", curie=FIX_BASE.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.InfrastructureMessageDetail_msg_type, domain=InfrastructureMessageDetail, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9]{1,3}$'))

slots.InfrastructureMessageDetail_message_name = Slot(uri=SCHEMA.name, name="InfrastructureMessageDetail_message_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.InfrastructureMessageDetail_message_name, domain=InfrastructureMessageDetail, range=str)

slots.InfrastructureComponentDetail_component_name = Slot(uri=SCHEMA.name, name="InfrastructureComponentDetail_component_name", curie=SCHEMA.curie('name'),
                   model_uri=FIX_PROTOCOL.InfrastructureComponentDetail_component_name, domain=InfrastructureComponentDetail, range=str)

slots.InfrastructureLayoutRow_infra_layout_kind = Slot(uri=FIX_INFRASTRUCTURE.infra_layout_kind, name="InfrastructureLayoutRow_infra_layout_kind", curie=FIX_INFRASTRUCTURE.curie('infra_layout_kind'),
                   model_uri=FIX_PROTOCOL.InfrastructureLayoutRow_infra_layout_kind, domain=InfrastructureLayoutRow, range=Union[str, "InfrastructureLayoutRowKindEnum"])

slots.InfrastructureLayoutRow_infra_layout_element_name = Slot(uri=FIX_INFRASTRUCTURE.infra_layout_element_name, name="InfrastructureLayoutRow_infra_layout_element_name", curie=FIX_INFRASTRUCTURE.curie('infra_layout_element_name'),
                   model_uri=FIX_PROTOCOL.InfrastructureLayoutRow_infra_layout_element_name, domain=InfrastructureLayoutRow, range=str)

slots.StandardResponseMapping_category_label = Slot(uri=FIX_INFRASTRUCTURE.category_label, name="StandardResponseMapping_category_label", curie=FIX_INFRASTRUCTURE.curie('category_label'),
                   model_uri=FIX_PROTOCOL.StandardResponseMapping_category_label, domain=StandardResponseMapping, range=str)

slots.StandardResponseMapping_fix_message = Slot(uri=FIX_INFRASTRUCTURE.fix_message, name="StandardResponseMapping_fix_message", curie=FIX_INFRASTRUCTURE.curie('fix_message'),
                   model_uri=FIX_PROTOCOL.StandardResponseMapping_fix_message, domain=StandardResponseMapping, range=str)

slots.StandardResponseMapping_appropriate_responses = Slot(uri=FIX_INFRASTRUCTURE.appropriate_responses, name="StandardResponseMapping_appropriate_responses", curie=FIX_INFRASTRUCTURE.curie('appropriate_responses'),
                   model_uri=FIX_PROTOCOL.StandardResponseMapping_appropriate_responses, domain=StandardResponseMapping, range=str)

slots.ApplicationMessageReferenceKey_category_label = Slot(uri=FIX_INFRASTRUCTURE.category_label, name="ApplicationMessageReferenceKey_category_label", curie=FIX_INFRASTRUCTURE.curie('category_label'),
                   model_uri=FIX_PROTOCOL.ApplicationMessageReferenceKey_category_label, domain=ApplicationMessageReferenceKey, range=str)

slots.ApplicationMessageReferenceKey_fix_message = Slot(uri=FIX_INFRASTRUCTURE.fix_message, name="ApplicationMessageReferenceKey_fix_message", curie=FIX_INFRASTRUCTURE.curie('fix_message'),
                   model_uri=FIX_PROTOCOL.ApplicationMessageReferenceKey_fix_message, domain=ApplicationMessageReferenceKey, range=str)

slots.ApplicationMessageReferenceKey_business_reject_ref_id_value = Slot(uri=FIX_INFRASTRUCTURE.business_reject_ref_id_value, name="ApplicationMessageReferenceKey_business_reject_ref_id_value", curie=FIX_INFRASTRUCTURE.curie('business_reject_ref_id_value'),
                   model_uri=FIX_PROTOCOL.ApplicationMessageReferenceKey_business_reject_ref_id_value, domain=ApplicationMessageReferenceKey, range=str)

slots.BusinessRejectReasonDescription_reject_reason_code = Slot(uri=FIX_INFRASTRUCTURE.reject_reason_code, name="BusinessRejectReasonDescription_reject_reason_code", curie=FIX_INFRASTRUCTURE.curie('reject_reason_code'),
                   model_uri=FIX_PROTOCOL.BusinessRejectReasonDescription_reject_reason_code, domain=BusinessRejectReasonDescription, range=Union[int, BusinessRejectReasonDescriptionRejectReasonCode])

slots.BusinessRejectReasonDescription_reject_reason_label = Slot(uri=FIX_INFRASTRUCTURE.reject_reason_label, name="BusinessRejectReasonDescription_reject_reason_label", curie=FIX_INFRASTRUCTURE.curie('reject_reason_label'),
                   model_uri=FIX_PROTOCOL.BusinessRejectReasonDescription_reject_reason_label, domain=BusinessRejectReasonDescription, range=str)

slots.InfrastructureGlobalComponentReference_infra_global_component_name = Slot(uri=FIX_INFRASTRUCTURE.infra_global_component_name, name="InfrastructureGlobalComponentReference_infra_global_component_name", curie=FIX_INFRASTRUCTURE.curie('infra_global_component_name'),
                   model_uri=FIX_PROTOCOL.InfrastructureGlobalComponentReference_infra_global_component_name, domain=InfrastructureGlobalComponentReference, range=Union[str, "InfrastructureGlobalComponentReferenceInfraGlobalComponentName"])

slots.InfrastructureGlobalComponentReference_infra_global_component_used_in = Slot(uri=FIX_INFRASTRUCTURE.infra_global_component_used_in, name="InfrastructureGlobalComponentReference_infra_global_component_used_in", curie=FIX_INFRASTRUCTURE.curie('infra_global_component_used_in'),
                   model_uri=FIX_PROTOCOL.InfrastructureGlobalComponentReference_infra_global_component_used_in, domain=InfrastructureGlobalComponentReference, range=Union[Union[str, "InfrastructureCategoryEnum"], list[Union[str, "InfrastructureCategoryEnum"]]])
