-- ====================================================================
-- SQL Validation Queries
-- Generated from LinkML schema
-- LinkML v1.11.1
-- Generator: sqlvalidationgen.py v0.1.0
-- Dialect: sqlite
-- ====================================================================

SELECT 'FIXIntroduction' AS table_name, 'product_coverage' AS column_name, 'enum' AS constraint_type, id AS record_id, product_coverage AS invalid_value 
FROM "FIXIntroduction" 
WHERE "FIXIntroduction".product_coverage IS NOT NULL AND ("FIXIntroduction".product_coverage NOT IN ('EQUITIES', 'CIV', 'DERIVATIVES', 'FIXED_INCOME', 'FOREIGN_EXCHANGE'))

UNION ALL

SELECT 'FIXProtocolLimited' AS table_name, 'member_types' AS column_name, 'enum' AS constraint_type, id AS record_id, member_types AS invalid_value 
FROM "FIXProtocolLimited" 
WHERE "FIXProtocolLimited".member_types IS NOT NULL AND ("FIXProtocolLimited".member_types NOT IN ('BUY_SIDE_FIRM', 'SELL_SIDE_FIRM', 'EXCHANGE', 'ECN_ATS', 'UTILITY', 'VENDOR', 'OTHER_ASSOCIATION'))

UNION ALL

SELECT 'FIXProtocolLimited' AS table_name, 'governance_bodies' AS column_name, 'enum' AS constraint_type, id AS record_id, governance_bodies AS invalid_value 
FROM "FIXProtocolLimited" 
WHERE "FIXProtocolLimited".governance_bodies IS NOT NULL AND ("FIXProtocolLimited".governance_bodies NOT IN ('GLOBAL_STEERING_COMMITTEE', 'GLOBAL_TECHNICAL_COMMITTEE', 'GLOBAL_PRODUCT_COMMITTEE', 'GLOBAL_BUY_SIDE_COMMITTEE', 'GLOBAL_MEMBER_SERVICES_COMMITTEE', 'REGIONAL_COMMITTEE'))

UNION ALL

SELECT 'FIXProtocolLimited' AS table_name, 'product_committees' AS column_name, 'enum' AS constraint_type, id AS record_id, product_committees AS invalid_value 
FROM "FIXProtocolLimited" 
WHERE "FIXProtocolLimited".product_committees IS NOT NULL AND ("FIXProtocolLimited".product_committees NOT IN ('FIXED_INCOME_AND_CURRENCIES', 'LISTED_PRODUCTS_AND_EXCHANGES'))

UNION ALL

SELECT 'FIXProtocolLimited' AS table_name, 'regional_committees' AS column_name, 'enum' AS constraint_type, id AS record_id, regional_committees AS invalid_value 
FROM "FIXProtocolLimited" 
WHERE "FIXProtocolLimited".regional_committees IS NOT NULL AND ("FIXProtocolLimited".regional_committees NOT IN ('AMERICAS', 'ASIA_PACIFIC', 'EMEA', 'JAPAN'))

UNION ALL

SELECT 'FIXFamilyStandard' AS table_name, 'id' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "FIXFamilyStandard" 
WHERE "FIXFamilyStandard".id IS NULL

UNION ALL

SELECT 'FIXFamilyStandard' AS table_name, 'id' AS column_name, 'identifier' AS constraint_type, id AS record_id, id AS invalid_value 
FROM "FIXFamilyStandard" 
WHERE "FIXFamilyStandard".id IN (SELECT id 
FROM "FIXFamilyStandard" GROUP BY id 
HAVING count(*) > 1)

UNION ALL

SELECT 'FIXFamilyStandard' AS table_name, 'name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "FIXFamilyStandard" 
WHERE "FIXFamilyStandard".name IS NULL

UNION ALL

SELECT 'FIXFamilyStandard' AS table_name, 'layer' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "FIXFamilyStandard" 
WHERE "FIXFamilyStandard".layer IS NULL

UNION ALL

SELECT 'FIXFamilyStandard' AS table_name, 'layer' AS column_name, 'enum' AS constraint_type, id AS record_id, layer AS invalid_value 
FROM "FIXFamilyStandard" 
WHERE "FIXFamilyStandard".layer IS NOT NULL AND ("FIXFamilyStandard".layer NOT IN ('APPLICATION', 'ENCODING', 'SESSION'))

UNION ALL

SELECT 'FIXFamilyStandard' AS table_name, 'session_profile' AS column_name, 'enum' AS constraint_type, id AS record_id, session_profile AS invalid_value 
FROM "FIXFamilyStandard" 
WHERE "FIXFamilyStandard".session_profile IS NOT NULL AND ("FIXFamilyStandard".session_profile NOT IN ('FIX_4_2', 'FIX4', 'FIXT', 'LFIXT', 'FIXP', 'SOFH', 'FIXS', 'AMQP'))

UNION ALL

SELECT 'FIXFamilyStandard' AS table_name, 'encoding_name' AS column_name, 'enum' AS constraint_type, id AS record_id, encoding_name AS invalid_value 
FROM "FIXFamilyStandard" 
WHERE "FIXFamilyStandard".encoding_name IS NOT NULL AND ("FIXFamilyStandard".encoding_name NOT IN ('TAGVALUE', 'FIXML', 'FAST', 'SBE', 'GPB', 'JSON', 'ASN_1'))

UNION ALL

SELECT 'ExtensionPack' AS table_name, 'number' AS column_name, 'required' AS constraint_type, number AS record_id, NULL AS invalid_value 
FROM "ExtensionPack" 
WHERE "ExtensionPack".number IS NULL

UNION ALL

SELECT 'ExtensionPack' AS table_name, 'number' AS column_name, 'identifier' AS constraint_type, number AS record_id, number AS invalid_value 
FROM "ExtensionPack" 
WHERE "ExtensionPack".number IN (SELECT number 
FROM "ExtensionPack" GROUP BY number 
HAVING count(*) > 1)

UNION ALL

SELECT 'ExtensionPack' AS table_name, 'title' AS column_name, 'required' AS constraint_type, number AS record_id, NULL AS invalid_value 
FROM "ExtensionPack" 
WHERE "ExtensionPack".title IS NULL

UNION ALL

SELECT 'ExtensionPack' AS table_name, 'size' AS column_name, 'enum' AS constraint_type, number AS record_id, size AS invalid_value 
FROM "ExtensionPack" 
WHERE "ExtensionPack".size IS NOT NULL AND ("ExtensionPack".size NOT IN ('XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL'))

UNION ALL

SELECT 'FIXDatatype' AS table_name, 'datatype_name' AS column_name, 'required' AS constraint_type, datatype_name AS record_id, NULL AS invalid_value 
FROM "FIXDatatype" 
WHERE "FIXDatatype".datatype_name IS NULL

UNION ALL

SELECT 'FIXDatatype' AS table_name, 'datatype_name' AS column_name, 'identifier' AS constraint_type, datatype_name AS record_id, datatype_name AS invalid_value 
FROM "FIXDatatype" 
WHERE "FIXDatatype".datatype_name IN (SELECT datatype_name 
FROM "FIXDatatype" GROUP BY datatype_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'FIXDatatype' AS table_name, 'datatype_name' AS column_name, 'enum' AS constraint_type, datatype_name AS record_id, datatype_name AS invalid_value 
FROM "FIXDatatype" 
WHERE "FIXDatatype".datatype_name IS NOT NULL AND ("FIXDatatype".datatype_name NOT IN ('int', 'TagNum', 'SeqNum', 'NumInGroup', 'DayOfMonth', 'float', 'Qty', 'Price', 'PriceOffset', 'Amt', 'Percentage', 'char', 'Boolean', 'String', 'MultipleCharValue', 'MultipleStringValue', 'Country', 'Currency', 'Exchange', 'MonthYear', 'UTCTimestamp', 'UTCTimeOnly', 'UTCDateOnly', 'LocalMktDate', 'TZTimeOnly', 'TZTimestamp', 'Length', 'data', 'Tenor', 'Reserved100Plus', 'Reserved1000Plus', 'Reserved4000Plus', 'XMLData', 'Language', 'LocalMktTime'))

UNION ALL

SELECT 'FIXDatatype' AS table_name, 'definition' AS column_name, 'required' AS constraint_type, datatype_name AS record_id, NULL AS invalid_value 
FROM "FIXDatatype" 
WHERE "FIXDatatype".definition IS NULL

UNION ALL

SELECT 'FIXDatatype' AS table_name, 'value_space' AS column_name, 'enum' AS constraint_type, datatype_name AS record_id, value_space AS invalid_value 
FROM "FIXDatatype" 
WHERE "FIXDatatype".value_space IS NOT NULL AND ("FIXDatatype".value_space NOT IN ('integer', 'ordinal', 'size', 'real', 'scaled', 'character', 'characterstring', 'boolean', 'set', 'array', 'time', 'union'))

UNION ALL

SELECT 'FIXDatatype' AS table_name, 'time_unit' AS column_name, 'enum' AS constraint_type, datatype_name AS record_id, time_unit AS invalid_value 
FROM "FIXDatatype" 
WHERE "FIXDatatype".time_unit IS NOT NULL AND ("FIXDatatype".time_unit NOT IN ('SECOND', 'MILLISECOND', 'MICROSECOND', 'NANOSECOND', 'PICOSECOND', 'DAY'))

UNION ALL

SELECT 'BusinessArea' AS table_name, 'area' AS column_name, 'required' AS constraint_type, area AS record_id, NULL AS invalid_value 
FROM "BusinessArea" 
WHERE "BusinessArea".area IS NULL

UNION ALL

SELECT 'BusinessArea' AS table_name, 'area' AS column_name, 'identifier' AS constraint_type, area AS record_id, area AS invalid_value 
FROM "BusinessArea" 
WHERE "BusinessArea".area IN (SELECT area 
FROM "BusinessArea" GROUP BY area 
HAVING count(*) > 1)

UNION ALL

SELECT 'BusinessArea' AS table_name, 'area' AS column_name, 'enum' AS constraint_type, area AS record_id, area AS invalid_value 
FROM "BusinessArea" 
WHERE "BusinessArea".area IS NOT NULL AND ("BusinessArea".area NOT IN ('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE'))

UNION ALL

SELECT 'MessageCategory' AS table_name, 'category' AS column_name, 'required' AS constraint_type, category AS record_id, NULL AS invalid_value 
FROM "MessageCategory" 
WHERE "MessageCategory".category IS NULL

UNION ALL

SELECT 'MessageCategory' AS table_name, 'category' AS column_name, 'identifier' AS constraint_type, category AS record_id, category AS invalid_value 
FROM "MessageCategory" 
WHERE "MessageCategory".category IN (SELECT category 
FROM "MessageCategory" GROUP BY category 
HAVING count(*) > 1)

UNION ALL

SELECT 'MessageCategory' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, category AS record_id, category AS invalid_value 
FROM "MessageCategory" 
WHERE "MessageCategory".category IS NOT NULL AND ("MessageCategory".category NOT IN ('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', 'SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDERS', 'MULTILEG_ORDERS', 'LIST_PROGRAM_BASKET_TRADING', 'ALLOCATION_AND_READY_TO_BOOK', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTIONS', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTIONS', 'POSITIONS_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', 'BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING'))

UNION ALL

SELECT 'MessageCategory' AS table_name, 'business_area' AS column_name, 'required' AS constraint_type, category AS record_id, NULL AS invalid_value 
FROM "MessageCategory" 
WHERE "MessageCategory".business_area IS NULL

UNION ALL

SELECT 'MessageCategory' AS table_name, 'business_area' AS column_name, 'enum' AS constraint_type, category AS record_id, business_area AS invalid_value 
FROM "MessageCategory" 
WHERE "MessageCategory".business_area IS NOT NULL AND ("MessageCategory".business_area NOT IN ('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE'))

UNION ALL

SELECT 'Field' AS table_name, 'tag' AS column_name, 'required' AS constraint_type, tag AS record_id, NULL AS invalid_value 
FROM "Field" 
WHERE "Field".tag IS NULL

UNION ALL

SELECT 'Field' AS table_name, 'tag' AS column_name, 'identifier' AS constraint_type, tag AS record_id, tag AS invalid_value 
FROM "Field" 
WHERE "Field".tag IN (SELECT tag 
FROM "Field" GROUP BY tag 
HAVING count(*) > 1)

UNION ALL

SELECT 'Field' AS table_name, 'field_name' AS column_name, 'required' AS constraint_type, tag AS record_id, NULL AS invalid_value 
FROM "Field" 
WHERE "Field".field_name IS NULL

UNION ALL

SELECT 'Field' AS table_name, 'datatype' AS column_name, 'required' AS constraint_type, tag AS record_id, NULL AS invalid_value 
FROM "Field" 
WHERE "Field".datatype IS NULL

UNION ALL

SELECT 'Field' AS table_name, 'datatype' AS column_name, 'enum' AS constraint_type, tag AS record_id, datatype AS invalid_value 
FROM "Field" 
WHERE "Field".datatype IS NOT NULL AND ("Field".datatype NOT IN ('int', 'TagNum', 'SeqNum', 'NumInGroup', 'DayOfMonth', 'float', 'Qty', 'Price', 'PriceOffset', 'Amt', 'Percentage', 'char', 'Boolean', 'String', 'MultipleCharValue', 'MultipleStringValue', 'Country', 'Currency', 'Exchange', 'MonthYear', 'UTCTimestamp', 'UTCTimeOnly', 'UTCDateOnly', 'LocalMktDate', 'TZTimeOnly', 'TZTimestamp', 'Length', 'data', 'Tenor', 'Reserved100Plus', 'Reserved1000Plus', 'Reserved4000Plus', 'XMLData', 'Language', 'LocalMktTime'))

UNION ALL

SELECT 'Field' AS table_name, 'requirement' AS column_name, 'enum' AS constraint_type, tag AS record_id, requirement AS invalid_value 
FROM "Field" 
WHERE "Field".requirement IS NOT NULL AND ("Field".requirement NOT IN ('REQUIRED', 'OPTIONAL', 'CONDITIONALLY_REQUIRED'))

UNION ALL

SELECT 'GlobalComponent' AS table_name, 'component_group' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "GlobalComponent" 
WHERE "GlobalComponent".component_group IS NULL

UNION ALL

SELECT 'GlobalComponent' AS table_name, 'component_group' AS column_name, 'enum' AS constraint_type, component_name AS record_id, component_group AS invalid_value 
FROM "GlobalComponent" 
WHERE "GlobalComponent".component_group IS NOT NULL AND ("GlobalComponent".component_group NOT IN ('SECURITIES', 'LEG_SECURITIES', 'UNDERLYING_SECURITIES', 'PARTIES', 'ORDERS_AND_QUOTES', 'TRADES', 'COMMISSIONS_AND_FEES', 'FINANCING', 'PAYMENTS', 'STIPULATIONS', 'HEADER_AND_TRAILER', 'MISCELLANEOUS'))

UNION ALL

SELECT 'GlobalComponent' AS table_name, 'gc_id' AS column_name, 'range' AS constraint_type, component_name AS record_id, gc_id AS invalid_value 
FROM "GlobalComponent" 
WHERE "GlobalComponent".gc_id < 0

UNION ALL

SELECT 'GlobalComponent' AS table_name, 'gc_referenced_in' AS column_name, 'enum' AS constraint_type, component_name AS record_id, gc_referenced_in AS invalid_value 
FROM "GlobalComponent" 
WHERE "GlobalComponent".gc_referenced_in IS NOT NULL AND ("GlobalComponent".gc_referenced_in NOT IN ('PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE'))

UNION ALL

SELECT 'GlobalComponent' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "GlobalComponent" 
WHERE "GlobalComponent".component_name IS NULL

UNION ALL

SELECT 'GlobalComponent' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "GlobalComponent" 
WHERE "GlobalComponent".component_name IN (SELECT component_name 
FROM "GlobalComponent" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'GlobalComponent' AS table_name, 'scope' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "GlobalComponent" 
WHERE "GlobalComponent".scope IS NULL

UNION ALL

SELECT 'GlobalComponent' AS table_name, 'scope' AS column_name, 'enum' AS constraint_type, component_name AS record_id, scope AS invalid_value 
FROM "GlobalComponent" 
WHERE "GlobalComponent".scope IS NOT NULL AND ("GlobalComponent".scope NOT IN ('GLOBAL', 'COMMON', 'SPECIFIC'))

UNION ALL

SELECT 'CommonComponent' AS table_name, 'business_area' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "CommonComponent" 
WHERE "CommonComponent".business_area IS NULL

UNION ALL

SELECT 'CommonComponent' AS table_name, 'business_area' AS column_name, 'enum' AS constraint_type, component_name AS record_id, business_area AS invalid_value 
FROM "CommonComponent" 
WHERE "CommonComponent".business_area IS NOT NULL AND ("CommonComponent".business_area NOT IN ('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE'))

UNION ALL

SELECT 'CommonComponent' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "CommonComponent" 
WHERE "CommonComponent".component_name IS NULL

UNION ALL

SELECT 'CommonComponent' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "CommonComponent" 
WHERE "CommonComponent".component_name IN (SELECT component_name 
FROM "CommonComponent" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'CommonComponent' AS table_name, 'scope' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "CommonComponent" 
WHERE "CommonComponent".scope IS NULL

UNION ALL

SELECT 'CommonComponent' AS table_name, 'scope' AS column_name, 'enum' AS constraint_type, component_name AS record_id, scope AS invalid_value 
FROM "CommonComponent" 
WHERE "CommonComponent".scope IS NOT NULL AND ("CommonComponent".scope NOT IN ('GLOBAL', 'COMMON', 'SPECIFIC'))

UNION ALL

SELECT 'SpecificComponent' AS table_name, 'business_area' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "SpecificComponent" 
WHERE "SpecificComponent".business_area IS NULL

UNION ALL

SELECT 'SpecificComponent' AS table_name, 'business_area' AS column_name, 'enum' AS constraint_type, component_name AS record_id, business_area AS invalid_value 
FROM "SpecificComponent" 
WHERE "SpecificComponent".business_area IS NOT NULL AND ("SpecificComponent".business_area NOT IN ('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE'))

UNION ALL

SELECT 'SpecificComponent' AS table_name, 'category' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "SpecificComponent" 
WHERE "SpecificComponent".category IS NULL

UNION ALL

SELECT 'SpecificComponent' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, component_name AS record_id, category AS invalid_value 
FROM "SpecificComponent" 
WHERE "SpecificComponent".category IS NOT NULL AND ("SpecificComponent".category NOT IN ('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', 'SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDERS', 'MULTILEG_ORDERS', 'LIST_PROGRAM_BASKET_TRADING', 'ALLOCATION_AND_READY_TO_BOOK', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTIONS', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTIONS', 'POSITIONS_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', 'BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING'))

UNION ALL

SELECT 'SpecificComponent' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "SpecificComponent" 
WHERE "SpecificComponent".component_name IS NULL

UNION ALL

SELECT 'SpecificComponent' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "SpecificComponent" 
WHERE "SpecificComponent".component_name IN (SELECT component_name 
FROM "SpecificComponent" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'SpecificComponent' AS table_name, 'scope' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "SpecificComponent" 
WHERE "SpecificComponent".scope IS NULL

UNION ALL

SELECT 'SpecificComponent' AS table_name, 'scope' AS column_name, 'enum' AS constraint_type, component_name AS record_id, scope AS invalid_value 
FROM "SpecificComponent" 
WHERE "SpecificComponent".scope IS NOT NULL AND ("SpecificComponent".scope NOT IN ('GLOBAL', 'COMMON', 'SPECIFIC'))

UNION ALL

SELECT 'Message' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "Message" 
WHERE "Message".msg_type IS NULL

UNION ALL

SELECT 'Message' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "Message" 
WHERE "Message".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'Message' AS table_name, 'msg_type' AS column_name, 'identifier' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "Message" 
WHERE "Message".msg_type IN (SELECT msg_type 
FROM "Message" GROUP BY msg_type 
HAVING count(*) > 1)

UNION ALL

SELECT 'Message' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "Message" 
WHERE "Message".message_name IS NULL

UNION ALL

SELECT 'Message' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, msg_type AS record_id, category AS invalid_value 
FROM "Message" 
WHERE "Message".category IS NOT NULL AND ("Message".category NOT IN ('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION', 'SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDERS', 'MULTILEG_ORDERS', 'LIST_PROGRAM_BASKET_TRADING', 'ALLOCATION_AND_READY_TO_BOOK', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTIONS', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTIONS', 'POSITIONS_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT', 'BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING'))

UNION ALL

SELECT 'UDFTagRange' AS table_name, 'range_id' AS column_name, 'required' AS constraint_type, range_id AS record_id, NULL AS invalid_value 
FROM "UDFTagRange" 
WHERE "UDFTagRange".range_id IS NULL

UNION ALL

SELECT 'UDFTagRange' AS table_name, 'range_id' AS column_name, 'identifier' AS constraint_type, range_id AS record_id, range_id AS invalid_value 
FROM "UDFTagRange" 
WHERE "UDFTagRange".range_id IN (SELECT range_id 
FROM "UDFTagRange" GROUP BY range_id 
HAVING count(*) > 1)

UNION ALL

SELECT 'UDFTagRange' AS table_name, 'low_tag' AS column_name, 'required' AS constraint_type, range_id AS record_id, NULL AS invalid_value 
FROM "UDFTagRange" 
WHERE "UDFTagRange".low_tag IS NULL

UNION ALL

SELECT 'UDFTagRange' AS table_name, 'usage' AS column_name, 'required' AS constraint_type, range_id AS record_id, NULL AS invalid_value 
FROM "UDFTagRange" 
WHERE "UDFTagRange".usage IS NULL

UNION ALL

SELECT 'UDFTagRange' AS table_name, 'usage' AS column_name, 'enum' AS constraint_type, range_id AS record_id, usage AS invalid_value 
FROM "UDFTagRange" 
WHERE "UDFTagRange".usage IS NOT NULL AND ("UDFTagRange".usage NOT IN ('INTER_FIRM_REGISTERED', 'INTER_FIRM_BILATERAL', 'GTC_REGULATORY_LEGACY', 'WIP_CHINA', 'INTERNAL_FIRM', 'GTC_OTC_DERIVATIVES', 'GTC_RESERVED'))

UNION ALL

SELECT 'PreTradeBusinessArea' AS table_name, 'area' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PreTradeBusinessArea" 
WHERE "PreTradeBusinessArea".area IS NULL

UNION ALL

SELECT 'PreTradeBusinessArea' AS table_name, 'area' AS column_name, 'enum' AS constraint_type, id AS record_id, area AS invalid_value 
FROM "PreTradeBusinessArea" 
WHERE "PreTradeBusinessArea".area IS NOT NULL AND ("PreTradeBusinessArea".area NOT IN ('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE'))

UNION ALL

SELECT 'PreTradeBusinessArea' AS table_name, 'common_components' AS column_name, 'enum' AS constraint_type, id AS record_id, common_components AS invalid_value 
FROM "PreTradeBusinessArea" 
WHERE "PreTradeBusinessArea".common_components IS NOT NULL AND ("PreTradeBusinessArea".common_components NOT IN ('AuctionTypeRuleGrp', 'BaseTradingRules', 'ExecInstRules', 'InstrumentScope', 'InstrumentScopeGrp', 'InstrumentScopeSecurityAltIDGrp', 'LotTypeRules', 'MarketDataFeedTypes', 'MarketSegmentScopeGrp', 'MatchRules', 'OrdTypeRules', 'PriceLimits', 'PriceRangeRuleGrp', 'QuoteSizeRuleGrp', 'RequestedPartyRoleGrp', 'RequestingPartyGrp', 'RequestingPartySubGrp', 'RoutingGrp', 'TickRules', 'TimeInForceRules', 'TradingSessionRules'))

UNION ALL

SELECT 'PreTradeMessageEntry' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PreTradeMessageEntry" 
WHERE "PreTradeMessageEntry".msg_type IS NULL

UNION ALL

SELECT 'PreTradeMessageEntry' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "PreTradeMessageEntry" 
WHERE "PreTradeMessageEntry".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'PreTradeMessageEntry' AS table_name, 'msg_type' AS column_name, 'identifier' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "PreTradeMessageEntry" 
WHERE "PreTradeMessageEntry".msg_type IN (SELECT msg_type 
FROM "PreTradeMessageEntry" GROUP BY msg_type 
HAVING count(*) > 1)

UNION ALL

SELECT 'PreTradeMessageEntry' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PreTradeMessageEntry" 
WHERE "PreTradeMessageEntry".message_name IS NULL

UNION ALL

SELECT 'PreTradeMessageEntry' AS table_name, 'category' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PreTradeMessageEntry" 
WHERE "PreTradeMessageEntry".category IS NULL

UNION ALL

SELECT 'PreTradeMessageEntry' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, msg_type AS record_id, category AS invalid_value 
FROM "PreTradeMessageEntry" 
WHERE "PreTradeMessageEntry".category IS NOT NULL AND ("PreTradeMessageEntry".category NOT IN ('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION'))

UNION ALL

SELECT 'PreTradeComponentEntry' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "PreTradeComponentEntry" 
WHERE "PreTradeComponentEntry".component_name IS NULL

UNION ALL

SELECT 'PreTradeComponentEntry' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "PreTradeComponentEntry" 
WHERE "PreTradeComponentEntry".component_name IN (SELECT component_name 
FROM "PreTradeComponentEntry" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'PreTradeComponentEntry' AS table_name, 'repetition' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "PreTradeComponentEntry" 
WHERE "PreTradeComponentEntry".repetition IS NULL

UNION ALL

SELECT 'PreTradeComponentEntry' AS table_name, 'repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, repetition AS invalid_value 
FROM "PreTradeComponentEntry" 
WHERE "PreTradeComponentEntry".repetition IS NOT NULL AND ("PreTradeComponentEntry".repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'PreTradeComponentEntry' AS table_name, 'category' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "PreTradeComponentEntry" 
WHERE "PreTradeComponentEntry".category IS NULL

UNION ALL

SELECT 'PreTradeComponentEntry' AS table_name, 'footnote_number' AS column_name, 'range' AS constraint_type, component_name AS record_id, footnote_number AS invalid_value 
FROM "PreTradeComponentEntry" 
WHERE "PreTradeComponentEntry".footnote_number < 1 OR "PreTradeComponentEntry".footnote_number > 25

UNION ALL

SELECT 'ComponentTableFootnote' AS table_name, 'footnote_number' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "ComponentTableFootnote" 
WHERE "ComponentTableFootnote".footnote_number IS NULL

UNION ALL

SELECT 'ComponentTableFootnote' AS table_name, 'footnote_number' AS column_name, 'range' AS constraint_type, footnote_number AS record_id, footnote_number AS invalid_value 
FROM "ComponentTableFootnote" 
WHERE "ComponentTableFootnote".footnote_number < 1 OR "ComponentTableFootnote".footnote_number > 25

UNION ALL

SELECT 'ComponentTableFootnote' AS table_name, 'footnote_number' AS column_name, 'identifier' AS constraint_type, footnote_number AS record_id, footnote_number AS invalid_value 
FROM "ComponentTableFootnote" 
WHERE "ComponentTableFootnote".footnote_number IN (SELECT footnote_number 
FROM "ComponentTableFootnote" GROUP BY footnote_number 
HAVING count(*) > 1)

UNION ALL

SELECT 'ComponentTableFootnote' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "ComponentTableFootnote" 
WHERE "ComponentTableFootnote".component_name IS NULL

UNION ALL

SELECT 'ComponentTableFootnote' AS table_name, 'introduced_in' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "ComponentTableFootnote" 
WHERE "ComponentTableFootnote".introduced_in IS NULL

UNION ALL

SELECT 'ComponentTableFootnote' AS table_name, 'sole_category' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "ComponentTableFootnote" 
WHERE "ComponentTableFootnote".sole_category IS NULL

UNION ALL

SELECT 'ComponentTableFootnote' AS table_name, 'sole_category' AS column_name, 'enum' AS constraint_type, footnote_number AS record_id, sole_category AS invalid_value 
FROM "ComponentTableFootnote" 
WHERE "ComponentTableFootnote".sole_category IS NOT NULL AND ("ComponentTableFootnote".sole_category NOT IN ('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION'))

UNION ALL

SELECT 'PreTradeCategorySection' AS table_name, 'category' AS column_name, 'required' AS constraint_type, category AS record_id, NULL AS invalid_value 
FROM "PreTradeCategorySection" 
WHERE "PreTradeCategorySection".category IS NULL

UNION ALL

SELECT 'PreTradeCategorySection' AS table_name, 'category' AS column_name, 'identifier' AS constraint_type, category AS record_id, category AS invalid_value 
FROM "PreTradeCategorySection" 
WHERE "PreTradeCategorySection".category IN (SELECT category 
FROM "PreTradeCategorySection" GROUP BY category 
HAVING count(*) > 1)

UNION ALL

SELECT 'PreTradeCategorySection' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, category AS record_id, category AS invalid_value 
FROM "PreTradeCategorySection" 
WHERE "PreTradeCategorySection".category IS NOT NULL AND ("PreTradeCategorySection".category NOT IN ('INDICATION', 'EVENT_COMMUNICATION', 'QUOTATION_NEGOTIATION', 'MARKET_DATA', 'MARKET_STRUCTURE_REFERENCE_DATA', 'SECURITIES_REFERENCE_DATA', 'PARTIES_REFERENCE_DATA', 'PARTIES_ACTION'))

UNION ALL

SELECT 'PreTradeCategorySection' AS table_name, 'quote_models' AS column_name, 'enum' AS constraint_type, category AS record_id, quote_models AS invalid_value 
FROM "PreTradeCategorySection" 
WHERE "PreTradeCategorySection".quote_models IS NOT NULL AND ("PreTradeCategorySection".quote_models NOT IN ('INDICATIVE', 'TRADEABLE', 'RESTRICTED_TRADEABLE', 'NEGOTIATION'))

UNION ALL

SELECT 'PreTradeMessageDetail' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PreTradeMessageDetail" 
WHERE "PreTradeMessageDetail".msg_type IS NULL

UNION ALL

SELECT 'PreTradeMessageDetail' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "PreTradeMessageDetail" 
WHERE "PreTradeMessageDetail".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'PreTradeMessageDetail' AS table_name, 'msg_type' AS column_name, 'identifier' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "PreTradeMessageDetail" 
WHERE "PreTradeMessageDetail".msg_type IN (SELECT msg_type 
FROM "PreTradeMessageDetail" GROUP BY msg_type 
HAVING count(*) > 1)

UNION ALL

SELECT 'PreTradeMessageDetail' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PreTradeMessageDetail" 
WHERE "PreTradeMessageDetail".message_name IS NULL

UNION ALL

SELECT 'PreTradeComponentDetail' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "PreTradeComponentDetail" 
WHERE "PreTradeComponentDetail".component_name IS NULL

UNION ALL

SELECT 'PreTradeComponentDetail' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "PreTradeComponentDetail" 
WHERE "PreTradeComponentDetail".component_name IN (SELECT component_name 
FROM "PreTradeComponentDetail" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'PreTradeComponentDetail' AS table_name, 'repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, repetition AS invalid_value 
FROM "PreTradeComponentDetail" 
WHERE "PreTradeComponentDetail".repetition IS NOT NULL AND ("PreTradeComponentDetail".repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'MessageGroup' AS table_name, 'group_title' AS column_name, 'required' AS constraint_type, group_title AS record_id, NULL AS invalid_value 
FROM "MessageGroup" 
WHERE "MessageGroup".group_title IS NULL

UNION ALL

SELECT 'MessageGroup' AS table_name, 'group_title' AS column_name, 'identifier' AS constraint_type, group_title AS record_id, group_title AS invalid_value 
FROM "MessageGroup" 
WHERE "MessageGroup".group_title IN (SELECT group_title 
FROM "MessageGroup" GROUP BY group_title 
HAVING count(*) > 1)

UNION ALL

SELECT 'MessageGroup' AS table_name, 'messages' AS column_name, 'required' AS constraint_type, group_title AS record_id, NULL AS invalid_value 
FROM "MessageGroup" 
WHERE "MessageGroup".messages IS NULL

UNION ALL

SELECT 'CommonComponentDetail' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "CommonComponentDetail" 
WHERE "CommonComponentDetail".component_name IS NULL

UNION ALL

SELECT 'CommonComponentDetail' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "CommonComponentDetail" 
WHERE "CommonComponentDetail".component_name IN (SELECT component_name 
FROM "CommonComponentDetail" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'CommonComponentDetail' AS table_name, 'component_name' AS column_name, 'enum' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "CommonComponentDetail" 
WHERE "CommonComponentDetail".component_name IS NOT NULL AND ("CommonComponentDetail".component_name NOT IN ('AuctionTypeRuleGrp', 'BaseTradingRules', 'ExecInstRules', 'InstrumentScope', 'InstrumentScopeGrp', 'InstrumentScopeSecurityAltIDGrp', 'LotTypeRules', 'MarketDataFeedTypes', 'MarketSegmentScopeGrp', 'MatchRules', 'OrdTypeRules', 'PriceLimits', 'PriceRangeRuleGrp', 'QuoteSizeRuleGrp', 'RequestedPartyRoleGrp', 'RequestingPartyGrp', 'RequestingPartySubGrp', 'RoutingGrp', 'TickRules', 'TimeInForceRules', 'TradingSessionRules'))

UNION ALL

SELECT 'CommonComponentDetail' AS table_name, 'repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, repetition AS invalid_value 
FROM "CommonComponentDetail" 
WHERE "CommonComponentDetail".repetition IS NOT NULL AND ("CommonComponentDetail".repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'PreTradeLayoutRow' AS table_name, 'pre_layout_kind' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PreTradeLayoutRow" 
WHERE "PreTradeLayoutRow".pre_layout_kind IS NULL

UNION ALL

SELECT 'PreTradeLayoutRow' AS table_name, 'pre_layout_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, pre_layout_kind AS invalid_value 
FROM "PreTradeLayoutRow" 
WHERE "PreTradeLayoutRow".pre_layout_kind IS NOT NULL AND ("PreTradeLayoutRow".pre_layout_kind NOT IN ('FIELD', 'COMPONENT'))

UNION ALL

SELECT 'PreTradeLayoutRow' AS table_name, 'pre_layout_field_tag' AS column_name, 'range' AS constraint_type, id AS record_id, pre_layout_field_tag AS invalid_value 
FROM "PreTradeLayoutRow" 
WHERE "PreTradeLayoutRow".pre_layout_field_tag < 0

UNION ALL

SELECT 'PreTradeLayoutRow' AS table_name, 'pre_layout_element_name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PreTradeLayoutRow" 
WHERE "PreTradeLayoutRow".pre_layout_element_name IS NULL

UNION ALL

SELECT 'TradeBusinessArea' AS table_name, 'trade_area' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TradeBusinessArea" 
WHERE "TradeBusinessArea".trade_area IS NULL

UNION ALL

SELECT 'TradeBusinessArea' AS table_name, 'trade_area' AS column_name, 'enum' AS constraint_type, id AS record_id, trade_area AS invalid_value 
FROM "TradeBusinessArea" 
WHERE "TradeBusinessArea".trade_area IS NOT NULL AND ("TradeBusinessArea".trade_area NOT IN ('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE'))

UNION ALL

SELECT 'TradeBusinessArea' AS table_name, 'trade_common_components' AS column_name, 'enum' AS constraint_type, id AS record_id, trade_common_components AS invalid_value 
FROM "TradeBusinessArea" 
WHERE "TradeBusinessArea".trade_common_components IS NOT NULL AND ("TradeBusinessArea".trade_common_components NOT IN ('DisclosureInstructionGrp', 'DiscretionInstructions', 'PegInstructions', 'PreAllocGrp', 'StrategyParametersGrp', 'TriggeringInstruction'))

UNION ALL

SELECT 'TradeMessageEntry' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "TradeMessageEntry" 
WHERE "TradeMessageEntry".msg_type IS NULL

UNION ALL

SELECT 'TradeMessageEntry' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "TradeMessageEntry" 
WHERE "TradeMessageEntry".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'TradeMessageEntry' AS table_name, 'msg_type' AS column_name, 'identifier' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "TradeMessageEntry" 
WHERE "TradeMessageEntry".msg_type IN (SELECT msg_type 
FROM "TradeMessageEntry" GROUP BY msg_type 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeMessageEntry' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "TradeMessageEntry" 
WHERE "TradeMessageEntry".message_name IS NULL

UNION ALL

SELECT 'TradeMessageEntry' AS table_name, 'category' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "TradeMessageEntry" 
WHERE "TradeMessageEntry".category IS NULL

UNION ALL

SELECT 'TradeMessageEntry' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, msg_type AS record_id, category AS invalid_value 
FROM "TradeMessageEntry" 
WHERE "TradeMessageEntry".category IS NOT NULL AND ("TradeMessageEntry".category NOT IN ('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING'))

UNION ALL

SELECT 'TradeComponentEntry' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "TradeComponentEntry" 
WHERE "TradeComponentEntry".component_name IS NULL

UNION ALL

SELECT 'TradeComponentEntry' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "TradeComponentEntry" 
WHERE "TradeComponentEntry".component_name IN (SELECT component_name 
FROM "TradeComponentEntry" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeComponentEntry' AS table_name, 'trade_repetition' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "TradeComponentEntry" 
WHERE "TradeComponentEntry".trade_repetition IS NULL

UNION ALL

SELECT 'TradeComponentEntry' AS table_name, 'trade_repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, trade_repetition AS invalid_value 
FROM "TradeComponentEntry" 
WHERE "TradeComponentEntry".trade_repetition IS NOT NULL AND ("TradeComponentEntry".trade_repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'TradeComponentEntry' AS table_name, 'category' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "TradeComponentEntry" 
WHERE "TradeComponentEntry".category IS NULL

UNION ALL

SELECT 'TradeComponentEntry' AS table_name, 'trade_footnote_number' AS column_name, 'range' AS constraint_type, component_name AS record_id, trade_footnote_number AS invalid_value 
FROM "TradeComponentEntry" 
WHERE "TradeComponentEntry".trade_footnote_number < 1 OR "TradeComponentEntry".trade_footnote_number > 25

UNION ALL

SELECT 'TradeComponentTableFootnote' AS table_name, 'trade_footnote_number' AS column_name, 'required' AS constraint_type, trade_footnote_number AS record_id, NULL AS invalid_value 
FROM "TradeComponentTableFootnote" 
WHERE "TradeComponentTableFootnote".trade_footnote_number IS NULL

UNION ALL

SELECT 'TradeComponentTableFootnote' AS table_name, 'trade_footnote_number' AS column_name, 'range' AS constraint_type, trade_footnote_number AS record_id, trade_footnote_number AS invalid_value 
FROM "TradeComponentTableFootnote" 
WHERE "TradeComponentTableFootnote".trade_footnote_number < 1 OR "TradeComponentTableFootnote".trade_footnote_number > 25

UNION ALL

SELECT 'TradeComponentTableFootnote' AS table_name, 'trade_footnote_number' AS column_name, 'identifier' AS constraint_type, trade_footnote_number AS record_id, trade_footnote_number AS invalid_value 
FROM "TradeComponentTableFootnote" 
WHERE "TradeComponentTableFootnote".trade_footnote_number IN (SELECT trade_footnote_number 
FROM "TradeComponentTableFootnote" GROUP BY trade_footnote_number 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeComponentTableFootnote' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, trade_footnote_number AS record_id, NULL AS invalid_value 
FROM "TradeComponentTableFootnote" 
WHERE "TradeComponentTableFootnote".component_name IS NULL

UNION ALL

SELECT 'TradeComponentTableFootnote' AS table_name, 'trade_introduced_in' AS column_name, 'required' AS constraint_type, trade_footnote_number AS record_id, NULL AS invalid_value 
FROM "TradeComponentTableFootnote" 
WHERE "TradeComponentTableFootnote".trade_introduced_in IS NULL

UNION ALL

SELECT 'TradeComponentTableFootnote' AS table_name, 'trade_sole_category' AS column_name, 'required' AS constraint_type, trade_footnote_number AS record_id, NULL AS invalid_value 
FROM "TradeComponentTableFootnote" 
WHERE "TradeComponentTableFootnote".trade_sole_category IS NULL

UNION ALL

SELECT 'TradeComponentTableFootnote' AS table_name, 'trade_sole_category' AS column_name, 'enum' AS constraint_type, trade_footnote_number AS record_id, trade_sole_category AS invalid_value 
FROM "TradeComponentTableFootnote" 
WHERE "TradeComponentTableFootnote".trade_sole_category IS NOT NULL AND ("TradeComponentTableFootnote".trade_sole_category NOT IN ('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING'))

UNION ALL

SELECT 'TradeCategorySection' AS table_name, 'category' AS column_name, 'required' AS constraint_type, category AS record_id, NULL AS invalid_value 
FROM "TradeCategorySection" 
WHERE "TradeCategorySection".category IS NULL

UNION ALL

SELECT 'TradeCategorySection' AS table_name, 'category' AS column_name, 'identifier' AS constraint_type, category AS record_id, category AS invalid_value 
FROM "TradeCategorySection" 
WHERE "TradeCategorySection".category IN (SELECT category 
FROM "TradeCategorySection" GROUP BY category 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeCategorySection' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, category AS record_id, category AS invalid_value 
FROM "TradeCategorySection" 
WHERE "TradeCategorySection".category IS NOT NULL AND ("TradeCategorySection".category NOT IN ('SINGLE_GENERAL_ORDER_HANDLING', 'ORDER_MASS_HANDLING', 'CROSS_ORDER_HANDLING', 'MULTILEG_ORDER_HANDLING', 'LIST_PROGRAM_BASKET_TRADING'))

UNION ALL

SELECT 'TradeMessageDetail' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "TradeMessageDetail" 
WHERE "TradeMessageDetail".msg_type IS NULL

UNION ALL

SELECT 'TradeMessageDetail' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "TradeMessageDetail" 
WHERE "TradeMessageDetail".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'TradeMessageDetail' AS table_name, 'msg_type' AS column_name, 'identifier' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "TradeMessageDetail" 
WHERE "TradeMessageDetail".msg_type IN (SELECT msg_type 
FROM "TradeMessageDetail" GROUP BY msg_type 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeMessageDetail' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "TradeMessageDetail" 
WHERE "TradeMessageDetail".message_name IS NULL

UNION ALL

SELECT 'TradeComponentDetail' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "TradeComponentDetail" 
WHERE "TradeComponentDetail".component_name IS NULL

UNION ALL

SELECT 'TradeComponentDetail' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "TradeComponentDetail" 
WHERE "TradeComponentDetail".component_name IN (SELECT component_name 
FROM "TradeComponentDetail" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeComponentDetail' AS table_name, 'trade_repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, trade_repetition AS invalid_value 
FROM "TradeComponentDetail" 
WHERE "TradeComponentDetail".trade_repetition IS NOT NULL AND ("TradeComponentDetail".trade_repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'TradeMessageGroup' AS table_name, 'trade_group_title' AS column_name, 'required' AS constraint_type, trade_group_title AS record_id, NULL AS invalid_value 
FROM "TradeMessageGroup" 
WHERE "TradeMessageGroup".trade_group_title IS NULL

UNION ALL

SELECT 'TradeMessageGroup' AS table_name, 'trade_group_title' AS column_name, 'identifier' AS constraint_type, trade_group_title AS record_id, trade_group_title AS invalid_value 
FROM "TradeMessageGroup" 
WHERE "TradeMessageGroup".trade_group_title IN (SELECT trade_group_title 
FROM "TradeMessageGroup" GROUP BY trade_group_title 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeMessageGroup' AS table_name, 'messages' AS column_name, 'required' AS constraint_type, trade_group_title AS record_id, NULL AS invalid_value 
FROM "TradeMessageGroup" 
WHERE "TradeMessageGroup".messages IS NULL

UNION ALL

SELECT 'TradeCommonComponentDetail' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "TradeCommonComponentDetail" 
WHERE "TradeCommonComponentDetail".component_name IS NULL

UNION ALL

SELECT 'TradeCommonComponentDetail' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "TradeCommonComponentDetail" 
WHERE "TradeCommonComponentDetail".component_name IN (SELECT component_name 
FROM "TradeCommonComponentDetail" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeCommonComponentDetail' AS table_name, 'component_name' AS column_name, 'enum' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "TradeCommonComponentDetail" 
WHERE "TradeCommonComponentDetail".component_name IS NOT NULL AND ("TradeCommonComponentDetail".component_name NOT IN ('DisclosureInstructionGrp', 'DiscretionInstructions', 'PegInstructions', 'PreAllocGrp', 'StrategyParametersGrp', 'TriggeringInstruction'))

UNION ALL

SELECT 'TradeCommonComponentDetail' AS table_name, 'trade_repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, trade_repetition AS invalid_value 
FROM "TradeCommonComponentDetail" 
WHERE "TradeCommonComponentDetail".trade_repetition IS NOT NULL AND ("TradeCommonComponentDetail".trade_repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'TradeLayoutRow' AS table_name, 'trade_layout_kind' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TradeLayoutRow" 
WHERE "TradeLayoutRow".trade_layout_kind IS NULL

UNION ALL

SELECT 'TradeLayoutRow' AS table_name, 'trade_layout_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, trade_layout_kind AS invalid_value 
FROM "TradeLayoutRow" 
WHERE "TradeLayoutRow".trade_layout_kind IS NOT NULL AND ("TradeLayoutRow".trade_layout_kind NOT IN ('FIELD', 'COMPONENT'))

UNION ALL

SELECT 'TradeLayoutRow' AS table_name, 'trade_layout_field_tag' AS column_name, 'range' AS constraint_type, id AS record_id, trade_layout_field_tag AS invalid_value 
FROM "TradeLayoutRow" 
WHERE "TradeLayoutRow".trade_layout_field_tag < 0

UNION ALL

SELECT 'TradeLayoutRow' AS table_name, 'trade_layout_element_name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "TradeLayoutRow" 
WHERE "TradeLayoutRow".trade_layout_element_name IS NULL

UNION ALL

SELECT 'TradeOrdStatusPrecedenceEntry' AS table_name, 'trade_ord_status_precedence' AS column_name, 'required' AS constraint_type, trade_ord_status_label AS record_id, NULL AS invalid_value 
FROM "TradeOrdStatusPrecedenceEntry" 
WHERE "TradeOrdStatusPrecedenceEntry".trade_ord_status_precedence IS NULL

UNION ALL

SELECT 'TradeOrdStatusPrecedenceEntry' AS table_name, 'trade_ord_status_precedence' AS column_name, 'range' AS constraint_type, trade_ord_status_label AS record_id, trade_ord_status_precedence AS invalid_value 
FROM "TradeOrdStatusPrecedenceEntry" 
WHERE "TradeOrdStatusPrecedenceEntry".trade_ord_status_precedence < 1 OR "TradeOrdStatusPrecedenceEntry".trade_ord_status_precedence > 11

UNION ALL

SELECT 'TradeOrdStatusPrecedenceEntry' AS table_name, 'trade_ord_status_label' AS column_name, 'required' AS constraint_type, trade_ord_status_label AS record_id, NULL AS invalid_value 
FROM "TradeOrdStatusPrecedenceEntry" 
WHERE "TradeOrdStatusPrecedenceEntry".trade_ord_status_label IS NULL

UNION ALL

SELECT 'TradeOrdStatusPrecedenceEntry' AS table_name, 'trade_ord_status_label' AS column_name, 'identifier' AS constraint_type, trade_ord_status_label AS record_id, trade_ord_status_label AS invalid_value 
FROM "TradeOrdStatusPrecedenceEntry" 
WHERE "TradeOrdStatusPrecedenceEntry".trade_ord_status_label IN (SELECT trade_ord_status_label 
FROM "TradeOrdStatusPrecedenceEntry" GROUP BY trade_ord_status_label 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeFragmentationEntry' AS table_name, 'trade_fragmentation_message' AS column_name, 'required' AS constraint_type, trade_fragmentation_message AS record_id, NULL AS invalid_value 
FROM "TradeFragmentationEntry" 
WHERE "TradeFragmentationEntry".trade_fragmentation_message IS NULL

UNION ALL

SELECT 'TradeFragmentationEntry' AS table_name, 'trade_fragmentation_message' AS column_name, 'identifier' AS constraint_type, trade_fragmentation_message AS record_id, trade_fragmentation_message AS invalid_value 
FROM "TradeFragmentationEntry" 
WHERE "TradeFragmentationEntry".trade_fragmentation_message IN (SELECT trade_fragmentation_message 
FROM "TradeFragmentationEntry" GROUP BY trade_fragmentation_message 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeFragmentationEntry' AS table_name, 'trade_fragmentation_total_entries_field' AS column_name, 'required' AS constraint_type, trade_fragmentation_message AS record_id, NULL AS invalid_value 
FROM "TradeFragmentationEntry" 
WHERE "TradeFragmentationEntry".trade_fragmentation_total_entries_field IS NULL

UNION ALL

SELECT 'TradeFragmentationEntry' AS table_name, 'trade_fragmentation_repeating_group' AS column_name, 'required' AS constraint_type, trade_fragmentation_message AS record_id, NULL AS invalid_value 
FROM "TradeFragmentationEntry" 
WHERE "TradeFragmentationEntry".trade_fragmentation_repeating_group IS NULL

UNION ALL

SELECT 'TradeAppendixSection' AS table_name, 'trade_appendix_category' AS column_name, 'required' AS constraint_type, trade_appendix_category AS record_id, NULL AS invalid_value 
FROM "TradeAppendixSection" 
WHERE "TradeAppendixSection".trade_appendix_category IS NULL

UNION ALL

SELECT 'TradeAppendixSection' AS table_name, 'trade_appendix_category' AS column_name, 'identifier' AS constraint_type, trade_appendix_category AS record_id, trade_appendix_category AS invalid_value 
FROM "TradeAppendixSection" 
WHERE "TradeAppendixSection".trade_appendix_category IN (SELECT trade_appendix_category 
FROM "TradeAppendixSection" GROUP BY trade_appendix_category 
HAVING count(*) > 1)

UNION ALL

SELECT 'PostTradeBusinessArea' AS table_name, 'area' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PostTradeBusinessArea" 
WHERE "PostTradeBusinessArea".area IS NULL

UNION ALL

SELECT 'PostTradeBusinessArea' AS table_name, 'area' AS column_name, 'enum' AS constraint_type, id AS record_id, area AS invalid_value 
FROM "PostTradeBusinessArea" 
WHERE "PostTradeBusinessArea".area IS NOT NULL AND ("PostTradeBusinessArea".area NOT IN ('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE'))

UNION ALL

SELECT 'PostTradeBusinessArea' AS table_name, 'post_common_components' AS column_name, 'enum' AS constraint_type, id AS record_id, post_common_components AS invalid_value 
FROM "PostTradeBusinessArea" 
WHERE "PostTradeBusinessArea".post_common_components IS NOT NULL AND ("PostTradeBusinessArea".post_common_components NOT IN ('AllocCommissionDataGrp', 'AllocRegulatoryTradeIDGrp', 'ClrInstGrp', 'CollateralAmountGrp', 'CollateralReinvestmentGrp', 'DlvyInstGrp', 'ExecAllocGrp', 'MarginAmount', 'OrdAllocGrp', 'PositionAmountData', 'SettlDetails', 'SettlInstructionsData', 'SettlParties', 'SettlPtysSubGrp', 'TradeAllocAmtGrp', 'TransactionAttributeGrp'))

UNION ALL

SELECT 'PostTradeBusinessArea' AS table_name, 'messages' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PostTradeBusinessArea" 
WHERE "PostTradeBusinessArea".messages IS NULL

UNION ALL

SELECT 'PostTradeBusinessArea' AS table_name, 'components' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PostTradeBusinessArea" 
WHERE "PostTradeBusinessArea".components IS NULL

UNION ALL

SELECT 'PostTradeMessageEntry' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PostTradeMessageEntry" 
WHERE "PostTradeMessageEntry".msg_type IS NULL

UNION ALL

SELECT 'PostTradeMessageEntry' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "PostTradeMessageEntry" 
WHERE "PostTradeMessageEntry".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'PostTradeMessageEntry' AS table_name, 'msg_type' AS column_name, 'identifier' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "PostTradeMessageEntry" 
WHERE "PostTradeMessageEntry".msg_type IN (SELECT msg_type 
FROM "PostTradeMessageEntry" GROUP BY msg_type 
HAVING count(*) > 1)

UNION ALL

SELECT 'PostTradeMessageEntry' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PostTradeMessageEntry" 
WHERE "PostTradeMessageEntry".message_name IS NULL

UNION ALL

SELECT 'PostTradeMessageEntry' AS table_name, 'category' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PostTradeMessageEntry" 
WHERE "PostTradeMessageEntry".category IS NULL

UNION ALL

SELECT 'PostTradeMessageEntry' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, msg_type AS record_id, category AS invalid_value 
FROM "PostTradeMessageEntry" 
WHERE "PostTradeMessageEntry".category IS NOT NULL AND ("PostTradeMessageEntry".category NOT IN ('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT'))

UNION ALL

SELECT 'PostTradeComponentEntry' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "PostTradeComponentEntry" 
WHERE "PostTradeComponentEntry".component_name IS NULL

UNION ALL

SELECT 'PostTradeComponentEntry' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "PostTradeComponentEntry" 
WHERE "PostTradeComponentEntry".component_name IN (SELECT component_name 
FROM "PostTradeComponentEntry" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'PostTradeComponentEntry' AS table_name, 'repetition' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "PostTradeComponentEntry" 
WHERE "PostTradeComponentEntry".repetition IS NULL

UNION ALL

SELECT 'PostTradeComponentEntry' AS table_name, 'repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, repetition AS invalid_value 
FROM "PostTradeComponentEntry" 
WHERE "PostTradeComponentEntry".repetition IS NOT NULL AND ("PostTradeComponentEntry".repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'PostTradeComponentEntry' AS table_name, 'category' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "PostTradeComponentEntry" 
WHERE "PostTradeComponentEntry".category IS NULL

UNION ALL

SELECT 'PostTradeComponentEntry' AS table_name, 'footnote_number' AS column_name, 'range' AS constraint_type, component_name AS record_id, footnote_number AS invalid_value 
FROM "PostTradeComponentEntry" 
WHERE "PostTradeComponentEntry".footnote_number < 1 OR "PostTradeComponentEntry".footnote_number > 25

UNION ALL

SELECT 'PostTradeComponentTableFootnote' AS table_name, 'footnote_number' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "PostTradeComponentTableFootnote" 
WHERE "PostTradeComponentTableFootnote".footnote_number IS NULL

UNION ALL

SELECT 'PostTradeComponentTableFootnote' AS table_name, 'footnote_number' AS column_name, 'range' AS constraint_type, footnote_number AS record_id, footnote_number AS invalid_value 
FROM "PostTradeComponentTableFootnote" 
WHERE "PostTradeComponentTableFootnote".footnote_number < 1 OR "PostTradeComponentTableFootnote".footnote_number > 25

UNION ALL

SELECT 'PostTradeComponentTableFootnote' AS table_name, 'footnote_number' AS column_name, 'identifier' AS constraint_type, footnote_number AS record_id, footnote_number AS invalid_value 
FROM "PostTradeComponentTableFootnote" 
WHERE "PostTradeComponentTableFootnote".footnote_number IN (SELECT footnote_number 
FROM "PostTradeComponentTableFootnote" GROUP BY footnote_number 
HAVING count(*) > 1)

UNION ALL

SELECT 'PostTradeComponentTableFootnote' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "PostTradeComponentTableFootnote" 
WHERE "PostTradeComponentTableFootnote".component_name IS NULL

UNION ALL

SELECT 'PostTradeComponentTableFootnote' AS table_name, 'introduced_in' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "PostTradeComponentTableFootnote" 
WHERE "PostTradeComponentTableFootnote".introduced_in IS NULL

UNION ALL

SELECT 'PostTradeComponentTableFootnote' AS table_name, 'post_sole_category' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "PostTradeComponentTableFootnote" 
WHERE "PostTradeComponentTableFootnote".post_sole_category IS NULL

UNION ALL

SELECT 'PostTradeComponentTableFootnote' AS table_name, 'post_sole_category' AS column_name, 'enum' AS constraint_type, footnote_number AS record_id, post_sole_category AS invalid_value 
FROM "PostTradeComponentTableFootnote" 
WHERE "PostTradeComponentTableFootnote".post_sole_category IS NOT NULL AND ("PostTradeComponentTableFootnote".post_sole_category NOT IN ('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT'))

UNION ALL

SELECT 'PostTradeCategorySection' AS table_name, 'category' AS column_name, 'required' AS constraint_type, category AS record_id, NULL AS invalid_value 
FROM "PostTradeCategorySection" 
WHERE "PostTradeCategorySection".category IS NULL

UNION ALL

SELECT 'PostTradeCategorySection' AS table_name, 'category' AS column_name, 'identifier' AS constraint_type, category AS record_id, category AS invalid_value 
FROM "PostTradeCategorySection" 
WHERE "PostTradeCategorySection".category IN (SELECT category 
FROM "PostTradeCategorySection" GROUP BY category 
HAVING count(*) > 1)

UNION ALL

SELECT 'PostTradeCategorySection' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, category AS record_id, category AS invalid_value 
FROM "PostTradeCategorySection" 
WHERE "PostTradeCategorySection".category IS NOT NULL AND ("PostTradeCategorySection".category NOT IN ('ALLOCATION', 'CONFIRMATION', 'SETTLEMENT_INSTRUCTION', 'TRADE_CAPTURE_REPORTING', 'REGISTRATION_INSTRUCTION', 'POSITION_MAINTENANCE', 'COLLATERAL_MANAGEMENT', 'MARGIN_REQUIREMENT_MANAGEMENT', 'ACCOUNT_REPORTING', 'TRADE_MANAGEMENT', 'PAY_MANAGEMENT', 'SETTLEMENT_STATUS_MANAGEMENT'))

UNION ALL

SELECT 'PostTradeCategorySection' AS table_name, 'allocation_scenarios' AS column_name, 'enum' AS constraint_type, category AS record_id, allocation_scenarios AS invalid_value 
FROM "PostTradeCategorySection" 
WHERE "PostTradeCategorySection".allocation_scenarios IS NOT NULL AND ("PostTradeCategorySection".allocation_scenarios NOT IN ('PRE_ALLOCATED_ORDER', 'PRE_TRADE_ALLOCATION', 'POST_TRADE_ALLOCATION', 'READY_TO_BOOK'))

UNION ALL

SELECT 'PostTradeCategorySection' AS table_name, 'allocation_roles' AS column_name, 'enum' AS constraint_type, category AS record_id, allocation_roles AS invalid_value 
FROM "PostTradeCategorySection" 
WHERE "PostTradeCategorySection".allocation_roles IS NOT NULL AND ("PostTradeCategorySection".allocation_roles NOT IN ('INITIATOR', 'RESPONDENT'))

UNION ALL

SELECT 'PostTradeCategorySection' AS table_name, 'post_trade_allocation_pricing_methods' AS column_name, 'enum' AS constraint_type, category AS record_id, post_trade_allocation_pricing_methods AS invalid_value 
FROM "PostTradeCategorySection" 
WHERE "PostTradeCategorySection".post_trade_allocation_pricing_methods IS NOT NULL AND ("PostTradeCategorySection".post_trade_allocation_pricing_methods NOT IN ('AVERAGE_PRICE', 'EXECUTED_PRICE'))

UNION ALL

SELECT 'PostTradeCategorySection' AS table_name, 'clearing_services_for_position_management' AS column_name, 'enum' AS constraint_type, category AS record_id, clearing_services_for_position_management AS invalid_value 
FROM "PostTradeCategorySection" 
WHERE "PostTradeCategorySection".clearing_services_for_position_management IS NOT NULL AND ("PostTradeCategorySection".clearing_services_for_position_management NOT IN ('POSITION_CHANGE_SUBMISSION', 'POSITION_ADJUSTMENT', 'EXERCISE_NOTICE', 'ABANDONMENT_NOTICE', 'MARGIN_DISPOSITION', 'POSITION_PLEDGE', 'REQUEST_FOR_POSITION'))

UNION ALL

SELECT 'PostTradeCategorySection' AS table_name, 'collateral_management_usages' AS column_name, 'enum' AS constraint_type, category AS record_id, collateral_management_usages AS invalid_value 
FROM "PostTradeCategorySection" 
WHERE "PostTradeCategorySection".collateral_management_usages IS NOT NULL AND ("PostTradeCategorySection".collateral_management_usages NOT IN ('SECURITIES_FINANCING_COLLATERALIZATION', 'CLEARING_HOUSE_COLLATERALIZATION'))

UNION ALL

SELECT 'PostTradeCategorySection' AS table_name, 'collateral_assignment_purposes' AS column_name, 'enum' AS constraint_type, category AS record_id, collateral_assignment_purposes AS invalid_value 
FROM "PostTradeCategorySection" 
WHERE "PostTradeCategorySection".collateral_assignment_purposes IS NOT NULL AND ("PostTradeCategorySection".collateral_assignment_purposes NOT IN ('ASSIGN_INITIAL_COLLATERAL', 'REPLENISH_COLLATERAL', 'REPLACE_OR_SUBSTITUTE_COLLATERAL'))

UNION ALL

SELECT 'PostTradeMessageGroup' AS table_name, 'group_title' AS column_name, 'required' AS constraint_type, group_title AS record_id, NULL AS invalid_value 
FROM "PostTradeMessageGroup" 
WHERE "PostTradeMessageGroup".group_title IS NULL

UNION ALL

SELECT 'PostTradeMessageGroup' AS table_name, 'group_title' AS column_name, 'identifier' AS constraint_type, group_title AS record_id, group_title AS invalid_value 
FROM "PostTradeMessageGroup" 
WHERE "PostTradeMessageGroup".group_title IN (SELECT group_title 
FROM "PostTradeMessageGroup" GROUP BY group_title 
HAVING count(*) > 1)

UNION ALL

SELECT 'PostTradeMessageGroup' AS table_name, 'messages' AS column_name, 'required' AS constraint_type, group_title AS record_id, NULL AS invalid_value 
FROM "PostTradeMessageGroup" 
WHERE "PostTradeMessageGroup".messages IS NULL

UNION ALL

SELECT 'PostTradeMessageDetail' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PostTradeMessageDetail" 
WHERE "PostTradeMessageDetail".msg_type IS NULL

UNION ALL

SELECT 'PostTradeMessageDetail' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "PostTradeMessageDetail" 
WHERE "PostTradeMessageDetail".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'PostTradeMessageDetail' AS table_name, 'msg_type' AS column_name, 'identifier' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "PostTradeMessageDetail" 
WHERE "PostTradeMessageDetail".msg_type IN (SELECT msg_type 
FROM "PostTradeMessageDetail" GROUP BY msg_type 
HAVING count(*) > 1)

UNION ALL

SELECT 'PostTradeMessageDetail' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "PostTradeMessageDetail" 
WHERE "PostTradeMessageDetail".message_name IS NULL

UNION ALL

SELECT 'PostTradeComponentDetail' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "PostTradeComponentDetail" 
WHERE "PostTradeComponentDetail".component_name IS NULL

UNION ALL

SELECT 'PostTradeComponentDetail' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "PostTradeComponentDetail" 
WHERE "PostTradeComponentDetail".component_name IN (SELECT component_name 
FROM "PostTradeComponentDetail" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'PostTradeComponentDetail' AS table_name, 'repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, repetition AS invalid_value 
FROM "PostTradeComponentDetail" 
WHERE "PostTradeComponentDetail".repetition IS NOT NULL AND ("PostTradeComponentDetail".repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'PostTradeCommonComponentDetail' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "PostTradeCommonComponentDetail" 
WHERE "PostTradeCommonComponentDetail".component_name IS NULL

UNION ALL

SELECT 'PostTradeCommonComponentDetail' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "PostTradeCommonComponentDetail" 
WHERE "PostTradeCommonComponentDetail".component_name IN (SELECT component_name 
FROM "PostTradeCommonComponentDetail" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'PostTradeCommonComponentDetail' AS table_name, 'component_name' AS column_name, 'enum' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "PostTradeCommonComponentDetail" 
WHERE "PostTradeCommonComponentDetail".component_name IS NOT NULL AND ("PostTradeCommonComponentDetail".component_name NOT IN ('AllocCommissionDataGrp', 'AllocRegulatoryTradeIDGrp', 'ClrInstGrp', 'CollateralAmountGrp', 'CollateralReinvestmentGrp', 'DlvyInstGrp', 'ExecAllocGrp', 'MarginAmount', 'OrdAllocGrp', 'PositionAmountData', 'SettlDetails', 'SettlInstructionsData', 'SettlParties', 'SettlPtysSubGrp', 'TradeAllocAmtGrp', 'TransactionAttributeGrp'))

UNION ALL

SELECT 'PostTradeCommonComponentDetail' AS table_name, 'repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, repetition AS invalid_value 
FROM "PostTradeCommonComponentDetail" 
WHERE "PostTradeCommonComponentDetail".repetition IS NOT NULL AND ("PostTradeCommonComponentDetail".repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'AllocationStatusDescription' AS table_name, 'status_code' AS column_name, 'required' AS constraint_type, status_code AS record_id, NULL AS invalid_value 
FROM "AllocationStatusDescription" 
WHERE "AllocationStatusDescription".status_code IS NULL

UNION ALL

SELECT 'AllocationStatusDescription' AS table_name, 'status_code' AS column_name, 'identifier' AS constraint_type, status_code AS record_id, status_code AS invalid_value 
FROM "AllocationStatusDescription" 
WHERE "AllocationStatusDescription".status_code IN (SELECT status_code 
FROM "AllocationStatusDescription" GROUP BY status_code 
HAVING count(*) > 1)

UNION ALL

SELECT 'AllocationStatusDescription' AS table_name, 'status_label' AS column_name, 'required' AS constraint_type, status_code AS record_id, NULL AS invalid_value 
FROM "AllocationStatusDescription" 
WHERE "AllocationStatusDescription".status_label IS NULL

UNION ALL

SELECT 'AllocationFragmentationFieldMap' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "AllocationFragmentationFieldMap" 
WHERE "AllocationFragmentationFieldMap".msg_type IS NULL

UNION ALL

SELECT 'AllocationFragmentationFieldMap' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "AllocationFragmentationFieldMap" 
WHERE "AllocationFragmentationFieldMap".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'AllocationFragmentationFieldMap' AS table_name, 'msg_type' AS column_name, 'identifier' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "AllocationFragmentationFieldMap" 
WHERE "AllocationFragmentationFieldMap".msg_type IN (SELECT msg_type 
FROM "AllocationFragmentationFieldMap" GROUP BY msg_type 
HAVING count(*) > 1)

UNION ALL

SELECT 'AllocationFragmentationFieldMap' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "AllocationFragmentationFieldMap" 
WHERE "AllocationFragmentationFieldMap".message_name IS NULL

UNION ALL

SELECT 'AllocationFragmentationFieldMap' AS table_name, 'total_count_field' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "AllocationFragmentationFieldMap" 
WHERE "AllocationFragmentationFieldMap".total_count_field IS NULL

UNION ALL

SELECT 'AllocationFragmentationFieldMap' AS table_name, 'fragment_count_field' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "AllocationFragmentationFieldMap" 
WHERE "AllocationFragmentationFieldMap".fragment_count_field IS NULL

UNION ALL

SELECT 'AllocationFragmentationFieldMap' AS table_name, 'principal_message_reference' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "AllocationFragmentationFieldMap" 
WHERE "AllocationFragmentationFieldMap".principal_message_reference IS NULL

UNION ALL

SELECT 'TradeCaptureReportUsage' AS table_name, 'status_label' AS column_name, 'required' AS constraint_type, status_label AS record_id, NULL AS invalid_value 
FROM "TradeCaptureReportUsage" 
WHERE "TradeCaptureReportUsage".status_label IS NULL

UNION ALL

SELECT 'TradeCaptureReportUsage' AS table_name, 'status_label' AS column_name, 'identifier' AS constraint_type, status_label AS record_id, status_label AS invalid_value 
FROM "TradeCaptureReportUsage" 
WHERE "TradeCaptureReportUsage".status_label IN (SELECT status_label 
FROM "TradeCaptureReportUsage" GROUP BY status_label 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeCaptureReportUsage' AS table_name, 'identifier_role' AS column_name, 'enum' AS constraint_type, status_label AS record_id, identifier_role AS invalid_value 
FROM "TradeCaptureReportUsage" 
WHERE "TradeCaptureReportUsage".identifier_role IS NOT NULL AND ("TradeCaptureReportUsage".identifier_role NOT IN ('TRADE_REPORT_ID', 'TRADE_ID', 'TRADE_REPORT_REF_ID', 'SECONDARY_TRADE_ID'))

UNION ALL

SELECT 'TradeCaptureReportIdentifierRule' AS table_name, 'identifier_role' AS column_name, 'required' AS constraint_type, identifier_role AS record_id, NULL AS invalid_value 
FROM "TradeCaptureReportIdentifierRule" 
WHERE "TradeCaptureReportIdentifierRule".identifier_role IS NULL

UNION ALL

SELECT 'TradeCaptureReportIdentifierRule' AS table_name, 'identifier_role' AS column_name, 'identifier' AS constraint_type, identifier_role AS record_id, identifier_role AS invalid_value 
FROM "TradeCaptureReportIdentifierRule" 
WHERE "TradeCaptureReportIdentifierRule".identifier_role IN (SELECT identifier_role 
FROM "TradeCaptureReportIdentifierRule" GROUP BY identifier_role 
HAVING count(*) > 1)

UNION ALL

SELECT 'TradeCaptureReportIdentifierRule' AS table_name, 'identifier_role' AS column_name, 'enum' AS constraint_type, identifier_role AS record_id, identifier_role AS invalid_value 
FROM "TradeCaptureReportIdentifierRule" 
WHERE "TradeCaptureReportIdentifierRule".identifier_role IS NOT NULL AND ("TradeCaptureReportIdentifierRule".identifier_role NOT IN ('TRADE_REPORT_ID', 'TRADE_ID', 'TRADE_REPORT_REF_ID', 'SECONDARY_TRADE_ID'))

UNION ALL

SELECT 'RegistrationStatusDescription' AS table_name, 'status_code' AS column_name, 'required' AS constraint_type, status_code AS record_id, NULL AS invalid_value 
FROM "RegistrationStatusDescription" 
WHERE "RegistrationStatusDescription".status_code IS NULL

UNION ALL

SELECT 'RegistrationStatusDescription' AS table_name, 'status_code' AS column_name, 'identifier' AS constraint_type, status_code AS record_id, status_code AS invalid_value 
FROM "RegistrationStatusDescription" 
WHERE "RegistrationStatusDescription".status_code IN (SELECT status_code 
FROM "RegistrationStatusDescription" GROUP BY status_code 
HAVING count(*) > 1)

UNION ALL

SELECT 'RegistrationStatusDescription' AS table_name, 'status_label' AS column_name, 'required' AS constraint_type, status_code AS record_id, NULL AS invalid_value 
FROM "RegistrationStatusDescription" 
WHERE "RegistrationStatusDescription".status_label IS NULL

UNION ALL

SELECT 'ClearingServicePostTradeProcessingFormat' AS table_name, 'message_format' AS column_name, 'required' AS constraint_type, message_format AS record_id, NULL AS invalid_value 
FROM "ClearingServicePostTradeProcessingFormat" 
WHERE "ClearingServicePostTradeProcessingFormat".message_format IS NULL

UNION ALL

SELECT 'ClearingServicePostTradeProcessingFormat' AS table_name, 'message_format' AS column_name, 'identifier' AS constraint_type, message_format AS record_id, message_format AS invalid_value 
FROM "ClearingServicePostTradeProcessingFormat" 
WHERE "ClearingServicePostTradeProcessingFormat".message_format IN (SELECT message_format 
FROM "ClearingServicePostTradeProcessingFormat" GROUP BY message_format 
HAVING count(*) > 1)

UNION ALL

SELECT 'ClearingServicePostTradeProcessingFormat' AS table_name, 'message_format' AS column_name, 'enum' AS constraint_type, message_format AS record_id, message_format AS invalid_value 
FROM "ClearingServicePostTradeProcessingFormat" 
WHERE "ClearingServicePostTradeProcessingFormat".message_format IS NOT NULL AND ("ClearingServicePostTradeProcessingFormat".message_format NOT IN ('ETP', 'GIVE_UP', 'EXCHANGE_FOR_PHYSICAL', 'AVERAGE_PRICE_SYSTEM', 'MUTUAL_OFFSET_SYSTEM', 'TRADE_ENTRY_EDIT'))

UNION ALL

SELECT 'ClearingServicePostTradeProcessingFormat' AS table_name, 'supported_actions' AS column_name, 'required' AS constraint_type, message_format AS record_id, NULL AS invalid_value 
FROM "ClearingServicePostTradeProcessingFormat" 
WHERE "ClearingServicePostTradeProcessingFormat".supported_actions IS NULL

UNION ALL

SELECT 'PostTradeLayoutRow' AS table_name, 'post_layout_kind' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PostTradeLayoutRow" 
WHERE "PostTradeLayoutRow".post_layout_kind IS NULL

UNION ALL

SELECT 'PostTradeLayoutRow' AS table_name, 'post_layout_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, post_layout_kind AS invalid_value 
FROM "PostTradeLayoutRow" 
WHERE "PostTradeLayoutRow".post_layout_kind IS NOT NULL AND ("PostTradeLayoutRow".post_layout_kind NOT IN ('FIELD', 'COMPONENT'))

UNION ALL

SELECT 'PostTradeLayoutRow' AS table_name, 'post_layout_field_tag' AS column_name, 'range' AS constraint_type, id AS record_id, post_layout_field_tag AS invalid_value 
FROM "PostTradeLayoutRow" 
WHERE "PostTradeLayoutRow".post_layout_field_tag < 0

UNION ALL

SELECT 'PostTradeLayoutRow' AS table_name, 'post_layout_element_name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "PostTradeLayoutRow" 
WHERE "PostTradeLayoutRow".post_layout_element_name IS NULL

UNION ALL

SELECT 'InfrastructureBusinessArea' AS table_name, 'area' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InfrastructureBusinessArea" 
WHERE "InfrastructureBusinessArea".area IS NULL

UNION ALL

SELECT 'InfrastructureBusinessArea' AS table_name, 'area' AS column_name, 'enum' AS constraint_type, id AS record_id, area AS invalid_value 
FROM "InfrastructureBusinessArea" 
WHERE "InfrastructureBusinessArea".area IS NOT NULL AND ("InfrastructureBusinessArea".area NOT IN ('INTRODUCTION', 'PRE_TRADE', 'TRADE', 'POST_TRADE', 'INFRASTRUCTURE'))

UNION ALL

SELECT 'InfrastructureBusinessArea' AS table_name, 'infra_common_components' AS column_name, 'enum' AS constraint_type, id AS record_id, infra_common_components AS invalid_value 
FROM "InfrastructureBusinessArea" 
WHERE "InfrastructureBusinessArea".infra_common_components IS NOT NULL AND ("InfrastructureBusinessArea".infra_common_components NOT IN ('ApplIDReportGrp', 'ApplIDRequestAckGrp', 'ApplIDRequestGrp', 'CompIDReqGrp', 'CompIDStatGrp', 'ThrottleMsgTypeGrp', 'ThrottleParamsGrp', 'UsernameGrp'))

UNION ALL

SELECT 'InfrastructureBusinessArea' AS table_name, 'messages' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InfrastructureBusinessArea" 
WHERE "InfrastructureBusinessArea".messages IS NULL

UNION ALL

SELECT 'InfrastructureBusinessArea' AS table_name, 'components' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InfrastructureBusinessArea" 
WHERE "InfrastructureBusinessArea".components IS NULL

UNION ALL

SELECT 'InfrastructureMessageEntry' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "InfrastructureMessageEntry" 
WHERE "InfrastructureMessageEntry".msg_type IS NULL

UNION ALL

SELECT 'InfrastructureMessageEntry' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "InfrastructureMessageEntry" 
WHERE "InfrastructureMessageEntry".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'InfrastructureMessageEntry' AS table_name, 'msg_type' AS column_name, 'identifier' AS constraint_type, msg_type AS record_id, msg_type AS invalid_value 
FROM "InfrastructureMessageEntry" 
WHERE "InfrastructureMessageEntry".msg_type IN (SELECT msg_type 
FROM "InfrastructureMessageEntry" GROUP BY msg_type 
HAVING count(*) > 1)

UNION ALL

SELECT 'InfrastructureMessageEntry' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "InfrastructureMessageEntry" 
WHERE "InfrastructureMessageEntry".message_name IS NULL

UNION ALL

SELECT 'InfrastructureMessageEntry' AS table_name, 'category' AS column_name, 'required' AS constraint_type, msg_type AS record_id, NULL AS invalid_value 
FROM "InfrastructureMessageEntry" 
WHERE "InfrastructureMessageEntry".category IS NULL

UNION ALL

SELECT 'InfrastructureMessageEntry' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, msg_type AS record_id, category AS invalid_value 
FROM "InfrastructureMessageEntry" 
WHERE "InfrastructureMessageEntry".category IS NOT NULL AND ("InfrastructureMessageEntry".category NOT IN ('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING'))

UNION ALL

SELECT 'InfrastructureComponentEntry' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "InfrastructureComponentEntry" 
WHERE "InfrastructureComponentEntry".component_name IS NULL

UNION ALL

SELECT 'InfrastructureComponentEntry' AS table_name, 'component_name' AS column_name, 'identifier' AS constraint_type, component_name AS record_id, component_name AS invalid_value 
FROM "InfrastructureComponentEntry" 
WHERE "InfrastructureComponentEntry".component_name IN (SELECT component_name 
FROM "InfrastructureComponentEntry" GROUP BY component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'InfrastructureComponentEntry' AS table_name, 'repetition' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "InfrastructureComponentEntry" 
WHERE "InfrastructureComponentEntry".repetition IS NULL

UNION ALL

SELECT 'InfrastructureComponentEntry' AS table_name, 'repetition' AS column_name, 'enum' AS constraint_type, component_name AS record_id, repetition AS invalid_value 
FROM "InfrastructureComponentEntry" 
WHERE "InfrastructureComponentEntry".repetition IS NOT NULL AND ("InfrastructureComponentEntry".repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'InfrastructureComponentEntry' AS table_name, 'category' AS column_name, 'required' AS constraint_type, component_name AS record_id, NULL AS invalid_value 
FROM "InfrastructureComponentEntry" 
WHERE "InfrastructureComponentEntry".category IS NULL

UNION ALL

SELECT 'InfrastructureComponentEntry' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, component_name AS record_id, category AS invalid_value 
FROM "InfrastructureComponentEntry" 
WHERE "InfrastructureComponentEntry".category IS NOT NULL AND ("InfrastructureComponentEntry".category NOT IN ('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING'))

UNION ALL

SELECT 'InfrastructureComponentEntry' AS table_name, 'footnote_number' AS column_name, 'range' AS constraint_type, component_name AS record_id, footnote_number AS invalid_value 
FROM "InfrastructureComponentEntry" 
WHERE "InfrastructureComponentEntry".footnote_number < 1 OR "InfrastructureComponentEntry".footnote_number > 25

UNION ALL

SELECT 'InfrastructureComponentTableFootnote' AS table_name, 'footnote_number' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "InfrastructureComponentTableFootnote" 
WHERE "InfrastructureComponentTableFootnote".footnote_number IS NULL

UNION ALL

SELECT 'InfrastructureComponentTableFootnote' AS table_name, 'footnote_number' AS column_name, 'range' AS constraint_type, footnote_number AS record_id, footnote_number AS invalid_value 
FROM "InfrastructureComponentTableFootnote" 
WHERE "InfrastructureComponentTableFootnote".footnote_number < 1 OR "InfrastructureComponentTableFootnote".footnote_number > 25

UNION ALL

SELECT 'InfrastructureComponentTableFootnote' AS table_name, 'footnote_number' AS column_name, 'identifier' AS constraint_type, footnote_number AS record_id, footnote_number AS invalid_value 
FROM "InfrastructureComponentTableFootnote" 
WHERE "InfrastructureComponentTableFootnote".footnote_number IN (SELECT footnote_number 
FROM "InfrastructureComponentTableFootnote" GROUP BY footnote_number 
HAVING count(*) > 1)

UNION ALL

SELECT 'InfrastructureComponentTableFootnote' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "InfrastructureComponentTableFootnote" 
WHERE "InfrastructureComponentTableFootnote".component_name IS NULL

UNION ALL

SELECT 'InfrastructureComponentTableFootnote' AS table_name, 'introduced_in' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "InfrastructureComponentTableFootnote" 
WHERE "InfrastructureComponentTableFootnote".introduced_in IS NULL

UNION ALL

SELECT 'InfrastructureComponentTableFootnote' AS table_name, 'infra_sole_category' AS column_name, 'required' AS constraint_type, footnote_number AS record_id, NULL AS invalid_value 
FROM "InfrastructureComponentTableFootnote" 
WHERE "InfrastructureComponentTableFootnote".infra_sole_category IS NULL

UNION ALL

SELECT 'InfrastructureComponentTableFootnote' AS table_name, 'infra_sole_category' AS column_name, 'enum' AS constraint_type, footnote_number AS record_id, infra_sole_category AS invalid_value 
FROM "InfrastructureComponentTableFootnote" 
WHERE "InfrastructureComponentTableFootnote".infra_sole_category IS NOT NULL AND ("InfrastructureComponentTableFootnote".infra_sole_category NOT IN ('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING'))

UNION ALL

SELECT 'InfrastructureCategorySection' AS table_name, 'category' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InfrastructureCategorySection" 
WHERE "InfrastructureCategorySection".category IS NULL

UNION ALL

SELECT 'InfrastructureCategorySection' AS table_name, 'category' AS column_name, 'enum' AS constraint_type, id AS record_id, category AS invalid_value 
FROM "InfrastructureCategorySection" 
WHERE "InfrastructureCategorySection".category IS NOT NULL AND ("InfrastructureCategorySection".category NOT IN ('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING'))

UNION ALL

SELECT 'InfrastructureCategorySection' AS table_name, 'network_status_scenarios' AS column_name, 'enum' AS constraint_type, id AS record_id, network_status_scenarios AS invalid_value 
FROM "InfrastructureCategorySection" 
WHERE "InfrastructureCategorySection".network_status_scenarios IS NOT NULL AND ("InfrastructureCategorySection".network_status_scenarios NOT IN ('SCENARIO_A', 'SCENARIO_B'))

UNION ALL

SELECT 'InfrastructureCategorySection' AS table_name, 'network_request_types_referenced' AS column_name, 'enum' AS constraint_type, id AS record_id, network_request_types_referenced AS invalid_value 
FROM "InfrastructureCategorySection" 
WHERE "InfrastructureCategorySection".network_request_types_referenced IS NOT NULL AND ("InfrastructureCategorySection".network_request_types_referenced NOT IN ('SNAPSHOT', 'STOP_SUBSCRIBING'))

UNION ALL

SELECT 'InfrastructureCategorySection' AS table_name, 'application_message_report_uses' AS column_name, 'enum' AS constraint_type, id AS record_id, application_message_report_uses AS invalid_value 
FROM "InfrastructureCategorySection" 
WHERE "InfrastructureCategorySection".application_message_report_uses IS NOT NULL AND ("InfrastructureCategorySection".application_message_report_uses NOT IN ('RESET', 'LAST_MESSAGE', 'KEEP_ALIVE', 'RESEND_COMPLETED'))

UNION ALL

SELECT 'InfrastructureMessageDetail' AS table_name, 'msg_type' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InfrastructureMessageDetail" 
WHERE "InfrastructureMessageDetail".msg_type IS NULL

UNION ALL

SELECT 'InfrastructureMessageDetail' AS table_name, 'msg_type' AS column_name, 'pattern' AS constraint_type, id AS record_id, msg_type AS invalid_value 
FROM "InfrastructureMessageDetail" 
WHERE "InfrastructureMessageDetail".msg_type IS NOT NULL AND NOT (REGEXP('^[A-Za-z0-9]{1,3}$', msg_type) = 1)

UNION ALL

SELECT 'InfrastructureMessageDetail' AS table_name, 'message_name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InfrastructureMessageDetail" 
WHERE "InfrastructureMessageDetail".message_name IS NULL

UNION ALL

SELECT 'InfrastructureComponentDetail' AS table_name, 'component_name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InfrastructureComponentDetail" 
WHERE "InfrastructureComponentDetail".component_name IS NULL

UNION ALL

SELECT 'InfrastructureComponentDetail' AS table_name, 'repetition' AS column_name, 'enum' AS constraint_type, id AS record_id, repetition AS invalid_value 
FROM "InfrastructureComponentDetail" 
WHERE "InfrastructureComponentDetail".repetition IS NOT NULL AND ("InfrastructureComponentDetail".repetition NOT IN ('REPEATING', 'NON_REPEATING'))

UNION ALL

SELECT 'InfrastructureLayoutRow' AS table_name, 'infra_layout_kind' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InfrastructureLayoutRow" 
WHERE "InfrastructureLayoutRow".infra_layout_kind IS NULL

UNION ALL

SELECT 'InfrastructureLayoutRow' AS table_name, 'infra_layout_kind' AS column_name, 'enum' AS constraint_type, id AS record_id, infra_layout_kind AS invalid_value 
FROM "InfrastructureLayoutRow" 
WHERE "InfrastructureLayoutRow".infra_layout_kind IS NOT NULL AND ("InfrastructureLayoutRow".infra_layout_kind NOT IN ('FIELD', 'COMPONENT'))

UNION ALL

SELECT 'InfrastructureLayoutRow' AS table_name, 'infra_layout_field_tag' AS column_name, 'range' AS constraint_type, id AS record_id, infra_layout_field_tag AS invalid_value 
FROM "InfrastructureLayoutRow" 
WHERE "InfrastructureLayoutRow".infra_layout_field_tag < 0

UNION ALL

SELECT 'InfrastructureLayoutRow' AS table_name, 'infra_layout_element_name' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "InfrastructureLayoutRow" 
WHERE "InfrastructureLayoutRow".infra_layout_element_name IS NULL

UNION ALL

SELECT 'StandardResponseMapping' AS table_name, 'category_label' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "StandardResponseMapping" 
WHERE "StandardResponseMapping".category_label IS NULL

UNION ALL

SELECT 'StandardResponseMapping' AS table_name, 'fix_message' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "StandardResponseMapping" 
WHERE "StandardResponseMapping".fix_message IS NULL

UNION ALL

SELECT 'StandardResponseMapping' AS table_name, 'appropriate_responses' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "StandardResponseMapping" 
WHERE "StandardResponseMapping".appropriate_responses IS NULL

UNION ALL

SELECT 'ApplicationMessageReferenceKey' AS table_name, 'category_label' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ApplicationMessageReferenceKey" 
WHERE "ApplicationMessageReferenceKey".category_label IS NULL

UNION ALL

SELECT 'ApplicationMessageReferenceKey' AS table_name, 'fix_message' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ApplicationMessageReferenceKey" 
WHERE "ApplicationMessageReferenceKey".fix_message IS NULL

UNION ALL

SELECT 'ApplicationMessageReferenceKey' AS table_name, 'business_reject_ref_id_value' AS column_name, 'required' AS constraint_type, id AS record_id, NULL AS invalid_value 
FROM "ApplicationMessageReferenceKey" 
WHERE "ApplicationMessageReferenceKey".business_reject_ref_id_value IS NULL

UNION ALL

SELECT 'BusinessRejectReasonDescription' AS table_name, 'reject_reason_code' AS column_name, 'required' AS constraint_type, reject_reason_code AS record_id, NULL AS invalid_value 
FROM "BusinessRejectReasonDescription" 
WHERE "BusinessRejectReasonDescription".reject_reason_code IS NULL

UNION ALL

SELECT 'BusinessRejectReasonDescription' AS table_name, 'reject_reason_code' AS column_name, 'range' AS constraint_type, reject_reason_code AS record_id, reject_reason_code AS invalid_value 
FROM "BusinessRejectReasonDescription" 
WHERE "BusinessRejectReasonDescription".reject_reason_code < 0 OR "BusinessRejectReasonDescription".reject_reason_code > 999

UNION ALL

SELECT 'BusinessRejectReasonDescription' AS table_name, 'reject_reason_code' AS column_name, 'identifier' AS constraint_type, reject_reason_code AS record_id, reject_reason_code AS invalid_value 
FROM "BusinessRejectReasonDescription" 
WHERE "BusinessRejectReasonDescription".reject_reason_code IN (SELECT reject_reason_code 
FROM "BusinessRejectReasonDescription" GROUP BY reject_reason_code 
HAVING count(*) > 1)

UNION ALL

SELECT 'BusinessRejectReasonDescription' AS table_name, 'reject_reason_label' AS column_name, 'required' AS constraint_type, reject_reason_code AS record_id, NULL AS invalid_value 
FROM "BusinessRejectReasonDescription" 
WHERE "BusinessRejectReasonDescription".reject_reason_label IS NULL

UNION ALL

SELECT 'InfrastructureGlobalComponentReference' AS table_name, 'infra_global_component_name' AS column_name, 'required' AS constraint_type, infra_global_component_name AS record_id, NULL AS invalid_value 
FROM "InfrastructureGlobalComponentReference" 
WHERE "InfrastructureGlobalComponentReference".infra_global_component_name IS NULL

UNION ALL

SELECT 'InfrastructureGlobalComponentReference' AS table_name, 'infra_global_component_name' AS column_name, 'identifier' AS constraint_type, infra_global_component_name AS record_id, infra_global_component_name AS invalid_value 
FROM "InfrastructureGlobalComponentReference" 
WHERE "InfrastructureGlobalComponentReference".infra_global_component_name IN (SELECT infra_global_component_name 
FROM "InfrastructureGlobalComponentReference" GROUP BY infra_global_component_name 
HAVING count(*) > 1)

UNION ALL

SELECT 'InfrastructureGlobalComponentReference' AS table_name, 'infra_global_component_name' AS column_name, 'enum' AS constraint_type, infra_global_component_name AS record_id, infra_global_component_name AS invalid_value 
FROM "InfrastructureGlobalComponentReference" 
WHERE "InfrastructureGlobalComponentReference".infra_global_component_name IS NOT NULL AND ("InfrastructureGlobalComponentReference".infra_global_component_name NOT IN ('ApplicationSequenceControl'))

UNION ALL

SELECT 'InfrastructureGlobalComponentReference' AS table_name, 'infra_global_component_field_tags' AS column_name, 'range' AS constraint_type, infra_global_component_name AS record_id, infra_global_component_field_tags AS invalid_value 
FROM "InfrastructureGlobalComponentReference" 
WHERE "InfrastructureGlobalComponentReference".infra_global_component_field_tags < 0

UNION ALL

SELECT 'InfrastructureGlobalComponentReference' AS table_name, 'infra_global_component_used_in' AS column_name, 'required' AS constraint_type, infra_global_component_name AS record_id, NULL AS invalid_value 
FROM "InfrastructureGlobalComponentReference" 
WHERE "InfrastructureGlobalComponentReference".infra_global_component_used_in IS NULL

UNION ALL

SELECT 'InfrastructureGlobalComponentReference' AS table_name, 'infra_global_component_used_in' AS column_name, 'enum' AS constraint_type, infra_global_component_name AS record_id, infra_global_component_used_in AS invalid_value 
FROM "InfrastructureGlobalComponentReference" 
WHERE "InfrastructureGlobalComponentReference".infra_global_component_used_in IS NOT NULL AND ("InfrastructureGlobalComponentReference".infra_global_component_used_in NOT IN ('BUSINESS_MESSAGE_REJECTS', 'NETWORK_STATUS_COMMUNICATION', 'USER_MANAGEMENT', 'APPLICATION_SEQUENCING'));

