import pandera.polars as pla
from pandera.api.polars.types import PolarsData
from . import panderagen_polars_schema as pa_pl
import polars as pl
from typing import Optional


from pandera.typing import (
    Index,
    DataFrame,
    Series
)
from pandera.engines.polars_engine import (
    DateTime,
    Date,
    Time,
    Enum,
    Struct,
    List,
    Object
)


from linkml.generators.panderagen.linkml_pandera_validator import LinkmlPanderaValidator as _LinkmlPanderaValidator


# These are all str for now
ID_TYPES = {
    "FIXProtocolLimited": "str",
    "FIXFamilyStandard": "str",
    "ExtensionPack": "str",
    "FIXDatatype": "str",
    "Field": "str",
    "Message": "str",
    "MessageCategory": "str",
    "BusinessArea": "str",
    "Component": "str",
    "GlobalComponent": "str",
    "UDFTagRange": "str",
    "FIXIntroduction": "str",
    "CommonComponent": "str",
    "SpecificComponent": "str",
    "PreTradeMessageEntry": "str",
    "PreTradeComponentEntry": "str",
    "PreTradeLayoutRow": "str",
    "CommonComponentDetail": "str",
    "ComponentTableFootnote": "str",
    "PreTradeMessageDetail": "str",
    "MessageGroup": "str",
    "PreTradeComponentDetail": "str",
    "PreTradeCategorySection": "str",
    "PreTradeBusinessArea": "str",
    "TradeMessageEntry": "str",
    "TradeComponentEntry": "str",
    "TradeLayoutRow": "str",
    "TradeCommonComponentDetail": "str",
    "TradeComponentTableFootnote": "str",
    "TradeMessageDetail": "str",
    "TradeOrdStatusPrecedenceEntry": "str",
    "TradeMessageGroup": "str",
    "TradeComponentDetail": "str",
    "TradeFragmentationEntry": "str",
    "TradeCategorySection": "str",
    "TradeBusinessArea": "str",
    "TradeAppendixSection": "str",
    "TradeAppendix": "str",
    "PostTradeMessageEntry": "str",
    "PostTradeComponentEntry": "str",
    "PostTradeComponentTableFootnote": "str",
    "PostTradeLayoutRow": "str",
    "PostTradeMessageDetail": "str",
    "PostTradeMessageGroup": "str",
    "PostTradeComponentDetail": "str",
    "AllocationStatusDescription": "str",
    "AllocationFragmentationFieldMap": "str",
    "TradeCaptureReportUsage": "str",
    "TradeCaptureReportIdentifierRule": "str",
    "RegistrationStatusDescription": "str",
    "ClearingServicePostTradeProcessingFormat": "str",
    "PostTradeCategorySection": "str",
    "PostTradeCommonComponentDetail": "str",
    "PostTradeBusinessArea": "str",
    "InfrastructureMessageEntry": "str",
    "InfrastructureComponentEntry": "str",
    "InfrastructureComponentTableFootnote": "str",
    "InfrastructureLayoutRow": "str",
    "InfrastructureMessageDetail": "str",
    "InfrastructureComponentDetail": "str",
    "InfrastructureCategorySection": "str",
    "StandardResponseMapping": "str",
    "ApplicationMessageReferenceKey": "str",
    "BusinessRejectReasonDescription": "str",
    "InfrastructureGlobalComponentReference": "str",
    "InfrastructureBusinessArea": "str",
}

# metamodel_version: 1.11.0
class FIXProtocolLimited(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    The organization that maintains the FIX Protocol specification.
    """

    _id_name : str = None
    brand_name: Optional[str] = pla.Field(nullable=True, )
    """
    Brand name used by the organization.
    """
    
    legal_name: Optional[str] = pla.Field(nullable=True, )
    """
    Legal name of the organization.
    """
    
    website: Optional[str] = pla.Field(nullable=True, )
    """
    Main website URL of the organization.
    """
    
    member_firms_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL listing current FPL Member firms.
    """
    
    working_groups_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL listing currently active FPL Working Groups.
    """
    
    committees_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL listing Product and Regional Committees.
    """
    
    member_types: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('BUY_SIDE_FIRM','SELL_SIDE_FIRM','EXCHANGE','ECN_ATS','UTILITY','VENDOR','OTHER_ASSOCIATION',)})
    """
    Organization categories represented in FPL membership.
    """
    
    governance_bodies: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('GLOBAL_STEERING_COMMITTEE','GLOBAL_TECHNICAL_COMMITTEE','GLOBAL_PRODUCT_COMMITTEE','GLOBAL_BUY_SIDE_COMMITTEE','GLOBAL_MEMBER_SERVICES_COMMITTEE','REGIONAL_COMMITTEE',)})
    """
    High-level governance bodies that represent FPL.
    """
    
    product_committees: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('FIXED_INCOME_AND_CURRENCIES','LISTED_PRODUCTS_AND_EXCHANGES',)})
    """
    Global Product Committees maintained by FPL.
    """
    
    regional_committees: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('AMERICAS','ASIA_PACIFIC','EMEA','JAPAN',)})
    """
    Regional Committees maintained by FPL.
    """
    
    
class FIXFamilyStandard(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A member standard of the FIX Family of Standards.
    """

    _id_name : str =  'id' 
    id: str = pla.Field()
    """
    Unique identifier (CURIE or local name) of the element.
    """
    
    name: str = pla.Field()
    """
    Display name of the element.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    acronym: Optional[str] = pla.Field(nullable=True, )
    """
    Short acronym used to refer to the standard.
    """
    
    see_also: Optional[str] = pla.Field(nullable=True, )
    """
    Related external resources.
    """
    
    layer: Enum = pla.Field(dtype_kwargs={"categories":('APPLICATION','ENCODING','SESSION',)})
    """
    The layer the standard belongs to.
    """
    
    version: Optional[str] = pla.Field(nullable=True, )
    """
    Version of the standard, if applicable.
    """
    
    session_profile: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('FIX_4_2','FIX4','FIXT','LFIXT','FIXP','SOFH','FIXS','AMQP',)})
    """
    Name of the session profile for session-layer variants.
    """
    
    encoding_name: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('TAGVALUE','FIXML','FAST','SBE','GPB','JSON','ASN_1',)})
    """
    Named encoding, when layer is ENCODING.
    """
    
    
class ExtensionPack(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A unit of change to FIX Latest.
    """

    _id_name : str =  'number' 
    number: int = pla.Field()
    """
    Sequential identifier of the Extension Pack.
    """
    
    title: str = pla.Field()
    """
    Short descriptive title.
    """
    
    size: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('XXS','XS','S','M','L','XL','XXL',)})
    """
    Qualitative size indicator (XXS..XXL).
    """
    
    enhancement_summary: Optional[str] = pla.Field(nullable=True, )
    """
    Narrative summary of what the EP introduces.
    """
    
    applies_to_session_layer_only: Optional[bool] = pla.Field(nullable=True, )
    """
    True when the EP applies only to the FIX Session Layer.
    """
    
    applies_to_fixml_only: Optional[bool] = pla.Field(nullable=True, )
    """
    True when the EP applies only to the FIXML encoding.
    """
    
    
class FIXDatatype(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A FIX Protocol datatype.
    """

    _id_name : str =  'datatype_name' 
    datatype_name: Enum = pla.Field(dtype_kwargs={"categories":('int','TagNum','SeqNum','NumInGroup','DayOfMonth','float','Qty','Price','PriceOffset','Amt','Percentage','char','Boolean','String','MultipleCharValue','MultipleStringValue','Country','Currency','Exchange','MonthYear','UTCTimestamp','UTCTimeOnly','UTCDateOnly','LocalMktDate','TZTimeOnly','TZTimestamp','Length','data','Tenor','Reserved100Plus','Reserved1000Plus','Reserved4000Plus','XMLData','Language','LocalMktTime',)})
    """
    Canonical FIX datatype name.
    """
    
    definition: str = pla.Field()
    """
    Prose definition of the datatype.
    """
    
    value_space: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('integer','ordinal','size','real','scaled','character','characterstring','boolean','set','array','time','union',)})
    """
    ISO/IEC 11404:2007 GPD value space assigned to the datatype.
    """
    
    value_space_notes: Optional[str] = pla.Field(nullable=True, )
    """
    Additional value-space constraints.
    """
    
    deprecated_for_new_designs: Optional[bool] = pla.Field(nullable=True, )
    """
    True for datatypes not permitted in new designs.
    """
    
    external_code_set: Optional[str] = pla.Field(nullable=True, )
    """
    Reference standard for datatypes backed by an external code set.
    """
    
    time_unit: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('SECOND','MILLISECOND','MICROSECOND','NANOSECOND','PICOSECOND','DAY',)})
    """
    Time-unit precision for time-bearing datatypes.
    """
    
    radix: Optional[int] = pla.Field(nullable=True, )
    """
    Numeric radix for scaled value-space datatypes.
    """
    
    repertoire: Optional[str] = pla.Field(nullable=True, )
    """
    Character repertoire for character/string datatypes.
    """
    
    index_lower_bound: Optional[int] = pla.Field(nullable=True, )
    """
    Inclusive lower bound of a bounded-array index.
    """
    
    index_upper_bound: Optional[int] = pla.Field(nullable=True, )
    """
    Inclusive upper bound of a bounded-array index.
    """
    
    minimum_value: Optional[int] = pla.Field(nullable=True, )
    """
    Inclusive lower bound on the integer value space.
    """
    
    maximum_value: Optional[int] = pla.Field(nullable=True, )
    """
    Inclusive upper bound on the integer value space.
    """
    
    footnote_numbers: Optional[int] = pla.Field(nullable=True, )
    """
    Footnote indicators attached to a datatype row.
    """
    
    
class Field(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A FIX field — a uniquely tagged data element with a FIX datatype.
    """

    _id_name : str =  'tag' 
    tag: int = pla.Field()
    """
    Numeric tag of the field.
    """
    
    field_name: str = pla.Field()
    """
    PascalCase name of the field.
    """
    
    datatype: Enum = pla.Field(dtype_kwargs={"categories":('int','TagNum','SeqNum','NumInGroup','DayOfMonth','float','Qty','Price','PriceOffset','Amt','Percentage','char','Boolean','String','MultipleCharValue','MultipleStringValue','Country','Currency','Exchange','MonthYear','UTCTimestamp','UTCTimeOnly','UTCDateOnly','LocalMktDate','TZTimeOnly','TZTimestamp','Length','data','Tenor','Reserved100Plus','Reserved1000Plus','Reserved4000Plus','XMLData','Language','LocalMktTime',)})
    """
    FIX datatype of the field.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the field's purpose.
    """
    
    requirement: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('REQUIRED','OPTIONAL','CONDITIONALLY_REQUIRED',)})
    """
    Required-status of the field within the enclosing context.
    """
    
    is_user_defined: Optional[bool] = pla.Field(nullable=True, )
    """
    True when the field is a User Defined Field.
    """
    
    
class Message(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A FIX application message.
    """

    _id_name : str =  'msg_type' 
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the message's purpose.
    """
    
    category: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('INDICATION','EVENT_COMMUNICATION','QUOTATION_NEGOTIATION','MARKET_DATA','MARKET_STRUCTURE_REFERENCE_DATA','SECURITIES_REFERENCE_DATA','PARTIES_REFERENCE_DATA','PARTIES_ACTION','SINGLE_GENERAL_ORDER_HANDLING','ORDER_MASS_HANDLING','CROSS_ORDERS','MULTILEG_ORDERS','LIST_PROGRAM_BASKET_TRADING','ALLOCATION_AND_READY_TO_BOOK','CONFIRMATION','SETTLEMENT_INSTRUCTIONS','TRADE_CAPTURE_REPORTING','REGISTRATION_INSTRUCTIONS','POSITIONS_MAINTENANCE','COLLATERAL_MANAGEMENT','MARGIN_REQUIREMENT_MANAGEMENT','ACCOUNT_REPORTING','TRADE_MANAGEMENT','PAY_MANAGEMENT','SETTLEMENT_STATUS_MANAGEMENT','BUSINESS_MESSAGE_REJECTS','NETWORK_STATUS_COMMUNICATION','USER_MANAGEMENT','APPLICATION_SEQUENCING',)})
    """
    Message category.
    """
    
    fields: Optional[List] = pla.Field(nullable=True, )
    """
    Fields directly contained by the enclosing element.
    """
    
    components: Optional[List] = pla.Field(nullable=True, )
    """
    Components referenced by the enclosing element.
    """
    
    
    @pla.check("fields")
    def check_nested_struct_fields(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Field, pa_pl.FieldDict)
        
class MessageCategory(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A message category within a business area.
    """

    _id_name : str =  'category' 
    category: Enum = pla.Field(dtype_kwargs={"categories":('INDICATION','EVENT_COMMUNICATION','QUOTATION_NEGOTIATION','MARKET_DATA','MARKET_STRUCTURE_REFERENCE_DATA','SECURITIES_REFERENCE_DATA','PARTIES_REFERENCE_DATA','PARTIES_ACTION','SINGLE_GENERAL_ORDER_HANDLING','ORDER_MASS_HANDLING','CROSS_ORDERS','MULTILEG_ORDERS','LIST_PROGRAM_BASKET_TRADING','ALLOCATION_AND_READY_TO_BOOK','CONFIRMATION','SETTLEMENT_INSTRUCTIONS','TRADE_CAPTURE_REPORTING','REGISTRATION_INSTRUCTIONS','POSITIONS_MAINTENANCE','COLLATERAL_MANAGEMENT','MARGIN_REQUIREMENT_MANAGEMENT','ACCOUNT_REPORTING','TRADE_MANAGEMENT','PAY_MANAGEMENT','SETTLEMENT_STATUS_MANAGEMENT','BUSINESS_MESSAGE_REJECTS','NETWORK_STATUS_COMMUNICATION','USER_MANAGEMENT','APPLICATION_SEQUENCING',)})
    """
    Identity of the message category.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title of the category.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the category.
    """
    
    business_area: Enum = pla.Field(dtype_kwargs={"categories":('INTRODUCTION','PRE_TRADE','TRADE','POST_TRADE','INFRASTRUCTURE',)})
    """
    Business area the element belongs to.
    """
    
    messages: Optional[List] = pla.Field(nullable=True, )
    """
    Messages defined within the enclosing element.
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Message, pa_pl.MessageDict)
        
class BusinessArea(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A top-level business area of the FIX Latest specification.
    """

    _id_name : str =  'area' 
    area: Enum = pla.Field(dtype_kwargs={"categories":('INTRODUCTION','PRE_TRADE','TRADE','POST_TRADE','INFRASTRUCTURE',)})
    """
    Identity of the business area.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title of the area.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the area.
    """
    
    categories: Optional[List] = pla.Field(nullable=True, )
    """
    Message categories defined within a business area.
    """
    
    
    @pla.check("categories")
    def check_nested_struct_categories(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, MessageCategory, pa_pl.MessageCategoryDict)
        
class Component(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A FIX component — a named set of related fields.
    """

    _id_name : str =  'component_name' 
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the component.
    """
    
    scope: Enum = pla.Field(dtype_kwargs={"categories":('GLOBAL','COMMON','SPECIFIC',)})
    """
    Sharing scope of the component.
    """
    
    is_repeating_group: Optional[bool] = pla.Field(nullable=True, )
    """
    True when the component is a repeating group.
    """
    
    fields: Optional[List] = pla.Field(nullable=True, )
    """
    Fields directly contained by the enclosing element.
    """
    
    nested_components: Optional[List] = pla.Field(nullable=True, )
    """
    Components nested within this component.
    """
    
    
    @pla.check("fields")
    def check_nested_struct_fields(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, Field, pa_pl.FieldDict)
        
class GlobalComponent(Component):
    """
    A component shared by messages of two or more business areas.
    """

    _id_name : str =  'component_name' 
    component_group: Enum = pla.Field(dtype_kwargs={"categories":('SECURITIES','LEG_SECURITIES','UNDERLYING_SECURITIES','PARTIES','ORDERS_AND_QUOTES','TRADES','COMMISSIONS_AND_FEES','FINANCING','PAYMENTS','STIPULATIONS','HEADER_AND_TRAILER','MISCELLANEOUS',)})
    """
    Thematic group under which the component is presented.
    """
    
    applies_to_instrument: Optional[bool] = pla.Field(nullable=True, )
    """
    Applicable at the Instrument level.
    """
    
    applies_to_leg: Optional[bool] = pla.Field(nullable=True, )
    """
    Applicable at the InstrumentLeg level.
    """
    
    applies_to_underlying: Optional[bool] = pla.Field(nullable=True, )
    """
    Applicable at the UnderlyingInstrument level.
    """
    
    conceptually_identical_to: Optional[str] = pla.Field(nullable=True, )
    """
    Names of other components conceptually identical to this one.
    """
    
    gc_id: Optional[int] = pla.Field(ge=0, nullable=True, )
    """
    Numeric component identifier extracted from the FIX Latest "Global Components" page anchor ID (e.g. "comp1057-1" → 1057). Stable across Extension Packs and shared with the FIX Orchestra repository.
    """
    
    gc_referenced_in: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('PRE_TRADE','TRADE','POST_TRADE','INFRASTRUCTURE',)})
    """
    FIX business areas whose messages embed the Global Component.
    """
    
    
class UDFTagRange(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A reserved range of tag numbers for User Defined Fields.
    """

    _id_name : str =  'range_id' 
    range_id: str = pla.Field()
    """
    Identifier of the range.
    """
    
    low_tag: int = pla.Field()
    """
    Inclusive lower bound of the range.
    """
    
    high_tag: Optional[int] = pla.Field(nullable=True, )
    """
    Upper bound of the tag range. Required for all ``usage`` values except ``GTC_RESERVED`` (which is open-ended, 50000+). Downstream validators should enforce this; the constraint cannot be expressed here because LinkML's ``equals_string`` operator only accepts string-ranged slots and ``usage`` is an enum.
    """
    
    usage: Enum = pla.Field(dtype_kwargs={"categories":('INTER_FIRM_REGISTERED','INTER_FIRM_BILATERAL','GTC_REGULATORY_LEGACY','WIP_CHINA','INTERNAL_FIRM','GTC_OTC_DERIVATIVES','GTC_RESERVED',)})
    """
    Usage policy assigned to the range.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Notes on the range's intended use.
    """
    
    requires_registration: Optional[bool] = pla.Field(nullable=True, )
    """
    True when tags in the range must be registered.
    """
    
    
class FIXIntroduction(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Container for the structural elements of the FIX Latest Introduction section. Tree root for instance data.
    """

    _id_name : str = None
    published_version: Optional[str] = pla.Field(nullable=True, )
    """
    Version stamp from the document header.
    """
    
    published_date: Optional[Date] = pla.Field(nullable=True, )
    """
    Publication date of the document.
    """
    
    publisher: Optional[str] = pla.Field(nullable=True, )
    """
    Publishing body of the FIX Latest specification.
    """
    
    preface: Optional[str] = pla.Field(nullable=True, )
    """
    The Preface text of the specification.
    """
    
    introduction_text: Optional[str] = pla.Field(nullable=True, )
    """
    The Introduction prose section.
    """
    
    utc_leap_seconds_note: Optional[str] = pla.Field(nullable=True, )
    """
    Prose note on UTC leap-second handling for UTCTimestamp.
    """
    
    about_fpl: Optional[Struct] = pla.Field(nullable=True, )
    """
    Information about FIX Protocol Limited.
    """
    
    standards: Optional[List] = pla.Field(nullable=True, )
    """
    The FIX Family of Standards.
    """
    
    extension_packs: Optional[List] = pla.Field(nullable=True, )
    """
    The list of Extension Packs.
    """
    
    datatypes: Optional[List] = pla.Field(nullable=True, )
    """
    FIX Protocol datatype definitions and value spaces.
    """
    
    business_areas: Optional[List] = pla.Field(nullable=True, )
    """
    Top-level business areas of FIX Latest.
    """
    
    global_components: Optional[List] = pla.Field(nullable=True, )
    """
    Global Components defined in the Introduction.
    """
    
    udf_ranges: Optional[List] = pla.Field(nullable=True, )
    """
    Reserved ranges of user-defined-field tag numbers.
    """
    
    product_coverage: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('EQUITIES','CIV','DERIVATIVES','FIXED_INCOME','FOREIGN_EXCHANGE',)})
    """
    Product/asset classes covered by FIX at the application layer.
    """
    
    
    @pla.check("about_fpl")
    def check_nested_struct_about_fpl(cls, data: PolarsData):
        
        return cls._check_nested_struct(data, FIXProtocolLimited, pa_pl.FIXProtocolLimited)
        
    @pla.check("standards")
    def check_nested_struct_standards(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, FIXFamilyStandard, pa_pl.FIXFamilyStandardDict)
        
    @pla.check("extension_packs")
    def check_nested_struct_extension_packs(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ExtensionPack, pa_pl.ExtensionPackDict)
        
    @pla.check("datatypes")
    def check_nested_struct_datatypes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, FIXDatatype, pa_pl.FIXDatatypeDict)
        
    @pla.check("business_areas")
    def check_nested_struct_business_areas(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, BusinessArea, pa_pl.BusinessAreaDict)
        
    @pla.check("global_components")
    def check_nested_struct_global_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, GlobalComponent, pa_pl.GlobalComponentDict)
        
    @pla.check("udf_ranges")
    def check_nested_struct_udf_ranges(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, UDFTagRange, pa_pl.UDFTagRangeDict)
        
class CommonComponent(Component):
    """
    A component used only by messages within a single business area.
    """

    _id_name : str =  'component_name' 
    business_area: Enum = pla.Field(dtype_kwargs={"categories":('INTRODUCTION','PRE_TRADE','TRADE','POST_TRADE','INFRASTRUCTURE',)})
    """
    Business area the element belongs to.
    """
    
    
class SpecificComponent(Component):
    """
    A component used only by messages within a single category.
    """

    _id_name : str =  'component_name' 
    business_area: Enum = pla.Field(dtype_kwargs={"categories":('INTRODUCTION','PRE_TRADE','TRADE','POST_TRADE','INFRASTRUCTURE',)})
    """
    Business area the element belongs to.
    """
    
    category: Enum = pla.Field(dtype_kwargs={"categories":('INDICATION','EVENT_COMMUNICATION','QUOTATION_NEGOTIATION','MARKET_DATA','MARKET_STRUCTURE_REFERENCE_DATA','SECURITIES_REFERENCE_DATA','PARTIES_REFERENCE_DATA','PARTIES_ACTION','SINGLE_GENERAL_ORDER_HANDLING','ORDER_MASS_HANDLING','CROSS_ORDERS','MULTILEG_ORDERS','LIST_PROGRAM_BASKET_TRADING','ALLOCATION_AND_READY_TO_BOOK','CONFIRMATION','SETTLEMENT_INSTRUCTIONS','TRADE_CAPTURE_REPORTING','REGISTRATION_INSTRUCTIONS','POSITIONS_MAINTENANCE','COLLATERAL_MANAGEMENT','MARGIN_REQUIREMENT_MANAGEMENT','ACCOUNT_REPORTING','TRADE_MANAGEMENT','PAY_MANAGEMENT','SETTLEMENT_STATUS_MANAGEMENT','BUSINESS_MESSAGE_REJECTS','NETWORK_STATUS_COMMUNICATION','USER_MANAGEMENT','APPLICATION_SEQUENCING',)})
    """
    Message category.
    """
    
    
class PreTradeMessageEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the area-wide pre-trade messages table.
    """

    _id_name : str =  'msg_type' 
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    category: Enum = pla.Field(dtype_kwargs={"categories":('INDICATION','EVENT_COMMUNICATION','QUOTATION_NEGOTIATION','MARKET_DATA','MARKET_STRUCTURE_REFERENCE_DATA','SECURITIES_REFERENCE_DATA','PARTIES_REFERENCE_DATA','PARTIES_ACTION',)})
    """
    Message category.
    """
    
    
class PreTradeComponentEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the area-wide pre-trade components table.
    """

    _id_name : str =  'component_name' 
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    repetition: Enum = pla.Field(dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    category: str = pla.Field()
    """
    Category the component is listed under. Common Components are listed under the synthetic "Common Components" value.
    """
    
    is_common: Optional[bool] = pla.Field(nullable=True, )
    """
    True when the component is declared as a Common Component.
    """
    
    footnote_number: Optional[int] = pla.Field(ge=1, le=25, nullable=True, )
    """
    Footnote indicator on a component-table row.
    """
    
    
class PreTradeLayoutRow(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the layout table published in the Pre-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """

    _id_name : str = None
    pre_layout_kind: Enum = pla.Field(dtype_kwargs={"categories":('FIELD','COMPONENT',)})
    """
    Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table).
    """
    
    pre_layout_field_tag: Optional[int] = pla.Field(ge=0, nullable=True, )
    """
    FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.
    """
    
    pre_layout_element_name: str = pla.Field()
    """
    Element name as printed in the Name column — either the FIX field name or the component name.
    """
    
    pre_layout_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the field or component is required, as printed in the Req’d column of the source layout table ("Y" / "N").
    """
    
    pre_layout_description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text content of the Description column of the row (may be empty).
    """
    
    pre_layout_nested: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table).
    """
    
    
class CommonComponentDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-common-component description.
    """

    _id_name : str =  'component_name' 
    component_name: Enum = pla.Field(dtype_kwargs={"categories":('AuctionTypeRuleGrp','BaseTradingRules','ExecInstRules','InstrumentScope','InstrumentScopeGrp','InstrumentScopeSecurityAltIDGrp','LotTypeRules','MarketDataFeedTypes','MarketSegmentScopeGrp','MatchRules','OrdTypeRules','PriceLimits','PriceRangeRuleGrp','QuoteSizeRuleGrp','RequestedPartyRoleGrp','RequestingPartyGrp','RequestingPartySubGrp','RoutingGrp','TickRules','TimeInForceRules','TradingSessionRules',)})
    """
    PascalCase name of the component.
    """
    
    repetition: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the common component's purpose.
    """
    
    layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout.
    """
    
    pre_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Pre-Trade Appendix.
    """
    
    
    @pla.check("pre_layout_rows")
    def check_nested_struct_pre_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PreTradeLayoutRow, pa_pl.PreTradeLayoutRowDict)
        
class ComponentTableFootnote(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A footnote on the area-wide components table.
    """

    _id_name : str =  'footnote_number' 
    footnote_number: int = pla.Field(ge=1, le=25, )
    """
    Footnote indicator on a component-table row.
    """
    
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    introduced_in: str = pla.Field()
    """
    FIX version or Extension Pack that introduced the component.
    """
    
    sole_category: Enum = pla.Field(dtype_kwargs={"categories":('INDICATION','EVENT_COMMUNICATION','QUOTATION_NEGOTIATION','MARKET_DATA','MARKET_STRUCTURE_REFERENCE_DATA','SECURITIES_REFERENCE_DATA','PARTIES_REFERENCE_DATA','PARTIES_ACTION',)})
    """
    Single category that actually uses the component.
    """
    
    text: Optional[str] = pla.Field(nullable=True, )
    """
    Footnote text.
    """
    
    
class PreTradeMessageDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-category message description.
    """

    _id_name : str =  'msg_type' 
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the message's purpose and usage.
    """
    
    layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout.
    """
    
    pre_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Pre-Trade Appendix.
    """
    
    
    @pla.check("pre_layout_rows")
    def check_nested_struct_pre_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PreTradeLayoutRow, pa_pl.PreTradeLayoutRowDict)
        
class MessageGroup(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Purpose-grouped sub-section inside a category's Messages section.
    """

    _id_name : str =  'group_title' 
    group_title: str = pla.Field()
    """
    Purpose-group heading inside a category's Messages sub-section.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the purpose-group's role within the category.
    """
    
    messages: List = pla.Field()
    """
    Messages bundled under the purpose-group heading.
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PreTradeMessageDetail, pa_pl.PreTradeMessageDetailDict)
        
class PreTradeComponentDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-category component description.
    """

    _id_name : str =  'component_name' 
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    repetition: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the component's purpose.
    """
    
    layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout.
    """
    
    pre_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Pre-Trade Appendix.
    """
    
    
    @pla.check("pre_layout_rows")
    def check_nested_struct_pre_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PreTradeLayoutRow, pa_pl.PreTradeLayoutRowDict)
        
class PreTradeCategorySection(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A per-category sub-section of the Pre-Trade chapter.
    """

    _id_name : str =  'category' 
    category: Enum = pla.Field(dtype_kwargs={"categories":('INDICATION','EVENT_COMMUNICATION','QUOTATION_NEGOTIATION','MARKET_DATA','MARKET_STRUCTURE_REFERENCE_DATA','SECURITIES_REFERENCE_DATA','PARTIES_REFERENCE_DATA','PARTIES_ACTION',)})
    """
    Message category.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    quote_models: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('INDICATIVE','TRADEABLE','RESTRICTED_TRADEABLE','NEGOTIATION',)})
    """
    Quoting business models referenced in the Quotation / Negotiation category.
    """
    
    message_groups: Optional[List] = pla.Field(nullable=True, )
    """
    Purpose-grouped message descriptions inside a category.
    """
    
    messages: Optional[List] = pla.Field(nullable=True, )
    """
    Messages defined in this category.
    """
    
    category_components_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of a category's Components sub-section.
    """
    
    category_specific_components: Optional[List] = pla.Field(nullable=True, )
    """
    Components used exclusively by messages within a category.
    """
    
    
    @pla.check("message_groups")
    def check_nested_struct_message_groups(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, MessageGroup, pa_pl.MessageGroupDict)
        
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PreTradeMessageDetail, pa_pl.PreTradeMessageDetailDict)
        
    @pla.check("category_specific_components")
    def check_nested_struct_category_specific_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PreTradeComponentDetail, pa_pl.PreTradeComponentDetailDict)
        
class PreTradeBusinessArea(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Tree-root container for the Pre-Trade business area of FIX Latest.
    """

    _id_name : str = None
    area: Enum = pla.Field(dtype_kwargs={"categories":('INTRODUCTION','PRE_TRADE','TRADE','POST_TRADE','INFRASTRUCTURE',)})
    """
    Identity of the business area.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title.
    """
    
    published_version: Optional[str] = pla.Field(nullable=True, )
    """
    Version stamp from the document header.
    """
    
    publisher: Optional[str] = pla.Field(nullable=True, )
    """
    Publishing body of the FIX Latest specification.
    """
    
    introduction: Optional[str] = pla.Field(nullable=True, )
    """
    Prose introduction of the chapter.
    """
    
    diagram_conventions: Optional[str] = pla.Field(nullable=True, )
    """
    Sentence describing diagram conventions used in the chapter.
    """
    
    messages_overview_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of the area-wide Messages sub-section.
    """
    
    messages: Optional[List] = pla.Field(nullable=True, )
    """
    Area-wide pre-trade messages table.
    """
    
    components_overview_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of the area-wide Components sub-section.
    """
    
    components: Optional[List] = pla.Field(nullable=True, )
    """
    Area-wide pre-trade components table.
    """
    
    common_components: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('AuctionTypeRuleGrp','BaseTradingRules','ExecInstRules','InstrumentScope','InstrumentScopeGrp','InstrumentScopeSecurityAltIDGrp','LotTypeRules','MarketDataFeedTypes','MarketSegmentScopeGrp','MatchRules','OrdTypeRules','PriceLimits','PriceRangeRuleGrp','QuoteSizeRuleGrp','RequestedPartyRoleGrp','RequestingPartyGrp','RequestingPartySubGrp','RoutingGrp','TickRules','TimeInForceRules','TradingSessionRules',)})
    """
    Common Components declared at the top of the chapter.
    """
    
    common_component_details: Optional[List] = pla.Field(nullable=True, )
    """
    Per-common-component descriptions from the chapter's final section.
    """
    
    footnotes: Optional[List] = pla.Field(nullable=True, )
    """
    Footnotes attached to the area-wide components table.
    """
    
    category_sections: Optional[List] = pla.Field(nullable=True, )
    """
    Per-category sub-sections of the chapter.
    """
    
    referenced_global_components: Optional[List] = pla.Field(nullable=True, )
    """
    Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PreTradeMessageEntry, pa_pl.PreTradeMessageEntryDict)
        
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PreTradeComponentEntry, pa_pl.PreTradeComponentEntryDict)
        
    @pla.check("common_component_details")
    def check_nested_struct_common_component_details(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, CommonComponentDetail, pa_pl.CommonComponentDetailDict)
        
    @pla.check("footnotes")
    def check_nested_struct_footnotes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ComponentTableFootnote, pa_pl.ComponentTableFootnoteDict)
        
    @pla.check("category_sections")
    def check_nested_struct_category_sections(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PreTradeCategorySection, pa_pl.PreTradeCategorySectionDict)
        
class TradeMessageEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the area-wide trade messages table.
    """

    _id_name : str =  'msg_type' 
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    category: Enum = pla.Field(dtype_kwargs={"categories":('SINGLE_GENERAL_ORDER_HANDLING','ORDER_MASS_HANDLING','CROSS_ORDER_HANDLING','MULTILEG_ORDER_HANDLING','LIST_PROGRAM_BASKET_TRADING',)})
    """
    Message category.
    """
    
    
class TradeComponentEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the area-wide trade components table.
    """

    _id_name : str =  'component_name' 
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    trade_repetition: Enum = pla.Field(dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    category: str = pla.Field()
    """
    Category the component is listed under. Common Components are listed under the synthetic "Common Components" value.
    """
    
    trade_is_common: Optional[bool] = pla.Field(nullable=True, )
    """
    True when the component is declared as a Common Component.
    """
    
    trade_footnote_number: Optional[int] = pla.Field(ge=1, le=25, nullable=True, )
    """
    Footnote indicator on a component-table row.
    """
    
    
class TradeLayoutRow(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the layout table published in the Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """

    _id_name : str = None
    trade_layout_kind: Enum = pla.Field(dtype_kwargs={"categories":('FIELD','COMPONENT',)})
    """
    Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table).
    """
    
    trade_layout_field_tag: Optional[int] = pla.Field(ge=0, nullable=True, )
    """
    FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.
    """
    
    trade_layout_element_name: str = pla.Field()
    """
    Element name as printed in the Name column — either the FIX field name or the component name.
    """
    
    trade_layout_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the field or component is required, as printed in the Req'd column of the source layout table ("Y" / "N").
    """
    
    trade_layout_description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text content of the Description column of the row (may be empty).
    """
    
    trade_layout_nested: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table).
    """
    
    
class TradeCommonComponentDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-common-component description from the chapter's final "Common Components" section.
    """

    _id_name : str =  'component_name' 
    component_name: Enum = pla.Field(dtype_kwargs={"categories":('DisclosureInstructionGrp','DiscretionInstructions','PegInstructions','PreAllocGrp','StrategyParametersGrp','TriggeringInstruction',)})
    """
    PascalCase name of the component.
    """
    
    trade_repetition: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the common component's purpose.
    """
    
    trade_layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout in the Trade Appendix.
    """
    
    trade_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Trade Appendix.
    """
    
    
    @pla.check("trade_layout_rows")
    def check_nested_struct_trade_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeLayoutRow, pa_pl.TradeLayoutRowDict)
        
class TradeComponentTableFootnote(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A footnote on the area-wide components table.
    """

    _id_name : str =  'trade_footnote_number' 
    trade_footnote_number: int = pla.Field(ge=1, le=25, )
    """
    Footnote indicator on a component-table row.
    """
    
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    trade_introduced_in: str = pla.Field()
    """
    FIX version or Extension Pack that introduced the component.
    """
    
    trade_sole_category: Enum = pla.Field(dtype_kwargs={"categories":('SINGLE_GENERAL_ORDER_HANDLING','ORDER_MASS_HANDLING','CROSS_ORDER_HANDLING','MULTILEG_ORDER_HANDLING','LIST_PROGRAM_BASKET_TRADING',)})
    """
    Single category that actually uses the component.
    """
    
    trade_footnote_text: Optional[str] = pla.Field(nullable=True, )
    """
    Footnote text.
    """
    
    
class TradeMessageDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-category message description.
    """

    _id_name : str =  'msg_type' 
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the message's purpose and usage.
    """
    
    trade_layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout in the Trade Appendix.
    """
    
    trade_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Trade Appendix.
    """
    
    
    @pla.check("trade_layout_rows")
    def check_nested_struct_trade_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeLayoutRow, pa_pl.TradeLayoutRowDict)
        
class TradeOrdStatusPrecedenceEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the OrdStatus(39) precedence table published in the Execution Reports purpose-group of the Single/General Order Handling category. Defines the precedence ranking used to resolve simultaneous state transitions on an order, paired with the human-readable OrdStatus label and its descriptive prose.
    """

    _id_name : str =  'trade_ord_status_label' 
    trade_ord_status_precedence: int = pla.Field(ge=1, le=11, )
    """
    Precedence rank (1 = lowest, higher numbers take precedence) of an OrdStatus(39) value used to resolve simultaneous state transitions on an order.
    """
    
    trade_ord_status_label: str = pla.Field()
    """
    Human-readable OrdStatus(39) label as printed in the Execution Reports precedence table (e.g. "Pending Cancel", "Done for Day", "Filled").
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Verbatim OrdStatus description from the table.
    """
    
    
class TradeMessageGroup(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Purpose-grouped sub-section inside a category's Messages sub-section (e.g. "New Order Single", "Execution Reports", "Order Cancel Requests" under Single/General Order Handling).
    """

    _id_name : str =  'trade_group_title' 
    trade_group_title: str = pla.Field()
    """
    Purpose-group heading inside a category's Messages sub-section.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the purpose-group's role within the category.
    """
    
    messages: List = pla.Field()
    """
    Messages bundled under the purpose-group heading.
    """
    
    trade_ord_status_precedence_entries: Optional[List] = pla.Field(nullable=True, )
    """
    Rows of the OrdStatus(39) precedence table that appears inside the Execution Reports purpose-group of the Single/General Order Handling category.
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeMessageDetail, pa_pl.TradeMessageDetailDict)
        
    @pla.check("trade_ord_status_precedence_entries")
    def check_nested_struct_trade_ord_status_precedence_entries(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeOrdStatusPrecedenceEntry, pa_pl.TradeOrdStatusPrecedenceEntryDict)
        
class TradeComponentDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-category component description.
    """

    _id_name : str =  'component_name' 
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    trade_repetition: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Description of the component's purpose.
    """
    
    trade_layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout in the Trade Appendix.
    """
    
    trade_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Trade Appendix.
    """
    
    
    @pla.check("trade_layout_rows")
    def check_nested_struct_trade_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeLayoutRow, pa_pl.TradeLayoutRowDict)
        
class TradeFragmentationEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of a fragmentation table published in a Trade category (currently only List/Program/Basket Trading) identifying a message that may be fragmented, the "Total Entries" field used to indicate the total count across all fragments of the batch, and the verbatim description of the repeating group that may be fragmented.
    """

    _id_name : str =  'trade_fragmentation_message' 
    trade_fragmentation_message: str = pla.Field()
    """
    Message that may be fragmented — verbatim text from the Message column of the fragmentation table (e.g. "NewOrderList(35=E)").
    """
    
    trade_fragmentation_total_entries_field: str = pla.Field()
    """
    Name and tag of the "Total Entries" field used to indicate the total count across all fragments of the batch (e.g. "TotNoOrders(68)").
    """
    
    trade_fragmentation_repeating_group: str = pla.Field()
    """
    Verbatim description of the repeating group that may be fragmented — from the table's third column.
    """
    
    
class TradeCategorySection(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A per-category sub-section of the Trade chapter.
    """

    _id_name : str =  'category' 
    category: Enum = pla.Field(dtype_kwargs={"categories":('SINGLE_GENERAL_ORDER_HANDLING','ORDER_MASS_HANDLING','CROSS_ORDER_HANDLING','MULTILEG_ORDER_HANDLING','LIST_PROGRAM_BASKET_TRADING',)})
    """
    Message category.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    trade_category_background: Optional[str] = pla.Field(nullable=True, )
    """
    Optional "Background" prose preceding a category's message descriptions (e.g. the Cross Order Handling chapter's cross-trade overview).
    """
    
    trade_message_groups: Optional[List] = pla.Field(nullable=True, )
    """
    Purpose-grouped message descriptions inside a category.
    """
    
    messages: Optional[List] = pla.Field(nullable=True, )
    """
    Messages defined in this category.
    """
    
    trade_category_components_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of a category's Components sub-section.
    """
    
    trade_category_specific_components: Optional[List] = pla.Field(nullable=True, )
    """
    Components used exclusively by messages within a single category.
    """
    
    trade_fragmentation_entries: Optional[List] = pla.Field(nullable=True, )
    """
    Rows of the fragmentation table listed in a Trade category that documents which messages may be fragmented and which repeating group is fragmentable (currently published only for List/Program/Basket Trading).
    """
    
    
    @pla.check("trade_message_groups")
    def check_nested_struct_trade_message_groups(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeMessageGroup, pa_pl.TradeMessageGroupDict)
        
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeMessageDetail, pa_pl.TradeMessageDetailDict)
        
    @pla.check("trade_category_specific_components")
    def check_nested_struct_trade_category_specific_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeComponentDetail, pa_pl.TradeComponentDetailDict)
        
    @pla.check("trade_fragmentation_entries")
    def check_nested_struct_trade_fragmentation_entries(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeFragmentationEntry, pa_pl.TradeFragmentationEntryDict)
        
class TradeBusinessArea(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Tree-root container for the Trade (Orders and Executions) business area of FIX Latest.
    """

    _id_name : str = None
    trade_area: Enum = pla.Field(dtype_kwargs={"categories":('INTRODUCTION','PRE_TRADE','TRADE','POST_TRADE','INFRASTRUCTURE',)})
    """
    Identity of the business area the chapter describes.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title.
    """
    
    published_version: Optional[str] = pla.Field(nullable=True, )
    """
    Version stamp from the document header.
    """
    
    publisher: Optional[str] = pla.Field(nullable=True, )
    """
    Publishing body of the FIX Latest specification.
    """
    
    trade_introduction: Optional[str] = pla.Field(nullable=True, )
    """
    Prose introduction of the chapter.
    """
    
    trade_diagram_conventions: Optional[str] = pla.Field(nullable=True, )
    """
    Sentence describing diagram conventions used in the chapter.
    """
    
    trade_message_diagram_template_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the "Message Diagram Templates" page referenced by the chapter introduction.
    """
    
    trade_messages_overview_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of the area-wide Messages sub-section.
    """
    
    messages: Optional[List] = pla.Field(nullable=True, )
    """
    Area-wide trade messages table.
    """
    
    trade_components_overview_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of the area-wide Components sub-section.
    """
    
    components: Optional[List] = pla.Field(nullable=True, )
    """
    Area-wide trade components table.
    """
    
    trade_common_components: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('DisclosureInstructionGrp','DiscretionInstructions','PegInstructions','PreAllocGrp','StrategyParametersGrp','TriggeringInstruction',)})
    """
    Common Components declared at the bottom of the chapter.
    """
    
    trade_common_component_details: Optional[List] = pla.Field(nullable=True, )
    """
    Per-common-component descriptions from the chapter's final section.
    """
    
    trade_footnotes: Optional[List] = pla.Field(nullable=True, )
    """
    Footnotes attached to the area-wide components table.
    """
    
    trade_category_sections: Optional[List] = pla.Field(nullable=True, )
    """
    Per-category sub-sections of the chapter.
    """
    
    referenced_global_components: Optional[List] = pla.Field(nullable=True, )
    """
    Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeMessageEntry, pa_pl.TradeMessageEntryDict)
        
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeComponentEntry, pa_pl.TradeComponentEntryDict)
        
    @pla.check("trade_common_component_details")
    def check_nested_struct_trade_common_component_details(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeCommonComponentDetail, pa_pl.TradeCommonComponentDetailDict)
        
    @pla.check("trade_footnotes")
    def check_nested_struct_trade_footnotes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeComponentTableFootnote, pa_pl.TradeComponentTableFootnoteDict)
        
    @pla.check("trade_category_sections")
    def check_nested_struct_trade_category_sections(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeCategorySection, pa_pl.TradeCategorySectionDict)
        
class TradeAppendixSection(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One "Appendix – <X> Category" sub-section of the Trade Appendix. Bundles the per-message layout tables (TradeMessageDetail) and per-component layout tables (TradeComponentDetail) for messages and components that belong to one Trade category — or, for the synthetic "Common" section, the layouts of the chapter's common components.
    """

    _id_name : str =  'trade_appendix_category' 
    trade_appendix_category: str = pla.Field()
    """
    Identifier for an appendix section — either the Trade category name as printed in the heading (e.g. "CrossOrders", "MultilegOrders", "OrderMassHandling", "ProgramTrading", "SingleGeneralOrderHandling") or the literal "Common" for the common-components appendix.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Section heading exactly as printed in the Trade Appendix (e.g. "Appendix – CrossOrders Category").
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    messages: Optional[List] = pla.Field(nullable=True, )
    """
    Layout tables for the messages that belong to the appendix section. Empty for the "Common" section.
    """
    
    components: Optional[List] = pla.Field(nullable=True, )
    """
    Layout tables for the components that belong to the appendix section.
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeMessageDetail, pa_pl.TradeMessageDetailDict)
        
class TradeAppendix(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Tree-root container for the Trade Appendix — the spec companion document that publishes the full message- and component-layout tables for every message and component used in the Trade business area, organized into one "Appendix – <X> Category" sub-section per Trade category plus a final "Appendix – Common Category" sub-section covering the layouts of the chapter's common components.
    """

    _id_name : str = None
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title.
    """
    
    published_version: Optional[str] = pla.Field(nullable=True, )
    """
    Version stamp from the document header.
    """
    
    publisher: Optional[str] = pla.Field(nullable=True, )
    """
    Publishing body of the FIX Latest specification.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Optional preface prose for the Trade Appendix as a whole.
    """
    
    trade_appendix_sections: Optional[List] = pla.Field(nullable=True, )
    """
    Per-category sub-sections of the Trade Appendix — one "Appendix – <X> Category" section per Trade category, plus a synthetic "Common Category" section that lists layouts of the chapter's common components.
    """
    
    
    @pla.check("trade_appendix_sections")
    def check_nested_struct_trade_appendix_sections(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeAppendixSection, pa_pl.TradeAppendixSectionDict)
        
class PostTradeMessageEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the area-wide "Messages for Post-Trade Business Area" table.
    """

    _id_name : str =  'msg_type' 
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    category: Enum = pla.Field(dtype_kwargs={"categories":('ALLOCATION','CONFIRMATION','SETTLEMENT_INSTRUCTION','TRADE_CAPTURE_REPORTING','REGISTRATION_INSTRUCTION','POSITION_MAINTENANCE','COLLATERAL_MANAGEMENT','MARGIN_REQUIREMENT_MANAGEMENT','ACCOUNT_REPORTING','TRADE_MANAGEMENT','PAY_MANAGEMENT','SETTLEMENT_STATUS_MANAGEMENT',)})
    """
    Message category.
    """
    
    
class PostTradeComponentEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the area-wide "Components for Post-Trade Business Area" table.
    """

    _id_name : str =  'component_name' 
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    repetition: Enum = pla.Field(dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    category: str = pla.Field()
    """
    Category label as printed in the component table; the token "Common Components" is allowed in addition to the PostTradeCategoryEnum values.
    """
    
    is_common: Optional[bool] = pla.Field(nullable=True, )
    """
    True when the component is declared as a Common Component.
    """
    
    footnote_number: Optional[int] = pla.Field(ge=1, le=25, nullable=True, )
    """
    Footnote indicator on a component-table row.
    """
    
    
class PostTradeComponentTableFootnote(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A footnote attached to a row of the area-wide Post-Trade components table.
    """

    _id_name : str =  'footnote_number' 
    footnote_number: int = pla.Field(ge=1, le=25, )
    """
    Footnote indicator on a component-table row.
    """
    
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    introduced_in: str = pla.Field()
    """
    FIX version or Extension Pack that introduced the component.
    """
    
    post_sole_category: Enum = pla.Field(dtype_kwargs={"categories":('ALLOCATION','CONFIRMATION','SETTLEMENT_INSTRUCTION','TRADE_CAPTURE_REPORTING','REGISTRATION_INSTRUCTION','POSITION_MAINTENANCE','COLLATERAL_MANAGEMENT','MARGIN_REQUIREMENT_MANAGEMENT','ACCOUNT_REPORTING','TRADE_MANAGEMENT','PAY_MANAGEMENT','SETTLEMENT_STATUS_MANAGEMENT',)})
    """
    Single Post-Trade category that actually uses the component (per footnote).
    """
    
    text: Optional[str] = pla.Field(nullable=True, )
    """
    Footnote text.
    """
    
    
class PostTradeLayoutRow(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the layout table published in the Post-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """

    _id_name : str = None
    post_layout_kind: Enum = pla.Field(dtype_kwargs={"categories":('FIELD','COMPONENT',)})
    """
    Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table).
    """
    
    post_layout_field_tag: Optional[int] = pla.Field(ge=0, nullable=True, )
    """
    FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.
    """
    
    post_layout_element_name: str = pla.Field()
    """
    Element name as printed in the Name column — either the FIX field name or the component name.
    """
    
    post_layout_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the field or component is required, as printed in the Req’d column of the source layout table ("Y" / "N").
    """
    
    post_layout_description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text content of the Description column of the row (may be empty).
    """
    
    post_layout_nested: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table).
    """
    
    
class PostTradeMessageDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-message description block from a Post-Trade category section.
    """

    _id_name : str =  'msg_type' 
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout.
    """
    
    post_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Post-Trade Appendix.
    """
    
    
    @pla.check("post_layout_rows")
    def check_nested_struct_post_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeLayoutRow, pa_pl.PostTradeLayoutRowDict)
        
class PostTradeMessageGroup(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A purpose-themed grouping of messages within a Post-Trade category (e.g. "Allocation Instructions").
    """

    _id_name : str =  'group_title' 
    group_title: str = pla.Field()
    """
    Purpose-group heading inside a category's Messages sub-section.
    """
    
    messages: List = pla.Field()
    """
    Messages defined within the enclosing element.
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeMessageDetail, pa_pl.PostTradeMessageDetailDict)
        
class PostTradeComponentDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-component description block from a Post-Trade category section's Components sub-section.
    """

    _id_name : str =  'component_name' 
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    repetition: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout.
    """
    
    post_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Post-Trade Appendix.
    """
    
    
    @pla.check("post_layout_rows")
    def check_nested_struct_post_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeLayoutRow, pa_pl.PostTradeLayoutRowDict)
        
class AllocationStatusDescription(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the AllocStatus(87) value/description table.
    """

    _id_name : str =  'status_code' 
    status_code: str = pla.Field()
    """
    Wire status code as referenced in the chapter.
    """
    
    status_label: str = pla.Field()
    """
    Human-readable label of the status code.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    
class AllocationFragmentationFieldMap(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the table mapping an allocation message to its fragmentation-related fields.
    """

    _id_name : str =  'msg_type' 
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    total_count_field: str = pla.Field()
    """
    Field carrying the total number of repeating-group entries across all fragments (e.g. TotNoAllocs).
    """
    
    fragment_count_field: str = pla.Field()
    """
    Field carrying the number of entries in the current message fragment (e.g. NoAllocs).
    """
    
    principal_message_reference: str = pla.Field()
    """
    Principal message reference field used to bind allocation message fragments together (e.g. AllocID, AllocReportID).
    """
    
    
class TradeCaptureReportUsage(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One documented usage of the TradeCaptureReport(35=AE) message.
    """

    _id_name : str =  'status_label' 
    status_label: str = pla.Field()
    """
    Short label for the usage.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    identifier_role: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('TRADE_REPORT_ID','TRADE_ID','TRADE_REPORT_REF_ID','SECONDARY_TRADE_ID',)})
    """
    Role of the trade-capture-report identifier field.
    """
    
    
class TradeCaptureReportIdentifierRule(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A rule governing one of the TradeCaptureReport(35=AE) identifier fields.
    """

    _id_name : str =  'identifier_role' 
    identifier_role: Enum = pla.Field(dtype_kwargs={"categories":('TRADE_REPORT_ID','TRADE_ID','TRADE_REPORT_REF_ID','SECONDARY_TRADE_ID',)})
    """
    Role of the trade-capture-report identifier field.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    
class RegistrationStatusDescription(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the RegistStatus(506) value/description table.
    """

    _id_name : str =  'status_code' 
    status_code: str = pla.Field()
    """
    Wire status code as referenced in the chapter.
    """
    
    status_label: str = pla.Field()
    """
    Human-readable label of the status code.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    
class ClearingServicePostTradeProcessingFormat(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One message-format row from the Post-Trade Processing Clearing Services section, with its supported actions.
    """

    _id_name : str =  'message_format' 
    message_format: Enum = pla.Field(dtype_kwargs={"categories":('ETP','GIVE_UP','EXCHANGE_FOR_PHYSICAL','AVERAGE_PRICE_SYSTEM','MUTUAL_OFFSET_SYSTEM','TRADE_ENTRY_EDIT',)})
    """
    Clearing-service message format family referenced in the chapter.
    """
    
    supported_actions: str = pla.Field()
    """
    Action labels (e.g. Allocation, Accept, Reject, Release, Change, Delete) supported by a clearing-service message format.
    """
    
    
class PostTradeCategorySection(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A "Category – <name>" sub-section of the Post-Trade chapter.
    """

    _id_name : str =  'category' 
    category: Enum = pla.Field(dtype_kwargs={"categories":('ALLOCATION','CONFIRMATION','SETTLEMENT_INSTRUCTION','TRADE_CAPTURE_REPORTING','REGISTRATION_INSTRUCTION','POSITION_MAINTENANCE','COLLATERAL_MANAGEMENT','MARGIN_REQUIREMENT_MANAGEMENT','ACCOUNT_REPORTING','TRADE_MANAGEMENT','PAY_MANAGEMENT','SETTLEMENT_STATUS_MANAGEMENT',)})
    """
    Message category.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    category_components_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of a category's Components sub-section.
    """
    
    post_message_groups: Optional[List] = pla.Field(nullable=True, )
    """
    Purpose-grouped message descriptions inside a Post-Trade category.
    """
    
    messages: Optional[List] = pla.Field(nullable=True, )
    """
    Messages defined within the enclosing element.
    """
    
    post_category_specific_components: Optional[List] = pla.Field(nullable=True, )
    """
    Components used exclusively by messages within a category.
    """
    
    allocation_scenarios: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('PRE_ALLOCATED_ORDER','PRE_TRADE_ALLOCATION','POST_TRADE_ALLOCATION','READY_TO_BOOK',)})
    """
    Communication options supported by the Allocation category for conveying allocation instructions.
    """
    
    allocation_roles: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('INITIATOR','RESPONDENT',)})
    """
    Role labels used throughout the Allocation category prose.
    """
    
    post_trade_allocation_pricing_methods: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('AVERAGE_PRICE','EXECUTED_PRICE',)})
    """
    Methods supported for computing post-trade allocations.
    """
    
    allocation_status_descriptions: Optional[List] = pla.Field(nullable=True, )
    """
    Descriptions tied to AllocStatus(87) values as listed in the Allocation Instruction Acknowledgements section.
    """
    
    fragmentation_field_map: Optional[List] = pla.Field(nullable=True, )
    """
    Per-message mapping of fragmentation-related fields used by the Allocation messages.
    """
    
    trade_capture_report_usages: Optional[List] = pla.Field(nullable=True, )
    """
    Usages described in the "Trade Capture Report Usages" sub-section of the Trade Capture Reporting category.
    """
    
    trade_capture_report_identifier_rules: Optional[List] = pla.Field(nullable=True, )
    """
    Rules governing TradeCaptureReport(35=AE) identifier fields.
    """
    
    registration_status_descriptions: Optional[List] = pla.Field(nullable=True, )
    """
    Descriptions tied to RegistStatus(506) values.
    """
    
    clearing_services_for_position_management: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('POSITION_CHANGE_SUBMISSION','POSITION_ADJUSTMENT','EXERCISE_NOTICE','ABANDONMENT_NOTICE','MARGIN_DISPOSITION','POSITION_PLEDGE','REQUEST_FOR_POSITION',)})
    """
    Business functions exposed by the Position Management Clearing Services.
    """
    
    clearing_services_for_post_trade_processing: Optional[List] = pla.Field(nullable=True, )
    """
    Per-format action sets exposed by the Post-Trade Processing Clearing Services.
    """
    
    collateral_management_usages: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('SECURITIES_FINANCING_COLLATERALIZATION','CLEARING_HOUSE_COLLATERALIZATION',)})
    """
    Documented usages for the Collateral Management messages.
    """
    
    collateral_assignment_purposes: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('ASSIGN_INITIAL_COLLATERAL','REPLENISH_COLLATERAL','REPLACE_OR_SUBSTITUTE_COLLATERAL',)})
    """
    Documented purposes for the CollateralAssignment(35=AY) message.
    """
    
    
    @pla.check("post_message_groups")
    def check_nested_struct_post_message_groups(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeMessageGroup, pa_pl.PostTradeMessageGroupDict)
        
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeMessageDetail, pa_pl.PostTradeMessageDetailDict)
        
    @pla.check("post_category_specific_components")
    def check_nested_struct_post_category_specific_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeComponentDetail, pa_pl.PostTradeComponentDetailDict)
        
    @pla.check("allocation_status_descriptions")
    def check_nested_struct_allocation_status_descriptions(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AllocationStatusDescription, pa_pl.AllocationStatusDescriptionDict)
        
    @pla.check("fragmentation_field_map")
    def check_nested_struct_fragmentation_field_map(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, AllocationFragmentationFieldMap, pa_pl.AllocationFragmentationFieldMapDict)
        
    @pla.check("trade_capture_report_usages")
    def check_nested_struct_trade_capture_report_usages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeCaptureReportUsage, pa_pl.TradeCaptureReportUsageDict)
        
    @pla.check("trade_capture_report_identifier_rules")
    def check_nested_struct_trade_capture_report_identifier_rules(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, TradeCaptureReportIdentifierRule, pa_pl.TradeCaptureReportIdentifierRuleDict)
        
    @pla.check("registration_status_descriptions")
    def check_nested_struct_registration_status_descriptions(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, RegistrationStatusDescription, pa_pl.RegistrationStatusDescriptionDict)
        
    @pla.check("clearing_services_for_post_trade_processing")
    def check_nested_struct_clearing_services_for_post_trade_processing(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ClearingServicePostTradeProcessingFormat, pa_pl.ClearingServicePostTradeProcessingFormatDict)
        
class PostTradeCommonComponentDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-common-component description block from the chapter's final "Common Components" section.
    """

    _id_name : str =  'component_name' 
    component_name: Enum = pla.Field(dtype_kwargs={"categories":('AllocCommissionDataGrp','AllocRegulatoryTradeIDGrp','ClrInstGrp','CollateralAmountGrp','CollateralReinvestmentGrp','DlvyInstGrp','ExecAllocGrp','MarginAmount','OrdAllocGrp','PositionAmountData','SettlDetails','SettlInstructionsData','SettlParties','SettlPtysSubGrp','TradeAllocAmtGrp','TransactionAttributeGrp',)})
    """
    PascalCase name of the component.
    """
    
    repetition: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout.
    """
    
    post_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Post-Trade Appendix.
    """
    
    
    @pla.check("post_layout_rows")
    def check_nested_struct_post_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeLayoutRow, pa_pl.PostTradeLayoutRowDict)
        
class PostTradeBusinessArea(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Tree-root container for the Post-Trade business area of FIX Latest.
    """

    _id_name : str = None
    area: Enum = pla.Field(dtype_kwargs={"categories":('INTRODUCTION','PRE_TRADE','TRADE','POST_TRADE','INFRASTRUCTURE',)})
    """
    Identity of the business area.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title.
    """
    
    published_version: Optional[str] = pla.Field(nullable=True, )
    """
    Version stamp from the document header.
    """
    
    publisher: Optional[str] = pla.Field(nullable=True, )
    """
    Publishing body of the FIX Latest specification.
    """
    
    post_introduction: Optional[str] = pla.Field(nullable=True, )
    """
    Prose introduction of the Post-Trade chapter.
    """
    
    diagram_conventions: Optional[str] = pla.Field(nullable=True, )
    """
    Sentence describing diagram conventions used in the chapter.
    """
    
    post_common_components: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('AllocCommissionDataGrp','AllocRegulatoryTradeIDGrp','ClrInstGrp','CollateralAmountGrp','CollateralReinvestmentGrp','DlvyInstGrp','ExecAllocGrp','MarginAmount','OrdAllocGrp','PositionAmountData','SettlDetails','SettlInstructionsData','SettlParties','SettlPtysSubGrp','TradeAllocAmtGrp','TransactionAttributeGrp',)})
    """
    Common Components declared at the top of the Post-Trade chapter.
    """
    
    messages: List = pla.Field()
    """
    Messages defined within the enclosing element.
    """
    
    components: List = pla.Field()
    """
    Components referenced by the enclosing element.
    """
    
    post_footnotes: Optional[List] = pla.Field(nullable=True, )
    """
    Footnotes attached to the area-wide components table.
    """
    
    post_category_sections: Optional[List] = pla.Field(nullable=True, )
    """
    Per-category sub-sections of the Post-Trade chapter.
    """
    
    post_common_component_details: Optional[List] = pla.Field(nullable=True, )
    """
    Per-common-component descriptions from the chapter's final Common Components section.
    """
    
    messages_overview_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of the area-wide Messages sub-section.
    """
    
    components_overview_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of the area-wide Components sub-section.
    """
    
    referenced_global_components: Optional[List] = pla.Field(nullable=True, )
    """
    Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeMessageEntry, pa_pl.PostTradeMessageEntryDict)
        
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeComponentEntry, pa_pl.PostTradeComponentEntryDict)
        
    @pla.check("post_footnotes")
    def check_nested_struct_post_footnotes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeComponentTableFootnote, pa_pl.PostTradeComponentTableFootnoteDict)
        
    @pla.check("post_category_sections")
    def check_nested_struct_post_category_sections(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeCategorySection, pa_pl.PostTradeCategorySectionDict)
        
    @pla.check("post_common_component_details")
    def check_nested_struct_post_common_component_details(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, PostTradeCommonComponentDetail, pa_pl.PostTradeCommonComponentDetailDict)
        
class InfrastructureMessageEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the area-wide "Messages for Infrastructure Business Area" table.
    """

    _id_name : str =  'msg_type' 
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    category: Enum = pla.Field(dtype_kwargs={"categories":('BUSINESS_MESSAGE_REJECTS','NETWORK_STATUS_COMMUNICATION','USER_MANAGEMENT','APPLICATION_SEQUENCING',)})
    """
    Message category.
    """
    
    
class InfrastructureComponentEntry(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the area-wide "Components for Infrastructure Business Area" table.
    """

    _id_name : str =  'component_name' 
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    repetition: Enum = pla.Field(dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    category: Enum = pla.Field(dtype_kwargs={"categories":('BUSINESS_MESSAGE_REJECTS','NETWORK_STATUS_COMMUNICATION','USER_MANAGEMENT','APPLICATION_SEQUENCING',)})
    """
    Message category.
    """
    
    footnote_number: Optional[int] = pla.Field(ge=1, le=25, nullable=True, )
    """
    Footnote indicator on a component-table row.
    """
    
    
class InfrastructureComponentTableFootnote(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A footnote attached to a row of the area-wide Infrastructure components table.
    """

    _id_name : str =  'footnote_number' 
    footnote_number: int = pla.Field(ge=1, le=25, )
    """
    Footnote indicator on a component-table row.
    """
    
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    introduced_in: str = pla.Field()
    """
    FIX version or Extension Pack that introduced the component.
    """
    
    infra_sole_category: Enum = pla.Field(dtype_kwargs={"categories":('BUSINESS_MESSAGE_REJECTS','NETWORK_STATUS_COMMUNICATION','USER_MANAGEMENT','APPLICATION_SEQUENCING',)})
    """
    Single Infrastructure category that actually uses the footnoted component.
    """
    
    text: Optional[str] = pla.Field(nullable=True, )
    """
    Footnote text.
    """
    
    
class InfrastructureLayoutRow(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of the layout table published in the Infrastructure Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """

    _id_name : str = None
    infra_layout_kind: Enum = pla.Field(dtype_kwargs={"categories":('FIELD','COMPONENT',)})
    """
    Row kind — either a FIX field (numeric Tag) or an embedded component (literal "Component" in the Tag column of the source table).
    """
    
    infra_layout_field_tag: Optional[int] = pla.Field(ge=0, nullable=True, )
    """
    FIX tag number drawn from the Tag column when the row is a field (i.e. layout_kind = FIELD). Absent for COMPONENT rows.
    """
    
    infra_layout_element_name: str = pla.Field()
    """
    Element name as printed in the Name column — either the FIX field name (e.g. ApplReqID) or the component name (e.g. StandardHeader, ApplIDRequestGrp).
    """
    
    infra_layout_required: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the field or component is required, as printed in the Req’d column of the source layout table ("Y" / "N").
    """
    
    infra_layout_description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text content of the Description column of the row (may be empty).
    """
    
    infra_layout_nested: Optional[bool] = pla.Field(nullable=True, )
    """
    Whether the row appears nested under a repeating-group counter (i.e. its Tag column is prefixed with the "→" arrow in the source table).
    """
    
    
class InfrastructureMessageDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-message description appearing in a category's Messages sub-section.
    """

    _id_name : str = None
    msg_type: str = pla.Field(str_matches=r"^[A-Za-z0-9]{1,3}$", )
    """
    MsgType(35) wire value identifying the message.
    """
    
    message_name: str = pla.Field()
    """
    PascalCase name of the message.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout.
    """
    
    infra_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Infrastructure Appendix.
    """
    
    
    @pla.check("infra_layout_rows")
    def check_nested_struct_infra_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InfrastructureLayoutRow, pa_pl.InfrastructureLayoutRowDict)
        
class InfrastructureComponentDetail(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Per-component description appearing in a category's Components sub-section.
    """

    _id_name : str = None
    component_name: str = pla.Field()
    """
    PascalCase name of the component.
    """
    
    repetition: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('REPEATING','NON_REPEATING',)})
    """
    REPEATING or NON_REPEATING.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    layout_url: Optional[str] = pla.Field(nullable=True, )
    """
    URL of the detailed message- or component-layout.
    """
    
    infra_layout_rows: Optional[List] = pla.Field(nullable=True, )
    """
    Ordered rows of the layout table published for the message or component in the Infrastructure Appendix.
    """
    
    
    @pla.check("infra_layout_rows")
    def check_nested_struct_infra_layout_rows(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InfrastructureLayoutRow, pa_pl.InfrastructureLayoutRowDict)
        
class InfrastructureCategorySection(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A "Category – <name>" sub-section of the Infrastructure chapter.
    """

    _id_name : str = None
    category: Enum = pla.Field(dtype_kwargs={"categories":('BUSINESS_MESSAGE_REJECTS','NETWORK_STATUS_COMMUNICATION','USER_MANAGEMENT','APPLICATION_SEQUENCING',)})
    """
    Message category.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title.
    """
    
    description: Optional[str] = pla.Field(nullable=True, )
    """
    Free-text description.
    """
    
    category_components_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of a category's Components sub-section.
    """
    
    messages: Optional[List] = pla.Field(nullable=True, )
    """
    Messages defined within the enclosing element.
    """
    
    infra_category_specific_components: Optional[List] = pla.Field(nullable=True, )
    """
    Per-component descriptions appearing in a category's Components sub-section.
    """
    
    network_status_scenarios: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('SCENARIO_A','SCENARIO_B',)})
    """
    Network Status Communication usage scenarios.
    """
    
    network_request_types_referenced: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('SNAPSHOT','STOP_SUBSCRIBING',)})
    """
    NetworkRequestType(935) values explicitly cited in the Network Status Communication category prose.
    """
    
    application_message_report_uses: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('RESET','LAST_MESSAGE','KEEP_ALIVE','RESEND_COMPLETED',)})
    """
    Documented uses of ApplicationMessageReport(35=BY).
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InfrastructureMessageDetail, pa_pl.InfrastructureMessageDetailDict)
        
    @pla.check("infra_category_specific_components")
    def check_nested_struct_infra_category_specific_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InfrastructureComponentDetail, pa_pl.InfrastructureComponentDetailDict)
        
class StandardResponseMapping(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of a "Standard Responses for <area> Messages" table mapping a request message to its appropriate response(s).
    """

    _id_name : str = None
    category_label: str = pla.Field()
    """
    Category label as printed in the source table (free text; may include parenthesised sub-categories such as "Single General Order Handling").
    """
    
    fix_message: str = pla.Field()
    """
    FIX message name with MsgType in parentheses, e.g. AllocationInstruction(35=J).
    """
    
    appropriate_responses: str = pla.Field()
    """
    Free-text appropriate-response cell from the Standard Responses tables.
    """
    
    
class ApplicationMessageReferenceKey(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One row of a "Key Fields for <area> Application Message References" table identifying the field whose value is copied into BusinessRejectRefID(379).
    """

    _id_name : str = None
    category_label: str = pla.Field()
    """
    Category label as printed in the source table (free text; may include parenthesised sub-categories such as "Single General Order Handling").
    """
    
    fix_message: str = pla.Field()
    """
    FIX message name with MsgType in parentheses, e.g. AllocationInstruction(35=J).
    """
    
    business_reject_ref_id_value: str = pla.Field()
    """
    Source field copied into BusinessRejectRefID(379) when the target message lacks its own reject. May enumerate several alternatives joined by "or".
    """
    
    
class BusinessRejectReasonDescription(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    One entry of the BusinessRejectReason(380) code table.
    """

    _id_name : str =  'reject_reason_code' 
    reject_reason_code: int = pla.Field(ge=0, le=999, )
    """
    Numeric code value of BusinessRejectReason(380).
    """
    
    reject_reason_label: str = pla.Field()
    """
    Human-readable label of a BusinessRejectReason(380) code.
    """
    
    
class InfrastructureGlobalComponentReference(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    A reference from the Infrastructure business area to a Global Component declared on the FIX Latest "Global Components" page. Records the component name, the FIX tags it contributes, and the Infrastructure categories and messages that embed it.
    """

    _id_name : str =  'infra_global_component_name' 
    infra_global_component_name: Enum = pla.Field(dtype_kwargs={"categories":('ApplicationSequenceControl',)})
    """
    Name of a Global Component referenced from within the Infrastructure business area.
    """
    
    infra_global_component_repetition: Optional[str] = pla.Field(nullable=True, )
    """
    Repetition indicator for the Global Component as it appears in the referenced Infrastructure messages.
    """
    
    infra_global_component_field_tags: Optional[int] = pla.Field(ge=0, nullable=True, )
    """
    FIX tag numbers contributed by the referenced Global Component (as listed on the Global Components page).
    """
    
    infra_global_component_field_names: Optional[str] = pla.Field(nullable=True, )
    """
    Human-readable field names of the tags contributed by the referenced Global Component.
    """
    
    infra_global_component_used_in: Enum = pla.Field(dtype_kwargs={"categories":('BUSINESS_MESSAGE_REJECTS','NETWORK_STATUS_COMMUNICATION','USER_MANAGEMENT','APPLICATION_SEQUENCING',)})
    """
    Infrastructure categories that reference the Global Component.
    """
    
    infra_global_component_msg_types: Optional[str] = pla.Field(nullable=True, )
    """
    MsgType values within the Infrastructure business area that embed the referenced Global Component.
    """
    
    
class InfrastructureBusinessArea(pla.DataFrameModel, _LinkmlPanderaValidator):
    """
    Tree-root container for the Infrastructure business area of FIX Latest.
    """

    _id_name : str = None
    area: Enum = pla.Field(dtype_kwargs={"categories":('INTRODUCTION','PRE_TRADE','TRADE','POST_TRADE','INFRASTRUCTURE',)})
    """
    Identity of the business area.
    """
    
    title: Optional[str] = pla.Field(nullable=True, )
    """
    Display title.
    """
    
    published_version: Optional[str] = pla.Field(nullable=True, )
    """
    Version stamp from the document header.
    """
    
    publisher: Optional[str] = pla.Field(nullable=True, )
    """
    Publishing body of the FIX Latest specification.
    """
    
    infra_introduction: Optional[str] = pla.Field(nullable=True, )
    """
    Prose introduction of the Infrastructure chapter.
    """
    
    diagram_conventions: Optional[str] = pla.Field(nullable=True, )
    """
    Sentence describing diagram conventions used in the chapter.
    """
    
    infra_common_components: Optional[Enum] = pla.Field(nullable=True, dtype_kwargs={"categories":('ApplIDReportGrp','ApplIDRequestAckGrp','ApplIDRequestGrp','CompIDReqGrp','CompIDStatGrp','ThrottleMsgTypeGrp','ThrottleParamsGrp','UsernameGrp',)})
    """
    Component names declared in the area-wide components listing. Per the chapter prose, none of these are shared across categories within the area.
    """
    
    messages: List = pla.Field()
    """
    Messages defined within the enclosing element.
    """
    
    messages_overview_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of the area-wide Messages sub-section.
    """
    
    components: List = pla.Field()
    """
    Components referenced by the enclosing element.
    """
    
    components_overview_note: Optional[str] = pla.Field(nullable=True, )
    """
    Intro prose of the area-wide Components sub-section.
    """
    
    infra_footnotes: Optional[List] = pla.Field(nullable=True, )
    """
    Footnotes attached to the area-wide Infrastructure components table.
    """
    
    infra_category_sections: Optional[List] = pla.Field(nullable=True, )
    """
    Per-category sub-sections of the Infrastructure chapter.
    """
    
    standard_responses_pre_trade: Optional[List] = pla.Field(nullable=True, )
    """
    "Standard Responses for Pre-Trade Messages" table rows.
    """
    
    standard_responses_trade: Optional[List] = pla.Field(nullable=True, )
    """
    "Standard Responses for Trade Messages" table rows.
    """
    
    standard_responses_post_trade: Optional[List] = pla.Field(nullable=True, )
    """
    "Standard Responses for Post-Trade Messages" table rows.
    """
    
    key_fields_pre_trade: Optional[List] = pla.Field(nullable=True, )
    """
    "Key Fields for Pre-Trade Application Message References" table rows.
    """
    
    key_fields_trade: Optional[List] = pla.Field(nullable=True, )
    """
    "Key Fields for Trade Application Message References" table rows.
    """
    
    key_fields_post_trade: Optional[List] = pla.Field(nullable=True, )
    """
    "Key Fields for Post-Trade Application Message References" table rows.
    """
    
    business_reject_reason_descriptions: Optional[List] = pla.Field(nullable=True, )
    """
    Descriptions tied to BusinessRejectReason(380) values.
    """
    
    infra_global_components: Optional[List] = pla.Field(nullable=True, )
    """
    Global Components (from the FIX Latest "Global Components" page) that are explicitly referenced by messages in the Infrastructure business area, together with their tag set and usage scope.
    """
    
    referenced_global_components: Optional[List] = pla.Field(nullable=True, )
    """
    Names of Global Components from the FIX Latest "Global Components" page that are referenced by messages in the containing business area. References instances of the :class:`GlobalComponent` class (declared in fix_base) by name.
    """
    
    
    @pla.check("messages")
    def check_nested_struct_messages(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InfrastructureMessageEntry, pa_pl.InfrastructureMessageEntryDict)
        
    @pla.check("components")
    def check_nested_struct_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InfrastructureComponentEntry, pa_pl.InfrastructureComponentEntryDict)
        
    @pla.check("infra_footnotes")
    def check_nested_struct_infra_footnotes(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InfrastructureComponentTableFootnote, pa_pl.InfrastructureComponentTableFootnoteDict)
        
    @pla.check("infra_category_sections")
    def check_nested_struct_infra_category_sections(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InfrastructureCategorySection, pa_pl.InfrastructureCategorySectionDict)
        
    @pla.check("standard_responses_pre_trade")
    def check_nested_struct_standard_responses_pre_trade(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, StandardResponseMapping, pa_pl.StandardResponseMappingDict)
        
    @pla.check("standard_responses_trade")
    def check_nested_struct_standard_responses_trade(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, StandardResponseMapping, pa_pl.StandardResponseMappingDict)
        
    @pla.check("standard_responses_post_trade")
    def check_nested_struct_standard_responses_post_trade(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, StandardResponseMapping, pa_pl.StandardResponseMappingDict)
        
    @pla.check("key_fields_pre_trade")
    def check_nested_struct_key_fields_pre_trade(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ApplicationMessageReferenceKey, pa_pl.ApplicationMessageReferenceKeyDict)
        
    @pla.check("key_fields_trade")
    def check_nested_struct_key_fields_trade(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ApplicationMessageReferenceKey, pa_pl.ApplicationMessageReferenceKeyDict)
        
    @pla.check("key_fields_post_trade")
    def check_nested_struct_key_fields_post_trade(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, ApplicationMessageReferenceKey, pa_pl.ApplicationMessageReferenceKeyDict)
        
    @pla.check("business_reject_reason_descriptions")
    def check_nested_struct_business_reject_reason_descriptions(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, BusinessRejectReasonDescription, pa_pl.BusinessRejectReasonDescriptionDict)
        
    @pla.check("infra_global_components")
    def check_nested_struct_infra_global_components(cls, data: PolarsData):
        return cls._check_nested_list_struct(data, InfrastructureGlobalComponentReference, pa_pl.InfrastructureGlobalComponentReferenceDict)
        

