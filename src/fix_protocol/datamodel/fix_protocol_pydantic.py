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


metamodel_version = "1.12.0"
version = "FIX.Latest_EP312"


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


linkml_meta = LinkMLMeta({'annotations': {'upstream_commit': {'tag': 'upstream_commit',
                                         'value': 'cd24169a2abd8daba7c360987c7a46ca11873a12'},
                     'upstream_created': {'tag': 'upstream_created',
                                          'value': '2026-09-08'},
                     'upstream_license': {'tag': 'upstream_license',
                                          'value': 'Apache-2.0'},
                     'upstream_repository': {'tag': 'upstream_repository',
                                             'value': 'https://github.com/FIXTradingCommunity/orchestrations'}},
     'comments': ['The version is the extension pack the catalogue renders. '
                  "upstream/ holds FIX Latest's Orchestra file unchanged, "
                  'scripts/fix_latest_to_records.py writes the catalogue from it, '
                  'and scripts/check_upstream_release.py reports when FIX '
                  'publishes another.'],
     'default_prefix': 'fix_protocol',
     'default_range': 'string',
     'description': 'A LinkML model of FIX Latest, the application layer of the '
                    'Financial Information eXchange (FIX) protocol that the FIX '
                    'Trading Community maintains. It holds every section, '
                    'category, datatype, code set, field, component, repeating '
                    'group and message of FIX Latest as a record, with the version '
                    'and extension pack that added and last changed each one. The '
                    "records keep FIX's names, numbers and codes and none of its "
                    'descriptive text.',
     'id': 'https://w3id.org/lmodel/fix-protocol',
     'imports': ['linkml:types',
                 './fix_protocol_core',
                 './fix_protocol_dictionary',
                 './fix_protocol_structure'],
     'keywords': ['FIX',
                  'FIX Latest',
                  'financial messaging',
                  'trading',
                  'Orchestra'],
     'license': 'Apache-2.0',
     'name': 'fix_protocol',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'fix_category': {'prefix_prefix': 'fix_category',
                                   'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/category/'},
                  'fix_code': {'prefix_prefix': 'fix_code',
                               'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/code/'},
                  'fix_code_set': {'prefix_prefix': 'fix_code_set',
                                   'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/code_set/'},
                  'fix_component': {'prefix_prefix': 'fix_component',
                                    'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/component/'},
                  'fix_datatype': {'prefix_prefix': 'fix_datatype',
                                   'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/datatype/'},
                  'fix_field': {'prefix_prefix': 'fix_field',
                                'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/field/'},
                  'fix_group': {'prefix_prefix': 'fix_group',
                                'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/group/'},
                  'fix_message': {'prefix_prefix': 'fix_message',
                                  'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/message/'},
                  'fix_orchestra': {'prefix_prefix': 'fix_orchestra',
                                    'prefix_reference': 'https://w3id.org/lmodel/fix-orchestra/'},
                  'fix_protocol': {'prefix_prefix': 'fix_protocol',
                                   'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/'},
                  'fix_section': {'prefix_prefix': 'fix_section',
                                  'prefix_reference': 'https://w3id.org/lmodel/fix-protocol/section/'},
                  'fixr': {'prefix_prefix': 'fixr',
                           'prefix_reference': 'http://fixprotocol.io/2020/orchestra/repository/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/fix-protocol',
                  'https://github.com/FIXTradingCommunity/orchestrations'],
     'source': 'https://github.com/FIXTradingCommunity/orchestrations/blob/cd24169a2abd8daba7c360987c7a46ca11873a12/FIX%20Standard/OrchestraFIXLatest.xml',
     'source_file': 'src/fix_protocol/schema/fix_protocol.yaml',
     'title': 'FIX Latest'} )

class FixPresence(str, Enum):
    """
    Whether a message, component or group must carry a member, in the terms Orchestra 1.0 defines.
    """
    Optional = "optional"
    """
    The member may be left out.
    """
    Required = "required"
    """
    The member must be there.
    """
    Forbidden = "forbidden"
    """
    The member must be left out.
    """
    Ignored = "ignored"
    """
    A receiver disregards the member if it is there.
    """
    Constant = "constant"
    """
    The member always takes one fixed value.
    """


class FixCategoryKind(str, Enum):
    """
    Whether a category groups messages or fields.
    """
    Messages = "Message"
    """
    The category groups messages and their components.
    """
    Fields = "Field"
    """
    The category groups fields.
    """


class FixIncludeFile(str, Enum):
    """
    Which shared FIXML schema file a category's own FIXML schema file brings in.
    """
    Components = "components"
    """
    The file that defines the shared components.
    """
    Fields = "fields"
    """
    The file that defines the fields.
    """



class FixPedigreeMixin(ConfiguredBaseModel):
    """
    When FIX added, last changed and deprecated an element, by version and extension pack.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_core',
         'mixin': True,
         'title': 'Pedigree'})

    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })


class FixElement(FixPedigreeMixin):
    """
    An element of FIX Latest with an identifier and a name of its own.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_core',
         'mixins': ['FixPedigreeMixin'],
         'title': 'FIX Element'})

    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })


class FixSection(FixElement):
    """
    One of the five parts FIX divides its messages into by business area, such as PreTrade.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fix_orchestra:OrchestraSectionV10', 'fixr:sectionType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_core',
         'slot_usage': {'id': {'name': 'id',
                               'pattern': '^fix_section:[A-Za-z][A-Za-z0-9_]*$'}},
         'title': 'Section'})

    fixml_file_name: Optional[str] = Field(default=None, title="FIXML File Name", description="""The FIXML schema file that holds the section's or category's elements, by its file name.""", json_schema_extra = { "linkml_meta": {'aliases': ['FIXMLFileName'],
         'domain_of': ['FixSection', 'FixCategory'],
         'exact_mappings': ['fixr:FIXMLFileName'],
         'slot_uri': 'fix_protocol:fixml_file_name'} })
    fixml_not_required: Optional[bool] = Field(default=None, title="Not Required in FIXML", description="""True when the element is left out of FIXML, FIX's XML encoding.""", json_schema_extra = { "linkml_meta": {'aliases': ['notReqXML'],
         'comments': ['FIX Latest writes it in a FIXML annotation, the only kind of '
                      'application information the file carries.'],
         'domain_of': ['FixSection',
                       'FixCategory',
                       'FixField',
                       'FixComponent',
                       'FixMessage'],
         'slot_uri': 'fix_protocol:fixml_not_required'} })
    section_order: Optional[int] = Field(default=None, title="Display Order", description="""Where the section comes in FIX's own order of sections, counting from 0.""", ge=0, json_schema_extra = { "linkml_meta": {'aliases': ['displayOrder'],
         'domain_of': ['FixSection'],
         'exact_mappings': ['fixr:displayOrder']} })
    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^fix_section:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FixCategory(FixElement):
    """
    A group of messages within a section. Three categories belong to no section, and hold the shared components and the fields instead.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fix_orchestra:OrchestraCategoryV10', 'fixr:categoryType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_core',
         'slot_usage': {'id': {'name': 'id',
                               'pattern': '^fix_category:[A-Za-z][A-Za-z0-9_]*$'}},
         'title': 'Category'})

    fixml_file_name: Optional[str] = Field(default=None, title="FIXML File Name", description="""The FIXML schema file that holds the section's or category's elements, by its file name.""", json_schema_extra = { "linkml_meta": {'aliases': ['FIXMLFileName'],
         'domain_of': ['FixSection', 'FixCategory'],
         'exact_mappings': ['fixr:FIXMLFileName'],
         'slot_uri': 'fix_protocol:fixml_file_name'} })
    in_section: Optional[str] = Field(default=None, title="Section", description="""The section a category belongs to.""", json_schema_extra = { "linkml_meta": {'aliases': ['section'],
         'domain_of': ['FixCategory'],
         'exact_mappings': ['fixr:section'],
         'slot_uri': 'fix_protocol:in_section'} })
    fixml_not_required: Optional[bool] = Field(default=None, title="Not Required in FIXML", description="""True when the element is left out of FIXML, FIX's XML encoding.""", json_schema_extra = { "linkml_meta": {'aliases': ['notReqXML'],
         'comments': ['FIX Latest writes it in a FIXML annotation, the only kind of '
                      'application information the file carries.'],
         'domain_of': ['FixSection',
                       'FixCategory',
                       'FixField',
                       'FixComponent',
                       'FixMessage'],
         'slot_uri': 'fix_protocol:fixml_not_required'} })
    category_kind: Optional[FixCategoryKind] = Field(default=None, title="Category Kind", description="""Whether the category groups messages or fields.""", json_schema_extra = { "linkml_meta": {'aliases': ['componentType'],
         'domain_of': ['FixCategory'],
         'exact_mappings': ['fixr:componentType']} })
    include_file: Optional[FixIncludeFile] = Field(default=None, title="Included FIXML File", description="""The shared FIXML schema file that the category's own FIXML schema file brings in.""", json_schema_extra = { "linkml_meta": {'aliases': ['includeFile'],
         'domain_of': ['FixCategory'],
         'exact_mappings': ['fixr:includeFile']} })
    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('in_section')
    def pattern_in_section(cls, v):
        pattern=re.compile(r"^fix_section:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid in_section format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid in_section format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^fix_category:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FixDatatype(FixElement):
    """
    A kind of value a field holds, such as int, Price or UTCTimestamp, with the XML Schema types it maps to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fix_orchestra:OrchestraDatatypeV10', 'fixr:datatype'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_dictionary',
         'slot_usage': {'id': {'name': 'id',
                               'pattern': '^fix_datatype:[A-Za-z][A-Za-z0-9_]*$'}},
         'title': 'Datatype'})

    base_type: Optional[str] = Field(default=None, title="Base Type", description="""The datatype this one narrows.""", json_schema_extra = { "linkml_meta": {'aliases': ['baseType'],
         'domain_of': ['FixDatatype'],
         'exact_mappings': ['fixr:baseType']} })
    mapped_datatypes: Optional[list[FixMappedDatatype]] = Field(default=None, title="Mapped Datatypes", description="""The types of other standards that FIX gives as this datatype's form.""", json_schema_extra = { "linkml_meta": {'aliases': ['mappedDatatype'],
         'domain_of': ['FixDatatype'],
         'exact_mappings': ['fixr:mappedDatatype']} })
    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('base_type')
    def pattern_base_type(cls, v):
        pattern=re.compile(r"^fix_datatype:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid base_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid base_type format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^fix_datatype:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FixMappedDatatype(ConfiguredBaseModel):
    """
    The type of another standard that a FIX datatype takes, such as xs:decimal in XML Schema.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fixr:mappedDatatype'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_dictionary',
         'title': 'Mapped Datatype'})

    mapped_standard: str = Field(default=..., title="Standard", description="""The standard the type belongs to, such as XML.""", json_schema_extra = { "linkml_meta": {'aliases': ['standard'],
         'domain_of': ['FixMappedDatatype'],
         'exact_mappings': ['fixr:standard']} })
    mapped_base: Optional[str] = Field(default=None, title="Base", description="""The standard's type, such as xs:decimal.""", json_schema_extra = { "linkml_meta": {'aliases': ['base'],
         'domain_of': ['FixMappedDatatype'],
         'exact_mappings': ['fixr:base']} })
    mapped_builtin: Optional[bool] = Field(default=None, title="Built In", description="""True when the type is one the standard defines itself.""", json_schema_extra = { "linkml_meta": {'aliases': ['builtin'],
         'domain_of': ['FixMappedDatatype'],
         'exact_mappings': ['fixr:builtin']} })
    mapped_min_inclusive: Optional[str] = Field(default=None, title="Least Value", description="""The smallest value the type allows, as FIX writes it.""", json_schema_extra = { "linkml_meta": {'aliases': ['minInclusive'],
         'domain_of': ['FixMappedDatatype'],
         'exact_mappings': ['fixr:minInclusive']} })
    mapped_pattern: Optional[str] = Field(default=None, title="Pattern", description="""A regular expression in XML Schema's syntax that a value must match.""", json_schema_extra = { "linkml_meta": {'aliases': ['pattern'],
         'domain_of': ['FixMappedDatatype'],
         'exact_mappings': ['fixr:pattern']} })


class FixCodeSet(FixElement):
    """
    A list of the values a field may take, each a code with a name, such as the sides of an order.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fix_orchestra:OrchestraCodeSetV10', 'fixr:codeSetType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_dictionary',
         'slot_usage': {'id': {'name': 'id', 'pattern': '^fix_code_set:[1-9][0-9]*$'}},
         'title': 'Code Set'})

    code_set_datatype: str = Field(default=..., title="Datatype", description="""The datatype of the codes' values.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['FixCodeSet'],
         'exact_mappings': ['fixr:type']} })
    fix_codes: Optional[list[FixCode]] = Field(default=None, title="Codes", description="""The codes of the set, in FIX's order.""", json_schema_extra = { "linkml_meta": {'aliases': ['code'],
         'domain_of': ['FixCodeSet'],
         'exact_mappings': ['fixr:code']} })
    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('code_set_datatype')
    def pattern_code_set_datatype(cls, v):
        pattern=re.compile(r"^fix_datatype:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid code_set_datatype format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid code_set_datatype format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^fix_code_set:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FixCode(FixElement):
    """
    One value of a code set, with its name, such as 1 for Buy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fix_orchestra:OrchestraCodeV10', 'fixr:codeType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_dictionary',
         'slot_usage': {'id': {'name': 'id', 'pattern': '^fix_code:[1-9][0-9]*$'}},
         'title': 'Code'})

    code_value: str = Field(default=..., title="Value", description="""The value as it travels on the wire.""", json_schema_extra = { "linkml_meta": {'aliases': ['value'],
         'domain_of': ['FixCode'],
         'exact_mappings': ['fixr:value']} })
    sort_order: Optional[int] = Field(default=None, title="Sort Order", description="""Where the code comes when FIX lists the set.""", ge=0, json_schema_extra = { "linkml_meta": {'aliases': ['sort'], 'domain_of': ['FixCode'], 'exact_mappings': ['fixr:sort']} })
    code_group: Optional[str] = Field(default=None, title="Code Group", description="""A label that groups some codes of a large set, such as one asset class.""", json_schema_extra = { "linkml_meta": {'aliases': ['group'],
         'domain_of': ['FixCode'],
         'exact_mappings': ['fixr:group']} })
    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('code_value')
    def pattern_code_value(cls, v):
        pattern=re.compile(r"^\S+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid code_value format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid code_value format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^fix_code:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FixField(FixElement):
    """
    A field of FIX, known by its tag number, such as 55 for Symbol, with the datatype or code set of its values.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["FIX Latest names a field's datatype or code set in one "
                      'attribute, type. The record splits it, so each reference has '
                      'one range, as Orchestra 1.1 does.'],
         'exact_mappings': ['fix_orchestra:OrchestraFieldV10', 'fixr:fieldType'],
         'exactly_one_of': [{'slot_conditions': {'field_code_set': {'name': 'field_code_set',
                                                                    'value_presence': 'ABSENT'},
                                                 'field_datatype': {'name': 'field_datatype',
                                                                    'required': True}}},
                            {'slot_conditions': {'field_code_set': {'name': 'field_code_set',
                                                                    'required': True},
                                                 'field_datatype': {'name': 'field_datatype',
                                                                    'value_presence': 'ABSENT'}}}],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_dictionary',
         'slot_usage': {'id': {'name': 'id', 'pattern': '^fix_field:[1-9][0-9]*$'}},
         'title': 'Field'})

    abbr_name: Optional[str] = Field(default=None, title="Abbreviated Name", description="""The shorter name FIXML uses for the element's tag.""", json_schema_extra = { "linkml_meta": {'aliases': ['abbrName'],
         'domain_of': ['FixField', 'FixComponent', 'FixGroup', 'FixMessage'],
         'exact_mappings': ['fixr:abbrName'],
         'slot_uri': 'fix_protocol:abbr_name'} })
    fixml_not_required: Optional[bool] = Field(default=None, title="Not Required in FIXML", description="""True when the element is left out of FIXML, FIX's XML encoding.""", json_schema_extra = { "linkml_meta": {'aliases': ['notReqXML'],
         'comments': ['FIX Latest writes it in a FIXML annotation, the only kind of '
                      'application information the file carries.'],
         'domain_of': ['FixSection',
                       'FixCategory',
                       'FixField',
                       'FixComponent',
                       'FixMessage'],
         'slot_uri': 'fix_protocol:fixml_not_required'} })
    field_datatype: Optional[str] = Field(default=None, title="Datatype", description="""The datatype of the field's values, when no code set lists them.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['FixField'],
         'exact_mappings': ['fixr:type']} })
    field_code_set: Optional[str] = Field(default=None, title="Code Set", description="""The code set that lists the field's values.""", json_schema_extra = { "linkml_meta": {'aliases': ['type'],
         'domain_of': ['FixField'],
         'exact_mappings': ['fixr:type']} })
    union_datatype: Optional[str] = Field(default=None, title="Union Datatype", description="""A datatype whose values the field also takes, beside those of its code set, such as a range of numbers kept for private use.""", json_schema_extra = { "linkml_meta": {'aliases': ['unionDataType'],
         'domain_of': ['FixField'],
         'exact_mappings': ['fixr:unionDataType']} })
    length_field: Optional[str] = Field(default=None, title="Length Field", description="""The field that gives this field's length in bytes.""", json_schema_extra = { "linkml_meta": {'aliases': ['lengthId'],
         'domain_of': ['FixField'],
         'exact_mappings': ['fixr:lengthId']} })
    discriminator_field: Optional[str] = Field(default=None, title="Discriminator Field", description="""The field whose value says how to read this field's value.""", json_schema_extra = { "linkml_meta": {'aliases': ['discriminatorId'],
         'domain_of': ['FixField'],
         'exact_mappings': ['fixr:discriminatorId']} })
    base_category: Optional[str] = Field(default=None, title="Base Category", description="""The category whose FIXML element carries the field, under the short name in base_category_abbr_name.""", json_schema_extra = { "linkml_meta": {'aliases': ['baseCategory'],
         'domain_of': ['FixField'],
         'exact_mappings': ['fixr:baseCategory']} })
    base_category_abbr_name: Optional[str] = Field(default=None, title="Base Category Abbreviated Name", description="""The field's short name within its base category's FIXML element.""", json_schema_extra = { "linkml_meta": {'aliases': ['baseCategoryAbbrName'],
         'domain_of': ['FixField'],
         'exact_mappings': ['fixr:baseCategoryAbbrName']} })
    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('field_datatype')
    def pattern_field_datatype(cls, v):
        pattern=re.compile(r"^fix_datatype:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid field_datatype format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid field_datatype format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('field_code_set')
    def pattern_field_code_set(cls, v):
        pattern=re.compile(r"^fix_code_set:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid field_code_set format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid field_code_set format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('union_datatype')
    def pattern_union_datatype(cls, v):
        pattern=re.compile(r"^fix_datatype:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid union_datatype format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid union_datatype format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('length_field')
    def pattern_length_field(cls, v):
        pattern=re.compile(r"^fix_field:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid length_field format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid length_field format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('discriminator_field')
    def pattern_discriminator_field(cls, v):
        pattern=re.compile(r"^fix_field:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid discriminator_field format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid discriminator_field format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('base_category')
    def pattern_base_category(cls, v):
        pattern=re.compile(r"^fix_category:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid base_category format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid base_category format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^fix_field:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FixMember(FixPedigreeMixin):
    """
    One field, component or group in a message, component or group, and whether it must be there.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['fixr:fieldRefType',
                            'fixr:componentRefType',
                            'fixr:groupRefType'],
         'comments': ['Orchestra gives the three kinds of member three elements of one '
                      'shape. The record gives each a key, and one member holds '
                      'exactly one of them.'],
         'exactly_one_of': [{'slot_conditions': {'member_component': {'name': 'member_component',
                                                                      'value_presence': 'ABSENT'},
                                                 'member_field': {'name': 'member_field',
                                                                  'required': True},
                                                 'member_group': {'name': 'member_group',
                                                                  'value_presence': 'ABSENT'}}},
                            {'slot_conditions': {'member_component': {'name': 'member_component',
                                                                      'required': True},
                                                 'member_field': {'name': 'member_field',
                                                                  'value_presence': 'ABSENT'},
                                                 'member_group': {'name': 'member_group',
                                                                  'value_presence': 'ABSENT'}}},
                            {'slot_conditions': {'member_component': {'name': 'member_component',
                                                                      'value_presence': 'ABSENT'},
                                                 'member_field': {'name': 'member_field',
                                                                  'value_presence': 'ABSENT'},
                                                 'member_group': {'name': 'member_group',
                                                                  'required': True}}}],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_structure',
         'mixins': ['FixPedigreeMixin'],
         'title': 'Member'})

    member_field: Optional[str] = Field(default=None, title="Field", description="""The field this member is.""", json_schema_extra = { "linkml_meta": {'aliases': ['fieldRef'],
         'domain_of': ['FixMember'],
         'exact_mappings': ['fixr:fieldRef']} })
    member_component: Optional[str] = Field(default=None, title="Component", description="""The component this member is.""", json_schema_extra = { "linkml_meta": {'aliases': ['componentRef'],
         'domain_of': ['FixMember'],
         'exact_mappings': ['fixr:componentRef']} })
    member_group: Optional[str] = Field(default=None, title="Group", description="""The repeating group this member is.""", json_schema_extra = { "linkml_meta": {'aliases': ['groupRef'],
         'domain_of': ['FixMember'],
         'exact_mappings': ['fixr:groupRef']} })
    presence: Optional[FixPresence] = Field(default=None, title="Presence", description="""Whether the member must be there. A member that states none is optional.""", json_schema_extra = { "linkml_meta": {'aliases': ['presence'],
         'domain_of': ['FixMember'],
         'exact_mappings': ['fixr:presence']} })
    fixml_inlined: Optional[bool] = Field(default=None, title="Inlined in FIXML", description="""True when FIXML writes the component's fields directly in the enclosing element rather than in an element of its own.""", json_schema_extra = { "linkml_meta": {'aliases': ['inlined'], 'domain_of': ['FixMember']} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('member_field')
    def pattern_member_field(cls, v):
        pattern=re.compile(r"^fix_field:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid member_field format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid member_field format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('member_component')
    def pattern_member_component(cls, v):
        pattern=re.compile(r"^fix_component:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid member_component format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid member_component format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('member_group')
    def pattern_member_group(cls, v):
        pattern=re.compile(r"^fix_group:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid member_group format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid member_group format: {v}"
            raise ValueError(err_msg)
        return v


class FixComponent(FixElement):
    """
    A named block of fields, components and groups that messages share, such as Instrument.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fix_orchestra:OrchestraComponentV10',
                            'fixr:componentType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_structure',
         'slot_usage': {'id': {'name': 'id', 'pattern': '^fix_component:[1-9][0-9]*$'}},
         'title': 'Component'})

    abbr_name: Optional[str] = Field(default=None, title="Abbreviated Name", description="""The shorter name FIXML uses for the element's tag.""", json_schema_extra = { "linkml_meta": {'aliases': ['abbrName'],
         'domain_of': ['FixField', 'FixComponent', 'FixGroup', 'FixMessage'],
         'exact_mappings': ['fixr:abbrName'],
         'slot_uri': 'fix_protocol:abbr_name'} })
    in_category: str = Field(default=..., title="Category", description="""The category a message, component or group belongs to.""", json_schema_extra = { "linkml_meta": {'aliases': ['category'],
         'domain_of': ['FixComponent', 'FixGroup', 'FixMessage'],
         'exact_mappings': ['fixr:category'],
         'slot_uri': 'fix_protocol:in_category'} })
    fix_members: Optional[list[FixMember]] = Field(default=None, title="Members", description="""The fields, components and groups the element holds, in the order FIX lists them.""", json_schema_extra = { "linkml_meta": {'comments': ['A message lists its members in a structure element and a '
                      'component or a group lists them directly. The record lists them '
                      'here in each case.'],
         'domain_of': ['FixComponent', 'FixGroup', 'FixMessage'],
         'slot_uri': 'fix_protocol:fix_members'} })
    fixml_not_required: Optional[bool] = Field(default=None, title="Not Required in FIXML", description="""True when the element is left out of FIXML, FIX's XML encoding.""", json_schema_extra = { "linkml_meta": {'aliases': ['notReqXML'],
         'comments': ['FIX Latest writes it in a FIXML annotation, the only kind of '
                      'application information the file carries.'],
         'domain_of': ['FixSection',
                       'FixCategory',
                       'FixField',
                       'FixComponent',
                       'FixMessage'],
         'slot_uri': 'fix_protocol:fixml_not_required'} })
    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('in_category')
    def pattern_in_category(cls, v):
        pattern=re.compile(r"^fix_category:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid in_category format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid in_category format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^fix_component:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FixGroup(FixElement):
    """
    A block of members that repeats in a message, with the field that counts the repeats.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fix_orchestra:OrchestraGroupV10', 'fixr:groupType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_structure',
         'slot_usage': {'fix_members': {'name': 'fix_members', 'required': True},
                        'id': {'name': 'id', 'pattern': '^fix_group:[1-9][0-9]*$'}},
         'title': 'Repeating Group'})

    abbr_name: Optional[str] = Field(default=None, title="Abbreviated Name", description="""The shorter name FIXML uses for the element's tag.""", json_schema_extra = { "linkml_meta": {'aliases': ['abbrName'],
         'domain_of': ['FixField', 'FixComponent', 'FixGroup', 'FixMessage'],
         'exact_mappings': ['fixr:abbrName'],
         'slot_uri': 'fix_protocol:abbr_name'} })
    in_category: str = Field(default=..., title="Category", description="""The category a message, component or group belongs to.""", json_schema_extra = { "linkml_meta": {'aliases': ['category'],
         'domain_of': ['FixComponent', 'FixGroup', 'FixMessage'],
         'exact_mappings': ['fixr:category'],
         'slot_uri': 'fix_protocol:in_category'} })
    fix_members: list[FixMember] = Field(default=..., title="Members", description="""The fields, components and groups the element holds, in the order FIX lists them.""", json_schema_extra = { "linkml_meta": {'comments': ['A message lists its members in a structure element and a '
                      'component or a group lists them directly. The record lists them '
                      'here in each case.'],
         'domain_of': ['FixComponent', 'FixGroup', 'FixMessage'],
         'slot_uri': 'fix_protocol:fix_members'} })
    num_in_group: FixNumInGroup = Field(default=..., title="Count Field", description="""The field that states how many times the group repeats.""", json_schema_extra = { "linkml_meta": {'aliases': ['numInGroup'],
         'domain_of': ['FixGroup'],
         'exact_mappings': ['fixr:numInGroup']} })
    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('in_category')
    def pattern_in_category(cls, v):
        pattern=re.compile(r"^fix_category:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid in_category format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid in_category format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^fix_group:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FixNumInGroup(FixPedigreeMixin):
    """
    The field that counts a group's repeats, as the group names it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['fixr:fieldRefType'],
         'comments': ['Orchestra 1.0 gives the count the shape of a field reference.'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_structure',
         'mixins': ['FixPedigreeMixin'],
         'title': 'Count Field Reference'})

    count_field: str = Field(default=..., title="Field", description="""The field that holds the count.""", json_schema_extra = { "linkml_meta": {'aliases': ['id'],
         'domain_of': ['FixNumInGroup'],
         'exact_mappings': ['fixr:id']} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('count_field')
    def pattern_count_field(cls, v):
        pattern=re.compile(r"^fix_field:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid count_field format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid count_field format: {v}"
            raise ValueError(err_msg)
        return v


class FixMessage(FixElement):
    """
    A FIX message, known by its MsgType, such as D for NewOrderSingle, with its members in order.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fix_orchestra:OrchestraMessageV10', 'fixr:messageType'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol/schema/fix_protocol_structure',
         'slot_usage': {'fix_members': {'name': 'fix_members', 'required': True},
                        'id': {'name': 'id', 'pattern': '^fix_message:[1-9][0-9]*$'}},
         'title': 'Message'})

    abbr_name: Optional[str] = Field(default=None, title="Abbreviated Name", description="""The shorter name FIXML uses for the element's tag.""", json_schema_extra = { "linkml_meta": {'aliases': ['abbrName'],
         'domain_of': ['FixField', 'FixComponent', 'FixGroup', 'FixMessage'],
         'exact_mappings': ['fixr:abbrName'],
         'slot_uri': 'fix_protocol:abbr_name'} })
    in_category: str = Field(default=..., title="Category", description="""The category a message, component or group belongs to.""", json_schema_extra = { "linkml_meta": {'aliases': ['category'],
         'domain_of': ['FixComponent', 'FixGroup', 'FixMessage'],
         'exact_mappings': ['fixr:category'],
         'slot_uri': 'fix_protocol:in_category'} })
    fix_members: list[FixMember] = Field(default=..., title="Members", description="""The fields, components and groups the element holds, in the order FIX lists them.""", json_schema_extra = { "linkml_meta": {'comments': ['A message lists its members in a structure element and a '
                      'component or a group lists them directly. The record lists them '
                      'here in each case.'],
         'domain_of': ['FixComponent', 'FixGroup', 'FixMessage'],
         'slot_uri': 'fix_protocol:fix_members'} })
    fixml_not_required: Optional[bool] = Field(default=None, title="Not Required in FIXML", description="""True when the element is left out of FIXML, FIX's XML encoding.""", json_schema_extra = { "linkml_meta": {'aliases': ['notReqXML'],
         'comments': ['FIX Latest writes it in a FIXML annotation, the only kind of '
                      'application information the file carries.'],
         'domain_of': ['FixSection',
                       'FixCategory',
                       'FixField',
                       'FixComponent',
                       'FixMessage'],
         'slot_uri': 'fix_protocol:fixml_not_required'} })
    msg_type: str = Field(default=..., title="MsgType", description="""The value of field 35 that marks a message of this kind.""", json_schema_extra = { "linkml_meta": {'aliases': ['msgType'],
         'domain_of': ['FixMessage'],
         'exact_mappings': ['fixr:msgType']} })
    id: str = Field(default=..., title="Identifier", description="""The element's identifier: a prefix for its kind, then the number or name FIX gives it, such as fix_field:55 or fix_category:Allocation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FixElement']} })
    name: str = Field(default=..., title="Name", description="""The element's name in FIX, such as NewOrderSingle or Symbol.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixElement'],
         'exact_mappings': ['fixr:name'],
         'slot_uri': 'fix_protocol:name'} })
    added_in: Optional[str] = Field(default=None, title="Added In", description="""The FIX version that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['added'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:added'],
         'slot_uri': 'fix_protocol:added_in'} })
    added_in_ep: Optional[int] = Field(default=None, title="Added In Extension Pack", description="""The extension pack that added the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['addedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:addedEP'],
         'slot_uri': 'fix_protocol:added_in_ep'} })
    updated_in: Optional[str] = Field(default=None, title="Last Updated In", description="""The FIX version that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updated'],
         'slot_uri': 'fix_protocol:updated_in'} })
    updated_in_ep: Optional[int] = Field(default=None, title="Last Updated In Extension Pack", description="""The extension pack that last changed the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['updatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:updatedEP'],
         'slot_uri': 'fix_protocol:updated_in_ep'} })
    deprecated_in: Optional[str] = Field(default=None, title="Deprecated In", description="""The FIX version that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecated'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecated'],
         'slot_uri': 'fix_protocol:deprecated_in'} })
    deprecated_in_ep: Optional[int] = Field(default=None, title="Deprecated In Extension Pack", description="""The extension pack that deprecated the element.""", json_schema_extra = { "linkml_meta": {'aliases': ['deprecatedEP'],
         'domain_of': ['FixPedigreeMixin'],
         'exact_mappings': ['fixr:deprecatedEP'],
         'slot_uri': 'fix_protocol:deprecated_in_ep'} })

    @field_validator('in_category')
    def pattern_in_category(cls, v):
        pattern=re.compile(r"^fix_category:[A-Za-z][A-Za-z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid in_category format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid in_category format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('msg_type')
    def pattern_msg_type(cls, v):
        pattern=re.compile(r"^[0-9A-Za-z]{1,2}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid msg_type format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid msg_type format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^fix_message:[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid id format: {v}"
            raise ValueError(err_msg)
        return v


class FixRepository(ConfiguredBaseModel):
    """
    One file of the catalogue: the edition it renders, with some kinds of FIX Latest's elements.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['fix_orchestra:OrchestraRepositoryV10', 'fixr:repository'],
         'from_schema': 'https://w3id.org/lmodel/fix-protocol',
         'title': 'FIX Latest Catalogue',
         'tree_root': True})

    repository_name: Literal["FIX.Latest"] = Field(default=..., title="Repository Name", description="""The name FIX gives the repository, FIX.Latest.""", json_schema_extra = { "linkml_meta": {'aliases': ['name'],
         'domain_of': ['FixRepository'],
         'equals_string': 'FIX.Latest',
         'exact_mappings': ['fixr:name']} })
    repository_version: str = Field(default=..., title="Edition", description="""The extension pack the repository stands at, such as FIX.Latest_EP312.""", json_schema_extra = { "linkml_meta": {'aliases': ['version'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['fixr:version']} })
    metadata_title: Optional[str] = Field(default=None, title="Title", description="""The title the repository's metadata gives.""", json_schema_extra = { "linkml_meta": {'aliases': ['title'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['dcterms:title']} })
    metadata_description: Optional[str] = Field(default=None, title="Edition Statement", description="""The metadata's one-line statement of which extension pack the file holds.""", json_schema_extra = { "linkml_meta": {'aliases': ['description'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['dcterms:description']} })
    metadata_creator: Optional[str] = Field(default=None, title="Creator", description="""Who made the repository, as its metadata states.""", json_schema_extra = { "linkml_meta": {'aliases': ['creator'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['dcterms:creator']} })
    metadata_publisher: Optional[str] = Field(default=None, title="Publisher", description="""Who published the repository, as its metadata states.""", json_schema_extra = { "linkml_meta": {'aliases': ['publisher'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['dcterms:publisher']} })
    metadata_rights: Optional[str] = Field(default=None, title="Rights Statement", description="""The rights line in the repository's metadata, word for word.""", json_schema_extra = { "linkml_meta": {'aliases': ['rights'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['dcterms:rights']} })
    metadata_format: Optional[str] = Field(default=None, title="Format", description="""The media type of the repository file.""", json_schema_extra = { "linkml_meta": {'aliases': ['format'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['dcterms:format']} })
    metadata_conforms_to: Optional[str] = Field(default=None, title="Conforms To", description="""The Orchestra version the repository file follows.""", json_schema_extra = { "linkml_meta": {'aliases': ['conformsTo'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['dcterms:conformsTo']} })
    metadata_created: Optional[str] = Field(default=None, title="Created", description="""The date the repository file was made.""", json_schema_extra = { "linkml_meta": {'aliases': ['created'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['dcterms:created']} })
    metadata_source: Optional[str] = Field(default=None, title="Source", description="""The tool or source the metadata names for the file.""", json_schema_extra = { "linkml_meta": {'aliases': ['source'],
         'domain_of': ['FixRepository'],
         'exact_mappings': ['dcterms:source']} })
    fix_sections: Optional[list[FixSection]] = Field(default=None, title="Sections", description="""The sections, in FIX's order.""", json_schema_extra = { "linkml_meta": {'aliases': ['sections'], 'domain_of': ['FixRepository']} })
    fix_categories: Optional[list[FixCategory]] = Field(default=None, title="Categories", description="""The categories, in FIX's order.""", json_schema_extra = { "linkml_meta": {'aliases': ['categories'], 'domain_of': ['FixRepository']} })
    fix_datatypes: Optional[list[FixDatatype]] = Field(default=None, title="Datatypes", description="""The datatypes, in FIX's order.""", json_schema_extra = { "linkml_meta": {'aliases': ['datatypes'], 'domain_of': ['FixRepository']} })
    fix_code_sets: Optional[list[FixCodeSet]] = Field(default=None, title="Code Sets", description="""The code sets, in FIX's order.""", json_schema_extra = { "linkml_meta": {'aliases': ['codeSets'], 'domain_of': ['FixRepository']} })
    fix_fields: Optional[list[FixField]] = Field(default=None, title="Fields", description="""The fields, in FIX's order.""", json_schema_extra = { "linkml_meta": {'aliases': ['fields'], 'domain_of': ['FixRepository']} })
    fix_components: Optional[list[FixComponent]] = Field(default=None, title="Components", description="""The components, in FIX's order.""", json_schema_extra = { "linkml_meta": {'aliases': ['components'], 'domain_of': ['FixRepository']} })
    fix_groups: Optional[list[FixGroup]] = Field(default=None, title="Repeating Groups", description="""The repeating groups, in FIX's order.""", json_schema_extra = { "linkml_meta": {'aliases': ['groups'], 'domain_of': ['FixRepository']} })
    fix_messages: Optional[list[FixMessage]] = Field(default=None, title="Messages", description="""The messages, in FIX's order.""", json_schema_extra = { "linkml_meta": {'aliases': ['messages'], 'domain_of': ['FixRepository']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
FixPedigreeMixin.model_rebuild()
FixElement.model_rebuild()
FixSection.model_rebuild()
FixCategory.model_rebuild()
FixDatatype.model_rebuild()
FixMappedDatatype.model_rebuild()
FixCodeSet.model_rebuild()
FixCode.model_rebuild()
FixField.model_rebuild()
FixMember.model_rebuild()
FixComponent.model_rebuild()
FixGroup.model_rebuild()
FixNumInGroup.model_rebuild()
FixMessage.model_rebuild()
FixRepository.model_rebuild()
