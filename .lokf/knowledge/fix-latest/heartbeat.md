---
type: FixMessage
id: https://w3id.org/lmodel/fix-protocol/knowledge/fix-latest/heartbeat
genre: reference
title: Heartbeat
description: The Heartbeat message, MsgType 0, record `fix_message:1`, with its three members, written as a concept of type `FixMessage`.
resource: src/fix_protocol/data/messages.yaml
derivedFrom:
  - https://w3id.org/lmodel/fix-protocol/knowledge/datasets/catalogue
abbr_name: Heartbeat
msg_type: "0"
in_category: fix_category:Session
added_in: FIX.2.7
fixml_not_required: true
fix_members:
  - member_component: fix_component:1024
    presence: required
    added_in: FIX.2.7
  - member_field: fix_field:112
    added_in: FIX.4.0
  - member_component: fix_component:1025
    presence: required
    added_in: FIX.2.7
sources:
  - id: src-fix_protocol-data-messages.yaml
    resource: src/fix_protocol/data/messages.yaml
    title: the record fix_message:1
  - id: readme.md
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-11-05T19:39:39Z"
status: draft
---

# Heartbeat

Heartbeat is the message of MsgType 0, in the Session category. Its members are the standard header, field 112 and the standard trailer.[^src-fix_protocol-data-messages.yaml]

The keys beside LOKF's are the catalogue's own for `fix_message:1`. `lokf validate` checks them against `.lokf/fix-protocol.yaml`.[^readme.md]

[^src-fix_protocol-data-messages.yaml]: src/fix_protocol/data/messages.yaml, the record fix_message:1
[^readme.md]: README.md, Knowledge Trust Ladder (KTL)
