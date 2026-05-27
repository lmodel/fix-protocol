
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class FIXIntroduction(Base):
    """
    Container for the structural elements of the FIX Latest Introduction section. Tree root for instance data.
    """
    __tablename__ = 'FIXIntroduction'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    published_version = Column(Text())
    published_date = Column(Date())
    publisher = Column(Text())
    preface = Column(Text())
    introduction_text = Column(Text())
    utc_leap_seconds_note = Column(Text())
    about_fpl_id = Column(Integer(), ForeignKey('FIXProtocolLimited.id'))
    about_fpl = relationship("FIXProtocolLimited", uselist=False, foreign_keys=[about_fpl_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='FIXIntroduction', source_slot='standards', mapping_type=None, target_class='FIXFamilyStandard', target_slot='FIXIntroduction_id', join_class=None, uses_join_table=None, multivalued=False)
    standards = relationship( "FIXFamilyStandard", foreign_keys="[FIXFamilyStandard.FIXIntroduction_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='FIXIntroduction', source_slot='extension_packs', mapping_type=None, target_class='ExtensionPack', target_slot='FIXIntroduction_id', join_class=None, uses_join_table=None, multivalued=False)
    extension_packs = relationship( "ExtensionPack", foreign_keys="[ExtensionPack.FIXIntroduction_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='FIXIntroduction', source_slot='datatypes', mapping_type=None, target_class='FIXDatatype', target_slot='FIXIntroduction_id', join_class=None, uses_join_table=None, multivalued=False)
    datatypes = relationship( "FIXDatatype", foreign_keys="[FIXDatatype.FIXIntroduction_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='FIXIntroduction', source_slot='business_areas', mapping_type=None, target_class='BusinessArea', target_slot='FIXIntroduction_id', join_class=None, uses_join_table=None, multivalued=False)
    business_areas = relationship( "BusinessArea", foreign_keys="[BusinessArea.FIXIntroduction_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='FIXIntroduction', source_slot='global_components', mapping_type=None, target_class='GlobalComponent', target_slot='FIXIntroduction_id', join_class=None, uses_join_table=None, multivalued=False)
    global_components = relationship( "GlobalComponent", foreign_keys="[GlobalComponent.FIXIntroduction_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='FIXIntroduction', source_slot='udf_ranges', mapping_type=None, target_class='UDFTagRange', target_slot='FIXIntroduction_id', join_class=None, uses_join_table=None, multivalued=False)
    udf_ranges = relationship( "UDFTagRange", foreign_keys="[UDFTagRange.FIXIntroduction_id]")
    
    
    product_coverage_rel = relationship( "FIXIntroductionProductCoverage" )
    product_coverage = association_proxy("product_coverage_rel", "product_coverage",
                                  creator=lambda x_: FIXIntroductionProductCoverage(product_coverage=x_))
    

    def __repr__(self):
        return f"FIXIntroduction(id={self.id},published_version={self.published_version},published_date={self.published_date},publisher={self.publisher},preface={self.preface},introduction_text={self.introduction_text},utc_leap_seconds_note={self.utc_leap_seconds_note},about_fpl_id={self.about_fpl_id},)"



    


class FIXProtocolLimited(Base):
    """
    The organization that maintains the FIX Protocol specification.
    """
    __tablename__ = 'FIXProtocolLimited'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    brand_name = Column(Text())
    legal_name = Column(Text())
    website = Column(Text())
    member_firms_url = Column(Text())
    working_groups_url = Column(Text())
    committees_url = Column(Text())
    
    
    member_types_rel = relationship( "FIXProtocolLimitedMemberTypes" )
    member_types = association_proxy("member_types_rel", "member_types",
                                  creator=lambda x_: FIXProtocolLimitedMemberTypes(member_types=x_))
    
    
    governance_bodies_rel = relationship( "FIXProtocolLimitedGovernanceBodies" )
    governance_bodies = association_proxy("governance_bodies_rel", "governance_bodies",
                                  creator=lambda x_: FIXProtocolLimitedGovernanceBodies(governance_bodies=x_))
    
    
    product_committees_rel = relationship( "FIXProtocolLimitedProductCommittees" )
    product_committees = association_proxy("product_committees_rel", "product_committees",
                                  creator=lambda x_: FIXProtocolLimitedProductCommittees(product_committees=x_))
    
    
    regional_committees_rel = relationship( "FIXProtocolLimitedRegionalCommittees" )
    regional_committees = association_proxy("regional_committees_rel", "regional_committees",
                                  creator=lambda x_: FIXProtocolLimitedRegionalCommittees(regional_committees=x_))
    

    def __repr__(self):
        return f"FIXProtocolLimited(id={self.id},brand_name={self.brand_name},legal_name={self.legal_name},website={self.website},member_firms_url={self.member_firms_url},working_groups_url={self.working_groups_url},committees_url={self.committees_url},)"



    


class FIXFamilyStandard(Base):
    """
    A member standard of the FIX Family of Standards.
    """
    __tablename__ = 'FIXFamilyStandard'

    id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text(), nullable=False )
    description = Column(Text())
    acronym = Column(Text())
    layer = Column(Enum('APPLICATION', 'ENCODING', 'SESSION', name='StandardLayer'), nullable=False )
    version = Column(Text())
    session_profile = Column(Enum('FIX_4_2', 'FIX4', 'FIXT', 'LFIXT', 'FIXP', 'SOFH', 'FIXS', 'AMQP', name='SessionProtocolName'))
    encoding_name = Column(Enum('TAGVALUE', 'FIXML', 'FAST', 'SBE', 'GPB', 'JSON', 'ASN_1', name='StandardEncodingName'))
    FIXIntroduction_id = Column(Integer(), ForeignKey('FIXIntroduction.id'))
    
    
    see_also_rel = relationship( "FIXFamilyStandardSeeAlso" )
    see_also = association_proxy("see_also_rel", "see_also",
                                  creator=lambda x_: FIXFamilyStandardSeeAlso(see_also=x_))
    

    def __repr__(self):
        return f"FIXFamilyStandard(id={self.id},name={self.name},description={self.description},acronym={self.acronym},layer={self.layer},version={self.version},session_profile={self.session_profile},encoding_name={self.encoding_name},FIXIntroduction_id={self.FIXIntroduction_id},)"



    


class ExtensionPack(Base):
    """
    A unit of change to FIX Latest.
    """
    __tablename__ = 'ExtensionPack'

    number = Column(Integer(), primary_key=True, nullable=False )
    title = Column(Text(), nullable=False )
    size = Column(Enum('XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', name='ExtensionPackSize'))
    enhancement_summary = Column(Text())
    applies_to_session_layer_only = Column(Boolean())
    applies_to_fixml_only = Column(Boolean())
    FIXIntroduction_id = Column(Integer(), ForeignKey('FIXIntroduction.id'))
    

    def __repr__(self):
        return f"ExtensionPack(number={self.number},title={self.title},size={self.size},enhancement_summary={self.enhancement_summary},applies_to_session_layer_only={self.applies_to_session_layer_only},applies_to_fixml_only={self.applies_to_fixml_only},FIXIntroduction_id={self.FIXIntroduction_id},)"



    


class FIXDatatype(Base):
    """
    A FIX Protocol datatype.
    """
    __tablename__ = 'FIXDatatype'

    datatype_name = Column(Enum('int', 'TagNum', 'SeqNum', 'NumInGroup', 'DayOfMonth', 'float', 'Qty', 'Price', 'PriceOffset', 'Amt', 'Percentage', 'char', 'Boolean', 'String', 'MultipleCharValue', 'MultipleStringValue', 'Country', 'Currency', 'Exchange', 'MonthYear', 'UTCTimestamp', 'UTCTimeOnly', 'UTCDateOnly', 'LocalMktDate', 'TZTimeOnly', 'TZTimestamp', 'Length', 'data', 'Tenor', 'Reserved100Plus', 'Reserved1000Plus', 'Reserved4000Plus', 'XMLData', 'Language', 'LocalMktTime', name='FIXDatatypeName'), primary_key=True, nullable=False )
    definition = Column(Text(), nullable=False )
    value_space_notes = Column(Text())
    deprecated_for_new_designs = Column(Boolean())
    external_code_set = Column(Text())
    radix = Column(Integer())
    repertoire = Column(Text())
    index_lower_bound = Column(Integer())
    index_upper_bound = Column(Integer())
    minimum_value = Column(Integer())
    maximum_value = Column(Integer())
    FIXIntroduction_id = Column(Integer(), ForeignKey('FIXIntroduction.id'))
    
    
    value_space_rel = relationship( "FIXDatatypeValueSpace" )
    value_space = association_proxy("value_space_rel", "value_space",
                                  creator=lambda x_: FIXDatatypeValueSpace(value_space=x_))
    
    
    time_unit_rel = relationship( "FIXDatatypeTimeUnit" )
    time_unit = association_proxy("time_unit_rel", "time_unit",
                                  creator=lambda x_: FIXDatatypeTimeUnit(time_unit=x_))
    
    
    footnote_numbers_rel = relationship( "FIXDatatypeFootnoteNumbers" )
    footnote_numbers = association_proxy("footnote_numbers_rel", "footnote_numbers",
                                  creator=lambda x_: FIXDatatypeFootnoteNumbers(footnote_numbers=x_))
    

    def __repr__(self):
        return f"FIXDatatype(datatype_name={self.datatype_name},definition={self.definition},value_space_notes={self.value_space_notes},deprecated_for_new_designs={self.deprecated_for_new_designs},external_code_set={self.external_code_set},radix={self.radix},repertoire={self.repertoire},index_lower_bound={self.index_lower_bound},index_upper_bound={self.index_upper_bound},minimum_value={self.minimum_value},maximum_value={self.maximum_value},FIXIntroduction_id={self.FIXIntroduction_id},)"



    


class BusinessArea(Base):
    """
    A top-level business area of the FIX Latest specification.
    """
    __tablename__ = 'BusinessArea'

    area = Column(Enum('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='BusinessAreaEnum'), primary_key=True, nullable=False )
    title = Column(Text())
    description = Column(Text())
    FIXIntroduction_id = Column(Integer(), ForeignKey('FIXIntroduction.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='BusinessArea', source_slot='categories', mapping_type=None, target_class='MessageCategory', target_slot='BusinessArea_area', join_class=None, uses_join_table=None, multivalued=False)
    categories = relationship( "MessageCategory", foreign_keys="[MessageCategory.BusinessArea_area]")
    

    def __repr__(self):
        return f"BusinessArea(area={self.area},title={self.title},description={self.description},FIXIntroduction_id={self.FIXIntroduction_id},)"



    


class MessageCategory(Base):
    """
    A message category within a business area.
    """
    __tablename__ = 'MessageCategory'

    category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', 'SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDERS', 'MULTILEG_ORDERS', 'LIST_PROGRAM_BASKET_TRADING', 'ALLOCATION_AND_READY_TO_BOOK', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTIONS', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTIONS', 'POSITIONS_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', 'BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING', name='MessageCategoryEnum'), primary_key=True, nullable=False )
    title = Column(Text())
    description = Column(Text())
    business_area = Column(Enum('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='BusinessAreaEnum'), nullable=False )
    BusinessArea_area = Column(Enum('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='BusinessAreaEnum'), ForeignKey('BusinessArea.area'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='MessageCategory', source_slot='messages', mapping_type=None, target_class='Message', target_slot='MessageCategory_category', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "Message", foreign_keys="[Message.MessageCategory_category]")
    

    def __repr__(self):
        return f"MessageCategory(category={self.category},title={self.title},description={self.description},business_area={self.business_area},BusinessArea_area={self.BusinessArea_area},)"



    


class Field(Base):
    """
    A FIX field — a uniquely tagged data element with a FIX datatype.
    """
    __tablename__ = 'Field'

    tag = Column(Integer(), primary_key=True, nullable=False )
    field_name = Column(Text(), nullable=False )
    datatype = Column(Enum('int', 'TagNum', 'SeqNum', 'NumInGroup', 'DayOfMonth', 'float', 'Qty', 'Price', 'PriceOffset', 'Amt', 'Percentage', 'char', 'Boolean', 'String', 'MultipleCharValue', 'MultipleStringValue', 'Country', 'Currency', 'Exchange', 'MonthYear', 'UTCTimestamp', 'UTCTimeOnly', 'UTCDateOnly', 'LocalMktDate', 'TZTimeOnly', 'TZTimestamp', 'Length', 'data', 'Tenor', 'Reserved100Plus', 'Reserved1000Plus', 'Reserved4000Plus', 'XMLData', 'Language', 'LocalMktTime', name='FIXDatatypeName'), nullable=False )
    description = Column(Text())
    requirement = Column(Enum('REQUIRED', 'OPTIONAL', 'CONDITIONALLY_REQUIRED', name='FieldRequirement'))
    is_user_defined = Column(Boolean())
    Component_component_name = Column(Text(), ForeignKey('Component.component_name'))
    GlobalComponent_component_name = Column(Text(), ForeignKey('GlobalComponent.component_name'))
    CommonComponent_component_name = Column(Text(), ForeignKey('CommonComponent.component_name'))
    SpecificComponent_component_name = Column(Text(), ForeignKey('SpecificComponent.component_name'))
    Message_msg_type = Column(Text(), ForeignKey('Message.msg_type'))
    

    def __repr__(self):
        return f"Field(tag={self.tag},field_name={self.field_name},datatype={self.datatype},description={self.description},requirement={self.requirement},is_user_defined={self.is_user_defined},Component_component_name={self.Component_component_name},GlobalComponent_component_name={self.GlobalComponent_component_name},CommonComponent_component_name={self.CommonComponent_component_name},SpecificComponent_component_name={self.SpecificComponent_component_name},Message_msg_type={self.Message_msg_type},)"



    


class Component(Base):
    """
    A FIX component — a named set of related fields.
    """
    __tablename__ = 'Component'

    component_name = Column(Text(), primary_key=True, nullable=False )
    description = Column(Text())
    scope = Column(Enum('GLOBAL', 'COMMON', 'SPECIFIC', name='ComponentScope'), nullable=False )
    is_repeating_group = Column(Boolean())
    
    
    # One-To-Many: OneToAnyMapping(source_class='Component', source_slot='fields', mapping_type=None, target_class='Field', target_slot='Component_component_name', join_class=None, uses_join_table=None, multivalued=False)
    fields = relationship( "Field", foreign_keys="[Field.Component_component_name]")
    
    
    # ManyToMany
    nested_components = relationship( "Component", secondary="Component_nested_components")
    

    def __repr__(self):
        return f"Component(component_name={self.component_name},description={self.description},scope={self.scope},is_repeating_group={self.is_repeating_group},)"



    


class Message(Base):
    """
    A FIX application message.
    """
    __tablename__ = 'Message'

    msg_type = Column(Text(), primary_key=True, nullable=False )
    message_name = Column(Text(), nullable=False )
    description = Column(Text())
    category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', 'SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDERS', 'MULTILEG_ORDERS', 'LIST_PROGRAM_BASKET_TRADING', 'ALLOCATION_AND_READY_TO_BOOK', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTIONS', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTIONS', 'POSITIONS_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', 'BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING', name='MessageCategoryEnum'))
    MessageCategory_category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', 'SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDERS', 'MULTILEG_ORDERS', 'LIST_PROGRAM_BASKET_TRADING', 'ALLOCATION_AND_READY_TO_BOOK', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTIONS', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTIONS', 'POSITIONS_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', 'BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING', name='MessageCategoryEnum'), ForeignKey('MessageCategory.category'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Message', source_slot='fields', mapping_type=None, target_class='Field', target_slot='Message_msg_type', join_class=None, uses_join_table=None, multivalued=False)
    fields = relationship( "Field", foreign_keys="[Field.Message_msg_type]")
    
    
    # ManyToMany
    components = relationship( "Component", secondary="Message_components")
    

    def __repr__(self):
        return f"Message(msg_type={self.msg_type},message_name={self.message_name},description={self.description},category={self.category},MessageCategory_category={self.MessageCategory_category},)"



    


class UDFTagRange(Base):
    """
    A reserved range of tag numbers for User Defined Fields.
    """
    __tablename__ = 'UDFTagRange'

    range_id = Column(Text(), primary_key=True, nullable=False )
    low_tag = Column(Integer(), nullable=False )
    high_tag = Column(Integer())
    usage = Column(Enum('INTER_FIRM_REGISTERED', 'INTER_FIRM_BILATERAL', 'GTC_REGULATORY_LEGACY', 'WIP_CHINA', 'INTERNAL_FIRM', 'GTC_OTC_DERIVATIVES', 'GTC_RESERVED', name='UDFTagRangeUsage'), nullable=False )
    description = Column(Text())
    requires_registration = Column(Boolean())
    FIXIntroduction_id = Column(Integer(), ForeignKey('FIXIntroduction.id'))
    

    def __repr__(self):
        return f"UDFTagRange(range_id={self.range_id},low_tag={self.low_tag},high_tag={self.high_tag},usage={self.usage},description={self.description},requires_registration={self.requires_registration},FIXIntroduction_id={self.FIXIntroduction_id},)"



    


class PreTradeBusinessArea(Base):
    """
    Tree-root container for the Pre-Trade business area of FIX Latest.
    """
    __tablename__ = 'PreTradeBusinessArea'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    area = Column(Enum('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='BusinessAreaEnum'), nullable=False )
    title = Column(Text())
    published_version = Column(Text())
    publisher = Column(Text())
    introduction = Column(Text())
    diagram_conventions = Column(Text())
    messages_overview_note = Column(Text())
    components_overview_note = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeBusinessArea', source_slot='messages', mapping_type=None, target_class='PreTradeMessageEntry', target_slot='PreTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "PreTradeMessageEntry", foreign_keys="[PreTradeMessageEntry.PreTradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeBusinessArea', source_slot='components', mapping_type=None, target_class='PreTradeComponentEntry', target_slot='PreTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "PreTradeComponentEntry", foreign_keys="[PreTradeComponentEntry.PreTradeBusinessArea_id]")
    
    
    common_components_rel = relationship( "PreTradeBusinessAreaCommonComponents" )
    common_components = association_proxy("common_components_rel", "common_components",
                                  creator=lambda x_: PreTradeBusinessAreaCommonComponents(common_components=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeBusinessArea', source_slot='common_component_details', mapping_type=None, target_class='CommonComponentDetail', target_slot='PreTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    common_component_details = relationship( "CommonComponentDetail", foreign_keys="[CommonComponentDetail.PreTradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeBusinessArea', source_slot='footnotes', mapping_type=None, target_class='ComponentTableFootnote', target_slot='PreTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    footnotes = relationship( "ComponentTableFootnote", foreign_keys="[ComponentTableFootnote.PreTradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeBusinessArea', source_slot='category_sections', mapping_type=None, target_class='PreTradeCategorySection', target_slot='PreTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    category_sections = relationship( "PreTradeCategorySection", foreign_keys="[PreTradeCategorySection.PreTradeBusinessArea_id]")
    
    
    # ManyToMany
    referenced_global_components = relationship( "GlobalComponent", secondary="PreTradeBusinessArea_referenced_global_components")
    

    def __repr__(self):
        return f"PreTradeBusinessArea(id={self.id},area={self.area},title={self.title},published_version={self.published_version},publisher={self.publisher},introduction={self.introduction},diagram_conventions={self.diagram_conventions},messages_overview_note={self.messages_overview_note},components_overview_note={self.components_overview_note},)"



    


class PreTradeMessageEntry(Base):
    """
    One row of the area-wide pre-trade messages table.
    """
    __tablename__ = 'PreTradeMessageEntry'

    msg_type = Column(Text(), primary_key=True, nullable=False )
    message_name = Column(Text(), nullable=False )
    category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', name='PreTradeCategoryEnum'), nullable=False )
    PreTradeBusinessArea_id = Column(Integer(), ForeignKey('PreTradeBusinessArea.id'))
    

    def __repr__(self):
        return f"PreTradeMessageEntry(msg_type={self.msg_type},message_name={self.message_name},category={self.category},PreTradeBusinessArea_id={self.PreTradeBusinessArea_id},)"



    


class PreTradeComponentEntry(Base):
    """
    One row of the area-wide pre-trade components table.
    """
    __tablename__ = 'PreTradeComponentEntry'

    component_name = Column(Text(), primary_key=True, nullable=False )
    repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='ComponentRepetition'), nullable=False )
    category = Column(Text(), nullable=False )
    is_common = Column(Boolean())
    footnote_number = Column(Integer())
    PreTradeBusinessArea_id = Column(Integer(), ForeignKey('PreTradeBusinessArea.id'))
    

    def __repr__(self):
        return f"PreTradeComponentEntry(component_name={self.component_name},repetition={self.repetition},category={self.category},is_common={self.is_common},footnote_number={self.footnote_number},PreTradeBusinessArea_id={self.PreTradeBusinessArea_id},)"



    


class ComponentTableFootnote(Base):
    """
    A footnote on the area-wide components table.
    """
    __tablename__ = 'ComponentTableFootnote'

    footnote_number = Column(Integer(), primary_key=True, nullable=False )
    component_name = Column(Text(), nullable=False )
    introduced_in = Column(Text(), nullable=False )
    sole_category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', name='PreTradeCategoryEnum'), nullable=False )
    text = Column(Text())
    PreTradeBusinessArea_id = Column(Integer(), ForeignKey('PreTradeBusinessArea.id'))
    

    def __repr__(self):
        return f"ComponentTableFootnote(footnote_number={self.footnote_number},component_name={self.component_name},introduced_in={self.introduced_in},sole_category={self.sole_category},text={self.text},PreTradeBusinessArea_id={self.PreTradeBusinessArea_id},)"



    


class PreTradeCategorySection(Base):
    """
    A per-category sub-section of the Pre-Trade chapter.
    """
    __tablename__ = 'PreTradeCategorySection'

    category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', name='PreTradeCategoryEnum'), primary_key=True, nullable=False )
    title = Column(Text())
    description = Column(Text())
    category_components_note = Column(Text())
    PreTradeBusinessArea_id = Column(Integer(), ForeignKey('PreTradeBusinessArea.id'))
    
    
    quote_models_rel = relationship( "PreTradeCategorySectionQuoteModels" )
    quote_models = association_proxy("quote_models_rel", "quote_models",
                                  creator=lambda x_: PreTradeCategorySectionQuoteModels(quote_models=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeCategorySection', source_slot='message_groups', mapping_type=None, target_class='MessageGroup', target_slot='PreTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    message_groups = relationship( "MessageGroup", foreign_keys="[MessageGroup.PreTradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeCategorySection', source_slot='messages', mapping_type=None, target_class='PreTradeMessageDetail', target_slot='PreTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "PreTradeMessageDetail", foreign_keys="[PreTradeMessageDetail.PreTradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeCategorySection', source_slot='category_specific_components', mapping_type=None, target_class='PreTradeComponentDetail', target_slot='PreTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    category_specific_components = relationship( "PreTradeComponentDetail", foreign_keys="[PreTradeComponentDetail.PreTradeCategorySection_category]")
    

    def __repr__(self):
        return f"PreTradeCategorySection(category={self.category},title={self.title},description={self.description},category_components_note={self.category_components_note},PreTradeBusinessArea_id={self.PreTradeBusinessArea_id},)"



    


class PreTradeMessageDetail(Base):
    """
    Per-category message description.
    """
    __tablename__ = 'PreTradeMessageDetail'

    msg_type = Column(Text(), primary_key=True, nullable=False )
    message_name = Column(Text(), nullable=False )
    description = Column(Text())
    layout_url = Column(Text())
    PreTradeCategorySection_category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', name='PreTradeCategoryEnum'), ForeignKey('PreTradeCategorySection.category'))
    MessageGroup_group_title = Column(Text(), ForeignKey('MessageGroup.group_title'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeMessageDetail', source_slot='pre_layout_rows', mapping_type=None, target_class='PreTradeLayoutRow', target_slot='PreTradeMessageDetail_msg_type', join_class=None, uses_join_table=None, multivalued=False)
    pre_layout_rows = relationship( "PreTradeLayoutRow", foreign_keys="[PreTradeLayoutRow.PreTradeMessageDetail_msg_type]")
    

    def __repr__(self):
        return f"PreTradeMessageDetail(msg_type={self.msg_type},message_name={self.message_name},description={self.description},layout_url={self.layout_url},PreTradeCategorySection_category={self.PreTradeCategorySection_category},MessageGroup_group_title={self.MessageGroup_group_title},)"



    


class PreTradeComponentDetail(Base):
    """
    Per-category component description.
    """
    __tablename__ = 'PreTradeComponentDetail'

    component_name = Column(Text(), primary_key=True, nullable=False )
    repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='ComponentRepetition'))
    description = Column(Text())
    layout_url = Column(Text())
    PreTradeCategorySection_category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', name='PreTradeCategoryEnum'), ForeignKey('PreTradeCategorySection.category'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PreTradeComponentDetail', source_slot='pre_layout_rows', mapping_type=None, target_class='PreTradeLayoutRow', target_slot='PreTradeComponentDetail_component_name', join_class=None, uses_join_table=None, multivalued=False)
    pre_layout_rows = relationship( "PreTradeLayoutRow", foreign_keys="[PreTradeLayoutRow.PreTradeComponentDetail_component_name]")
    

    def __repr__(self):
        return f"PreTradeComponentDetail(component_name={self.component_name},repetition={self.repetition},description={self.description},layout_url={self.layout_url},PreTradeCategorySection_category={self.PreTradeCategorySection_category},)"



    


class MessageGroup(Base):
    """
    Purpose-grouped sub-section inside a category's Messages section.
    """
    __tablename__ = 'MessageGroup'

    group_title = Column(Text(), primary_key=True, nullable=False )
    description = Column(Text())
    PreTradeCategorySection_category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', name='PreTradeCategoryEnum'), ForeignKey('PreTradeCategorySection.category'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='MessageGroup', source_slot='messages', mapping_type=None, target_class='PreTradeMessageDetail', target_slot='MessageGroup_group_title', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "PreTradeMessageDetail", foreign_keys="[PreTradeMessageDetail.MessageGroup_group_title]")
    

    def __repr__(self):
        return f"MessageGroup(group_title={self.group_title},description={self.description},PreTradeCategorySection_category={self.PreTradeCategorySection_category},)"



    


class CommonComponentDetail(Base):
    """
    Per-common-component description.
    """
    __tablename__ = 'CommonComponentDetail'

    component_name = Column(Enum('AuctionTypeRuleGrp', 'BaseTradingRules', 'ExecInstRules', 'InstrumentScope', 'InstrumentScopeGrp', 'InstrumentScopeSecurityAltIDGrp', 'LotTypeRules', 'MarketDataFeedTypes', 'MarketSegmentScopeGrp', 'MatchRules', 'OrdTypeRules', 'PriceLimits', 'PriceRangeRuleGrp', 'QuoteSizeRuleGrp', 'RequestedPartyRoleGrp', 'RequestingPartyGrp', 'RequestingPartySubGrp', 'RoutingGrp', 'TickRules', 'TimeInForceRules', 'TradingSessionRules', name='PreTradeCommonComponentName'), primary_key=True, nullable=False )
    repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='ComponentRepetition'))
    description = Column(Text())
    layout_url = Column(Text())
    PreTradeBusinessArea_id = Column(Integer(), ForeignKey('PreTradeBusinessArea.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='CommonComponentDetail', source_slot='pre_layout_rows', mapping_type=None, target_class='PreTradeLayoutRow', target_slot='CommonComponentDetail_component_name', join_class=None, uses_join_table=None, multivalued=False)
    pre_layout_rows = relationship( "PreTradeLayoutRow", foreign_keys="[PreTradeLayoutRow.CommonComponentDetail_component_name]")
    

    def __repr__(self):
        return f"CommonComponentDetail(component_name={self.component_name},repetition={self.repetition},description={self.description},layout_url={self.layout_url},PreTradeBusinessArea_id={self.PreTradeBusinessArea_id},)"



    


class PreTradeLayoutRow(Base):
    """
    One row of the layout table published in the Pre-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    __tablename__ = 'PreTradeLayoutRow'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    pre_layout_kind = Column(Enum('FIELD', 'COMPONENT', name='PreTradeLayoutRowKindEnum'), nullable=False )
    pre_layout_field_tag = Column(Integer())
    pre_layout_element_name = Column(Text(), nullable=False )
    pre_layout_required = Column(Boolean())
    pre_layout_description = Column(Text())
    pre_layout_nested = Column(Boolean())
    PreTradeMessageDetail_msg_type = Column(Text(), ForeignKey('PreTradeMessageDetail.msg_type'))
    PreTradeComponentDetail_component_name = Column(Text(), ForeignKey('PreTradeComponentDetail.component_name'))
    CommonComponentDetail_component_name = Column(Enum('AuctionTypeRuleGrp', 'BaseTradingRules', 'ExecInstRules', 'InstrumentScope', 'InstrumentScopeGrp', 'InstrumentScopeSecurityAltIDGrp', 'LotTypeRules', 'MarketDataFeedTypes', 'MarketSegmentScopeGrp', 'MatchRules', 'OrdTypeRules', 'PriceLimits', 'PriceRangeRuleGrp', 'QuoteSizeRuleGrp', 'RequestedPartyRoleGrp', 'RequestingPartyGrp', 'RequestingPartySubGrp', 'RoutingGrp', 'TickRules', 'TimeInForceRules', 'TradingSessionRules', name='PreTradeCommonComponentName'), ForeignKey('CommonComponentDetail.component_name'))
    

    def __repr__(self):
        return f"PreTradeLayoutRow(id={self.id},pre_layout_kind={self.pre_layout_kind},pre_layout_field_tag={self.pre_layout_field_tag},pre_layout_element_name={self.pre_layout_element_name},pre_layout_required={self.pre_layout_required},pre_layout_description={self.pre_layout_description},pre_layout_nested={self.pre_layout_nested},PreTradeMessageDetail_msg_type={self.PreTradeMessageDetail_msg_type},PreTradeComponentDetail_component_name={self.PreTradeComponentDetail_component_name},CommonComponentDetail_component_name={self.CommonComponentDetail_component_name},)"



    


class TradeBusinessArea(Base):
    """
    Tree-root container for the Trade (Orders and Executions) business area of FIX Latest.
    """
    __tablename__ = 'TradeBusinessArea'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    trade_area = Column(Enum('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='BusinessAreaEnum'), nullable=False )
    title = Column(Text())
    published_version = Column(Text())
    publisher = Column(Text())
    trade_introduction = Column(Text())
    trade_diagram_conventions = Column(Text())
    trade_message_diagram_template_url = Column(Text())
    trade_messages_overview_note = Column(Text())
    trade_components_overview_note = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeBusinessArea', source_slot='messages', mapping_type=None, target_class='TradeMessageEntry', target_slot='TradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "TradeMessageEntry", foreign_keys="[TradeMessageEntry.TradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeBusinessArea', source_slot='components', mapping_type=None, target_class='TradeComponentEntry', target_slot='TradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "TradeComponentEntry", foreign_keys="[TradeComponentEntry.TradeBusinessArea_id]")
    
    
    trade_common_components_rel = relationship( "TradeBusinessAreaTradeCommonComponents" )
    trade_common_components = association_proxy("trade_common_components_rel", "trade_common_components",
                                  creator=lambda x_: TradeBusinessAreaTradeCommonComponents(trade_common_components=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeBusinessArea', source_slot='trade_common_component_details', mapping_type=None, target_class='TradeCommonComponentDetail', target_slot='TradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    trade_common_component_details = relationship( "TradeCommonComponentDetail", foreign_keys="[TradeCommonComponentDetail.TradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeBusinessArea', source_slot='trade_footnotes', mapping_type=None, target_class='TradeComponentTableFootnote', target_slot='TradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    trade_footnotes = relationship( "TradeComponentTableFootnote", foreign_keys="[TradeComponentTableFootnote.TradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeBusinessArea', source_slot='trade_category_sections', mapping_type=None, target_class='TradeCategorySection', target_slot='TradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    trade_category_sections = relationship( "TradeCategorySection", foreign_keys="[TradeCategorySection.TradeBusinessArea_id]")
    
    
    # ManyToMany
    referenced_global_components = relationship( "GlobalComponent", secondary="TradeBusinessArea_referenced_global_components")
    

    def __repr__(self):
        return f"TradeBusinessArea(id={self.id},trade_area={self.trade_area},title={self.title},published_version={self.published_version},publisher={self.publisher},trade_introduction={self.trade_introduction},trade_diagram_conventions={self.trade_diagram_conventions},trade_message_diagram_template_url={self.trade_message_diagram_template_url},trade_messages_overview_note={self.trade_messages_overview_note},trade_components_overview_note={self.trade_components_overview_note},)"



    


class TradeMessageEntry(Base):
    """
    One row of the area-wide trade messages table.
    """
    __tablename__ = 'TradeMessageEntry'

    msg_type = Column(Text(), primary_key=True, nullable=False )
    message_name = Column(Text(), nullable=False )
    category = Column(Enum('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING', name='TradeCategoryEnum'), nullable=False )
    TradeBusinessArea_id = Column(Integer(), ForeignKey('TradeBusinessArea.id'))
    

    def __repr__(self):
        return f"TradeMessageEntry(msg_type={self.msg_type},message_name={self.message_name},category={self.category},TradeBusinessArea_id={self.TradeBusinessArea_id},)"



    


class TradeComponentEntry(Base):
    """
    One row of the area-wide trade components table.
    """
    __tablename__ = 'TradeComponentEntry'

    component_name = Column(Text(), primary_key=True, nullable=False )
    trade_repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='TradeComponentRepetition'), nullable=False )
    category = Column(Text(), nullable=False )
    trade_is_common = Column(Boolean())
    trade_footnote_number = Column(Integer())
    TradeBusinessArea_id = Column(Integer(), ForeignKey('TradeBusinessArea.id'))
    

    def __repr__(self):
        return f"TradeComponentEntry(component_name={self.component_name},trade_repetition={self.trade_repetition},category={self.category},trade_is_common={self.trade_is_common},trade_footnote_number={self.trade_footnote_number},TradeBusinessArea_id={self.TradeBusinessArea_id},)"



    


class TradeComponentTableFootnote(Base):
    """
    A footnote on the area-wide components table.
    """
    __tablename__ = 'TradeComponentTableFootnote'

    trade_footnote_number = Column(Integer(), primary_key=True, nullable=False )
    component_name = Column(Text(), nullable=False )
    trade_introduced_in = Column(Text(), nullable=False )
    trade_sole_category = Column(Enum('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING', name='TradeCategoryEnum'), nullable=False )
    trade_footnote_text = Column(Text())
    TradeBusinessArea_id = Column(Integer(), ForeignKey('TradeBusinessArea.id'))
    

    def __repr__(self):
        return f"TradeComponentTableFootnote(trade_footnote_number={self.trade_footnote_number},component_name={self.component_name},trade_introduced_in={self.trade_introduced_in},trade_sole_category={self.trade_sole_category},trade_footnote_text={self.trade_footnote_text},TradeBusinessArea_id={self.TradeBusinessArea_id},)"



    


class TradeCategorySection(Base):
    """
    A per-category sub-section of the Trade chapter.
    """
    __tablename__ = 'TradeCategorySection'

    category = Column(Enum('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING', name='TradeCategoryEnum'), primary_key=True, nullable=False )
    title = Column(Text())
    description = Column(Text())
    trade_category_background = Column(Text())
    trade_category_components_note = Column(Text())
    TradeBusinessArea_id = Column(Integer(), ForeignKey('TradeBusinessArea.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeCategorySection', source_slot='trade_message_groups', mapping_type=None, target_class='TradeMessageGroup', target_slot='TradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    trade_message_groups = relationship( "TradeMessageGroup", foreign_keys="[TradeMessageGroup.TradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeCategorySection', source_slot='messages', mapping_type=None, target_class='TradeMessageDetail', target_slot='TradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "TradeMessageDetail", foreign_keys="[TradeMessageDetail.TradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeCategorySection', source_slot='trade_category_specific_components', mapping_type=None, target_class='TradeComponentDetail', target_slot='TradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    trade_category_specific_components = relationship( "TradeComponentDetail", foreign_keys="[TradeComponentDetail.TradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeCategorySection', source_slot='trade_fragmentation_entries', mapping_type=None, target_class='TradeFragmentationEntry', target_slot='TradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    trade_fragmentation_entries = relationship( "TradeFragmentationEntry", foreign_keys="[TradeFragmentationEntry.TradeCategorySection_category]")
    

    def __repr__(self):
        return f"TradeCategorySection(category={self.category},title={self.title},description={self.description},trade_category_background={self.trade_category_background},trade_category_components_note={self.trade_category_components_note},TradeBusinessArea_id={self.TradeBusinessArea_id},)"



    


class TradeMessageDetail(Base):
    """
    Per-category message description.
    """
    __tablename__ = 'TradeMessageDetail'

    msg_type = Column(Text(), primary_key=True, nullable=False )
    message_name = Column(Text(), nullable=False )
    description = Column(Text())
    trade_layout_url = Column(Text())
    TradeCategorySection_category = Column(Enum('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING', name='TradeCategoryEnum'), ForeignKey('TradeCategorySection.category'))
    TradeMessageGroup_trade_group_title = Column(Text(), ForeignKey('TradeMessageGroup.trade_group_title'))
    TradeAppendixSection_trade_appendix_category = Column(Text(), ForeignKey('TradeAppendixSection.trade_appendix_category'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeMessageDetail', source_slot='trade_layout_rows', mapping_type=None, target_class='TradeLayoutRow', target_slot='TradeMessageDetail_msg_type', join_class=None, uses_join_table=None, multivalued=False)
    trade_layout_rows = relationship( "TradeLayoutRow", foreign_keys="[TradeLayoutRow.TradeMessageDetail_msg_type]")
    

    def __repr__(self):
        return f"TradeMessageDetail(msg_type={self.msg_type},message_name={self.message_name},description={self.description},trade_layout_url={self.trade_layout_url},TradeCategorySection_category={self.TradeCategorySection_category},TradeMessageGroup_trade_group_title={self.TradeMessageGroup_trade_group_title},TradeAppendixSection_trade_appendix_category={self.TradeAppendixSection_trade_appendix_category},)"



    


class TradeComponentDetail(Base):
    """
    Per-category component description.
    """
    __tablename__ = 'TradeComponentDetail'

    component_name = Column(Text(), primary_key=True, nullable=False )
    trade_repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='TradeComponentRepetition'))
    description = Column(Text())
    trade_layout_url = Column(Text())
    TradeCategorySection_category = Column(Enum('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING', name='TradeCategoryEnum'), ForeignKey('TradeCategorySection.category'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeComponentDetail', source_slot='trade_layout_rows', mapping_type=None, target_class='TradeLayoutRow', target_slot='TradeComponentDetail_component_name', join_class=None, uses_join_table=None, multivalued=False)
    trade_layout_rows = relationship( "TradeLayoutRow", foreign_keys="[TradeLayoutRow.TradeComponentDetail_component_name]")
    

    def __repr__(self):
        return f"TradeComponentDetail(component_name={self.component_name},trade_repetition={self.trade_repetition},description={self.description},trade_layout_url={self.trade_layout_url},TradeCategorySection_category={self.TradeCategorySection_category},)"



    


class TradeMessageGroup(Base):
    """
    Purpose-grouped sub-section inside a category's Messages sub-section (e.g. "New Order Single", "Execution Reports", "Order Cancel Requests" under Single/General Order Handling).
    """
    __tablename__ = 'TradeMessageGroup'

    trade_group_title = Column(Text(), primary_key=True, nullable=False )
    description = Column(Text())
    TradeCategorySection_category = Column(Enum('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING', name='TradeCategoryEnum'), ForeignKey('TradeCategorySection.category'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeMessageGroup', source_slot='messages', mapping_type=None, target_class='TradeMessageDetail', target_slot='TradeMessageGroup_trade_group_title', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "TradeMessageDetail", foreign_keys="[TradeMessageDetail.TradeMessageGroup_trade_group_title]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeMessageGroup', source_slot='trade_ord_status_precedence_entries', mapping_type=None, target_class='TradeOrdStatusPrecedenceEntry', target_slot='TradeMessageGroup_trade_group_title', join_class=None, uses_join_table=None, multivalued=False)
    trade_ord_status_precedence_entries = relationship( "TradeOrdStatusPrecedenceEntry", foreign_keys="[TradeOrdStatusPrecedenceEntry.TradeMessageGroup_trade_group_title]")
    

    def __repr__(self):
        return f"TradeMessageGroup(trade_group_title={self.trade_group_title},description={self.description},TradeCategorySection_category={self.TradeCategorySection_category},)"



    


class TradeCommonComponentDetail(Base):
    """
    Per-common-component description from the chapter's final "Common Components" section.
    """
    __tablename__ = 'TradeCommonComponentDetail'

    component_name = Column(Enum('DisclosureInstructionGrp', 'DiscretionInstructions', 'PegInstructions', 'PreAllocGrp', 'StrategyParametersGrp', 'TriggeringInstruction', name='TradeCommonComponentName'), primary_key=True, nullable=False )
    trade_repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='TradeComponentRepetition'))
    description = Column(Text())
    trade_layout_url = Column(Text())
    TradeBusinessArea_id = Column(Integer(), ForeignKey('TradeBusinessArea.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeCommonComponentDetail', source_slot='trade_layout_rows', mapping_type=None, target_class='TradeLayoutRow', target_slot='TradeCommonComponentDetail_component_name', join_class=None, uses_join_table=None, multivalued=False)
    trade_layout_rows = relationship( "TradeLayoutRow", foreign_keys="[TradeLayoutRow.TradeCommonComponentDetail_component_name]")
    

    def __repr__(self):
        return f"TradeCommonComponentDetail(component_name={self.component_name},trade_repetition={self.trade_repetition},description={self.description},trade_layout_url={self.trade_layout_url},TradeBusinessArea_id={self.TradeBusinessArea_id},)"



    


class TradeLayoutRow(Base):
    """
    One row of the layout table published in the Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    __tablename__ = 'TradeLayoutRow'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    trade_layout_kind = Column(Enum('FIELD', 'COMPONENT', name='TradeLayoutRowKindEnum'), nullable=False )
    trade_layout_field_tag = Column(Integer())
    trade_layout_element_name = Column(Text(), nullable=False )
    trade_layout_required = Column(Boolean())
    trade_layout_description = Column(Text())
    trade_layout_nested = Column(Boolean())
    TradeMessageDetail_msg_type = Column(Text(), ForeignKey('TradeMessageDetail.msg_type'))
    TradeComponentDetail_component_name = Column(Text(), ForeignKey('TradeComponentDetail.component_name'))
    TradeCommonComponentDetail_component_name = Column(Enum('DisclosureInstructionGrp', 'DiscretionInstructions', 'PegInstructions', 'PreAllocGrp', 'StrategyParametersGrp', 'TriggeringInstruction', name='TradeCommonComponentName'), ForeignKey('TradeCommonComponentDetail.component_name'))
    

    def __repr__(self):
        return f"TradeLayoutRow(id={self.id},trade_layout_kind={self.trade_layout_kind},trade_layout_field_tag={self.trade_layout_field_tag},trade_layout_element_name={self.trade_layout_element_name},trade_layout_required={self.trade_layout_required},trade_layout_description={self.trade_layout_description},trade_layout_nested={self.trade_layout_nested},TradeMessageDetail_msg_type={self.TradeMessageDetail_msg_type},TradeComponentDetail_component_name={self.TradeComponentDetail_component_name},TradeCommonComponentDetail_component_name={self.TradeCommonComponentDetail_component_name},)"



    


class TradeOrdStatusPrecedenceEntry(Base):
    """
    One row of the OrdStatus(39) precedence table published in the Execution Reports purpose-group of the Single/General Order Handling category. Defines the precedence ranking used to resolve simultaneous state transitions on an order, paired with the human-readable OrdStatus label and its descriptive prose.
    """
    __tablename__ = 'TradeOrdStatusPrecedenceEntry'

    trade_ord_status_precedence = Column(Integer(), nullable=False )
    trade_ord_status_label = Column(Text(), primary_key=True, nullable=False )
    description = Column(Text())
    TradeMessageGroup_trade_group_title = Column(Text(), ForeignKey('TradeMessageGroup.trade_group_title'))
    

    def __repr__(self):
        return f"TradeOrdStatusPrecedenceEntry(trade_ord_status_precedence={self.trade_ord_status_precedence},trade_ord_status_label={self.trade_ord_status_label},description={self.description},TradeMessageGroup_trade_group_title={self.TradeMessageGroup_trade_group_title},)"



    


class TradeFragmentationEntry(Base):
    """
    One row of a fragmentation table published in a Trade category (currently only List/Program/Basket Trading) identifying a message that may be fragmented, the "Total Entries" field used to indicate the total count across all fragments of the batch, and the verbatim description of the repeating group that may be fragmented.
    """
    __tablename__ = 'TradeFragmentationEntry'

    trade_fragmentation_message = Column(Text(), primary_key=True, nullable=False )
    trade_fragmentation_total_entries_field = Column(Text(), nullable=False )
    trade_fragmentation_repeating_group = Column(Text(), nullable=False )
    TradeCategorySection_category = Column(Enum('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING', name='TradeCategoryEnum'), ForeignKey('TradeCategorySection.category'))
    

    def __repr__(self):
        return f"TradeFragmentationEntry(trade_fragmentation_message={self.trade_fragmentation_message},trade_fragmentation_total_entries_field={self.trade_fragmentation_total_entries_field},trade_fragmentation_repeating_group={self.trade_fragmentation_repeating_group},TradeCategorySection_category={self.TradeCategorySection_category},)"



    


class TradeAppendix(Base):
    """
    Tree-root container for the Trade Appendix — the spec companion document that publishes the full message- and component-layout tables for every message and component used in the Trade business area, organized into one "Appendix – <X> Category" sub-section per Trade category plus a final "Appendix – Common Category" sub-section covering the layouts of the chapter's common components.
    """
    __tablename__ = 'TradeAppendix'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    title = Column(Text())
    published_version = Column(Text())
    publisher = Column(Text())
    description = Column(Text())
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeAppendix', source_slot='trade_appendix_sections', mapping_type=None, target_class='TradeAppendixSection', target_slot='TradeAppendix_id', join_class=None, uses_join_table=None, multivalued=False)
    trade_appendix_sections = relationship( "TradeAppendixSection", foreign_keys="[TradeAppendixSection.TradeAppendix_id]")
    

    def __repr__(self):
        return f"TradeAppendix(id={self.id},title={self.title},published_version={self.published_version},publisher={self.publisher},description={self.description},)"



    


class TradeAppendixSection(Base):
    """
    One "Appendix – <X> Category" sub-section of the Trade Appendix. Bundles the per-message layout tables (TradeMessageDetail) and per-component layout tables (TradeComponentDetail) for messages and components that belong to one Trade category — or, for the synthetic "Common" section, the layouts of the chapter's common components.
    """
    __tablename__ = 'TradeAppendixSection'

    trade_appendix_category = Column(Text(), primary_key=True, nullable=False )
    title = Column(Text())
    description = Column(Text())
    TradeAppendix_id = Column(Integer(), ForeignKey('TradeAppendix.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='TradeAppendixSection', source_slot='messages', mapping_type=None, target_class='TradeMessageDetail', target_slot='TradeAppendixSection_trade_appendix_category', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "TradeMessageDetail", foreign_keys="[TradeMessageDetail.TradeAppendixSection_trade_appendix_category]")
    
    
    # ManyToMany
    components = relationship( "TradeComponentDetail", secondary="TradeAppendixSection_components")
    

    def __repr__(self):
        return f"TradeAppendixSection(trade_appendix_category={self.trade_appendix_category},title={self.title},description={self.description},TradeAppendix_id={self.TradeAppendix_id},)"



    


class PostTradeBusinessArea(Base):
    """
    Tree-root container for the Post-Trade business area of FIX Latest.
    """
    __tablename__ = 'PostTradeBusinessArea'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    area = Column(Enum('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='BusinessAreaEnum'), nullable=False )
    title = Column(Text())
    published_version = Column(Text())
    publisher = Column(Text())
    post_introduction = Column(Text())
    diagram_conventions = Column(Text())
    messages_overview_note = Column(Text())
    components_overview_note = Column(Text())
    
    
    post_common_components_rel = relationship( "PostTradeBusinessAreaPostCommonComponents" )
    post_common_components = association_proxy("post_common_components_rel", "post_common_components",
                                  creator=lambda x_: PostTradeBusinessAreaPostCommonComponents(post_common_components=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeBusinessArea', source_slot='messages', mapping_type=None, target_class='PostTradeMessageEntry', target_slot='PostTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "PostTradeMessageEntry", foreign_keys="[PostTradeMessageEntry.PostTradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeBusinessArea', source_slot='components', mapping_type=None, target_class='PostTradeComponentEntry', target_slot='PostTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "PostTradeComponentEntry", foreign_keys="[PostTradeComponentEntry.PostTradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeBusinessArea', source_slot='post_footnotes', mapping_type=None, target_class='PostTradeComponentTableFootnote', target_slot='PostTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    post_footnotes = relationship( "PostTradeComponentTableFootnote", foreign_keys="[PostTradeComponentTableFootnote.PostTradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeBusinessArea', source_slot='post_category_sections', mapping_type=None, target_class='PostTradeCategorySection', target_slot='PostTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    post_category_sections = relationship( "PostTradeCategorySection", foreign_keys="[PostTradeCategorySection.PostTradeBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeBusinessArea', source_slot='post_common_component_details', mapping_type=None, target_class='PostTradeCommonComponentDetail', target_slot='PostTradeBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    post_common_component_details = relationship( "PostTradeCommonComponentDetail", foreign_keys="[PostTradeCommonComponentDetail.PostTradeBusinessArea_id]")
    
    
    # ManyToMany
    referenced_global_components = relationship( "GlobalComponent", secondary="PostTradeBusinessArea_referenced_global_components")
    

    def __repr__(self):
        return f"PostTradeBusinessArea(id={self.id},area={self.area},title={self.title},published_version={self.published_version},publisher={self.publisher},post_introduction={self.post_introduction},diagram_conventions={self.diagram_conventions},messages_overview_note={self.messages_overview_note},components_overview_note={self.components_overview_note},)"



    


class PostTradeMessageEntry(Base):
    """
    One row of the area-wide "Messages for Post-Trade Business Area" table.
    """
    __tablename__ = 'PostTradeMessageEntry'

    msg_type = Column(Text(), primary_key=True, nullable=False )
    message_name = Column(Text(), nullable=False )
    category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), nullable=False )
    PostTradeBusinessArea_id = Column(Integer(), ForeignKey('PostTradeBusinessArea.id'))
    

    def __repr__(self):
        return f"PostTradeMessageEntry(msg_type={self.msg_type},message_name={self.message_name},category={self.category},PostTradeBusinessArea_id={self.PostTradeBusinessArea_id},)"



    


class PostTradeComponentEntry(Base):
    """
    One row of the area-wide "Components for Post-Trade Business Area" table.
    """
    __tablename__ = 'PostTradeComponentEntry'

    component_name = Column(Text(), primary_key=True, nullable=False )
    repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='ComponentRepetition'), nullable=False )
    category = Column(Text(), nullable=False )
    is_common = Column(Boolean())
    footnote_number = Column(Integer())
    PostTradeBusinessArea_id = Column(Integer(), ForeignKey('PostTradeBusinessArea.id'))
    

    def __repr__(self):
        return f"PostTradeComponentEntry(component_name={self.component_name},repetition={self.repetition},category={self.category},is_common={self.is_common},footnote_number={self.footnote_number},PostTradeBusinessArea_id={self.PostTradeBusinessArea_id},)"



    


class PostTradeComponentTableFootnote(Base):
    """
    A footnote attached to a row of the area-wide Post-Trade components table.
    """
    __tablename__ = 'PostTradeComponentTableFootnote'

    footnote_number = Column(Integer(), primary_key=True, nullable=False )
    component_name = Column(Text(), nullable=False )
    introduced_in = Column(Text(), nullable=False )
    post_sole_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), nullable=False )
    text = Column(Text())
    PostTradeBusinessArea_id = Column(Integer(), ForeignKey('PostTradeBusinessArea.id'))
    

    def __repr__(self):
        return f"PostTradeComponentTableFootnote(footnote_number={self.footnote_number},component_name={self.component_name},introduced_in={self.introduced_in},post_sole_category={self.post_sole_category},text={self.text},PostTradeBusinessArea_id={self.PostTradeBusinessArea_id},)"



    


class PostTradeCategorySection(Base):
    """
    A "Category – <name>" sub-section of the Post-Trade chapter.
    """
    __tablename__ = 'PostTradeCategorySection'

    category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), primary_key=True, nullable=False )
    title = Column(Text())
    description = Column(Text())
    category_components_note = Column(Text())
    PostTradeBusinessArea_id = Column(Integer(), ForeignKey('PostTradeBusinessArea.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCategorySection', source_slot='post_message_groups', mapping_type=None, target_class='PostTradeMessageGroup', target_slot='PostTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    post_message_groups = relationship( "PostTradeMessageGroup", foreign_keys="[PostTradeMessageGroup.PostTradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCategorySection', source_slot='messages', mapping_type=None, target_class='PostTradeMessageDetail', target_slot='PostTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "PostTradeMessageDetail", foreign_keys="[PostTradeMessageDetail.PostTradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCategorySection', source_slot='post_category_specific_components', mapping_type=None, target_class='PostTradeComponentDetail', target_slot='PostTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    post_category_specific_components = relationship( "PostTradeComponentDetail", foreign_keys="[PostTradeComponentDetail.PostTradeCategorySection_category]")
    
    
    allocation_scenarios_rel = relationship( "PostTradeCategorySectionAllocationScenarios" )
    allocation_scenarios = association_proxy("allocation_scenarios_rel", "allocation_scenarios",
                                  creator=lambda x_: PostTradeCategorySectionAllocationScenarios(allocation_scenarios=x_))
    
    
    allocation_roles_rel = relationship( "PostTradeCategorySectionAllocationRoles" )
    allocation_roles = association_proxy("allocation_roles_rel", "allocation_roles",
                                  creator=lambda x_: PostTradeCategorySectionAllocationRoles(allocation_roles=x_))
    
    
    post_trade_allocation_pricing_methods_rel = relationship( "PostTradeCategorySectionPostTradeAllocationPricingMethods" )
    post_trade_allocation_pricing_methods = association_proxy("post_trade_allocation_pricing_methods_rel", "post_trade_allocation_pricing_methods",
                                  creator=lambda x_: PostTradeCategorySectionPostTradeAllocationPricingMethods(post_trade_allocation_pricing_methods=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCategorySection', source_slot='allocation_status_descriptions', mapping_type=None, target_class='AllocationStatusDescription', target_slot='PostTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    allocation_status_descriptions = relationship( "AllocationStatusDescription", foreign_keys="[AllocationStatusDescription.PostTradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCategorySection', source_slot='fragmentation_field_map', mapping_type=None, target_class='AllocationFragmentationFieldMap', target_slot='PostTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    fragmentation_field_map = relationship( "AllocationFragmentationFieldMap", foreign_keys="[AllocationFragmentationFieldMap.PostTradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCategorySection', source_slot='trade_capture_report_usages', mapping_type=None, target_class='TradeCaptureReportUsage', target_slot='PostTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    trade_capture_report_usages = relationship( "TradeCaptureReportUsage", foreign_keys="[TradeCaptureReportUsage.PostTradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCategorySection', source_slot='trade_capture_report_identifier_rules', mapping_type=None, target_class='TradeCaptureReportIdentifierRule', target_slot='PostTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    trade_capture_report_identifier_rules = relationship( "TradeCaptureReportIdentifierRule", foreign_keys="[TradeCaptureReportIdentifierRule.PostTradeCategorySection_category]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCategorySection', source_slot='registration_status_descriptions', mapping_type=None, target_class='RegistrationStatusDescription', target_slot='PostTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    registration_status_descriptions = relationship( "RegistrationStatusDescription", foreign_keys="[RegistrationStatusDescription.PostTradeCategorySection_category]")
    
    
    clearing_services_for_position_management_rel = relationship( "PostTradeCategorySectionClearingServicesForPositionManagement" )
    clearing_services_for_position_management = association_proxy("clearing_services_for_position_management_rel", "clearing_services_for_position_management",
                                  creator=lambda x_: PostTradeCategorySectionClearingServicesForPositionManagement(clearing_services_for_position_management=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCategorySection', source_slot='clearing_services_for_post_trade_processing', mapping_type=None, target_class='ClearingServicePostTradeProcessingFormat', target_slot='PostTradeCategorySection_category', join_class=None, uses_join_table=None, multivalued=False)
    clearing_services_for_post_trade_processing = relationship( "ClearingServicePostTradeProcessingFormat", foreign_keys="[ClearingServicePostTradeProcessingFormat.PostTradeCategorySection_category]")
    
    
    collateral_management_usages_rel = relationship( "PostTradeCategorySectionCollateralManagementUsages" )
    collateral_management_usages = association_proxy("collateral_management_usages_rel", "collateral_management_usages",
                                  creator=lambda x_: PostTradeCategorySectionCollateralManagementUsages(collateral_management_usages=x_))
    
    
    collateral_assignment_purposes_rel = relationship( "PostTradeCategorySectionCollateralAssignmentPurposes" )
    collateral_assignment_purposes = association_proxy("collateral_assignment_purposes_rel", "collateral_assignment_purposes",
                                  creator=lambda x_: PostTradeCategorySectionCollateralAssignmentPurposes(collateral_assignment_purposes=x_))
    

    def __repr__(self):
        return f"PostTradeCategorySection(category={self.category},title={self.title},description={self.description},category_components_note={self.category_components_note},PostTradeBusinessArea_id={self.PostTradeBusinessArea_id},)"



    


class PostTradeMessageGroup(Base):
    """
    A purpose-themed grouping of messages within a Post-Trade category (e.g. "Allocation Instructions").
    """
    __tablename__ = 'PostTradeMessageGroup'

    group_title = Column(Text(), primary_key=True, nullable=False )
    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeMessageGroup', source_slot='messages', mapping_type=None, target_class='PostTradeMessageDetail', target_slot='PostTradeMessageGroup_group_title', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "PostTradeMessageDetail", foreign_keys="[PostTradeMessageDetail.PostTradeMessageGroup_group_title]")
    

    def __repr__(self):
        return f"PostTradeMessageGroup(group_title={self.group_title},PostTradeCategorySection_category={self.PostTradeCategorySection_category},)"



    


class PostTradeMessageDetail(Base):
    """
    Per-message description block from a Post-Trade category section.
    """
    __tablename__ = 'PostTradeMessageDetail'

    msg_type = Column(Text(), primary_key=True, nullable=False )
    message_name = Column(Text(), nullable=False )
    description = Column(Text())
    layout_url = Column(Text())
    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'))
    PostTradeMessageGroup_group_title = Column(Text(), ForeignKey('PostTradeMessageGroup.group_title'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeMessageDetail', source_slot='post_layout_rows', mapping_type=None, target_class='PostTradeLayoutRow', target_slot='PostTradeMessageDetail_msg_type', join_class=None, uses_join_table=None, multivalued=False)
    post_layout_rows = relationship( "PostTradeLayoutRow", foreign_keys="[PostTradeLayoutRow.PostTradeMessageDetail_msg_type]")
    

    def __repr__(self):
        return f"PostTradeMessageDetail(msg_type={self.msg_type},message_name={self.message_name},description={self.description},layout_url={self.layout_url},PostTradeCategorySection_category={self.PostTradeCategorySection_category},PostTradeMessageGroup_group_title={self.PostTradeMessageGroup_group_title},)"



    


class PostTradeComponentDetail(Base):
    """
    Per-component description block from a Post-Trade category section's Components sub-section.
    """
    __tablename__ = 'PostTradeComponentDetail'

    component_name = Column(Text(), primary_key=True, nullable=False )
    repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='ComponentRepetition'))
    description = Column(Text())
    layout_url = Column(Text())
    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeComponentDetail', source_slot='post_layout_rows', mapping_type=None, target_class='PostTradeLayoutRow', target_slot='PostTradeComponentDetail_component_name', join_class=None, uses_join_table=None, multivalued=False)
    post_layout_rows = relationship( "PostTradeLayoutRow", foreign_keys="[PostTradeLayoutRow.PostTradeComponentDetail_component_name]")
    

    def __repr__(self):
        return f"PostTradeComponentDetail(component_name={self.component_name},repetition={self.repetition},description={self.description},layout_url={self.layout_url},PostTradeCategorySection_category={self.PostTradeCategorySection_category},)"



    


class PostTradeCommonComponentDetail(Base):
    """
    Per-common-component description block from the chapter's final "Common Components" section.
    """
    __tablename__ = 'PostTradeCommonComponentDetail'

    component_name = Column(Enum('AllocCommissionDataGrp', 'AllocRegulatoryTradeIDGrp', 'ClrInstGrp', 'CollateralAmountGrp', 'CollateralReinvestmentGrp', 'DlvyInstGrp', 'ExecAllocGrp', 'MarginAmount', 'OrdAllocGrp', 'PositionAmountData', 'SettlDetails', 'SettlInstructionsData', 'SettlParties', 'SettlPtysSubGrp', 'TradeAllocAmtGrp', 'TransactionAttributeGrp', name='PostTradeCommonComponentName'), primary_key=True, nullable=False )
    repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='ComponentRepetition'))
    description = Column(Text())
    layout_url = Column(Text())
    PostTradeBusinessArea_id = Column(Integer(), ForeignKey('PostTradeBusinessArea.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PostTradeCommonComponentDetail', source_slot='post_layout_rows', mapping_type=None, target_class='PostTradeLayoutRow', target_slot='PostTradeCommonComponentDetail_component_name', join_class=None, uses_join_table=None, multivalued=False)
    post_layout_rows = relationship( "PostTradeLayoutRow", foreign_keys="[PostTradeLayoutRow.PostTradeCommonComponentDetail_component_name]")
    

    def __repr__(self):
        return f"PostTradeCommonComponentDetail(component_name={self.component_name},repetition={self.repetition},description={self.description},layout_url={self.layout_url},PostTradeBusinessArea_id={self.PostTradeBusinessArea_id},)"



    


class AllocationStatusDescription(Base):
    """
    One row of the AllocStatus(87) value/description table.
    """
    __tablename__ = 'AllocationStatusDescription'

    status_code = Column(Text(), primary_key=True, nullable=False )
    status_label = Column(Text(), nullable=False )
    description = Column(Text())
    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'))
    

    def __repr__(self):
        return f"AllocationStatusDescription(status_code={self.status_code},status_label={self.status_label},description={self.description},PostTradeCategorySection_category={self.PostTradeCategorySection_category},)"



    


class AllocationFragmentationFieldMap(Base):
    """
    One row of the table mapping an allocation message to its fragmentation-related fields.
    """
    __tablename__ = 'AllocationFragmentationFieldMap'

    msg_type = Column(Text(), primary_key=True, nullable=False )
    message_name = Column(Text(), nullable=False )
    total_count_field = Column(Text(), nullable=False )
    fragment_count_field = Column(Text(), nullable=False )
    principal_message_reference = Column(Text(), nullable=False )
    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'))
    

    def __repr__(self):
        return f"AllocationFragmentationFieldMap(msg_type={self.msg_type},message_name={self.message_name},total_count_field={self.total_count_field},fragment_count_field={self.fragment_count_field},principal_message_reference={self.principal_message_reference},PostTradeCategorySection_category={self.PostTradeCategorySection_category},)"



    


class TradeCaptureReportUsage(Base):
    """
    One documented usage of the TradeCaptureReport(35=AE) message.
    """
    __tablename__ = 'TradeCaptureReportUsage'

    status_label = Column(Text(), primary_key=True, nullable=False )
    description = Column(Text())
    identifier_role = Column(Enum('TRADE_REPORT_ID', 'TRADE_ID', 'TRADE_REPORT_REF_ID', 'SECONDARY_TRADE_ID', name='TradeCaptureReportIdentifierRoleEnum'))
    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'))
    

    def __repr__(self):
        return f"TradeCaptureReportUsage(status_label={self.status_label},description={self.description},identifier_role={self.identifier_role},PostTradeCategorySection_category={self.PostTradeCategorySection_category},)"



    


class TradeCaptureReportIdentifierRule(Base):
    """
    A rule governing one of the TradeCaptureReport(35=AE) identifier fields.
    """
    __tablename__ = 'TradeCaptureReportIdentifierRule'

    identifier_role = Column(Enum('TRADE_REPORT_ID', 'TRADE_ID', 'TRADE_REPORT_REF_ID', 'SECONDARY_TRADE_ID', name='TradeCaptureReportIdentifierRoleEnum'), primary_key=True, nullable=False )
    description = Column(Text())
    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'))
    

    def __repr__(self):
        return f"TradeCaptureReportIdentifierRule(identifier_role={self.identifier_role},description={self.description},PostTradeCategorySection_category={self.PostTradeCategorySection_category},)"



    


class RegistrationStatusDescription(Base):
    """
    One row of the RegistStatus(506) value/description table.
    """
    __tablename__ = 'RegistrationStatusDescription'

    status_code = Column(Text(), primary_key=True, nullable=False )
    status_label = Column(Text(), nullable=False )
    description = Column(Text())
    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'))
    

    def __repr__(self):
        return f"RegistrationStatusDescription(status_code={self.status_code},status_label={self.status_label},description={self.description},PostTradeCategorySection_category={self.PostTradeCategorySection_category},)"



    


class ClearingServicePostTradeProcessingFormat(Base):
    """
    One message-format row from the Post-Trade Processing Clearing Services section, with its supported actions.
    """
    __tablename__ = 'ClearingServicePostTradeProcessingFormat'

    message_format = Column(Enum('ETP', 'GIVE_UP', 'EXCHANGE_FOR_PHYSICAL', 'AVERAGE_PRICE_SYSTEM', 'MUTUAL_OFFSET_SYSTEM', 'TRADE_ENTRY_EDIT', name='ClearingServiceForPostTradeProcessingEnum'), primary_key=True, nullable=False )
    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'))
    
    
    supported_actions_rel = relationship( "ClearingServicePostTradeProcessingFormatSupportedActions" )
    supported_actions = association_proxy("supported_actions_rel", "supported_actions",
                                  creator=lambda x_: ClearingServicePostTradeProcessingFormatSupportedActions(supported_actions=x_))
    

    def __repr__(self):
        return f"ClearingServicePostTradeProcessingFormat(message_format={self.message_format},PostTradeCategorySection_category={self.PostTradeCategorySection_category},)"



    


class PostTradeLayoutRow(Base):
    """
    One row of the layout table published in the Post-Trade Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    __tablename__ = 'PostTradeLayoutRow'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    post_layout_kind = Column(Enum('FIELD', 'COMPONENT', name='PostTradeLayoutRowKindEnum'), nullable=False )
    post_layout_field_tag = Column(Integer())
    post_layout_element_name = Column(Text(), nullable=False )
    post_layout_required = Column(Boolean())
    post_layout_description = Column(Text())
    post_layout_nested = Column(Boolean())
    PostTradeMessageDetail_msg_type = Column(Text(), ForeignKey('PostTradeMessageDetail.msg_type'))
    PostTradeComponentDetail_component_name = Column(Text(), ForeignKey('PostTradeComponentDetail.component_name'))
    PostTradeCommonComponentDetail_component_name = Column(Enum('AllocCommissionDataGrp', 'AllocRegulatoryTradeIDGrp', 'ClrInstGrp', 'CollateralAmountGrp', 'CollateralReinvestmentGrp', 'DlvyInstGrp', 'ExecAllocGrp', 'MarginAmount', 'OrdAllocGrp', 'PositionAmountData', 'SettlDetails', 'SettlInstructionsData', 'SettlParties', 'SettlPtysSubGrp', 'TradeAllocAmtGrp', 'TransactionAttributeGrp', name='PostTradeCommonComponentName'), ForeignKey('PostTradeCommonComponentDetail.component_name'))
    

    def __repr__(self):
        return f"PostTradeLayoutRow(id={self.id},post_layout_kind={self.post_layout_kind},post_layout_field_tag={self.post_layout_field_tag},post_layout_element_name={self.post_layout_element_name},post_layout_required={self.post_layout_required},post_layout_description={self.post_layout_description},post_layout_nested={self.post_layout_nested},PostTradeMessageDetail_msg_type={self.PostTradeMessageDetail_msg_type},PostTradeComponentDetail_component_name={self.PostTradeComponentDetail_component_name},PostTradeCommonComponentDetail_component_name={self.PostTradeCommonComponentDetail_component_name},)"



    


class InfrastructureBusinessArea(Base):
    """
    Tree-root container for the Infrastructure business area of FIX Latest.
    """
    __tablename__ = 'InfrastructureBusinessArea'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    area = Column(Enum('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='BusinessAreaEnum'), nullable=False )
    title = Column(Text())
    published_version = Column(Text())
    publisher = Column(Text())
    infra_introduction = Column(Text())
    diagram_conventions = Column(Text())
    messages_overview_note = Column(Text())
    components_overview_note = Column(Text())
    
    
    infra_common_components_rel = relationship( "InfrastructureBusinessAreaInfraCommonComponents" )
    infra_common_components = association_proxy("infra_common_components_rel", "infra_common_components",
                                  creator=lambda x_: InfrastructureBusinessAreaInfraCommonComponents(infra_common_components=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='messages', mapping_type=None, target_class='InfrastructureMessageEntry', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "InfrastructureMessageEntry", foreign_keys="[InfrastructureMessageEntry.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='components', mapping_type=None, target_class='InfrastructureComponentEntry', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    components = relationship( "InfrastructureComponentEntry", foreign_keys="[InfrastructureComponentEntry.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='infra_footnotes', mapping_type=None, target_class='InfrastructureComponentTableFootnote', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    infra_footnotes = relationship( "InfrastructureComponentTableFootnote", foreign_keys="[InfrastructureComponentTableFootnote.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='infra_category_sections', mapping_type=None, target_class='InfrastructureCategorySection', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    infra_category_sections = relationship( "InfrastructureCategorySection", foreign_keys="[InfrastructureCategorySection.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='standard_responses_pre_trade', mapping_type=None, target_class='StandardResponseMapping', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    standard_responses_pre_trade = relationship( "StandardResponseMapping", foreign_keys="[StandardResponseMapping.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='standard_responses_trade', mapping_type=None, target_class='StandardResponseMapping', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    standard_responses_trade = relationship( "StandardResponseMapping", foreign_keys="[StandardResponseMapping.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='standard_responses_post_trade', mapping_type=None, target_class='StandardResponseMapping', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    standard_responses_post_trade = relationship( "StandardResponseMapping", foreign_keys="[StandardResponseMapping.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='key_fields_pre_trade', mapping_type=None, target_class='ApplicationMessageReferenceKey', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    key_fields_pre_trade = relationship( "ApplicationMessageReferenceKey", foreign_keys="[ApplicationMessageReferenceKey.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='key_fields_trade', mapping_type=None, target_class='ApplicationMessageReferenceKey', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    key_fields_trade = relationship( "ApplicationMessageReferenceKey", foreign_keys="[ApplicationMessageReferenceKey.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='key_fields_post_trade', mapping_type=None, target_class='ApplicationMessageReferenceKey', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    key_fields_post_trade = relationship( "ApplicationMessageReferenceKey", foreign_keys="[ApplicationMessageReferenceKey.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='business_reject_reason_descriptions', mapping_type=None, target_class='BusinessRejectReasonDescription', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    business_reject_reason_descriptions = relationship( "BusinessRejectReasonDescription", foreign_keys="[BusinessRejectReasonDescription.InfrastructureBusinessArea_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureBusinessArea', source_slot='infra_global_components', mapping_type=None, target_class='InfrastructureGlobalComponentReference', target_slot='InfrastructureBusinessArea_id', join_class=None, uses_join_table=None, multivalued=False)
    infra_global_components = relationship( "InfrastructureGlobalComponentReference", foreign_keys="[InfrastructureGlobalComponentReference.InfrastructureBusinessArea_id]")
    
    
    # ManyToMany
    referenced_global_components = relationship( "GlobalComponent", secondary="InfrastructureBusinessArea_referenced_global_components")
    

    def __repr__(self):
        return f"InfrastructureBusinessArea(id={self.id},area={self.area},title={self.title},published_version={self.published_version},publisher={self.publisher},infra_introduction={self.infra_introduction},diagram_conventions={self.diagram_conventions},messages_overview_note={self.messages_overview_note},components_overview_note={self.components_overview_note},)"



    


class InfrastructureMessageEntry(Base):
    """
    One row of the area-wide "Messages for Infrastructure Business Area" table.
    """
    __tablename__ = 'InfrastructureMessageEntry'

    msg_type = Column(Text(), primary_key=True, nullable=False )
    message_name = Column(Text(), nullable=False )
    category = Column(Enum('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING', name='InfrastructureCategoryEnum'), nullable=False )
    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'))
    

    def __repr__(self):
        return f"InfrastructureMessageEntry(msg_type={self.msg_type},message_name={self.message_name},category={self.category},InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},)"



    


class InfrastructureComponentEntry(Base):
    """
    One row of the area-wide "Components for Infrastructure Business Area" table.
    """
    __tablename__ = 'InfrastructureComponentEntry'

    component_name = Column(Text(), primary_key=True, nullable=False )
    repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='ComponentRepetition'), nullable=False )
    category = Column(Enum('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING', name='InfrastructureCategoryEnum'), nullable=False )
    footnote_number = Column(Integer())
    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'))
    

    def __repr__(self):
        return f"InfrastructureComponentEntry(component_name={self.component_name},repetition={self.repetition},category={self.category},footnote_number={self.footnote_number},InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},)"



    


class InfrastructureComponentTableFootnote(Base):
    """
    A footnote attached to a row of the area-wide Infrastructure components table.
    """
    __tablename__ = 'InfrastructureComponentTableFootnote'

    footnote_number = Column(Integer(), primary_key=True, nullable=False )
    component_name = Column(Text(), nullable=False )
    introduced_in = Column(Text(), nullable=False )
    infra_sole_category = Column(Enum('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING', name='InfrastructureCategoryEnum'), nullable=False )
    text = Column(Text())
    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'))
    

    def __repr__(self):
        return f"InfrastructureComponentTableFootnote(footnote_number={self.footnote_number},component_name={self.component_name},introduced_in={self.introduced_in},infra_sole_category={self.infra_sole_category},text={self.text},InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},)"



    


class InfrastructureCategorySection(Base):
    """
    A "Category – <name>" sub-section of the Infrastructure chapter.
    """
    __tablename__ = 'InfrastructureCategorySection'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    category = Column(Enum('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING', name='InfrastructureCategoryEnum'), nullable=False )
    title = Column(Text())
    description = Column(Text())
    category_components_note = Column(Text())
    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureCategorySection', source_slot='messages', mapping_type=None, target_class='InfrastructureMessageDetail', target_slot='InfrastructureCategorySection_id', join_class=None, uses_join_table=None, multivalued=False)
    messages = relationship( "InfrastructureMessageDetail", foreign_keys="[InfrastructureMessageDetail.InfrastructureCategorySection_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureCategorySection', source_slot='infra_category_specific_components', mapping_type=None, target_class='InfrastructureComponentDetail', target_slot='InfrastructureCategorySection_id', join_class=None, uses_join_table=None, multivalued=False)
    infra_category_specific_components = relationship( "InfrastructureComponentDetail", foreign_keys="[InfrastructureComponentDetail.InfrastructureCategorySection_id]")
    
    
    network_status_scenarios_rel = relationship( "InfrastructureCategorySectionNetworkStatusScenarios" )
    network_status_scenarios = association_proxy("network_status_scenarios_rel", "network_status_scenarios",
                                  creator=lambda x_: InfrastructureCategorySectionNetworkStatusScenarios(network_status_scenarios=x_))
    
    
    network_request_types_referenced_rel = relationship( "InfrastructureCategorySectionNetworkRequestTypesReferenced" )
    network_request_types_referenced = association_proxy("network_request_types_referenced_rel", "network_request_types_referenced",
                                  creator=lambda x_: InfrastructureCategorySectionNetworkRequestTypesReferenced(network_request_types_referenced=x_))
    
    
    application_message_report_uses_rel = relationship( "InfrastructureCategorySectionApplicationMessageReportUses" )
    application_message_report_uses = association_proxy("application_message_report_uses_rel", "application_message_report_uses",
                                  creator=lambda x_: InfrastructureCategorySectionApplicationMessageReportUses(application_message_report_uses=x_))
    

    def __repr__(self):
        return f"InfrastructureCategorySection(id={self.id},category={self.category},title={self.title},description={self.description},category_components_note={self.category_components_note},InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},)"



    


class InfrastructureMessageDetail(Base):
    """
    Per-message description appearing in a category's Messages sub-section.
    """
    __tablename__ = 'InfrastructureMessageDetail'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    msg_type = Column(Text(), nullable=False )
    message_name = Column(Text(), nullable=False )
    description = Column(Text())
    layout_url = Column(Text())
    InfrastructureCategorySection_id = Column(Integer(), ForeignKey('InfrastructureCategorySection.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureMessageDetail', source_slot='infra_layout_rows', mapping_type=None, target_class='InfrastructureLayoutRow', target_slot='InfrastructureMessageDetail_id', join_class=None, uses_join_table=None, multivalued=False)
    infra_layout_rows = relationship( "InfrastructureLayoutRow", foreign_keys="[InfrastructureLayoutRow.InfrastructureMessageDetail_id]")
    

    def __repr__(self):
        return f"InfrastructureMessageDetail(id={self.id},msg_type={self.msg_type},message_name={self.message_name},description={self.description},layout_url={self.layout_url},InfrastructureCategorySection_id={self.InfrastructureCategorySection_id},)"



    


class InfrastructureComponentDetail(Base):
    """
    Per-component description appearing in a category's Components sub-section.
    """
    __tablename__ = 'InfrastructureComponentDetail'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    component_name = Column(Text(), nullable=False )
    repetition = Column(Enum('REPEATING', 'NON_REPEATING', name='ComponentRepetition'))
    description = Column(Text())
    layout_url = Column(Text())
    InfrastructureCategorySection_id = Column(Integer(), ForeignKey('InfrastructureCategorySection.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='InfrastructureComponentDetail', source_slot='infra_layout_rows', mapping_type=None, target_class='InfrastructureLayoutRow', target_slot='InfrastructureComponentDetail_id', join_class=None, uses_join_table=None, multivalued=False)
    infra_layout_rows = relationship( "InfrastructureLayoutRow", foreign_keys="[InfrastructureLayoutRow.InfrastructureComponentDetail_id]")
    

    def __repr__(self):
        return f"InfrastructureComponentDetail(id={self.id},component_name={self.component_name},repetition={self.repetition},description={self.description},layout_url={self.layout_url},InfrastructureCategorySection_id={self.InfrastructureCategorySection_id},)"



    


class InfrastructureLayoutRow(Base):
    """
    One row of the layout table published in the Infrastructure Appendix for a message or component. Each row identifies either a FIX field (by tag number + name) or an embedded component (by name), records whether it is required, carries the Description-column text, and flags whether it appears as a nested child of a repeating-group counter.
    """
    __tablename__ = 'InfrastructureLayoutRow'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    infra_layout_kind = Column(Enum('FIELD', 'COMPONENT', name='InfrastructureLayoutRowKindEnum'), nullable=False )
    infra_layout_field_tag = Column(Integer())
    infra_layout_element_name = Column(Text(), nullable=False )
    infra_layout_required = Column(Boolean())
    infra_layout_description = Column(Text())
    infra_layout_nested = Column(Boolean())
    InfrastructureMessageDetail_id = Column(Integer(), ForeignKey('InfrastructureMessageDetail.id'))
    InfrastructureComponentDetail_id = Column(Integer(), ForeignKey('InfrastructureComponentDetail.id'))
    

    def __repr__(self):
        return f"InfrastructureLayoutRow(id={self.id},infra_layout_kind={self.infra_layout_kind},infra_layout_field_tag={self.infra_layout_field_tag},infra_layout_element_name={self.infra_layout_element_name},infra_layout_required={self.infra_layout_required},infra_layout_description={self.infra_layout_description},infra_layout_nested={self.infra_layout_nested},InfrastructureMessageDetail_id={self.InfrastructureMessageDetail_id},InfrastructureComponentDetail_id={self.InfrastructureComponentDetail_id},)"



    


class StandardResponseMapping(Base):
    """
    One row of a "Standard Responses for <area> Messages" table mapping a request message to its appropriate response(s).
    """
    __tablename__ = 'StandardResponseMapping'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    category_label = Column(Text(), nullable=False )
    fix_message = Column(Text(), nullable=False )
    appropriate_responses = Column(Text(), nullable=False )
    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'))
    

    def __repr__(self):
        return f"StandardResponseMapping(id={self.id},category_label={self.category_label},fix_message={self.fix_message},appropriate_responses={self.appropriate_responses},InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},)"



    


class ApplicationMessageReferenceKey(Base):
    """
    One row of a "Key Fields for <area> Application Message References" table identifying the field whose value is copied into BusinessRejectRefID(379).
    """
    __tablename__ = 'ApplicationMessageReferenceKey'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    category_label = Column(Text(), nullable=False )
    fix_message = Column(Text(), nullable=False )
    business_reject_ref_id_value = Column(Text(), nullable=False )
    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'))
    

    def __repr__(self):
        return f"ApplicationMessageReferenceKey(id={self.id},category_label={self.category_label},fix_message={self.fix_message},business_reject_ref_id_value={self.business_reject_ref_id_value},InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},)"



    


class BusinessRejectReasonDescription(Base):
    """
    One entry of the BusinessRejectReason(380) code table.
    """
    __tablename__ = 'BusinessRejectReasonDescription'

    reject_reason_code = Column(Integer(), primary_key=True, nullable=False )
    reject_reason_label = Column(Text(), nullable=False )
    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'))
    

    def __repr__(self):
        return f"BusinessRejectReasonDescription(reject_reason_code={self.reject_reason_code},reject_reason_label={self.reject_reason_label},InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},)"



    


class InfrastructureGlobalComponentReference(Base):
    """
    A reference from the Infrastructure business area to a Global Component declared on the FIX Latest "Global Components" page. Records the component name, the FIX tags it contributes, and the Infrastructure categories and messages that embed it.
    """
    __tablename__ = 'InfrastructureGlobalComponentReference'

    infra_global_component_name = Column(Enum('ApplicationSequenceControl', name='InfrastructureGlobalComponentName'), primary_key=True, nullable=False )
    infra_global_component_repetition = Column(Text())
    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'))
    
    
    infra_global_component_field_tags_rel = relationship( "InfrastructureGlobalComponentReferenceInfraGlobalComponentFieldTags" )
    infra_global_component_field_tags = association_proxy("infra_global_component_field_tags_rel", "infra_global_component_field_tags",
                                  creator=lambda x_: InfrastructureGlobalComponentReferenceInfraGlobalComponentFieldTags(infra_global_component_field_tags=x_))
    
    
    infra_global_component_field_names_rel = relationship( "InfrastructureGlobalComponentReferenceInfraGlobalComponentFieldNames" )
    infra_global_component_field_names = association_proxy("infra_global_component_field_names_rel", "infra_global_component_field_names",
                                  creator=lambda x_: InfrastructureGlobalComponentReferenceInfraGlobalComponentFieldNames(infra_global_component_field_names=x_))
    
    
    infra_global_component_used_in_rel = relationship( "InfrastructureGlobalComponentReferenceInfraGlobalComponentUsedIn" )
    infra_global_component_used_in = association_proxy("infra_global_component_used_in_rel", "infra_global_component_used_in",
                                  creator=lambda x_: InfrastructureGlobalComponentReferenceInfraGlobalComponentUsedIn(infra_global_component_used_in=x_))
    
    
    infra_global_component_msg_types_rel = relationship( "InfrastructureGlobalComponentReferenceInfraGlobalComponentMsgTypes" )
    infra_global_component_msg_types = association_proxy("infra_global_component_msg_types_rel", "infra_global_component_msg_types",
                                  creator=lambda x_: InfrastructureGlobalComponentReferenceInfraGlobalComponentMsgTypes(infra_global_component_msg_types=x_))
    

    def __repr__(self):
        return f"InfrastructureGlobalComponentReference(infra_global_component_name={self.infra_global_component_name},infra_global_component_repetition={self.infra_global_component_repetition},InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},)"



    


class FIXIntroductionProductCoverage(Base):
    """
    None
    """
    __tablename__ = 'FIXIntroduction_product_coverage'

    FIXIntroduction_id = Column(Integer(), ForeignKey('FIXIntroduction.id'), primary_key=True)
    product_coverage = Column(Enum('EQUITIES', 'CIV', 'DERIVATIVES', 'FIXED_INCOME', 'FOREIGN_EXCHANGE', name='ProductCoverage'), primary_key=True)
    

    def __repr__(self):
        return f"FIXIntroduction_product_coverage(FIXIntroduction_id={self.FIXIntroduction_id},product_coverage={self.product_coverage},)"



    


class FIXProtocolLimitedMemberTypes(Base):
    """
    None
    """
    __tablename__ = 'FIXProtocolLimited_member_types'

    FIXProtocolLimited_id = Column(Integer(), ForeignKey('FIXProtocolLimited.id'), primary_key=True)
    member_types = Column(Enum('BUY_SIDE_FIRM', 'SELL_SIDE_FIRM', 'EXCHANGE', 'ECN_ATS', 'UTILITY', 'VENDOR', 'OTHER_ASSOCIATION', name='FPLMemberType'), primary_key=True)
    

    def __repr__(self):
        return f"FIXProtocolLimited_member_types(FIXProtocolLimited_id={self.FIXProtocolLimited_id},member_types={self.member_types},)"



    


class FIXProtocolLimitedGovernanceBodies(Base):
    """
    None
    """
    __tablename__ = 'FIXProtocolLimited_governance_bodies'

    FIXProtocolLimited_id = Column(Integer(), ForeignKey('FIXProtocolLimited.id'), primary_key=True)
    governance_bodies = Column(Enum('GLOBAL_STEERING_COMMITTEE', 'GLOBAL_TECHNICAL_COMMITTEE', 'GLOBAL_PRODUCT_COMMITTEE', 'GLOBAL_BUY_SIDE_COMMITTEE', 'GLOBAL_MEMBER_SERVICES_COMMITTEE', 'REGIONAL_COMMITTEE', name='FPLCommitteeRole'), primary_key=True)
    

    def __repr__(self):
        return f"FIXProtocolLimited_governance_bodies(FIXProtocolLimited_id={self.FIXProtocolLimited_id},governance_bodies={self.governance_bodies},)"



    


class FIXProtocolLimitedProductCommittees(Base):
    """
    None
    """
    __tablename__ = 'FIXProtocolLimited_product_committees'

    FIXProtocolLimited_id = Column(Integer(), ForeignKey('FIXProtocolLimited.id'), primary_key=True)
    product_committees = Column(Enum('FIXED_INCOME_AND_CURRENCIES', 'LISTED_PRODUCTS_AND_EXCHANGES', name='FPLProductGroup'), primary_key=True)
    

    def __repr__(self):
        return f"FIXProtocolLimited_product_committees(FIXProtocolLimited_id={self.FIXProtocolLimited_id},product_committees={self.product_committees},)"



    


class FIXProtocolLimitedRegionalCommittees(Base):
    """
    None
    """
    __tablename__ = 'FIXProtocolLimited_regional_committees'

    FIXProtocolLimited_id = Column(Integer(), ForeignKey('FIXProtocolLimited.id'), primary_key=True)
    regional_committees = Column(Enum('AMERICAS', 'ASIA_PACIFIC', 'EMEA', 'JAPAN', name='FPLRegion'), primary_key=True)
    

    def __repr__(self):
        return f"FIXProtocolLimited_regional_committees(FIXProtocolLimited_id={self.FIXProtocolLimited_id},regional_committees={self.regional_committees},)"



    


class FIXFamilyStandardSeeAlso(Base):
    """
    None
    """
    __tablename__ = 'FIXFamilyStandard_see_also'

    FIXFamilyStandard_id = Column(Text(), ForeignKey('FIXFamilyStandard.id'), primary_key=True)
    see_also = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"FIXFamilyStandard_see_also(FIXFamilyStandard_id={self.FIXFamilyStandard_id},see_also={self.see_also},)"



    


class FIXDatatypeValueSpace(Base):
    """
    None
    """
    __tablename__ = 'FIXDatatype_value_space'

    FIXDatatype_datatype_name = Column(Enum('int', 'TagNum', 'SeqNum', 'NumInGroup', 'DayOfMonth', 'float', 'Qty', 'Price', 'PriceOffset', 'Amt', 'Percentage', 'char', 'Boolean', 'String', 'MultipleCharValue', 'MultipleStringValue', 'Country', 'Currency', 'Exchange', 'MonthYear', 'UTCTimestamp', 'UTCTimeOnly', 'UTCDateOnly', 'LocalMktDate', 'TZTimeOnly', 'TZTimestamp', 'Length', 'data', 'Tenor', 'Reserved100Plus', 'Reserved1000Plus', 'Reserved4000Plus', 'XMLData', 'Language', 'LocalMktTime', name='FIXDatatypeName'), ForeignKey('FIXDatatype.datatype_name'), primary_key=True)
    value_space = Column(Enum('integer', 'ordinal', 'size', 'real', 'scaled', 'character', 'characterstring', 'boolean', 'set', 'array', 'time', 'union', name='ISO11404ValueSpace'), primary_key=True)
    

    def __repr__(self):
        return f"FIXDatatype_value_space(FIXDatatype_datatype_name={self.FIXDatatype_datatype_name},value_space={self.value_space},)"



    


class FIXDatatypeTimeUnit(Base):
    """
    None
    """
    __tablename__ = 'FIXDatatype_time_unit'

    FIXDatatype_datatype_name = Column(Enum('int', 'TagNum', 'SeqNum', 'NumInGroup', 'DayOfMonth', 'float', 'Qty', 'Price', 'PriceOffset', 'Amt', 'Percentage', 'char', 'Boolean', 'String', 'MultipleCharValue', 'MultipleStringValue', 'Country', 'Currency', 'Exchange', 'MonthYear', 'UTCTimestamp', 'UTCTimeOnly', 'UTCDateOnly', 'LocalMktDate', 'TZTimeOnly', 'TZTimestamp', 'Length', 'data', 'Tenor', 'Reserved100Plus', 'Reserved1000Plus', 'Reserved4000Plus', 'XMLData', 'Language', 'LocalMktTime', name='FIXDatatypeName'), ForeignKey('FIXDatatype.datatype_name'), primary_key=True)
    time_unit = Column(Enum('SECOND', 'MILLISECOND', 'MICROSECOND', 'NANOSECOND', 'PICOSECOND', 'DAY', name='TimePrecision'), primary_key=True)
    

    def __repr__(self):
        return f"FIXDatatype_time_unit(FIXDatatype_datatype_name={self.FIXDatatype_datatype_name},time_unit={self.time_unit},)"



    


class FIXDatatypeFootnoteNumbers(Base):
    """
    None
    """
    __tablename__ = 'FIXDatatype_footnote_numbers'

    FIXDatatype_datatype_name = Column(Enum('int', 'TagNum', 'SeqNum', 'NumInGroup', 'DayOfMonth', 'float', 'Qty', 'Price', 'PriceOffset', 'Amt', 'Percentage', 'char', 'Boolean', 'String', 'MultipleCharValue', 'MultipleStringValue', 'Country', 'Currency', 'Exchange', 'MonthYear', 'UTCTimestamp', 'UTCTimeOnly', 'UTCDateOnly', 'LocalMktDate', 'TZTimeOnly', 'TZTimestamp', 'Length', 'data', 'Tenor', 'Reserved100Plus', 'Reserved1000Plus', 'Reserved4000Plus', 'XMLData', 'Language', 'LocalMktTime', name='FIXDatatypeName'), ForeignKey('FIXDatatype.datatype_name'), primary_key=True)
    footnote_numbers = Column(Integer(), primary_key=True)
    

    def __repr__(self):
        return f"FIXDatatype_footnote_numbers(FIXDatatype_datatype_name={self.FIXDatatype_datatype_name},footnote_numbers={self.footnote_numbers},)"



    


class ComponentNestedComponents(Base):
    """
    None
    """
    __tablename__ = 'Component_nested_components'

    Component_component_name = Column(Text(), ForeignKey('Component.component_name'), primary_key=True)
    nested_components_component_name = Column(Text(), ForeignKey('Component.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"Component_nested_components(Component_component_name={self.Component_component_name},nested_components_component_name={self.nested_components_component_name},)"



    


class GlobalComponentConceptuallyIdenticalTo(Base):
    """
    None
    """
    __tablename__ = 'GlobalComponent_conceptually_identical_to'

    GlobalComponent_component_name = Column(Text(), ForeignKey('GlobalComponent.component_name'), primary_key=True)
    conceptually_identical_to = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"GlobalComponent_conceptually_identical_to(GlobalComponent_component_name={self.GlobalComponent_component_name},conceptually_identical_to={self.conceptually_identical_to},)"



    


class GlobalComponentGcReferencedIn(Base):
    """
    None
    """
    __tablename__ = 'GlobalComponent_gc_referenced_in'

    GlobalComponent_component_name = Column(Text(), ForeignKey('GlobalComponent.component_name'), primary_key=True)
    gc_referenced_in = Column(Enum('PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='GlobalComponentBusinessAreaEnum'), primary_key=True)
    

    def __repr__(self):
        return f"GlobalComponent_gc_referenced_in(GlobalComponent_component_name={self.GlobalComponent_component_name},gc_referenced_in={self.gc_referenced_in},)"



    


class GlobalComponentNestedComponents(Base):
    """
    None
    """
    __tablename__ = 'GlobalComponent_nested_components'

    GlobalComponent_component_name = Column(Text(), ForeignKey('GlobalComponent.component_name'), primary_key=True)
    nested_components_component_name = Column(Text(), ForeignKey('Component.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"GlobalComponent_nested_components(GlobalComponent_component_name={self.GlobalComponent_component_name},nested_components_component_name={self.nested_components_component_name},)"



    


class CommonComponentNestedComponents(Base):
    """
    None
    """
    __tablename__ = 'CommonComponent_nested_components'

    CommonComponent_component_name = Column(Text(), ForeignKey('CommonComponent.component_name'), primary_key=True)
    nested_components_component_name = Column(Text(), ForeignKey('Component.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"CommonComponent_nested_components(CommonComponent_component_name={self.CommonComponent_component_name},nested_components_component_name={self.nested_components_component_name},)"



    


class SpecificComponentNestedComponents(Base):
    """
    None
    """
    __tablename__ = 'SpecificComponent_nested_components'

    SpecificComponent_component_name = Column(Text(), ForeignKey('SpecificComponent.component_name'), primary_key=True)
    nested_components_component_name = Column(Text(), ForeignKey('Component.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"SpecificComponent_nested_components(SpecificComponent_component_name={self.SpecificComponent_component_name},nested_components_component_name={self.nested_components_component_name},)"



    


class MessageComponents(Base):
    """
    None
    """
    __tablename__ = 'Message_components'

    Message_msg_type = Column(Text(), ForeignKey('Message.msg_type'), primary_key=True)
    components_component_name = Column(Text(), ForeignKey('Component.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"Message_components(Message_msg_type={self.Message_msg_type},components_component_name={self.components_component_name},)"



    


class PreTradeBusinessAreaCommonComponents(Base):
    """
    None
    """
    __tablename__ = 'PreTradeBusinessArea_common_components'

    PreTradeBusinessArea_id = Column(Integer(), ForeignKey('PreTradeBusinessArea.id'), primary_key=True)
    common_components = Column(Enum('AuctionTypeRuleGrp', 'BaseTradingRules', 'ExecInstRules', 'InstrumentScope', 'InstrumentScopeGrp', 'InstrumentScopeSecurityAltIDGrp', 'LotTypeRules', 'MarketDataFeedTypes', 'MarketSegmentScopeGrp', 'MatchRules', 'OrdTypeRules', 'PriceLimits', 'PriceRangeRuleGrp', 'QuoteSizeRuleGrp', 'RequestedPartyRoleGrp', 'RequestingPartyGrp', 'RequestingPartySubGrp', 'RoutingGrp', 'TickRules', 'TimeInForceRules', 'TradingSessionRules', name='PreTradeCommonComponentName'), primary_key=True)
    

    def __repr__(self):
        return f"PreTradeBusinessArea_common_components(PreTradeBusinessArea_id={self.PreTradeBusinessArea_id},common_components={self.common_components},)"



    


class PreTradeBusinessAreaReferencedGlobalComponents(Base):
    """
    None
    """
    __tablename__ = 'PreTradeBusinessArea_referenced_global_components'

    PreTradeBusinessArea_id = Column(Integer(), ForeignKey('PreTradeBusinessArea.id'), primary_key=True)
    referenced_global_components_component_name = Column(Text(), ForeignKey('GlobalComponent.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"PreTradeBusinessArea_referenced_global_components(PreTradeBusinessArea_id={self.PreTradeBusinessArea_id},referenced_global_components_component_name={self.referenced_global_components_component_name},)"



    


class PreTradeCategorySectionQuoteModels(Base):
    """
    None
    """
    __tablename__ = 'PreTradeCategorySection_quote_models'

    PreTradeCategorySection_category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', name='PreTradeCategoryEnum'), ForeignKey('PreTradeCategorySection.category'), primary_key=True)
    quote_models = Column(Enum('INDICATIVE', 'TRADEABLE', 'RESTRICTED_TRADEABLE', 'NEGOTIATION', name='QuoteModelEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PreTradeCategorySection_quote_models(PreTradeCategorySection_category={self.PreTradeCategorySection_category},quote_models={self.quote_models},)"



    


class TradeBusinessAreaTradeCommonComponents(Base):
    """
    None
    """
    __tablename__ = 'TradeBusinessArea_trade_common_components'

    TradeBusinessArea_id = Column(Integer(), ForeignKey('TradeBusinessArea.id'), primary_key=True)
    trade_common_components = Column(Enum('DisclosureInstructionGrp', 'DiscretionInstructions', 'PegInstructions', 'PreAllocGrp', 'StrategyParametersGrp', 'TriggeringInstruction', name='TradeCommonComponentName'), primary_key=True)
    

    def __repr__(self):
        return f"TradeBusinessArea_trade_common_components(TradeBusinessArea_id={self.TradeBusinessArea_id},trade_common_components={self.trade_common_components},)"



    


class TradeBusinessAreaReferencedGlobalComponents(Base):
    """
    None
    """
    __tablename__ = 'TradeBusinessArea_referenced_global_components'

    TradeBusinessArea_id = Column(Integer(), ForeignKey('TradeBusinessArea.id'), primary_key=True)
    referenced_global_components_component_name = Column(Text(), ForeignKey('GlobalComponent.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"TradeBusinessArea_referenced_global_components(TradeBusinessArea_id={self.TradeBusinessArea_id},referenced_global_components_component_name={self.referenced_global_components_component_name},)"



    


class TradeAppendixSectionComponents(Base):
    """
    None
    """
    __tablename__ = 'TradeAppendixSection_components'

    TradeAppendixSection_trade_appendix_category = Column(Text(), ForeignKey('TradeAppendixSection.trade_appendix_category'), primary_key=True)
    components_component_name = Column(Text(), ForeignKey('TradeComponentDetail.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"TradeAppendixSection_components(TradeAppendixSection_trade_appendix_category={self.TradeAppendixSection_trade_appendix_category},components_component_name={self.components_component_name},)"



    


class PostTradeBusinessAreaPostCommonComponents(Base):
    """
    None
    """
    __tablename__ = 'PostTradeBusinessArea_post_common_components'

    PostTradeBusinessArea_id = Column(Integer(), ForeignKey('PostTradeBusinessArea.id'), primary_key=True)
    post_common_components = Column(Enum('AllocCommissionDataGrp', 'AllocRegulatoryTradeIDGrp', 'ClrInstGrp', 'CollateralAmountGrp', 'CollateralReinvestmentGrp', 'DlvyInstGrp', 'ExecAllocGrp', 'MarginAmount', 'OrdAllocGrp', 'PositionAmountData', 'SettlDetails', 'SettlInstructionsData', 'SettlParties', 'SettlPtysSubGrp', 'TradeAllocAmtGrp', 'TransactionAttributeGrp', name='PostTradeCommonComponentName'), primary_key=True)
    

    def __repr__(self):
        return f"PostTradeBusinessArea_post_common_components(PostTradeBusinessArea_id={self.PostTradeBusinessArea_id},post_common_components={self.post_common_components},)"



    


class PostTradeBusinessAreaReferencedGlobalComponents(Base):
    """
    None
    """
    __tablename__ = 'PostTradeBusinessArea_referenced_global_components'

    PostTradeBusinessArea_id = Column(Integer(), ForeignKey('PostTradeBusinessArea.id'), primary_key=True)
    referenced_global_components_component_name = Column(Text(), ForeignKey('GlobalComponent.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"PostTradeBusinessArea_referenced_global_components(PostTradeBusinessArea_id={self.PostTradeBusinessArea_id},referenced_global_components_component_name={self.referenced_global_components_component_name},)"



    


class PostTradeCategorySectionAllocationScenarios(Base):
    """
    None
    """
    __tablename__ = 'PostTradeCategorySection_allocation_scenarios'

    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'), primary_key=True)
    allocation_scenarios = Column(Enum('PRE_ALLOCATED_ORDER', 'PRE_TRADE_ALLOCATION', 'POST_TRADE_ALLOCATION', 'READY_TO_BOOK', name='AllocationScenarioEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PostTradeCategorySection_allocation_scenarios(PostTradeCategorySection_category={self.PostTradeCategorySection_category},allocation_scenarios={self.allocation_scenarios},)"



    


class PostTradeCategorySectionAllocationRoles(Base):
    """
    None
    """
    __tablename__ = 'PostTradeCategorySection_allocation_roles'

    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'), primary_key=True)
    allocation_roles = Column(Enum('INITIATOR', 'RESPONDENT', name='AllocationRoleEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PostTradeCategorySection_allocation_roles(PostTradeCategorySection_category={self.PostTradeCategorySection_category},allocation_roles={self.allocation_roles},)"



    


class PostTradeCategorySectionPostTradeAllocationPricingMethods(Base):
    """
    None
    """
    __tablename__ = 'PostTradeCategorySection_post_trade_allocation_pricing_methods'

    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'), primary_key=True)
    post_trade_allocation_pricing_methods = Column(Enum('AVERAGE_PRICE', 'EXECUTED_PRICE', name='PostTradeAllocationPricingMethodEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PostTradeCategorySection_post_trade_allocation_pricing_methods(PostTradeCategorySection_category={self.PostTradeCategorySection_category},post_trade_allocation_pricing_methods={self.post_trade_allocation_pricing_methods},)"



    


class PostTradeCategorySectionClearingServicesForPositionManagement(Base):
    """
    None
    """
    __tablename__ = 'PostTradeCategorySection_clearing_services_for_position_management'

    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'), primary_key=True)
    clearing_services_for_position_management = Column(Enum('POSITION_CHANGE_SUBMISSION', 'POSITION_ADJUSTMENT', 'EXERCISE_NOTICE', 'ABANDONMENT_NOTICE', 'MARGIN_DISPOSITION', 'POSITION_PLEDGE', 'REQUEST_FOR_POSITION', name='ClearingServiceForPositionManagementEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PostTradeCategorySection_clearing_services_for_position_management(PostTradeCategorySection_category={self.PostTradeCategorySection_category},clearing_services_for_position_management={self.clearing_services_for_position_management},)"



    


class PostTradeCategorySectionCollateralManagementUsages(Base):
    """
    None
    """
    __tablename__ = 'PostTradeCategorySection_collateral_management_usages'

    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'), primary_key=True)
    collateral_management_usages = Column(Enum('SECURITIES_FINANCING_COLLATERALIZATION', 'CLEARING_HOUSE_COLLATERALIZATION', name='CollateralManagementUsageEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PostTradeCategorySection_collateral_management_usages(PostTradeCategorySection_category={self.PostTradeCategorySection_category},collateral_management_usages={self.collateral_management_usages},)"



    


class PostTradeCategorySectionCollateralAssignmentPurposes(Base):
    """
    None
    """
    __tablename__ = 'PostTradeCategorySection_collateral_assignment_purposes'

    PostTradeCategorySection_category = Column(Enum('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', name='PostTradeCategoryEnum'), ForeignKey('PostTradeCategorySection.category'), primary_key=True)
    collateral_assignment_purposes = Column(Enum('ASSIGN_INITIAL_COLLATERAL', 'REPLENISH_COLLATERAL', 'REPLACE_OR_SUBSTITUTE_COLLATERAL', name='CollateralAssignmentPurposeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"PostTradeCategorySection_collateral_assignment_purposes(PostTradeCategorySection_category={self.PostTradeCategorySection_category},collateral_assignment_purposes={self.collateral_assignment_purposes},)"



    


class ClearingServicePostTradeProcessingFormatSupportedActions(Base):
    """
    None
    """
    __tablename__ = 'ClearingServicePostTradeProcessingFormat_supported_actions'

    ClearingServicePostTradeProcessingFormat_message_format = Column(Enum('ETP', 'GIVE_UP', 'EXCHANGE_FOR_PHYSICAL', 'AVERAGE_PRICE_SYSTEM', 'MUTUAL_OFFSET_SYSTEM', 'TRADE_ENTRY_EDIT', name='ClearingServiceForPostTradeProcessingEnum'), ForeignKey('ClearingServicePostTradeProcessingFormat.message_format'), primary_key=True)
    supported_actions = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"ClearingServicePostTradeProcessingFormat_supported_actions(ClearingServicePostTradeProcessingFormat_message_format={self.ClearingServicePostTradeProcessingFormat_message_format},supported_actions={self.supported_actions},)"



    


class InfrastructureBusinessAreaInfraCommonComponents(Base):
    """
    None
    """
    __tablename__ = 'InfrastructureBusinessArea_infra_common_components'

    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'), primary_key=True)
    infra_common_components = Column(Enum('ApplIDReportGrp', 'ApplIDRequestAckGrp', 'ApplIDRequestGrp', 'CompIDReqGrp', 'CompIDStatGrp', 'ThrottleMsgTypeGrp', 'ThrottleParamsGrp', 'UsernameGrp', name='InfrastructureComponentName'), primary_key=True)
    

    def __repr__(self):
        return f"InfrastructureBusinessArea_infra_common_components(InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},infra_common_components={self.infra_common_components},)"



    


class InfrastructureBusinessAreaReferencedGlobalComponents(Base):
    """
    None
    """
    __tablename__ = 'InfrastructureBusinessArea_referenced_global_components'

    InfrastructureBusinessArea_id = Column(Integer(), ForeignKey('InfrastructureBusinessArea.id'), primary_key=True)
    referenced_global_components_component_name = Column(Text(), ForeignKey('GlobalComponent.component_name'), primary_key=True)
    

    def __repr__(self):
        return f"InfrastructureBusinessArea_referenced_global_components(InfrastructureBusinessArea_id={self.InfrastructureBusinessArea_id},referenced_global_components_component_name={self.referenced_global_components_component_name},)"



    


class InfrastructureCategorySectionNetworkStatusScenarios(Base):
    """
    None
    """
    __tablename__ = 'InfrastructureCategorySection_network_status_scenarios'

    InfrastructureCategorySection_id = Column(Integer(), ForeignKey('InfrastructureCategorySection.id'), primary_key=True)
    network_status_scenarios = Column(Enum('SCENARIO_A', 'SCENARIO_B', name='NetworkStatusScenarioEnum'), primary_key=True)
    

    def __repr__(self):
        return f"InfrastructureCategorySection_network_status_scenarios(InfrastructureCategorySection_id={self.InfrastructureCategorySection_id},network_status_scenarios={self.network_status_scenarios},)"



    


class InfrastructureCategorySectionNetworkRequestTypesReferenced(Base):
    """
    None
    """
    __tablename__ = 'InfrastructureCategorySection_network_request_types_referenced'

    InfrastructureCategorySection_id = Column(Integer(), ForeignKey('InfrastructureCategorySection.id'), primary_key=True)
    network_request_types_referenced = Column(Enum('SNAPSHOT', 'STOP_SUBSCRIBING', name='NetworkRequestTypeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"InfrastructureCategorySection_network_request_types_referenced(InfrastructureCategorySection_id={self.InfrastructureCategorySection_id},network_request_types_referenced={self.network_request_types_referenced},)"



    


class InfrastructureCategorySectionApplicationMessageReportUses(Base):
    """
    None
    """
    __tablename__ = 'InfrastructureCategorySection_application_message_report_uses'

    InfrastructureCategorySection_id = Column(Integer(), ForeignKey('InfrastructureCategorySection.id'), primary_key=True)
    application_message_report_uses = Column(Enum('RESET', 'LAST_MESSAGE', 'KEEP_ALIVE', 'RESEND_COMPLETED', name='ApplicationMessageReportTypeEnum'), primary_key=True)
    

    def __repr__(self):
        return f"InfrastructureCategorySection_application_message_report_uses(InfrastructureCategorySection_id={self.InfrastructureCategorySection_id},application_message_report_uses={self.application_message_report_uses},)"



    


class InfrastructureGlobalComponentReferenceInfraGlobalComponentFieldTags(Base):
    """
    None
    """
    __tablename__ = 'InfrastructureGlobalComponentReference_infra_global_component_field_tags'

    InfrastructureGlobalComponentReference_infra_global_component_name = Column(Enum('ApplicationSequenceControl', name='InfrastructureGlobalComponentName'), ForeignKey('InfrastructureGlobalComponentReference.infra_global_component_name'), primary_key=True)
    infra_global_component_field_tags = Column(Integer(), primary_key=True)
    

    def __repr__(self):
        return f"InfrastructureGlobalComponentReference_infra_global_component_field_tags(InfrastructureGlobalComponentReference_infra_global_component_name={self.InfrastructureGlobalComponentReference_infra_global_component_name},infra_global_component_field_tags={self.infra_global_component_field_tags},)"



    


class InfrastructureGlobalComponentReferenceInfraGlobalComponentFieldNames(Base):
    """
    None
    """
    __tablename__ = 'InfrastructureGlobalComponentReference_infra_global_component_field_names'

    InfrastructureGlobalComponentReference_infra_global_component_name = Column(Enum('ApplicationSequenceControl', name='InfrastructureGlobalComponentName'), ForeignKey('InfrastructureGlobalComponentReference.infra_global_component_name'), primary_key=True)
    infra_global_component_field_names = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InfrastructureGlobalComponentReference_infra_global_component_field_names(InfrastructureGlobalComponentReference_infra_global_component_name={self.InfrastructureGlobalComponentReference_infra_global_component_name},infra_global_component_field_names={self.infra_global_component_field_names},)"



    


class InfrastructureGlobalComponentReferenceInfraGlobalComponentUsedIn(Base):
    """
    None
    """
    __tablename__ = 'InfrastructureGlobalComponentReference_infra_global_component_used_in'

    InfrastructureGlobalComponentReference_infra_global_component_name = Column(Enum('ApplicationSequenceControl', name='InfrastructureGlobalComponentName'), ForeignKey('InfrastructureGlobalComponentReference.infra_global_component_name'), primary_key=True)
    infra_global_component_used_in = Column(Enum('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING', name='InfrastructureCategoryEnum'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"InfrastructureGlobalComponentReference_infra_global_component_used_in(InfrastructureGlobalComponentReference_infra_global_component_name={self.InfrastructureGlobalComponentReference_infra_global_component_name},infra_global_component_used_in={self.infra_global_component_used_in},)"



    


class InfrastructureGlobalComponentReferenceInfraGlobalComponentMsgTypes(Base):
    """
    None
    """
    __tablename__ = 'InfrastructureGlobalComponentReference_infra_global_component_msg_types'

    InfrastructureGlobalComponentReference_infra_global_component_name = Column(Enum('ApplicationSequenceControl', name='InfrastructureGlobalComponentName'), ForeignKey('InfrastructureGlobalComponentReference.infra_global_component_name'), primary_key=True)
    infra_global_component_msg_types = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"InfrastructureGlobalComponentReference_infra_global_component_msg_types(InfrastructureGlobalComponentReference_infra_global_component_name={self.InfrastructureGlobalComponentReference_infra_global_component_name},infra_global_component_msg_types={self.infra_global_component_msg_types},)"



    


class GlobalComponent(Component):
    """
    A component shared by messages of two or more business areas.
    """
    __tablename__ = 'GlobalComponent'

    component_group = Column(Enum('SECURITIES', 'LEG_SECURITIES', 'UNDERLYING_SECURITIES', 'PARTIES', 'ORDERS_AND_QUOTES', 'TRADES', 'COMMISSIONS_AND_FEES', 'FINANCING', 'PAYMENTS', 'STIPULATIONS', 'HEADER_AND_TRAILER', 'MISCELLANEOUS', name='ComponentGroup'), nullable=False )
    applies_to_instrument = Column(Boolean())
    applies_to_leg = Column(Boolean())
    applies_to_underlying = Column(Boolean())
    gc_id = Column(Integer())
    component_name = Column(Text(), primary_key=True, nullable=False )
    description = Column(Text())
    scope = Column(Enum('GLOBAL', 'COMMON', 'SPECIFIC', name='ComponentScope'), nullable=False )
    is_repeating_group = Column(Boolean())
    FIXIntroduction_id = Column(Integer(), ForeignKey('FIXIntroduction.id'))
    
    
    conceptually_identical_to_rel = relationship( "GlobalComponentConceptuallyIdenticalTo" )
    conceptually_identical_to = association_proxy("conceptually_identical_to_rel", "conceptually_identical_to",
                                  creator=lambda x_: GlobalComponentConceptuallyIdenticalTo(conceptually_identical_to=x_))
    
    
    gc_referenced_in_rel = relationship( "GlobalComponentGcReferencedIn" )
    gc_referenced_in = association_proxy("gc_referenced_in_rel", "gc_referenced_in",
                                  creator=lambda x_: GlobalComponentGcReferencedIn(gc_referenced_in=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='GlobalComponent', source_slot='fields', mapping_type=None, target_class='Field', target_slot='GlobalComponent_component_name', join_class=None, uses_join_table=None, multivalued=False)
    fields = relationship( "Field", foreign_keys="[Field.GlobalComponent_component_name]")
    
    
    # ManyToMany
    nested_components = relationship( "Component", secondary="GlobalComponent_nested_components")
    

    def __repr__(self):
        return f"GlobalComponent(component_group={self.component_group},applies_to_instrument={self.applies_to_instrument},applies_to_leg={self.applies_to_leg},applies_to_underlying={self.applies_to_underlying},gc_id={self.gc_id},component_name={self.component_name},description={self.description},scope={self.scope},is_repeating_group={self.is_repeating_group},FIXIntroduction_id={self.FIXIntroduction_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CommonComponent(Component):
    """
    A component used only by messages within a single business area.
    """
    __tablename__ = 'CommonComponent'

    business_area = Column(Enum('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='BusinessAreaEnum'), nullable=False )
    component_name = Column(Text(), primary_key=True, nullable=False )
    description = Column(Text())
    scope = Column(Enum('GLOBAL', 'COMMON', 'SPECIFIC', name='ComponentScope'), nullable=False )
    is_repeating_group = Column(Boolean())
    
    
    # One-To-Many: OneToAnyMapping(source_class='CommonComponent', source_slot='fields', mapping_type=None, target_class='Field', target_slot='CommonComponent_component_name', join_class=None, uses_join_table=None, multivalued=False)
    fields = relationship( "Field", foreign_keys="[Field.CommonComponent_component_name]")
    
    
    # ManyToMany
    nested_components = relationship( "Component", secondary="CommonComponent_nested_components")
    

    def __repr__(self):
        return f"CommonComponent(business_area={self.business_area},component_name={self.component_name},description={self.description},scope={self.scope},is_repeating_group={self.is_repeating_group},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SpecificComponent(Component):
    """
    A component used only by messages within a single category.
    """
    __tablename__ = 'SpecificComponent'

    business_area = Column(Enum('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE', name='BusinessAreaEnum'), nullable=False )
    category = Column(Enum('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', 'SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDERS', 'MULTILEG_ORDERS', 'LIST_PROGRAM_BASKET_TRADING', 'ALLOCATION_AND_READY_TO_BOOK', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTIONS', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTIONS', 'POSITIONS_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', 'BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING', name='MessageCategoryEnum'), nullable=False )
    component_name = Column(Text(), primary_key=True, nullable=False )
    description = Column(Text())
    scope = Column(Enum('GLOBAL', 'COMMON', 'SPECIFIC', name='ComponentScope'), nullable=False )
    is_repeating_group = Column(Boolean())
    
    
    # One-To-Many: OneToAnyMapping(source_class='SpecificComponent', source_slot='fields', mapping_type=None, target_class='Field', target_slot='SpecificComponent_component_name', join_class=None, uses_join_table=None, multivalued=False)
    fields = relationship( "Field", foreign_keys="[Field.SpecificComponent_component_name]")
    
    
    # ManyToMany
    nested_components = relationship( "Component", secondary="SpecificComponent_nested_components")
    

    def __repr__(self):
        return f"SpecificComponent(business_area={self.business_area},category={self.category},component_name={self.component_name},description={self.description},scope={self.scope},is_repeating_group={self.is_repeating_group},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


