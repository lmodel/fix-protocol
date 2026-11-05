# Fix-latest

* [PreTrade](pre-trade.md) - The PreTrade section of FIX Latest, record `fix_section:PreTrade`, written as a concept of type `FixSection`. FIX lists it second of its five sections.
* [SingleGeneralOrderHandling](single-general-order-handling.md) - The category of single orders, record `fix_category:SingleGeneralOrderHandling`, in the Trade section, written as a concept of type `FixCategory`.
* [Price](price.md) - The Price datatype, record `fix_datatype:Price`, which narrows float and maps to xs:decimal, written as a concept of type `FixDatatype`.
* [SideCodeSet](side-code-set.md) - The code set of field 54, Side, record `fix_code_set:54`, whose values are single characters, written as a concept of type `FixCodeSet` without its codes.
* [Buy](buy.md) - The code 1, Buy, of the Side code set, record `fix_code:54001`, written as a concept of type `FixCode`.
* [Symbol](symbol.md) - Field 55, Symbol, record `fix_field:55`, a String with the FIXML short name Sym, written as a concept of type `FixField`.
* [Instrument](instrument.md) - The Instrument component, record `fix_component:1003`, in the Common category, written as a concept of type `FixComponent` without its members.
* [Parties](parties.md) - The Parties repeating group, record `fix_group:1012`, counted by field 453 and holding five members, written as a concept of type `FixGroup`.
* [Heartbeat](heartbeat.md) - The Heartbeat message, MsgType 0, record `fix_message:1`, with its three members, written as a concept of type `FixMessage`.
