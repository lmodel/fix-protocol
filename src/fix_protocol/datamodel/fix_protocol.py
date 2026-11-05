# Auto generated from fix_protocol.yaml by pythongen.py version: 0.0.1
# Schema: fix_protocol
#
# id: https://w3id.org/lmodel/fix-protocol
# description: A LinkML model of FIX Latest, the application layer of the Financial Information eXchange (FIX) protocol that the FIX Trading Community maintains. It holds every section, category, datatype, code set, field, component, repeating group and message of FIX Latest as a record, with the version and extension pack that added and last changed each one. The records keep FIX's names, numbers and codes and none of its descriptive text.
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

from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.12.0"
version = "FIX.Latest_EP312"

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
FIX_CATEGORY = CurieNamespace('fix_category', 'https://w3id.org/lmodel/fix-protocol/category/')
FIX_CODE = CurieNamespace('fix_code', 'https://w3id.org/lmodel/fix-protocol/code/')
FIX_CODE_SET = CurieNamespace('fix_code_set', 'https://w3id.org/lmodel/fix-protocol/code_set/')
FIX_COMPONENT = CurieNamespace('fix_component', 'https://w3id.org/lmodel/fix-protocol/component/')
FIX_DATATYPE = CurieNamespace('fix_datatype', 'https://w3id.org/lmodel/fix-protocol/datatype/')
FIX_FIELD = CurieNamespace('fix_field', 'https://w3id.org/lmodel/fix-protocol/field/')
FIX_GROUP = CurieNamespace('fix_group', 'https://w3id.org/lmodel/fix-protocol/group/')
FIX_MESSAGE = CurieNamespace('fix_message', 'https://w3id.org/lmodel/fix-protocol/message/')
FIX_ORCHESTRA = CurieNamespace('fix_orchestra', 'https://w3id.org/lmodel/fix-orchestra/')
FIX_PROTOCOL = CurieNamespace('fix_protocol', 'https://w3id.org/lmodel/fix-protocol/')
FIX_SECTION = CurieNamespace('fix_section', 'https://w3id.org/lmodel/fix-protocol/section/')
FIXR = CurieNamespace('fixr', 'http://fixprotocol.io/2020/orchestra/repository/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = FIX_PROTOCOL


# Types
class FixVersion(String):
    """ A version of the FIX standard, such as FIX.4.4, FIX.5.0SP2 or FIX.Latest. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "fix_version"
    type_model_uri = FIX_PROTOCOL.FixVersion


class FixExtensionPack(Integer):
    """ The number of a FIX extension pack, the unit in which FIX Latest changes. """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "fix_extension_pack"
    type_model_uri = FIX_PROTOCOL.FixExtensionPack


class FixDate(String):
    """ A date as the repository's metadata writes it, year first. """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "fix_date"
    type_model_uri = FIX_PROTOCOL.FixDate


class FixName(String):
    """ A name as FIX writes one: a letter, then letters, digits and underscores. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "fix_name"
    type_model_uri = FIX_PROTOCOL.FixName


# Class references
class FixElementId(URIorCURIE):
    pass


class FixSectionId(FixElementId):
    pass


class FixCategoryId(FixElementId):
    pass


class FixDatatypeId(FixElementId):
    pass


class FixCodeSetId(FixElementId):
    pass


class FixCodeId(FixElementId):
    pass


class FixFieldId(FixElementId):
    pass


class FixComponentId(FixElementId):
    pass


class FixGroupId(FixElementId):
    pass


class FixMessageId(FixElementId):
    pass


@dataclass(repr=False)
class FixRepository(YAMLRoot):
    """
    One file of the catalogue: the edition it renders and one or more kinds of FIX Latest's elements.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixRepository"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixRepository"
    class_name: ClassVar[str] = "FixRepository"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixRepository

    repository_name: str = None
    repository_version: Union[str, FixVersion] = None
    metadata_title: Optional[str] = None
    metadata_description: Optional[str] = None
    metadata_creator: Optional[str] = None
    metadata_publisher: Optional[str] = None
    metadata_rights: Optional[str] = None
    metadata_format: Optional[str] = None
    metadata_conforms_to: Optional[str] = None
    metadata_created: Optional[Union[str, FixDate]] = None
    metadata_source: Optional[str] = None
    fix_sections: Optional[Union[dict[Union[str, FixSectionId], Union[dict, "FixSection"]], list[Union[dict, "FixSection"]]]] = empty_dict()
    fix_categories: Optional[Union[dict[Union[str, FixCategoryId], Union[dict, "FixCategory"]], list[Union[dict, "FixCategory"]]]] = empty_dict()
    fix_datatypes: Optional[Union[dict[Union[str, FixDatatypeId], Union[dict, "FixDatatype"]], list[Union[dict, "FixDatatype"]]]] = empty_dict()
    fix_code_sets: Optional[Union[dict[Union[str, FixCodeSetId], Union[dict, "FixCodeSet"]], list[Union[dict, "FixCodeSet"]]]] = empty_dict()
    fix_fields: Optional[Union[dict[Union[str, FixFieldId], Union[dict, "FixField"]], list[Union[dict, "FixField"]]]] = empty_dict()
    fix_components: Optional[Union[dict[Union[str, FixComponentId], Union[dict, "FixComponent"]], list[Union[dict, "FixComponent"]]]] = empty_dict()
    fix_groups: Optional[Union[dict[Union[str, FixGroupId], Union[dict, "FixGroup"]], list[Union[dict, "FixGroup"]]]] = empty_dict()
    fix_messages: Optional[Union[dict[Union[str, FixMessageId], Union[dict, "FixMessage"]], list[Union[dict, "FixMessage"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.repository_name):
            self.MissingRequiredField("repository_name")
        if not isinstance(self.repository_name, str):
            self.repository_name = str(self.repository_name)

        if self._is_empty(self.repository_version):
            self.MissingRequiredField("repository_version")
        if not isinstance(self.repository_version, FixVersion):
            self.repository_version = FixVersion(self.repository_version)

        if self.metadata_title is not None and not isinstance(self.metadata_title, str):
            self.metadata_title = str(self.metadata_title)

        if self.metadata_description is not None and not isinstance(self.metadata_description, str):
            self.metadata_description = str(self.metadata_description)

        if self.metadata_creator is not None and not isinstance(self.metadata_creator, str):
            self.metadata_creator = str(self.metadata_creator)

        if self.metadata_publisher is not None and not isinstance(self.metadata_publisher, str):
            self.metadata_publisher = str(self.metadata_publisher)

        if self.metadata_rights is not None and not isinstance(self.metadata_rights, str):
            self.metadata_rights = str(self.metadata_rights)

        if self.metadata_format is not None and not isinstance(self.metadata_format, str):
            self.metadata_format = str(self.metadata_format)

        if self.metadata_conforms_to is not None and not isinstance(self.metadata_conforms_to, str):
            self.metadata_conforms_to = str(self.metadata_conforms_to)

        if self.metadata_created is not None and not isinstance(self.metadata_created, FixDate):
            self.metadata_created = FixDate(self.metadata_created)

        if self.metadata_source is not None and not isinstance(self.metadata_source, str):
            self.metadata_source = str(self.metadata_source)

        self._normalize_inlined_as_list(slot_name="fix_sections", slot_type=FixSection, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fix_categories", slot_type=FixCategory, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fix_datatypes", slot_type=FixDatatype, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fix_code_sets", slot_type=FixCodeSet, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fix_fields", slot_type=FixField, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fix_components", slot_type=FixComponent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fix_groups", slot_type=FixGroup, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="fix_messages", slot_type=FixMessage, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixPedigreeMixin(YAMLRoot):
    """
    When FIX added, last changed and deprecated an element, by version and extension pack.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixPedigreeMixin"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixPedigreeMixin"
    class_name: ClassVar[str] = "FixPedigreeMixin"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixPedigreeMixin

    added_in: Optional[Union[str, FixVersion]] = None
    added_in_ep: Optional[Union[int, FixExtensionPack]] = None
    updated_in: Optional[Union[str, FixVersion]] = None
    updated_in_ep: Optional[Union[int, FixExtensionPack]] = None
    deprecated_in: Optional[Union[str, FixVersion]] = None
    deprecated_in_ep: Optional[Union[int, FixExtensionPack]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.added_in is not None and not isinstance(self.added_in, FixVersion):
            self.added_in = FixVersion(self.added_in)

        if self.added_in_ep is not None and not isinstance(self.added_in_ep, FixExtensionPack):
            self.added_in_ep = FixExtensionPack(self.added_in_ep)

        if self.updated_in is not None and not isinstance(self.updated_in, FixVersion):
            self.updated_in = FixVersion(self.updated_in)

        if self.updated_in_ep is not None and not isinstance(self.updated_in_ep, FixExtensionPack):
            self.updated_in_ep = FixExtensionPack(self.updated_in_ep)

        if self.deprecated_in is not None and not isinstance(self.deprecated_in, FixVersion):
            self.deprecated_in = FixVersion(self.deprecated_in)

        if self.deprecated_in_ep is not None and not isinstance(self.deprecated_in_ep, FixExtensionPack):
            self.deprecated_in_ep = FixExtensionPack(self.deprecated_in_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixElement(YAMLRoot):
    """
    An element of FIX Latest with an identifier and a name of its own.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixElement"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixElement"
    class_name: ClassVar[str] = "FixElement"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixElement

    id: Union[str, FixElementId] = None
    name: Union[str, FixName] = None
    added_in: Optional[Union[str, FixVersion]] = None
    added_in_ep: Optional[Union[int, FixExtensionPack]] = None
    updated_in: Optional[Union[str, FixVersion]] = None
    updated_in_ep: Optional[Union[int, FixExtensionPack]] = None
    deprecated_in: Optional[Union[str, FixVersion]] = None
    deprecated_in_ep: Optional[Union[int, FixExtensionPack]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixElementId):
            self.id = FixElementId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, FixName):
            self.name = FixName(self.name)

        if self.added_in is not None and not isinstance(self.added_in, FixVersion):
            self.added_in = FixVersion(self.added_in)

        if self.added_in_ep is not None and not isinstance(self.added_in_ep, FixExtensionPack):
            self.added_in_ep = FixExtensionPack(self.added_in_ep)

        if self.updated_in is not None and not isinstance(self.updated_in, FixVersion):
            self.updated_in = FixVersion(self.updated_in)

        if self.updated_in_ep is not None and not isinstance(self.updated_in_ep, FixExtensionPack):
            self.updated_in_ep = FixExtensionPack(self.updated_in_ep)

        if self.deprecated_in is not None and not isinstance(self.deprecated_in, FixVersion):
            self.deprecated_in = FixVersion(self.deprecated_in)

        if self.deprecated_in_ep is not None and not isinstance(self.deprecated_in_ep, FixExtensionPack):
            self.deprecated_in_ep = FixExtensionPack(self.deprecated_in_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixSection(FixElement):
    """
    One of the five parts of FIX by business area, such as pre-trade or post-trade.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixSection"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixSection"
    class_name: ClassVar[str] = "FixSection"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixSection

    id: Union[str, FixSectionId] = None
    name: Union[str, FixName] = None
    fixml_file_name: Optional[Union[str, FixName]] = None
    fixml_not_required: Optional[Union[bool, Bool]] = None
    section_order: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixSectionId):
            self.id = FixSectionId(self.id)

        if self.fixml_file_name is not None and not isinstance(self.fixml_file_name, FixName):
            self.fixml_file_name = FixName(self.fixml_file_name)

        if self.fixml_not_required is not None and not isinstance(self.fixml_not_required, Bool):
            self.fixml_not_required = Bool(self.fixml_not_required)

        if self.section_order is not None and not isinstance(self.section_order, int):
            self.section_order = int(self.section_order)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixCategory(FixElement):
    """
    A group of messages within a section, or one of the groups that hold the shared components and the fields.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixCategory"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixCategory"
    class_name: ClassVar[str] = "FixCategory"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixCategory

    id: Union[str, FixCategoryId] = None
    name: Union[str, FixName] = None
    fixml_file_name: Optional[Union[str, FixName]] = None
    in_section: Optional[Union[str, FixSectionId]] = None
    fixml_not_required: Optional[Union[bool, Bool]] = None
    category_kind: Optional[Union[str, "FixCategoryKind"]] = None
    include_file: Optional[Union[str, "FixIncludeFile"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixCategoryId):
            self.id = FixCategoryId(self.id)

        if self.fixml_file_name is not None and not isinstance(self.fixml_file_name, FixName):
            self.fixml_file_name = FixName(self.fixml_file_name)

        if self.in_section is not None and not isinstance(self.in_section, FixSectionId):
            self.in_section = FixSectionId(self.in_section)

        if self.fixml_not_required is not None and not isinstance(self.fixml_not_required, Bool):
            self.fixml_not_required = Bool(self.fixml_not_required)

        if self.category_kind is not None and not isinstance(self.category_kind, FixCategoryKind):
            self.category_kind = FixCategoryKind(self.category_kind)

        if self.include_file is not None and not isinstance(self.include_file, FixIncludeFile):
            self.include_file = FixIncludeFile(self.include_file)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixDatatype(FixElement):
    """
    A kind of value a field holds, such as int, Price or UTCTimestamp, with the XML Schema types it maps to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixDatatype"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixDatatype"
    class_name: ClassVar[str] = "FixDatatype"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixDatatype

    id: Union[str, FixDatatypeId] = None
    name: Union[str, FixName] = None
    base_type: Optional[Union[str, FixDatatypeId]] = None
    mapped_datatypes: Optional[Union[Union[dict, "FixMappedDatatype"], list[Union[dict, "FixMappedDatatype"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixDatatypeId):
            self.id = FixDatatypeId(self.id)

        if self.base_type is not None and not isinstance(self.base_type, FixDatatypeId):
            self.base_type = FixDatatypeId(self.base_type)

        self._normalize_inlined_as_list(slot_name="mapped_datatypes", slot_type=FixMappedDatatype, key_name="mapped_standard", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixMappedDatatype(YAMLRoot):
    """
    The type of another standard that a FIX datatype takes, such as xs:decimal in XML Schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixMappedDatatype"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixMappedDatatype"
    class_name: ClassVar[str] = "FixMappedDatatype"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixMappedDatatype

    mapped_standard: str = None
    mapped_base: Optional[str] = None
    mapped_builtin: Optional[Union[bool, Bool]] = None
    mapped_min_inclusive: Optional[str] = None
    mapped_pattern: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.mapped_standard):
            self.MissingRequiredField("mapped_standard")
        if not isinstance(self.mapped_standard, str):
            self.mapped_standard = str(self.mapped_standard)

        if self.mapped_base is not None and not isinstance(self.mapped_base, str):
            self.mapped_base = str(self.mapped_base)

        if self.mapped_builtin is not None and not isinstance(self.mapped_builtin, Bool):
            self.mapped_builtin = Bool(self.mapped_builtin)

        if self.mapped_min_inclusive is not None and not isinstance(self.mapped_min_inclusive, str):
            self.mapped_min_inclusive = str(self.mapped_min_inclusive)

        if self.mapped_pattern is not None and not isinstance(self.mapped_pattern, str):
            self.mapped_pattern = str(self.mapped_pattern)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixCodeSet(FixElement):
    """
    A list of the values a field may take, each a code with a name, such as the sides of an order.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixCodeSet"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixCodeSet"
    class_name: ClassVar[str] = "FixCodeSet"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixCodeSet

    id: Union[str, FixCodeSetId] = None
    name: Union[str, FixName] = None
    code_set_datatype: Union[str, FixDatatypeId] = None
    fix_codes: Union[dict[Union[str, FixCodeId], Union[dict, "FixCode"]], list[Union[dict, "FixCode"]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixCodeSetId):
            self.id = FixCodeSetId(self.id)

        if self._is_empty(self.code_set_datatype):
            self.MissingRequiredField("code_set_datatype")
        if not isinstance(self.code_set_datatype, FixDatatypeId):
            self.code_set_datatype = FixDatatypeId(self.code_set_datatype)

        if self._is_empty(self.fix_codes):
            self.MissingRequiredField("fix_codes")
        self._normalize_inlined_as_list(slot_name="fix_codes", slot_type=FixCode, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixCode(FixElement):
    """
    One value of a code set, with its name, such as 1 for Buy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixCode"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixCode"
    class_name: ClassVar[str] = "FixCode"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixCode

    id: Union[str, FixCodeId] = None
    name: Union[str, FixName] = None
    code_value: str = None
    sort_order: Optional[int] = None
    code_group: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixCodeId):
            self.id = FixCodeId(self.id)

        if self._is_empty(self.code_value):
            self.MissingRequiredField("code_value")
        if not isinstance(self.code_value, str):
            self.code_value = str(self.code_value)

        if self.sort_order is not None and not isinstance(self.sort_order, int):
            self.sort_order = int(self.sort_order)

        if self.code_group is not None and not isinstance(self.code_group, str):
            self.code_group = str(self.code_group)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixField(FixElement):
    """
    A field of FIX, known by its tag number, such as 55 for Symbol, with the datatype or code set of its values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixField"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixField"
    class_name: ClassVar[str] = "FixField"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixField

    id: Union[str, FixFieldId] = None
    name: Union[str, FixName] = None
    abbr_name: Optional[Union[str, FixName]] = None
    fixml_not_required: Optional[Union[bool, Bool]] = None
    field_datatype: Optional[Union[str, FixDatatypeId]] = None
    field_code_set: Optional[Union[str, FixCodeSetId]] = None
    union_datatype: Optional[Union[str, FixDatatypeId]] = None
    length_field: Optional[Union[str, FixFieldId]] = None
    discriminator_field: Optional[Union[str, FixFieldId]] = None
    base_category: Optional[Union[str, FixCategoryId]] = None
    base_category_abbr_name: Optional[Union[str, FixName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixFieldId):
            self.id = FixFieldId(self.id)

        if self.abbr_name is not None and not isinstance(self.abbr_name, FixName):
            self.abbr_name = FixName(self.abbr_name)

        if self.fixml_not_required is not None and not isinstance(self.fixml_not_required, Bool):
            self.fixml_not_required = Bool(self.fixml_not_required)

        if self.field_datatype is not None and not isinstance(self.field_datatype, FixDatatypeId):
            self.field_datatype = FixDatatypeId(self.field_datatype)

        if self.field_code_set is not None and not isinstance(self.field_code_set, FixCodeSetId):
            self.field_code_set = FixCodeSetId(self.field_code_set)

        if self.union_datatype is not None and not isinstance(self.union_datatype, FixDatatypeId):
            self.union_datatype = FixDatatypeId(self.union_datatype)

        if self.length_field is not None and not isinstance(self.length_field, FixFieldId):
            self.length_field = FixFieldId(self.length_field)

        if self.discriminator_field is not None and not isinstance(self.discriminator_field, FixFieldId):
            self.discriminator_field = FixFieldId(self.discriminator_field)

        if self.base_category is not None and not isinstance(self.base_category, FixCategoryId):
            self.base_category = FixCategoryId(self.base_category)

        if self.base_category_abbr_name is not None and not isinstance(self.base_category_abbr_name, FixName):
            self.base_category_abbr_name = FixName(self.base_category_abbr_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixMember(YAMLRoot):
    """
    One field, component or group in a message, component or group, and whether it must be there.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixMember"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixMember"
    class_name: ClassVar[str] = "FixMember"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixMember

    member_field: Optional[Union[str, FixFieldId]] = None
    member_component: Optional[Union[str, FixComponentId]] = None
    member_group: Optional[Union[str, FixGroupId]] = None
    presence: Optional[Union[str, "FixPresence"]] = None
    fixml_inlined: Optional[Union[bool, Bool]] = None
    added_in: Optional[Union[str, FixVersion]] = None
    added_in_ep: Optional[Union[int, FixExtensionPack]] = None
    updated_in: Optional[Union[str, FixVersion]] = None
    updated_in_ep: Optional[Union[int, FixExtensionPack]] = None
    deprecated_in: Optional[Union[str, FixVersion]] = None
    deprecated_in_ep: Optional[Union[int, FixExtensionPack]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.member_field is not None and not isinstance(self.member_field, FixFieldId):
            self.member_field = FixFieldId(self.member_field)

        if self.member_component is not None and not isinstance(self.member_component, FixComponentId):
            self.member_component = FixComponentId(self.member_component)

        if self.member_group is not None and not isinstance(self.member_group, FixGroupId):
            self.member_group = FixGroupId(self.member_group)

        if self.presence is not None and not isinstance(self.presence, FixPresence):
            self.presence = FixPresence(self.presence)

        if self.fixml_inlined is not None and not isinstance(self.fixml_inlined, Bool):
            self.fixml_inlined = Bool(self.fixml_inlined)

        if self.added_in is not None and not isinstance(self.added_in, FixVersion):
            self.added_in = FixVersion(self.added_in)

        if self.added_in_ep is not None and not isinstance(self.added_in_ep, FixExtensionPack):
            self.added_in_ep = FixExtensionPack(self.added_in_ep)

        if self.updated_in is not None and not isinstance(self.updated_in, FixVersion):
            self.updated_in = FixVersion(self.updated_in)

        if self.updated_in_ep is not None and not isinstance(self.updated_in_ep, FixExtensionPack):
            self.updated_in_ep = FixExtensionPack(self.updated_in_ep)

        if self.deprecated_in is not None and not isinstance(self.deprecated_in, FixVersion):
            self.deprecated_in = FixVersion(self.deprecated_in)

        if self.deprecated_in_ep is not None and not isinstance(self.deprecated_in_ep, FixExtensionPack):
            self.deprecated_in_ep = FixExtensionPack(self.deprecated_in_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixComponent(FixElement):
    """
    A named block of fields, components and groups that messages share, such as Instrument.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixComponent"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixComponent"
    class_name: ClassVar[str] = "FixComponent"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixComponent

    id: Union[str, FixComponentId] = None
    name: Union[str, FixName] = None
    in_category: Union[str, FixCategoryId] = None
    abbr_name: Optional[Union[str, FixName]] = None
    fix_members: Optional[Union[Union[dict, FixMember], list[Union[dict, FixMember]]]] = empty_list()
    fixml_not_required: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixComponentId):
            self.id = FixComponentId(self.id)

        if self._is_empty(self.in_category):
            self.MissingRequiredField("in_category")
        if not isinstance(self.in_category, FixCategoryId):
            self.in_category = FixCategoryId(self.in_category)

        if self.abbr_name is not None and not isinstance(self.abbr_name, FixName):
            self.abbr_name = FixName(self.abbr_name)

        if not isinstance(self.fix_members, list):
            self.fix_members = [self.fix_members] if self.fix_members is not None else []
        self.fix_members = [v if isinstance(v, FixMember) else FixMember(**as_dict(v)) for v in self.fix_members]

        if self.fixml_not_required is not None and not isinstance(self.fixml_not_required, Bool):
            self.fixml_not_required = Bool(self.fixml_not_required)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixGroup(FixElement):
    """
    A block of members that repeats in a message, with the field that counts the repeats.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixGroup"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixGroup"
    class_name: ClassVar[str] = "FixGroup"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixGroup

    id: Union[str, FixGroupId] = None
    name: Union[str, FixName] = None
    in_category: Union[str, FixCategoryId] = None
    fix_members: Union[Union[dict, FixMember], list[Union[dict, FixMember]]] = None
    num_in_group: Union[dict, "FixNumInGroup"] = None
    abbr_name: Optional[Union[str, FixName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixGroupId):
            self.id = FixGroupId(self.id)

        if self._is_empty(self.in_category):
            self.MissingRequiredField("in_category")
        if not isinstance(self.in_category, FixCategoryId):
            self.in_category = FixCategoryId(self.in_category)

        if self._is_empty(self.fix_members):
            self.MissingRequiredField("fix_members")
        if not isinstance(self.fix_members, list):
            self.fix_members = [self.fix_members] if self.fix_members is not None else []
        self.fix_members = [v if isinstance(v, FixMember) else FixMember(**as_dict(v)) for v in self.fix_members]

        if self._is_empty(self.num_in_group):
            self.MissingRequiredField("num_in_group")
        if not isinstance(self.num_in_group, FixNumInGroup):
            self.num_in_group = FixNumInGroup(**as_dict(self.num_in_group))

        if self.abbr_name is not None and not isinstance(self.abbr_name, FixName):
            self.abbr_name = FixName(self.abbr_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixNumInGroup(YAMLRoot):
    """
    The field that counts a group's repeats, as the group names it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixNumInGroup"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixNumInGroup"
    class_name: ClassVar[str] = "FixNumInGroup"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixNumInGroup

    count_field: Union[str, FixFieldId] = None
    added_in: Optional[Union[str, FixVersion]] = None
    added_in_ep: Optional[Union[int, FixExtensionPack]] = None
    updated_in: Optional[Union[str, FixVersion]] = None
    updated_in_ep: Optional[Union[int, FixExtensionPack]] = None
    deprecated_in: Optional[Union[str, FixVersion]] = None
    deprecated_in_ep: Optional[Union[int, FixExtensionPack]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.count_field):
            self.MissingRequiredField("count_field")
        if not isinstance(self.count_field, FixFieldId):
            self.count_field = FixFieldId(self.count_field)

        if self.added_in is not None and not isinstance(self.added_in, FixVersion):
            self.added_in = FixVersion(self.added_in)

        if self.added_in_ep is not None and not isinstance(self.added_in_ep, FixExtensionPack):
            self.added_in_ep = FixExtensionPack(self.added_in_ep)

        if self.updated_in is not None and not isinstance(self.updated_in, FixVersion):
            self.updated_in = FixVersion(self.updated_in)

        if self.updated_in_ep is not None and not isinstance(self.updated_in_ep, FixExtensionPack):
            self.updated_in_ep = FixExtensionPack(self.updated_in_ep)

        if self.deprecated_in is not None and not isinstance(self.deprecated_in, FixVersion):
            self.deprecated_in = FixVersion(self.deprecated_in)

        if self.deprecated_in_ep is not None and not isinstance(self.deprecated_in_ep, FixExtensionPack):
            self.deprecated_in_ep = FixExtensionPack(self.deprecated_in_ep)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FixMessage(FixElement):
    """
    A FIX message, known by its MsgType, such as D for NewOrderSingle, with its members in order.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FIX_PROTOCOL["FixMessage"]
    class_class_curie: ClassVar[str] = "fix_protocol:FixMessage"
    class_name: ClassVar[str] = "FixMessage"
    class_model_uri: ClassVar[URIRef] = FIX_PROTOCOL.FixMessage

    id: Union[str, FixMessageId] = None
    name: Union[str, FixName] = None
    in_category: Union[str, FixCategoryId] = None
    fix_members: Union[Union[dict, FixMember], list[Union[dict, FixMember]]] = None
    msg_type: str = None
    abbr_name: Optional[Union[str, FixName]] = None
    fixml_not_required: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FixMessageId):
            self.id = FixMessageId(self.id)

        if self._is_empty(self.in_category):
            self.MissingRequiredField("in_category")
        if not isinstance(self.in_category, FixCategoryId):
            self.in_category = FixCategoryId(self.in_category)

        if self._is_empty(self.fix_members):
            self.MissingRequiredField("fix_members")
        if not isinstance(self.fix_members, list):
            self.fix_members = [self.fix_members] if self.fix_members is not None else []
        self.fix_members = [v if isinstance(v, FixMember) else FixMember(**as_dict(v)) for v in self.fix_members]

        if self._is_empty(self.msg_type):
            self.MissingRequiredField("msg_type")
        if not isinstance(self.msg_type, str):
            self.msg_type = str(self.msg_type)

        if self.abbr_name is not None and not isinstance(self.abbr_name, FixName):
            self.abbr_name = FixName(self.abbr_name)

        if self.fixml_not_required is not None and not isinstance(self.fixml_not_required, Bool):
            self.fixml_not_required = Bool(self.fixml_not_required)

        super().__post_init__(**kwargs)


# Enumerations
class FixPresence(EnumDefinitionImpl):
    """
    Whether a message, component or group must carry a member, as Orchestra 1.0 lets FIX Latest say it.
    """
    optional = PermissibleValue(
        text="optional",
        title="Optional",
        description="The member may be left out.")
    required = PermissibleValue(
        text="required",
        title="Required",
        description="The member must be there.")
    forbidden = PermissibleValue(
        text="forbidden",
        title="Forbidden",
        description="The member must be left out.")
    ignored = PermissibleValue(
        text="ignored",
        title="Ignored",
        description="A receiver disregards the member if it is there.")
    constant = PermissibleValue(
        text="constant",
        title="Constant",
        description="The member always takes one fixed value.")

    _defn = EnumDefinition(
        name="FixPresence",
        description="Whether a message, component or group must carry a member, as Orchestra 1.0 lets FIX Latest say it.",
    )

class FixCategoryKind(EnumDefinitionImpl):
    """
    Whether a category groups messages or fields.
    """
    Message = PermissibleValue(
        text="Message",
        title="Messages",
        description="The category groups messages and their components.")
    Field = PermissibleValue(
        text="Field",
        title="Fields",
        description="The category groups fields.")

    _defn = EnumDefinition(
        name="FixCategoryKind",
        description="Whether a category groups messages or fields.",
    )

class FixIncludeFile(EnumDefinitionImpl):
    """
    Which shared FIXML schema file a category's own FIXML schema file brings in.
    """
    components = PermissibleValue(
        text="components",
        title="Components",
        description="The file that defines the shared components.")
    fields = PermissibleValue(
        text="fields",
        title="Fields",
        description="The file that defines the fields.")

    _defn = EnumDefinition(
        name="FixIncludeFile",
        description="Which shared FIXML schema file a category's own FIXML schema file brings in.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=FIX_PROTOCOL.id, name="id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.id, domain=None, range=URIRef)

slots.name = Slot(uri=FIX_PROTOCOL.name, name="name", curie=FIX_PROTOCOL.curie('name'),
                   model_uri=FIX_PROTOCOL.name, domain=None, range=Union[str, FixName])

slots.abbr_name = Slot(uri=FIX_PROTOCOL.abbr_name, name="abbr_name", curie=FIX_PROTOCOL.curie('abbr_name'),
                   model_uri=FIX_PROTOCOL.abbr_name, domain=None, range=Optional[Union[str, FixName]])

slots.fixml_file_name = Slot(uri=FIX_PROTOCOL.fixml_file_name, name="fixml_file_name", curie=FIX_PROTOCOL.curie('fixml_file_name'),
                   model_uri=FIX_PROTOCOL.fixml_file_name, domain=None, range=Optional[Union[str, FixName]])

slots.fixml_not_required = Slot(uri=FIX_PROTOCOL.fixml_not_required, name="fixml_not_required", curie=FIX_PROTOCOL.curie('fixml_not_required'),
                   model_uri=FIX_PROTOCOL.fixml_not_required, domain=None, range=Optional[Union[bool, Bool]])

slots.added_in = Slot(uri=FIX_PROTOCOL.added_in, name="added_in", curie=FIX_PROTOCOL.curie('added_in'),
                   model_uri=FIX_PROTOCOL.added_in, domain=None, range=Optional[Union[str, FixVersion]])

slots.added_in_ep = Slot(uri=FIX_PROTOCOL.added_in_ep, name="added_in_ep", curie=FIX_PROTOCOL.curie('added_in_ep'),
                   model_uri=FIX_PROTOCOL.added_in_ep, domain=None, range=Optional[Union[int, FixExtensionPack]])

slots.updated_in = Slot(uri=FIX_PROTOCOL.updated_in, name="updated_in", curie=FIX_PROTOCOL.curie('updated_in'),
                   model_uri=FIX_PROTOCOL.updated_in, domain=None, range=Optional[Union[str, FixVersion]])

slots.updated_in_ep = Slot(uri=FIX_PROTOCOL.updated_in_ep, name="updated_in_ep", curie=FIX_PROTOCOL.curie('updated_in_ep'),
                   model_uri=FIX_PROTOCOL.updated_in_ep, domain=None, range=Optional[Union[int, FixExtensionPack]])

slots.deprecated_in = Slot(uri=FIX_PROTOCOL.deprecated_in, name="deprecated_in", curie=FIX_PROTOCOL.curie('deprecated_in'),
                   model_uri=FIX_PROTOCOL.deprecated_in, domain=None, range=Optional[Union[str, FixVersion]])

slots.deprecated_in_ep = Slot(uri=FIX_PROTOCOL.deprecated_in_ep, name="deprecated_in_ep", curie=FIX_PROTOCOL.curie('deprecated_in_ep'),
                   model_uri=FIX_PROTOCOL.deprecated_in_ep, domain=None, range=Optional[Union[int, FixExtensionPack]])

slots.in_section = Slot(uri=FIX_PROTOCOL.in_section, name="in_section", curie=FIX_PROTOCOL.curie('in_section'),
                   model_uri=FIX_PROTOCOL.in_section, domain=None, range=Optional[Union[str, FixSectionId]],
                   pattern=re.compile(r'^fix_section:[A-Za-z][A-Za-z0-9_]*$'))

slots.in_category = Slot(uri=FIX_PROTOCOL.in_category, name="in_category", curie=FIX_PROTOCOL.curie('in_category'),
                   model_uri=FIX_PROTOCOL.in_category, domain=None, range=Union[str, FixCategoryId],
                   pattern=re.compile(r'^fix_category:[A-Za-z][A-Za-z0-9_]*$'))

slots.fix_members = Slot(uri=FIX_PROTOCOL.fix_members, name="fix_members", curie=FIX_PROTOCOL.curie('fix_members'),
                   model_uri=FIX_PROTOCOL.fix_members, domain=None, range=Optional[Union[Union[dict, FixMember], list[Union[dict, FixMember]]]])

slots.fixRepository__repository_name = Slot(uri=FIX_PROTOCOL.repository_name, name="fixRepository__repository_name", curie=FIX_PROTOCOL.curie('repository_name'),
                   model_uri=FIX_PROTOCOL.fixRepository__repository_name, domain=None, range=str)

slots.fixRepository__repository_version = Slot(uri=FIX_PROTOCOL.repository_version, name="fixRepository__repository_version", curie=FIX_PROTOCOL.curie('repository_version'),
                   model_uri=FIX_PROTOCOL.fixRepository__repository_version, domain=None, range=Union[str, FixVersion])

slots.fixRepository__metadata_title = Slot(uri=FIX_PROTOCOL.metadata_title, name="fixRepository__metadata_title", curie=FIX_PROTOCOL.curie('metadata_title'),
                   model_uri=FIX_PROTOCOL.fixRepository__metadata_title, domain=None, range=Optional[str])

slots.fixRepository__metadata_description = Slot(uri=FIX_PROTOCOL.metadata_description, name="fixRepository__metadata_description", curie=FIX_PROTOCOL.curie('metadata_description'),
                   model_uri=FIX_PROTOCOL.fixRepository__metadata_description, domain=None, range=Optional[str])

slots.fixRepository__metadata_creator = Slot(uri=FIX_PROTOCOL.metadata_creator, name="fixRepository__metadata_creator", curie=FIX_PROTOCOL.curie('metadata_creator'),
                   model_uri=FIX_PROTOCOL.fixRepository__metadata_creator, domain=None, range=Optional[str])

slots.fixRepository__metadata_publisher = Slot(uri=FIX_PROTOCOL.metadata_publisher, name="fixRepository__metadata_publisher", curie=FIX_PROTOCOL.curie('metadata_publisher'),
                   model_uri=FIX_PROTOCOL.fixRepository__metadata_publisher, domain=None, range=Optional[str])

slots.fixRepository__metadata_rights = Slot(uri=FIX_PROTOCOL.metadata_rights, name="fixRepository__metadata_rights", curie=FIX_PROTOCOL.curie('metadata_rights'),
                   model_uri=FIX_PROTOCOL.fixRepository__metadata_rights, domain=None, range=Optional[str])

slots.fixRepository__metadata_format = Slot(uri=FIX_PROTOCOL.metadata_format, name="fixRepository__metadata_format", curie=FIX_PROTOCOL.curie('metadata_format'),
                   model_uri=FIX_PROTOCOL.fixRepository__metadata_format, domain=None, range=Optional[str])

slots.fixRepository__metadata_conforms_to = Slot(uri=FIX_PROTOCOL.metadata_conforms_to, name="fixRepository__metadata_conforms_to", curie=FIX_PROTOCOL.curie('metadata_conforms_to'),
                   model_uri=FIX_PROTOCOL.fixRepository__metadata_conforms_to, domain=None, range=Optional[str])

slots.fixRepository__metadata_created = Slot(uri=FIX_PROTOCOL.metadata_created, name="fixRepository__metadata_created", curie=FIX_PROTOCOL.curie('metadata_created'),
                   model_uri=FIX_PROTOCOL.fixRepository__metadata_created, domain=None, range=Optional[Union[str, FixDate]])

slots.fixRepository__metadata_source = Slot(uri=FIX_PROTOCOL.metadata_source, name="fixRepository__metadata_source", curie=FIX_PROTOCOL.curie('metadata_source'),
                   model_uri=FIX_PROTOCOL.fixRepository__metadata_source, domain=None, range=Optional[str])

slots.fixRepository__fix_sections = Slot(uri=FIX_PROTOCOL.fix_sections, name="fixRepository__fix_sections", curie=FIX_PROTOCOL.curie('fix_sections'),
                   model_uri=FIX_PROTOCOL.fixRepository__fix_sections, domain=None, range=Optional[Union[dict[Union[str, FixSectionId], Union[dict, FixSection]], list[Union[dict, FixSection]]]])

slots.fixRepository__fix_categories = Slot(uri=FIX_PROTOCOL.fix_categories, name="fixRepository__fix_categories", curie=FIX_PROTOCOL.curie('fix_categories'),
                   model_uri=FIX_PROTOCOL.fixRepository__fix_categories, domain=None, range=Optional[Union[dict[Union[str, FixCategoryId], Union[dict, FixCategory]], list[Union[dict, FixCategory]]]])

slots.fixRepository__fix_datatypes = Slot(uri=FIX_PROTOCOL.fix_datatypes, name="fixRepository__fix_datatypes", curie=FIX_PROTOCOL.curie('fix_datatypes'),
                   model_uri=FIX_PROTOCOL.fixRepository__fix_datatypes, domain=None, range=Optional[Union[dict[Union[str, FixDatatypeId], Union[dict, FixDatatype]], list[Union[dict, FixDatatype]]]])

slots.fixRepository__fix_code_sets = Slot(uri=FIX_PROTOCOL.fix_code_sets, name="fixRepository__fix_code_sets", curie=FIX_PROTOCOL.curie('fix_code_sets'),
                   model_uri=FIX_PROTOCOL.fixRepository__fix_code_sets, domain=None, range=Optional[Union[dict[Union[str, FixCodeSetId], Union[dict, FixCodeSet]], list[Union[dict, FixCodeSet]]]])

slots.fixRepository__fix_fields = Slot(uri=FIX_PROTOCOL.fix_fields, name="fixRepository__fix_fields", curie=FIX_PROTOCOL.curie('fix_fields'),
                   model_uri=FIX_PROTOCOL.fixRepository__fix_fields, domain=None, range=Optional[Union[dict[Union[str, FixFieldId], Union[dict, FixField]], list[Union[dict, FixField]]]])

slots.fixRepository__fix_components = Slot(uri=FIX_PROTOCOL.fix_components, name="fixRepository__fix_components", curie=FIX_PROTOCOL.curie('fix_components'),
                   model_uri=FIX_PROTOCOL.fixRepository__fix_components, domain=None, range=Optional[Union[dict[Union[str, FixComponentId], Union[dict, FixComponent]], list[Union[dict, FixComponent]]]])

slots.fixRepository__fix_groups = Slot(uri=FIX_PROTOCOL.fix_groups, name="fixRepository__fix_groups", curie=FIX_PROTOCOL.curie('fix_groups'),
                   model_uri=FIX_PROTOCOL.fixRepository__fix_groups, domain=None, range=Optional[Union[dict[Union[str, FixGroupId], Union[dict, FixGroup]], list[Union[dict, FixGroup]]]])

slots.fixRepository__fix_messages = Slot(uri=FIX_PROTOCOL.fix_messages, name="fixRepository__fix_messages", curie=FIX_PROTOCOL.curie('fix_messages'),
                   model_uri=FIX_PROTOCOL.fixRepository__fix_messages, domain=None, range=Optional[Union[dict[Union[str, FixMessageId], Union[dict, FixMessage]], list[Union[dict, FixMessage]]]])

slots.fixSection__section_order = Slot(uri=FIX_PROTOCOL.section_order, name="fixSection__section_order", curie=FIX_PROTOCOL.curie('section_order'),
                   model_uri=FIX_PROTOCOL.fixSection__section_order, domain=None, range=Optional[int])

slots.fixCategory__category_kind = Slot(uri=FIX_PROTOCOL.category_kind, name="fixCategory__category_kind", curie=FIX_PROTOCOL.curie('category_kind'),
                   model_uri=FIX_PROTOCOL.fixCategory__category_kind, domain=None, range=Optional[Union[str, "FixCategoryKind"]])

slots.fixCategory__include_file = Slot(uri=FIX_PROTOCOL.include_file, name="fixCategory__include_file", curie=FIX_PROTOCOL.curie('include_file'),
                   model_uri=FIX_PROTOCOL.fixCategory__include_file, domain=None, range=Optional[Union[str, "FixIncludeFile"]])

slots.fixDatatype__base_type = Slot(uri=FIX_PROTOCOL.base_type, name="fixDatatype__base_type", curie=FIX_PROTOCOL.curie('base_type'),
                   model_uri=FIX_PROTOCOL.fixDatatype__base_type, domain=None, range=Optional[Union[str, FixDatatypeId]],
                   pattern=re.compile(r'^fix_datatype:[A-Za-z][A-Za-z0-9_]*$'))

slots.fixDatatype__mapped_datatypes = Slot(uri=FIX_PROTOCOL.mapped_datatypes, name="fixDatatype__mapped_datatypes", curie=FIX_PROTOCOL.curie('mapped_datatypes'),
                   model_uri=FIX_PROTOCOL.fixDatatype__mapped_datatypes, domain=None, range=Optional[Union[Union[dict, FixMappedDatatype], list[Union[dict, FixMappedDatatype]]]])

slots.fixMappedDatatype__mapped_standard = Slot(uri=FIX_PROTOCOL.mapped_standard, name="fixMappedDatatype__mapped_standard", curie=FIX_PROTOCOL.curie('mapped_standard'),
                   model_uri=FIX_PROTOCOL.fixMappedDatatype__mapped_standard, domain=None, range=str)

slots.fixMappedDatatype__mapped_base = Slot(uri=FIX_PROTOCOL.mapped_base, name="fixMappedDatatype__mapped_base", curie=FIX_PROTOCOL.curie('mapped_base'),
                   model_uri=FIX_PROTOCOL.fixMappedDatatype__mapped_base, domain=None, range=Optional[str])

slots.fixMappedDatatype__mapped_builtin = Slot(uri=FIX_PROTOCOL.mapped_builtin, name="fixMappedDatatype__mapped_builtin", curie=FIX_PROTOCOL.curie('mapped_builtin'),
                   model_uri=FIX_PROTOCOL.fixMappedDatatype__mapped_builtin, domain=None, range=Optional[Union[bool, Bool]])

slots.fixMappedDatatype__mapped_min_inclusive = Slot(uri=FIX_PROTOCOL.mapped_min_inclusive, name="fixMappedDatatype__mapped_min_inclusive", curie=FIX_PROTOCOL.curie('mapped_min_inclusive'),
                   model_uri=FIX_PROTOCOL.fixMappedDatatype__mapped_min_inclusive, domain=None, range=Optional[str])

slots.fixMappedDatatype__mapped_pattern = Slot(uri=FIX_PROTOCOL.mapped_pattern, name="fixMappedDatatype__mapped_pattern", curie=FIX_PROTOCOL.curie('mapped_pattern'),
                   model_uri=FIX_PROTOCOL.fixMappedDatatype__mapped_pattern, domain=None, range=Optional[str])

slots.fixCodeSet__code_set_datatype = Slot(uri=FIX_PROTOCOL.code_set_datatype, name="fixCodeSet__code_set_datatype", curie=FIX_PROTOCOL.curie('code_set_datatype'),
                   model_uri=FIX_PROTOCOL.fixCodeSet__code_set_datatype, domain=None, range=Union[str, FixDatatypeId],
                   pattern=re.compile(r'^fix_datatype:[A-Za-z][A-Za-z0-9_]*$'))

slots.fixCodeSet__fix_codes = Slot(uri=FIX_PROTOCOL.fix_codes, name="fixCodeSet__fix_codes", curie=FIX_PROTOCOL.curie('fix_codes'),
                   model_uri=FIX_PROTOCOL.fixCodeSet__fix_codes, domain=None, range=Union[dict[Union[str, FixCodeId], Union[dict, FixCode]], list[Union[dict, FixCode]]])

slots.fixCode__code_value = Slot(uri=FIX_PROTOCOL.code_value, name="fixCode__code_value", curie=FIX_PROTOCOL.curie('code_value'),
                   model_uri=FIX_PROTOCOL.fixCode__code_value, domain=None, range=str,
                   pattern=re.compile(r'^\S+$'))

slots.fixCode__sort_order = Slot(uri=FIX_PROTOCOL.sort_order, name="fixCode__sort_order", curie=FIX_PROTOCOL.curie('sort_order'),
                   model_uri=FIX_PROTOCOL.fixCode__sort_order, domain=None, range=Optional[int])

slots.fixCode__code_group = Slot(uri=FIX_PROTOCOL.code_group, name="fixCode__code_group", curie=FIX_PROTOCOL.curie('code_group'),
                   model_uri=FIX_PROTOCOL.fixCode__code_group, domain=None, range=Optional[str])

slots.fixField__field_datatype = Slot(uri=FIX_PROTOCOL.field_datatype, name="fixField__field_datatype", curie=FIX_PROTOCOL.curie('field_datatype'),
                   model_uri=FIX_PROTOCOL.fixField__field_datatype, domain=None, range=Optional[Union[str, FixDatatypeId]],
                   pattern=re.compile(r'^fix_datatype:[A-Za-z][A-Za-z0-9_]*$'))

slots.fixField__field_code_set = Slot(uri=FIX_PROTOCOL.field_code_set, name="fixField__field_code_set", curie=FIX_PROTOCOL.curie('field_code_set'),
                   model_uri=FIX_PROTOCOL.fixField__field_code_set, domain=None, range=Optional[Union[str, FixCodeSetId]],
                   pattern=re.compile(r'^fix_code_set:[1-9][0-9]*$'))

slots.fixField__union_datatype = Slot(uri=FIX_PROTOCOL.union_datatype, name="fixField__union_datatype", curie=FIX_PROTOCOL.curie('union_datatype'),
                   model_uri=FIX_PROTOCOL.fixField__union_datatype, domain=None, range=Optional[Union[str, FixDatatypeId]],
                   pattern=re.compile(r'^fix_datatype:[A-Za-z][A-Za-z0-9_]*$'))

slots.fixField__length_field = Slot(uri=FIX_PROTOCOL.length_field, name="fixField__length_field", curie=FIX_PROTOCOL.curie('length_field'),
                   model_uri=FIX_PROTOCOL.fixField__length_field, domain=None, range=Optional[Union[str, FixFieldId]],
                   pattern=re.compile(r'^fix_field:[1-9][0-9]*$'))

slots.fixField__discriminator_field = Slot(uri=FIX_PROTOCOL.discriminator_field, name="fixField__discriminator_field", curie=FIX_PROTOCOL.curie('discriminator_field'),
                   model_uri=FIX_PROTOCOL.fixField__discriminator_field, domain=None, range=Optional[Union[str, FixFieldId]],
                   pattern=re.compile(r'^fix_field:[1-9][0-9]*$'))

slots.fixField__base_category = Slot(uri=FIX_PROTOCOL.base_category, name="fixField__base_category", curie=FIX_PROTOCOL.curie('base_category'),
                   model_uri=FIX_PROTOCOL.fixField__base_category, domain=None, range=Optional[Union[str, FixCategoryId]],
                   pattern=re.compile(r'^fix_category:[A-Za-z][A-Za-z0-9_]*$'))

slots.fixField__base_category_abbr_name = Slot(uri=FIX_PROTOCOL.base_category_abbr_name, name="fixField__base_category_abbr_name", curie=FIX_PROTOCOL.curie('base_category_abbr_name'),
                   model_uri=FIX_PROTOCOL.fixField__base_category_abbr_name, domain=None, range=Optional[Union[str, FixName]])

slots.fixMember__member_field = Slot(uri=FIX_PROTOCOL.member_field, name="fixMember__member_field", curie=FIX_PROTOCOL.curie('member_field'),
                   model_uri=FIX_PROTOCOL.fixMember__member_field, domain=None, range=Optional[Union[str, FixFieldId]],
                   pattern=re.compile(r'^fix_field:[1-9][0-9]*$'))

slots.fixMember__member_component = Slot(uri=FIX_PROTOCOL.member_component, name="fixMember__member_component", curie=FIX_PROTOCOL.curie('member_component'),
                   model_uri=FIX_PROTOCOL.fixMember__member_component, domain=None, range=Optional[Union[str, FixComponentId]],
                   pattern=re.compile(r'^fix_component:[1-9][0-9]*$'))

slots.fixMember__member_group = Slot(uri=FIX_PROTOCOL.member_group, name="fixMember__member_group", curie=FIX_PROTOCOL.curie('member_group'),
                   model_uri=FIX_PROTOCOL.fixMember__member_group, domain=None, range=Optional[Union[str, FixGroupId]],
                   pattern=re.compile(r'^fix_group:[1-9][0-9]*$'))

slots.fixMember__presence = Slot(uri=FIX_PROTOCOL.presence, name="fixMember__presence", curie=FIX_PROTOCOL.curie('presence'),
                   model_uri=FIX_PROTOCOL.fixMember__presence, domain=None, range=Optional[Union[str, "FixPresence"]])

slots.fixMember__fixml_inlined = Slot(uri=FIX_PROTOCOL.fixml_inlined, name="fixMember__fixml_inlined", curie=FIX_PROTOCOL.curie('fixml_inlined'),
                   model_uri=FIX_PROTOCOL.fixMember__fixml_inlined, domain=None, range=Optional[Union[bool, Bool]])

slots.fixGroup__num_in_group = Slot(uri=FIX_PROTOCOL.num_in_group, name="fixGroup__num_in_group", curie=FIX_PROTOCOL.curie('num_in_group'),
                   model_uri=FIX_PROTOCOL.fixGroup__num_in_group, domain=None, range=Union[dict, FixNumInGroup])

slots.fixNumInGroup__count_field = Slot(uri=FIX_PROTOCOL.count_field, name="fixNumInGroup__count_field", curie=FIX_PROTOCOL.curie('count_field'),
                   model_uri=FIX_PROTOCOL.fixNumInGroup__count_field, domain=None, range=Union[str, FixFieldId],
                   pattern=re.compile(r'^fix_field:[1-9][0-9]*$'))

slots.fixMessage__msg_type = Slot(uri=FIX_PROTOCOL.msg_type, name="fixMessage__msg_type", curie=FIX_PROTOCOL.curie('msg_type'),
                   model_uri=FIX_PROTOCOL.fixMessage__msg_type, domain=None, range=str,
                   pattern=re.compile(r'^[0-9A-Za-z]{1,2}$'))

slots.FixSection_id = Slot(uri=FIX_PROTOCOL.id, name="FixSection_id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.FixSection_id, domain=FixSection, range=Union[str, FixSectionId],
                   pattern=re.compile(r'^fix_section:[A-Za-z][A-Za-z0-9_]*$'))

slots.FixCategory_id = Slot(uri=FIX_PROTOCOL.id, name="FixCategory_id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.FixCategory_id, domain=FixCategory, range=Union[str, FixCategoryId],
                   pattern=re.compile(r'^fix_category:[A-Za-z][A-Za-z0-9_]*$'))

slots.FixDatatype_id = Slot(uri=FIX_PROTOCOL.id, name="FixDatatype_id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.FixDatatype_id, domain=FixDatatype, range=Union[str, FixDatatypeId],
                   pattern=re.compile(r'^fix_datatype:[A-Za-z][A-Za-z0-9_]*$'))

slots.FixCodeSet_id = Slot(uri=FIX_PROTOCOL.id, name="FixCodeSet_id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.FixCodeSet_id, domain=FixCodeSet, range=Union[str, FixCodeSetId],
                   pattern=re.compile(r'^fix_code_set:[1-9][0-9]*$'))

slots.FixCode_id = Slot(uri=FIX_PROTOCOL.id, name="FixCode_id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.FixCode_id, domain=FixCode, range=Union[str, FixCodeId],
                   pattern=re.compile(r'^fix_code:[1-9][0-9]*$'))

slots.FixField_id = Slot(uri=FIX_PROTOCOL.id, name="FixField_id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.FixField_id, domain=FixField, range=Union[str, FixFieldId],
                   pattern=re.compile(r'^fix_field:[1-9][0-9]*$'))

slots.FixComponent_id = Slot(uri=FIX_PROTOCOL.id, name="FixComponent_id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.FixComponent_id, domain=FixComponent, range=Union[str, FixComponentId],
                   pattern=re.compile(r'^fix_component:[1-9][0-9]*$'))

slots.FixGroup_id = Slot(uri=FIX_PROTOCOL.id, name="FixGroup_id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.FixGroup_id, domain=FixGroup, range=Union[str, FixGroupId],
                   pattern=re.compile(r'^fix_group:[1-9][0-9]*$'))

slots.FixGroup_fix_members = Slot(uri=FIX_PROTOCOL.fix_members, name="FixGroup_fix_members", curie=FIX_PROTOCOL.curie('fix_members'),
                   model_uri=FIX_PROTOCOL.FixGroup_fix_members, domain=FixGroup, range=Union[Union[dict, FixMember], list[Union[dict, FixMember]]])

slots.FixMessage_id = Slot(uri=FIX_PROTOCOL.id, name="FixMessage_id", curie=FIX_PROTOCOL.curie('id'),
                   model_uri=FIX_PROTOCOL.FixMessage_id, domain=FixMessage, range=Union[str, FixMessageId],
                   pattern=re.compile(r'^fix_message:[1-9][0-9]*$'))

slots.FixMessage_fix_members = Slot(uri=FIX_PROTOCOL.fix_members, name="FixMessage_fix_members", curie=FIX_PROTOCOL.curie('fix_members'),
                   model_uri=FIX_PROTOCOL.FixMessage_fix_members, domain=FixMessage, range=Union[Union[dict, FixMember], list[Union[dict, FixMember]]])
