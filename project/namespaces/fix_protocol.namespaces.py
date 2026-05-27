# Auto generated from fix_protocol.yaml by namespacegen.py version: 0.0.1
# Generation date: 2026-05-27T23:02:12
# Schema: fix-protocol
#
# id: https://w3id.org/lmodel/fix-protocol
# description: FIX Protocol - LinkML Schema
# license: Apache-2.0

from collections import defaultdict
from typing import Iterable, Dict, Tuple

from linkml_runtime.utils.curienamespace import CurieNamespace

GENE = 'gene'
DISEASE = 'disease'
CHEMICAL_SUBSTANCE = 'chemical substance'

SYMBOL = 'Approved_Symbol'


class IdentifierResolverException(RuntimeError):
    pass


class BiolinkNameSpace:
    """
    Map of BioLink Model registered URI Namespaces
    """

    _namespaces = [
        CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_'),
        CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/'),
        CurieNamespace('common_domain_model', 'https://w3id.org/lmodel/common-domain-model/'),
        CurieNamespace('dcterms', 'http://purl.org/dc/terms/'),
        CurieNamespace('example', 'http://www.example.org/rdf#'),
        CurieNamespace('fix_base', 'https://w3id.org/lmodel/fix-protocol/fix-base/'),
        CurieNamespace('fix_global_components', 'https://w3id.org/lmodel/fix-protocol/fix-global-components/'),
        CurieNamespace('fix_infrastructure', 'https://w3id.org/lmodel/fix-protocol/fix-infrastructure/'),
        CurieNamespace('fix_orchestra', 'https://w3id.org/lmodel/fix-orchestra/'),
        CurieNamespace('fix_post_trade', 'https://w3id.org/lmodel/fix-protocol/fix-post-trade/'),
        CurieNamespace('fix_pre_trade', 'https://w3id.org/lmodel/fix-protocol/fix-pre-trade/'),
        CurieNamespace('fix_protocol', 'https://w3id.org/lmodel/fix-protocol/'),
        CurieNamespace('fix_sbe', 'https://w3id.org/lmodel/fix-sbe/'),
        CurieNamespace('fix_trade', 'https://w3id.org/lmodel/fix-protocol/fix-trade/'),
        CurieNamespace('fixp', 'https://w3id.org/lmodel/fixp/'),
        CurieNamespace('fluxnova_bpm_platform', 'https://w3id.org/lmodel/fluxnova-bpm-platform/'),
        CurieNamespace('iso10383', 'https://www.iso.org/standard/61067.html#'),
        CurieNamespace('iso11404', 'https://www.iso.org/standard/39479.html#'),
        CurieNamespace('iso17442', 'https://www.iso.org/standard/78829.html#'),
        CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/'),
        CurieNamespace('iso3166', 'https://www.iso.org/iso-3166-country-codes.html#'),
        CurieNamespace('iso4217', 'https://www.iso.org/iso-4217-currency-codes.html#'),
        CurieNamespace('iso639', 'https://www.iso.org/iso-639-language-codes.html#'),
        CurieNamespace('linkml', 'https://w3id.org/linkml/'),
        CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/'),
        CurieNamespace('schema', 'http://schema.org/'),
        CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#'),
        CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#'),
    ]

    # class level dictionaries

    _prefix_map: Dict[str, CurieNamespace] = {}

    @classmethod
    def _get_prefix_map(cls):
        if not cls._prefix_map:
            for ns in cls._namespaces:
                # index by upper case for uniformity of search
                cls._prefix_map[ns.prefix.upper()] = ns
        return cls._prefix_map

    @classmethod
    def parse_curie(cls, curie: str) -> Tuple[CurieNamespace, str]:
        """
        Parse a candidate CURIE
        :param curie: candidate curie string
        :return: CURIE namespace and object_id
        """
        found = CurieNamespace("", ""), curie  # default value if not a CURIE or unknown XMLNS prefix
        if ':' in curie:
            part = curie.split(":")
            # Normalize retrieval with upper case of prefix for lookup
            prefix = part[0].upper()
            if prefix in cls._get_prefix_map():
                found = cls._prefix_map[prefix], part[1]
        return found

    @classmethod
    def parse_uri(cls, uri: str) -> Tuple[CurieNamespace,  str]:
        """
        Parse a candidate URI
        :param uri: candidate URI string
        :return: namespace and object_id
        """
        found = CurieNamespace("", ""), uri   # default value returned if unknown URI namespace

        # TODO: is there a more efficient lookup scheme here than a linear search of namespaces?
        for ns in cls._namespaces:
            base_uri = str(ns)
            if uri.startswith(base_uri):
                # simple minded deletion of base_uri to give the object_id
                object_id = uri.replace(base_uri, "")
                found = ns, object_id
                break
        return found

    @classmethod
    def parse_identifier(cls,  identifier: str) -> Tuple[CurieNamespace,  str]:

        # trivial case of a null identifier?
        if not identifier:
            return CurieNamespace("", ""), ""

        # check if this is a candidate URI...
        if identifier.lower().startswith("http"):
            # guess that perhaps it is, so try to parse it
            return cls.parse_uri(identifier)

        else:  # attempt to parse as a CURIE
            return cls.parse_curie(identifier)


def object_id(identifier, keep_version=False) -> str:
    """
    Returns the core object_id of a CURIE, with or without the version suffix.
    Note:  not designed to be used with a URI (will give an invalid outcome)
    :param identifier: candidate CURIE identifier for processing
    :param keep_version: True if the version string suffix is to be retained in the identifier
    :return:
    """
    # trivial case: null input value?
    if not identifier:
        return identifier

    if ':' in identifier:
        identifier = identifier.split(":")[1]

    if not keep_version and '.' in identifier:
        identifier = identifier.split(".")[0]

    return identifier


def fix_curies(identifiers, prefix=''):
    """
    Applies the specified XMLNS prefix to (an) identifier(s) known
    to be "raw" IDs as keys in a dictionary or elements in a list (or a simple string)
    :param identifiers:
    :param prefix:
    :return:
    """
    if not prefix:
        # return identifiers without modification
        # Caller may already consider them in curie format
        return identifiers

    if isinstance(identifiers, dict):
        curie_dict = defaultdict(dict)
        for key in identifiers.keys():
            curie_dict[prefix + ':' + object_id(key, keep_version=True)] = identifiers[key]
        return curie_dict

    # identifiers assumed to be just a single object identifier
    elif isinstance(identifiers, str):
        # single string to convert
        return prefix + ':' + object_id(identifiers, keep_version=True)

    elif isinstance(identifiers, Iterable):
        return [prefix + ':' + object_id(x, keep_version=True) for x in identifiers]

    else:
        raise RuntimeError("fix_curie() is not sure how to fix an instance of data type '", type(identifiers))


def curie(identifier) -> str:
    # Ignore enpty strings
    if not identifier:
        return ""
    else:
        namespace: CurieNamespace
        identifier_object_id: str
        namespace, identifier_object_id = BiolinkNameSpace.parse_identifier(identifier)
        return namespace.curie(identifier_object_id)

