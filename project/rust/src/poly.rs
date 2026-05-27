#![allow(non_camel_case_types)]

use crate::*;
use crate::poly_containers::*;


pub trait FIXIntroduction   {

    fn published_version<'a>(&'a self) -> Option<&'a str>;
    // fn published_version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_published_version(&mut self, value: Option<&'a str>);

    fn published_date<'a>(&'a self) -> Option<&'a crate::NaiveDate>;
    // fn published_date_mut(&mut self) -> &mut Option<&'a crate::NaiveDate>;
    // fn set_published_date(&mut self, value: Option<&'a NaiveDate>);

    fn publisher<'a>(&'a self) -> Option<&'a str>;
    // fn publisher_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_publisher(&mut self, value: Option<&'a str>);

    fn preface<'a>(&'a self) -> Option<&'a str>;
    // fn preface_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_preface(&mut self, value: Option<&'a str>);

    fn introduction_text<'a>(&'a self) -> Option<&'a str>;
    // fn introduction_text_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_introduction_text(&mut self, value: Option<&'a str>);

    fn utc_leap_seconds_note<'a>(&'a self) -> Option<&'a str>;
    // fn utc_leap_seconds_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_utc_leap_seconds_note(&mut self, value: Option<&'a str>);

    fn about_fpl<'a>(&'a self) -> Option<&'a crate::FIXProtocolLimited>;
    // fn about_fpl_mut(&mut self) -> &mut Option<&'a crate::FIXProtocolLimited>;
    // fn set_about_fpl<E>(&mut self, value: Option<E>) where E: Into<FIXProtocolLimited>;

    fn standards<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FIXFamilyStandard>>;
    // fn standards_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::FIXFamilyStandard>>;
    // fn set_standards<E>(&mut self, value: Option<&Vec<E>>) where E: Into<FIXFamilyStandard>;

    fn extension_packs<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ExtensionPack>>;
    // fn extension_packs_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ExtensionPack>>;
    // fn set_extension_packs<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ExtensionPack>;

    fn datatypes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FIXDatatype>>;
    // fn datatypes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::FIXDatatype>>;
    // fn set_datatypes<E>(&mut self, value: Option<&Vec<E>>) where E: Into<FIXDatatype>;

    fn business_areas<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::BusinessArea>>;
    // fn business_areas_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::BusinessArea>>;
    // fn set_business_areas<E>(&mut self, value: Option<&Vec<E>>) where E: Into<BusinessArea>;

    fn global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::GlobalComponent>>;
    // fn global_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::GlobalComponent>>;
    // fn set_global_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<GlobalComponent>;

    fn udf_ranges<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::UDFTagRange>>;
    // fn udf_ranges_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::UDFTagRange>>;
    // fn set_udf_ranges<E>(&mut self, value: Option<&Vec<E>>) where E: Into<UDFTagRange>;

    fn product_coverage<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProductCoverage>>;
    // fn product_coverage_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ProductCoverage>>;
    // fn set_product_coverage(&mut self, value: Option<&Vec<ProductCoverage>>);


}

impl FIXIntroduction for crate::FIXIntroduction {
        fn published_version<'a>(&'a self) -> Option<&'a str> {
        return self.published_version.as_deref();
    }
        fn published_date<'a>(&'a self) -> Option<&'a crate::NaiveDate> {
        return self.published_date.as_ref();
    }
        fn publisher<'a>(&'a self) -> Option<&'a str> {
        return self.publisher.as_deref();
    }
        fn preface<'a>(&'a self) -> Option<&'a str> {
        return self.preface.as_deref();
    }
        fn introduction_text<'a>(&'a self) -> Option<&'a str> {
        return self.introduction_text.as_deref();
    }
        fn utc_leap_seconds_note<'a>(&'a self) -> Option<&'a str> {
        return self.utc_leap_seconds_note.as_deref();
    }
        fn about_fpl<'a>(&'a self) -> Option<&'a crate::FIXProtocolLimited> {
        return self.about_fpl.as_ref();
    }
        fn standards<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FIXFamilyStandard>> {
        return self.standards.as_ref();
    }
        fn extension_packs<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ExtensionPack>> {
        return self.extension_packs.as_ref();
    }
        fn datatypes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FIXDatatype>> {
        return self.datatypes.as_ref();
    }
        fn business_areas<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::BusinessArea>> {
        return self.business_areas.as_ref();
    }
        fn global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::GlobalComponent>> {
        return self.global_components.as_ref();
    }
        fn udf_ranges<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::UDFTagRange>> {
        return self.udf_ranges.as_ref();
    }
        fn product_coverage<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ProductCoverage>> {
        return self.product_coverage.as_ref();
    }
}


pub trait FIXProtocolLimited   {

    fn brand_name<'a>(&'a self) -> Option<&'a str>;
    // fn brand_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_brand_name(&mut self, value: Option<&'a str>);

    fn legal_name<'a>(&'a self) -> Option<&'a str>;
    // fn legal_name_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_legal_name(&mut self, value: Option<&'a str>);

    fn website<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn website_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_website(&mut self, value: Option<&'a uri>);

    fn member_firms_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn member_firms_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_member_firms_url(&mut self, value: Option<&'a uri>);

    fn working_groups_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn working_groups_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_working_groups_url(&mut self, value: Option<&'a uri>);

    fn committees_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn committees_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_committees_url(&mut self, value: Option<&'a uri>);

    fn member_types<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FPLMemberType>>;
    // fn member_types_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::FPLMemberType>>;
    // fn set_member_types(&mut self, value: Option<&Vec<FPLMemberType>>);

    fn governance_bodies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FPLCommitteeRole>>;
    // fn governance_bodies_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::FPLCommitteeRole>>;
    // fn set_governance_bodies(&mut self, value: Option<&Vec<FPLCommitteeRole>>);

    fn product_committees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FPLProductGroup>>;
    // fn product_committees_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::FPLProductGroup>>;
    // fn set_product_committees(&mut self, value: Option<&Vec<FPLProductGroup>>);

    fn regional_committees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FPLRegion>>;
    // fn regional_committees_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::FPLRegion>>;
    // fn set_regional_committees(&mut self, value: Option<&Vec<FPLRegion>>);


}

impl FIXProtocolLimited for crate::FIXProtocolLimited {
        fn brand_name<'a>(&'a self) -> Option<&'a str> {
        return self.brand_name.as_deref();
    }
        fn legal_name<'a>(&'a self) -> Option<&'a str> {
        return self.legal_name.as_deref();
    }
        fn website<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.website.as_ref();
    }
        fn member_firms_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.member_firms_url.as_ref();
    }
        fn working_groups_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.working_groups_url.as_ref();
    }
        fn committees_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.committees_url.as_ref();
    }
        fn member_types<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FPLMemberType>> {
        return self.member_types.as_ref();
    }
        fn governance_bodies<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FPLCommitteeRole>> {
        return self.governance_bodies.as_ref();
    }
        fn product_committees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FPLProductGroup>> {
        return self.product_committees.as_ref();
    }
        fn regional_committees<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::FPLRegion>> {
        return self.regional_committees.as_ref();
    }
}


pub trait FIXFamilyStandard   {

    fn id<'a>(&'a self) -> &'a str;
    // fn id_mut(&mut self) -> &mut &'a str;
    // fn set_id(&mut self, value: String);

    fn name<'a>(&'a self) -> &'a str;
    // fn name_mut(&mut self) -> &mut &'a str;
    // fn set_name(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn acronym<'a>(&'a self) -> Option<&'a str>;
    // fn acronym_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_acronym(&mut self, value: Option<&'a str>);

    fn see_also<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::uri>>;
    // fn see_also_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::uri>>;
    // fn set_see_also(&mut self, value: Option<&Vec<uri>>);

    fn layer<'a>(&'a self) -> &'a crate::StandardLayer;
    // fn layer_mut(&mut self) -> &mut &'a crate::StandardLayer;
    // fn set_layer(&mut self, value: StandardLayer);

    fn version<'a>(&'a self) -> Option<&'a str>;
    // fn version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_version(&mut self, value: Option<&'a str>);

    fn session_profile<'a>(&'a self) -> Option<&'a crate::SessionProtocolName>;
    // fn session_profile_mut(&mut self) -> &mut Option<&'a crate::SessionProtocolName>;
    // fn set_session_profile(&mut self, value: Option<&'a SessionProtocolName>);

    fn encoding_name<'a>(&'a self) -> Option<&'a crate::StandardEncodingName>;
    // fn encoding_name_mut(&mut self) -> &mut Option<&'a crate::StandardEncodingName>;
    // fn set_encoding_name(&mut self, value: Option<&'a StandardEncodingName>);


}

impl FIXFamilyStandard for crate::FIXFamilyStandard {
        fn id<'a>(&'a self) -> &'a str {
        return &self.id[..];
    }
        fn name<'a>(&'a self) -> &'a str {
        return &self.name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn acronym<'a>(&'a self) -> Option<&'a str> {
        return self.acronym.as_deref();
    }
        fn see_also<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::uri>> {
        return self.see_also.as_ref();
    }
        fn layer<'a>(&'a self) -> &'a crate::StandardLayer {
        return &self.layer;
    }
        fn version<'a>(&'a self) -> Option<&'a str> {
        return self.version.as_deref();
    }
        fn session_profile<'a>(&'a self) -> Option<&'a crate::SessionProtocolName> {
        return self.session_profile.as_ref();
    }
        fn encoding_name<'a>(&'a self) -> Option<&'a crate::StandardEncodingName> {
        return self.encoding_name.as_ref();
    }
}


pub trait ExtensionPack   {

    fn number(&self) -> isize;
    // fn number_mut(&mut self) -> &mut isize;
    // fn set_number(&mut self, value: isize);

    fn title<'a>(&'a self) -> &'a str;
    // fn title_mut(&mut self) -> &mut &'a str;
    // fn set_title(&mut self, value: String);

    fn size<'a>(&'a self) -> Option<&'a crate::ExtensionPackSize>;
    // fn size_mut(&mut self) -> &mut Option<&'a crate::ExtensionPackSize>;
    // fn set_size(&mut self, value: Option<&'a ExtensionPackSize>);

    fn enhancement_summary<'a>(&'a self) -> Option<&'a str>;
    // fn enhancement_summary_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_enhancement_summary(&mut self, value: Option<&'a str>);

    fn applies_to_session_layer_only(&self) -> Option<bool>;
    // fn applies_to_session_layer_only_mut(&mut self) -> &mut Option<bool>;
    // fn set_applies_to_session_layer_only(&mut self, value: Option<bool>);

    fn applies_to_fixml_only(&self) -> Option<bool>;
    // fn applies_to_fixml_only_mut(&mut self) -> &mut Option<bool>;
    // fn set_applies_to_fixml_only(&mut self, value: Option<bool>);


}

impl ExtensionPack for crate::ExtensionPack {
        fn number(&self) -> isize {
        return self.number;
    }
        fn title<'a>(&'a self) -> &'a str {
        return &self.title[..];
    }
        fn size<'a>(&'a self) -> Option<&'a crate::ExtensionPackSize> {
        return self.size.as_ref();
    }
        fn enhancement_summary<'a>(&'a self) -> Option<&'a str> {
        return self.enhancement_summary.as_deref();
    }
        fn applies_to_session_layer_only(&self) -> Option<bool> {
        return self.applies_to_session_layer_only;
    }
        fn applies_to_fixml_only(&self) -> Option<bool> {
        return self.applies_to_fixml_only;
    }
}


pub trait FIXDatatype   {

    fn datatype_name<'a>(&'a self) -> &'a crate::FIXDatatypeName;
    // fn datatype_name_mut(&mut self) -> &mut &'a crate::FIXDatatypeName;
    // fn set_datatype_name(&mut self, value: FIXDatatypeName);

    fn definition<'a>(&'a self) -> &'a str;
    // fn definition_mut(&mut self) -> &mut &'a str;
    // fn set_definition(&mut self, value: String);

    fn value_space<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ISO11404ValueSpace>>;
    // fn value_space_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ISO11404ValueSpace>>;
    // fn set_value_space(&mut self, value: Option<&Vec<ISO11404ValueSpace>>);

    fn value_space_notes<'a>(&'a self) -> Option<&'a str>;
    // fn value_space_notes_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_value_space_notes(&mut self, value: Option<&'a str>);

    fn deprecated_for_new_designs(&self) -> Option<bool>;
    // fn deprecated_for_new_designs_mut(&mut self) -> &mut Option<bool>;
    // fn set_deprecated_for_new_designs(&mut self, value: Option<bool>);

    fn external_code_set<'a>(&'a self) -> Option<&'a str>;
    // fn external_code_set_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_external_code_set(&mut self, value: Option<&'a str>);

    fn time_unit<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TimePrecision>>;
    // fn time_unit_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TimePrecision>>;
    // fn set_time_unit(&mut self, value: Option<&Vec<TimePrecision>>);

    fn radix(&self) -> Option<isize>;
    // fn radix_mut(&mut self) -> &mut Option<isize>;
    // fn set_radix(&mut self, value: Option<isize>);

    fn repertoire<'a>(&'a self) -> Option<&'a str>;
    // fn repertoire_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_repertoire(&mut self, value: Option<&'a str>);

    fn index_lower_bound(&self) -> Option<isize>;
    // fn index_lower_bound_mut(&mut self) -> &mut Option<isize>;
    // fn set_index_lower_bound(&mut self, value: Option<isize>);

    fn index_upper_bound(&self) -> Option<isize>;
    // fn index_upper_bound_mut(&mut self) -> &mut Option<isize>;
    // fn set_index_upper_bound(&mut self, value: Option<isize>);

    fn minimum_value(&self) -> Option<isize>;
    // fn minimum_value_mut(&mut self) -> &mut Option<isize>;
    // fn set_minimum_value(&mut self, value: Option<isize>);

    fn maximum_value(&self) -> Option<isize>;
    // fn maximum_value_mut(&mut self) -> &mut Option<isize>;
    // fn set_maximum_value(&mut self, value: Option<isize>);

    fn footnote_numbers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, isize>>;
    // fn footnote_numbers_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, isize>>;
    // fn set_footnote_numbers(&mut self, value: Option<&Vec<isize>>);


}

impl FIXDatatype for crate::FIXDatatype {
        fn datatype_name<'a>(&'a self) -> &'a crate::FIXDatatypeName {
        return &self.datatype_name;
    }
        fn definition<'a>(&'a self) -> &'a str {
        return &self.definition[..];
    }
        fn value_space<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ISO11404ValueSpace>> {
        return self.value_space.as_ref();
    }
        fn value_space_notes<'a>(&'a self) -> Option<&'a str> {
        return self.value_space_notes.as_deref();
    }
        fn deprecated_for_new_designs(&self) -> Option<bool> {
        return self.deprecated_for_new_designs;
    }
        fn external_code_set<'a>(&'a self) -> Option<&'a str> {
        return self.external_code_set.as_deref();
    }
        fn time_unit<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TimePrecision>> {
        return self.time_unit.as_ref();
    }
        fn radix(&self) -> Option<isize> {
        return self.radix;
    }
        fn repertoire<'a>(&'a self) -> Option<&'a str> {
        return self.repertoire.as_deref();
    }
        fn index_lower_bound(&self) -> Option<isize> {
        return self.index_lower_bound;
    }
        fn index_upper_bound(&self) -> Option<isize> {
        return self.index_upper_bound;
    }
        fn minimum_value(&self) -> Option<isize> {
        return self.minimum_value;
    }
        fn maximum_value(&self) -> Option<isize> {
        return self.maximum_value;
    }
        fn footnote_numbers<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, isize>> {
        return self.footnote_numbers.as_ref();
    }
}


pub trait BusinessArea   {

    fn area<'a>(&'a self) -> &'a crate::BusinessAreaEnum;
    // fn area_mut(&mut self) -> &mut &'a crate::BusinessAreaEnum;
    // fn set_area(&mut self, value: BusinessAreaEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn categories<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MessageCategory>>;
    // fn categories_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::MessageCategory>>;
    // fn set_categories<E>(&mut self, value: Option<&Vec<E>>) where E: Into<MessageCategory>;


}

impl BusinessArea for crate::BusinessArea {
        fn area<'a>(&'a self) -> &'a crate::BusinessAreaEnum {
        return &self.area;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn categories<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MessageCategory>> {
        return self.categories.as_ref();
    }
}


pub trait MessageCategory   {

    fn category<'a>(&'a self) -> &'a crate::MessageCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::MessageCategoryEnum;
    // fn set_category(&mut self, value: MessageCategoryEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn business_area<'a>(&'a self) -> &'a crate::BusinessAreaEnum;
    // fn business_area_mut(&mut self) -> &mut &'a crate::BusinessAreaEnum;
    // fn set_business_area(&mut self, value: BusinessAreaEnum);

    fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Message>>;
    // fn messages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Message>>;
    // fn set_messages<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Message>;


}

impl MessageCategory for crate::MessageCategory {
        fn category<'a>(&'a self) -> &'a crate::MessageCategoryEnum {
        return &self.category;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn business_area<'a>(&'a self) -> &'a crate::BusinessAreaEnum {
        return &self.business_area;
    }
        fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Message>> {
        return self.messages.as_ref();
    }
}


pub trait Field   {

    fn tag(&self) -> isize;
    // fn tag_mut(&mut self) -> &mut isize;
    // fn set_tag(&mut self, value: isize);

    fn field_name<'a>(&'a self) -> &'a str;
    // fn field_name_mut(&mut self) -> &mut &'a str;
    // fn set_field_name(&mut self, value: String);

    fn datatype<'a>(&'a self) -> &'a crate::FIXDatatypeName;
    // fn datatype_mut(&mut self) -> &mut &'a crate::FIXDatatypeName;
    // fn set_datatype(&mut self, value: FIXDatatypeName);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn requirement<'a>(&'a self) -> Option<&'a crate::FieldRequirement>;
    // fn requirement_mut(&mut self) -> &mut Option<&'a crate::FieldRequirement>;
    // fn set_requirement(&mut self, value: Option<&'a FieldRequirement>);

    fn is_user_defined(&self) -> Option<bool>;
    // fn is_user_defined_mut(&mut self) -> &mut Option<bool>;
    // fn set_is_user_defined(&mut self, value: Option<bool>);


}

impl Field for crate::Field {
        fn tag(&self) -> isize {
        return self.tag;
    }
        fn field_name<'a>(&'a self) -> &'a str {
        return &self.field_name[..];
    }
        fn datatype<'a>(&'a self) -> &'a crate::FIXDatatypeName {
        return &self.datatype;
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn requirement<'a>(&'a self) -> Option<&'a crate::FieldRequirement> {
        return self.requirement.as_ref();
    }
        fn is_user_defined(&self) -> Option<bool> {
        return self.is_user_defined;
    }
}


pub trait Component   {

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn scope<'a>(&'a self) -> &'a crate::ComponentScope;
    // fn scope_mut(&mut self) -> &mut &'a crate::ComponentScope;
    // fn set_scope(&mut self, value: ComponentScope);

    fn is_repeating_group(&self) -> Option<bool>;
    // fn is_repeating_group_mut(&mut self) -> &mut Option<bool>;
    // fn set_is_repeating_group(&mut self, value: Option<bool>);

    fn fields<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Field>>;
    // fn fields_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Field>>;
    // fn set_fields<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Field>;

    fn nested_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn nested_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_nested_components<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;


}

impl Component for crate::Component {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn scope<'a>(&'a self) -> &'a crate::ComponentScope {
        return &self.scope;
    }
        fn is_repeating_group(&self) -> Option<bool> {
        return self.is_repeating_group;
    }
        fn fields<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Field>> {
        return self.fields.as_ref();
    }
        fn nested_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.nested_components.as_ref();
    }
}
impl Component for crate::GlobalComponent {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn scope<'a>(&'a self) -> &'a crate::ComponentScope {
        return &self.scope;
    }
        fn is_repeating_group(&self) -> Option<bool> {
        return self.is_repeating_group;
    }
        fn fields<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Field>> {
        return self.fields.as_ref();
    }
        fn nested_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.nested_components.as_ref();
    }
}
impl Component for crate::CommonComponent {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn scope<'a>(&'a self) -> &'a crate::ComponentScope {
        return &self.scope;
    }
        fn is_repeating_group(&self) -> Option<bool> {
        return self.is_repeating_group;
    }
        fn fields<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Field>> {
        return self.fields.as_ref();
    }
        fn nested_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.nested_components.as_ref();
    }
}
impl Component for crate::SpecificComponent {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn scope<'a>(&'a self) -> &'a crate::ComponentScope {
        return &self.scope;
    }
        fn is_repeating_group(&self) -> Option<bool> {
        return self.is_repeating_group;
    }
        fn fields<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Field>> {
        return self.fields.as_ref();
    }
        fn nested_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.nested_components.as_ref();
    }
}

impl Component for crate::ComponentOrSubtype {
        fn component_name<'a>(&'a self) -> &'a str {
        match self {
                ComponentOrSubtype::GlobalComponent(val) => val.component_name(),
                ComponentOrSubtype::CommonComponent(val) => val.component_name(),
                ComponentOrSubtype::SpecificComponent(val) => val.component_name(),

        }
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        match self {
                ComponentOrSubtype::GlobalComponent(val) => val.description(),
                ComponentOrSubtype::CommonComponent(val) => val.description(),
                ComponentOrSubtype::SpecificComponent(val) => val.description(),

        }
    }
        fn scope<'a>(&'a self) -> &'a crate::ComponentScope {
        match self {
                ComponentOrSubtype::GlobalComponent(val) => val.scope(),
                ComponentOrSubtype::CommonComponent(val) => val.scope(),
                ComponentOrSubtype::SpecificComponent(val) => val.scope(),

        }
    }
        fn is_repeating_group(&self) -> Option<bool> {
        match self {
                ComponentOrSubtype::GlobalComponent(val) => val.is_repeating_group(),
                ComponentOrSubtype::CommonComponent(val) => val.is_repeating_group(),
                ComponentOrSubtype::SpecificComponent(val) => val.is_repeating_group(),

        }
    }
        fn fields<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Field>> {
        match self {
                ComponentOrSubtype::GlobalComponent(val) => val.fields().map(|x| x.to_any()),
                ComponentOrSubtype::CommonComponent(val) => val.fields().map(|x| x.to_any()),
                ComponentOrSubtype::SpecificComponent(val) => val.fields().map(|x| x.to_any()),

        }
    }
        fn nested_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        match self {
                ComponentOrSubtype::GlobalComponent(val) => val.nested_components().map(|x| x.to_any()),
                ComponentOrSubtype::CommonComponent(val) => val.nested_components().map(|x| x.to_any()),
                ComponentOrSubtype::SpecificComponent(val) => val.nested_components().map(|x| x.to_any()),

        }
    }
}

pub trait GlobalComponent : Component   {

    fn component_group<'a>(&'a self) -> &'a crate::ComponentGroup;
    // fn component_group_mut(&mut self) -> &mut &'a crate::ComponentGroup;
    // fn set_component_group(&mut self, value: ComponentGroup);

    fn applies_to_instrument(&self) -> Option<bool>;
    // fn applies_to_instrument_mut(&mut self) -> &mut Option<bool>;
    // fn set_applies_to_instrument(&mut self, value: Option<bool>);

    fn applies_to_leg(&self) -> Option<bool>;
    // fn applies_to_leg_mut(&mut self) -> &mut Option<bool>;
    // fn set_applies_to_leg(&mut self, value: Option<bool>);

    fn applies_to_underlying(&self) -> Option<bool>;
    // fn applies_to_underlying_mut(&mut self) -> &mut Option<bool>;
    // fn set_applies_to_underlying(&mut self, value: Option<bool>);

    fn conceptually_identical_to<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn conceptually_identical_to_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_conceptually_identical_to(&mut self, value: Option<&Vec<String>>);

    fn gc_id(&self) -> Option<isize>;
    // fn gc_id_mut(&mut self) -> &mut Option<isize>;
    // fn set_gc_id(&mut self, value: Option<isize>);

    fn gc_referenced_in<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::GlobalComponentBusinessAreaEnum>>;
    // fn gc_referenced_in_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::GlobalComponentBusinessAreaEnum>>;
    // fn set_gc_referenced_in(&mut self, value: Option<&Vec<GlobalComponentBusinessAreaEnum>>);


}

impl GlobalComponent for crate::GlobalComponent {
        fn component_group<'a>(&'a self) -> &'a crate::ComponentGroup {
        return &self.component_group;
    }
        fn applies_to_instrument(&self) -> Option<bool> {
        return self.applies_to_instrument;
    }
        fn applies_to_leg(&self) -> Option<bool> {
        return self.applies_to_leg;
    }
        fn applies_to_underlying(&self) -> Option<bool> {
        return self.applies_to_underlying;
    }
        fn conceptually_identical_to<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.conceptually_identical_to.as_ref();
    }
        fn gc_id(&self) -> Option<isize> {
        return self.gc_id;
    }
        fn gc_referenced_in<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::GlobalComponentBusinessAreaEnum>> {
        return self.gc_referenced_in.as_ref();
    }
}


pub trait CommonComponent : Component   {

    fn business_area<'a>(&'a self) -> &'a crate::BusinessAreaEnum;
    // fn business_area_mut(&mut self) -> &mut &'a crate::BusinessAreaEnum;
    // fn set_business_area(&mut self, value: BusinessAreaEnum);


}

impl CommonComponent for crate::CommonComponent {
        fn business_area<'a>(&'a self) -> &'a crate::BusinessAreaEnum {
        return &self.business_area;
    }
}


pub trait SpecificComponent : Component   {

    fn business_area<'a>(&'a self) -> &'a crate::BusinessAreaEnum;
    // fn business_area_mut(&mut self) -> &mut &'a crate::BusinessAreaEnum;
    // fn set_business_area(&mut self, value: BusinessAreaEnum);

    fn category<'a>(&'a self) -> &'a crate::MessageCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::MessageCategoryEnum;
    // fn set_category(&mut self, value: MessageCategoryEnum);


}

impl SpecificComponent for crate::SpecificComponent {
        fn business_area<'a>(&'a self) -> &'a crate::BusinessAreaEnum {
        return &self.business_area;
    }
        fn category<'a>(&'a self) -> &'a crate::MessageCategoryEnum {
        return &self.category;
    }
}


pub trait Message   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn category<'a>(&'a self) -> Option<&'a crate::MessageCategoryEnum>;
    // fn category_mut(&mut self) -> &mut Option<&'a crate::MessageCategoryEnum>;
    // fn set_category(&mut self, value: Option<&'a MessageCategoryEnum>);

    fn fields<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Field>>;
    // fn fields_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::Field>>;
    // fn set_fields<E>(&mut self, value: Option<&Vec<E>>) where E: Into<Field>;

    fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_components<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;


}

impl Message for crate::Message {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn category<'a>(&'a self) -> Option<&'a crate::MessageCategoryEnum> {
        return self.category.as_ref();
    }
        fn fields<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::Field>> {
        return self.fields.as_ref();
    }
        fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.components.as_ref();
    }
}


pub trait UDFTagRange   {

    fn range_id<'a>(&'a self) -> &'a str;
    // fn range_id_mut(&mut self) -> &mut &'a str;
    // fn set_range_id(&mut self, value: String);

    fn low_tag(&self) -> isize;
    // fn low_tag_mut(&mut self) -> &mut isize;
    // fn set_low_tag(&mut self, value: isize);

    fn high_tag(&self) -> Option<isize>;
    // fn high_tag_mut(&mut self) -> &mut Option<isize>;
    // fn set_high_tag(&mut self, value: Option<isize>);

    fn usage<'a>(&'a self) -> &'a crate::UDFTagRangeUsage;
    // fn usage_mut(&mut self) -> &mut &'a crate::UDFTagRangeUsage;
    // fn set_usage(&mut self, value: UDFTagRangeUsage);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn requires_registration(&self) -> Option<bool>;
    // fn requires_registration_mut(&mut self) -> &mut Option<bool>;
    // fn set_requires_registration(&mut self, value: Option<bool>);


}

impl UDFTagRange for crate::UDFTagRange {
        fn range_id<'a>(&'a self) -> &'a str {
        return &self.range_id[..];
    }
        fn low_tag(&self) -> isize {
        return self.low_tag;
    }
        fn high_tag(&self) -> Option<isize> {
        return self.high_tag;
    }
        fn usage<'a>(&'a self) -> &'a crate::UDFTagRangeUsage {
        return &self.usage;
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn requires_registration(&self) -> Option<bool> {
        return self.requires_registration;
    }
}


pub trait PreTradeBusinessArea   {

    fn area<'a>(&'a self) -> &'a crate::BusinessAreaEnum;
    // fn area_mut(&mut self) -> &mut &'a crate::BusinessAreaEnum;
    // fn set_area(&mut self, value: BusinessAreaEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn published_version<'a>(&'a self) -> Option<&'a str>;
    // fn published_version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_published_version(&mut self, value: Option<&'a str>);

    fn publisher<'a>(&'a self) -> Option<&'a str>;
    // fn publisher_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_publisher(&mut self, value: Option<&'a str>);

    fn introduction<'a>(&'a self) -> Option<&'a str>;
    // fn introduction_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_introduction(&mut self, value: Option<&'a str>);

    fn diagram_conventions<'a>(&'a self) -> Option<&'a str>;
    // fn diagram_conventions_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_diagram_conventions(&mut self, value: Option<&'a str>);

    fn messages_overview_note<'a>(&'a self) -> Option<&'a str>;
    // fn messages_overview_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_messages_overview_note(&mut self, value: Option<&'a str>);

    fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeMessageEntry>>;
    // fn messages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PreTradeMessageEntry>>;
    // fn set_messages<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PreTradeMessageEntry>;

    fn components_overview_note<'a>(&'a self) -> Option<&'a str>;
    // fn components_overview_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_components_overview_note(&mut self, value: Option<&'a str>);

    fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeComponentEntry>>;
    // fn components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PreTradeComponentEntry>>;
    // fn set_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PreTradeComponentEntry>;

    fn common_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeCommonComponentName>>;
    // fn common_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PreTradeCommonComponentName>>;
    // fn set_common_components(&mut self, value: Option<&Vec<PreTradeCommonComponentName>>);

    fn common_component_details<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CommonComponentDetail>>;
    // fn common_component_details_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::CommonComponentDetail>>;
    // fn set_common_component_details<E>(&mut self, value: Option<&Vec<E>>) where E: Into<CommonComponentDetail>;

    fn footnotes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ComponentTableFootnote>>;
    // fn footnotes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ComponentTableFootnote>>;
    // fn set_footnotes<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ComponentTableFootnote>;

    fn category_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeCategorySection>>;
    // fn category_sections_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PreTradeCategorySection>>;
    // fn set_category_sections<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PreTradeCategorySection>;

    fn referenced_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn referenced_global_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_referenced_global_components<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;


}

impl PreTradeBusinessArea for crate::PreTradeBusinessArea {
        fn area<'a>(&'a self) -> &'a crate::BusinessAreaEnum {
        return &self.area;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn published_version<'a>(&'a self) -> Option<&'a str> {
        return self.published_version.as_deref();
    }
        fn publisher<'a>(&'a self) -> Option<&'a str> {
        return self.publisher.as_deref();
    }
        fn introduction<'a>(&'a self) -> Option<&'a str> {
        return self.introduction.as_deref();
    }
        fn diagram_conventions<'a>(&'a self) -> Option<&'a str> {
        return self.diagram_conventions.as_deref();
    }
        fn messages_overview_note<'a>(&'a self) -> Option<&'a str> {
        return self.messages_overview_note.as_deref();
    }
        fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeMessageEntry>> {
        return self.messages.as_ref();
    }
        fn components_overview_note<'a>(&'a self) -> Option<&'a str> {
        return self.components_overview_note.as_deref();
    }
        fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeComponentEntry>> {
        return self.components.as_ref();
    }
        fn common_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeCommonComponentName>> {
        return self.common_components.as_ref();
    }
        fn common_component_details<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CommonComponentDetail>> {
        return self.common_component_details.as_ref();
    }
        fn footnotes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ComponentTableFootnote>> {
        return self.footnotes.as_ref();
    }
        fn category_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeCategorySection>> {
        return self.category_sections.as_ref();
    }
        fn referenced_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.referenced_global_components.as_ref();
    }
}


pub trait PreTradeMessageEntry   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn category<'a>(&'a self) -> &'a crate::PreTradeCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::PreTradeCategoryEnum;
    // fn set_category(&mut self, value: PreTradeCategoryEnum);


}

impl PreTradeMessageEntry for crate::PreTradeMessageEntry {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn category<'a>(&'a self) -> &'a crate::PreTradeCategoryEnum {
        return &self.category;
    }
}


pub trait PreTradeComponentEntry   {

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn repetition<'a>(&'a self) -> &'a crate::ComponentRepetition;
    // fn repetition_mut(&mut self) -> &mut &'a crate::ComponentRepetition;
    // fn set_repetition(&mut self, value: ComponentRepetition);

    fn category<'a>(&'a self) -> &'a str;
    // fn category_mut(&mut self) -> &mut &'a str;
    // fn set_category(&mut self, value: String);

    fn is_common(&self) -> Option<bool>;
    // fn is_common_mut(&mut self) -> &mut Option<bool>;
    // fn set_is_common(&mut self, value: Option<bool>);

    fn footnote_number(&self) -> Option<isize>;
    // fn footnote_number_mut(&mut self) -> &mut Option<isize>;
    // fn set_footnote_number(&mut self, value: Option<isize>);


}

impl PreTradeComponentEntry for crate::PreTradeComponentEntry {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn repetition<'a>(&'a self) -> &'a crate::ComponentRepetition {
        return &self.repetition;
    }
        fn category<'a>(&'a self) -> &'a str {
        return &self.category[..];
    }
        fn is_common(&self) -> Option<bool> {
        return self.is_common;
    }
        fn footnote_number(&self) -> Option<isize> {
        return self.footnote_number;
    }
}


pub trait ComponentTableFootnote   {

    fn footnote_number(&self) -> isize;
    // fn footnote_number_mut(&mut self) -> &mut isize;
    // fn set_footnote_number(&mut self, value: isize);

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn introduced_in<'a>(&'a self) -> &'a str;
    // fn introduced_in_mut(&mut self) -> &mut &'a str;
    // fn set_introduced_in(&mut self, value: String);

    fn sole_category<'a>(&'a self) -> &'a crate::PreTradeCategoryEnum;
    // fn sole_category_mut(&mut self) -> &mut &'a crate::PreTradeCategoryEnum;
    // fn set_sole_category(&mut self, value: PreTradeCategoryEnum);

    fn text<'a>(&'a self) -> Option<&'a str>;
    // fn text_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_text(&mut self, value: Option<&'a str>);


}

impl ComponentTableFootnote for crate::ComponentTableFootnote {
        fn footnote_number(&self) -> isize {
        return self.footnote_number;
    }
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn introduced_in<'a>(&'a self) -> &'a str {
        return &self.introduced_in[..];
    }
        fn sole_category<'a>(&'a self) -> &'a crate::PreTradeCategoryEnum {
        return &self.sole_category;
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        return self.text.as_deref();
    }
}


pub trait PreTradeCategorySection   {

    fn category<'a>(&'a self) -> &'a crate::PreTradeCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::PreTradeCategoryEnum;
    // fn set_category(&mut self, value: PreTradeCategoryEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn quote_models<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::QuoteModelEnum>>;
    // fn quote_models_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::QuoteModelEnum>>;
    // fn set_quote_models(&mut self, value: Option<&Vec<QuoteModelEnum>>);

    fn message_groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MessageGroup>>;
    // fn message_groups_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::MessageGroup>>;
    // fn set_message_groups<E>(&mut self, value: Option<&Vec<E>>) where E: Into<MessageGroup>;

    fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeMessageDetail>>;
    // fn messages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PreTradeMessageDetail>>;
    // fn set_messages<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PreTradeMessageDetail>;

    fn category_components_note<'a>(&'a self) -> Option<&'a str>;
    // fn category_components_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_category_components_note(&mut self, value: Option<&'a str>);

    fn category_specific_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeComponentDetail>>;
    // fn category_specific_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PreTradeComponentDetail>>;
    // fn set_category_specific_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PreTradeComponentDetail>;


}

impl PreTradeCategorySection for crate::PreTradeCategorySection {
        fn category<'a>(&'a self) -> &'a crate::PreTradeCategoryEnum {
        return &self.category;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn quote_models<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::QuoteModelEnum>> {
        return self.quote_models.as_ref();
    }
        fn message_groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::MessageGroup>> {
        return self.message_groups.as_ref();
    }
        fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeMessageDetail>> {
        return self.messages.as_ref();
    }
        fn category_components_note<'a>(&'a self) -> Option<&'a str> {
        return self.category_components_note.as_deref();
    }
        fn category_specific_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeComponentDetail>> {
        return self.category_specific_components.as_ref();
    }
}


pub trait PreTradeMessageDetail   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_layout_url(&mut self, value: Option<&'a uri>);

    fn pre_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeLayoutRow>>;
    // fn pre_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PreTradeLayoutRow>>;
    // fn set_pre_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PreTradeLayoutRow>;


}

impl PreTradeMessageDetail for crate::PreTradeMessageDetail {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.layout_url.as_ref();
    }
        fn pre_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeLayoutRow>> {
        return self.pre_layout_rows.as_ref();
    }
}


pub trait PreTradeComponentDetail   {

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition>;
    // fn repetition_mut(&mut self) -> &mut Option<&'a crate::ComponentRepetition>;
    // fn set_repetition(&mut self, value: Option<&'a ComponentRepetition>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_layout_url(&mut self, value: Option<&'a uri>);

    fn pre_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeLayoutRow>>;
    // fn pre_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PreTradeLayoutRow>>;
    // fn set_pre_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PreTradeLayoutRow>;


}

impl PreTradeComponentDetail for crate::PreTradeComponentDetail {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition> {
        return self.repetition.as_ref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.layout_url.as_ref();
    }
        fn pre_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeLayoutRow>> {
        return self.pre_layout_rows.as_ref();
    }
}


pub trait MessageGroup   {

    fn group_title<'a>(&'a self) -> &'a str;
    // fn group_title_mut(&mut self) -> &mut &'a str;
    // fn set_group_title(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PreTradeMessageDetail>;
    // fn messages_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::PreTradeMessageDetail>;
    // fn set_messages<E>(&mut self, value: &Vec<E>) where E: Into<PreTradeMessageDetail>;


}

impl MessageGroup for crate::MessageGroup {
        fn group_title<'a>(&'a self) -> &'a str {
        return &self.group_title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PreTradeMessageDetail> {
        return &self.messages;
    }
}


pub trait CommonComponentDetail   {

    fn component_name<'a>(&'a self) -> &'a crate::PreTradeCommonComponentName;
    // fn component_name_mut(&mut self) -> &mut &'a crate::PreTradeCommonComponentName;
    // fn set_component_name(&mut self, value: PreTradeCommonComponentName);

    fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition>;
    // fn repetition_mut(&mut self) -> &mut Option<&'a crate::ComponentRepetition>;
    // fn set_repetition(&mut self, value: Option<&'a ComponentRepetition>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_layout_url(&mut self, value: Option<&'a uri>);

    fn pre_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeLayoutRow>>;
    // fn pre_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PreTradeLayoutRow>>;
    // fn set_pre_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PreTradeLayoutRow>;


}

impl CommonComponentDetail for crate::CommonComponentDetail {
        fn component_name<'a>(&'a self) -> &'a crate::PreTradeCommonComponentName {
        return &self.component_name;
    }
        fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition> {
        return self.repetition.as_ref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.layout_url.as_ref();
    }
        fn pre_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PreTradeLayoutRow>> {
        return self.pre_layout_rows.as_ref();
    }
}


pub trait PreTradeLayoutRow   {

    fn pre_layout_kind<'a>(&'a self) -> &'a crate::PreTradeLayoutRowKindEnum;
    // fn pre_layout_kind_mut(&mut self) -> &mut &'a crate::PreTradeLayoutRowKindEnum;
    // fn set_pre_layout_kind(&mut self, value: PreTradeLayoutRowKindEnum);

    fn pre_layout_field_tag(&self) -> Option<isize>;
    // fn pre_layout_field_tag_mut(&mut self) -> &mut Option<isize>;
    // fn set_pre_layout_field_tag(&mut self, value: Option<isize>);

    fn pre_layout_element_name<'a>(&'a self) -> &'a str;
    // fn pre_layout_element_name_mut(&mut self) -> &mut &'a str;
    // fn set_pre_layout_element_name(&mut self, value: String);

    fn pre_layout_required(&self) -> Option<bool>;
    // fn pre_layout_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_pre_layout_required(&mut self, value: Option<bool>);

    fn pre_layout_description<'a>(&'a self) -> Option<&'a str>;
    // fn pre_layout_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_pre_layout_description(&mut self, value: Option<&'a str>);

    fn pre_layout_nested(&self) -> Option<bool>;
    // fn pre_layout_nested_mut(&mut self) -> &mut Option<bool>;
    // fn set_pre_layout_nested(&mut self, value: Option<bool>);


}

impl PreTradeLayoutRow for crate::PreTradeLayoutRow {
        fn pre_layout_kind<'a>(&'a self) -> &'a crate::PreTradeLayoutRowKindEnum {
        return &self.pre_layout_kind;
    }
        fn pre_layout_field_tag(&self) -> Option<isize> {
        return self.pre_layout_field_tag;
    }
        fn pre_layout_element_name<'a>(&'a self) -> &'a str {
        return &self.pre_layout_element_name[..];
    }
        fn pre_layout_required(&self) -> Option<bool> {
        return self.pre_layout_required;
    }
        fn pre_layout_description<'a>(&'a self) -> Option<&'a str> {
        return self.pre_layout_description.as_deref();
    }
        fn pre_layout_nested(&self) -> Option<bool> {
        return self.pre_layout_nested;
    }
}


pub trait TradeBusinessArea   {

    fn trade_area<'a>(&'a self) -> &'a crate::BusinessAreaEnum;
    // fn trade_area_mut(&mut self) -> &mut &'a crate::BusinessAreaEnum;
    // fn set_trade_area(&mut self, value: BusinessAreaEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn published_version<'a>(&'a self) -> Option<&'a str>;
    // fn published_version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_published_version(&mut self, value: Option<&'a str>);

    fn publisher<'a>(&'a self) -> Option<&'a str>;
    // fn publisher_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_publisher(&mut self, value: Option<&'a str>);

    fn trade_introduction<'a>(&'a self) -> Option<&'a str>;
    // fn trade_introduction_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_trade_introduction(&mut self, value: Option<&'a str>);

    fn trade_diagram_conventions<'a>(&'a self) -> Option<&'a str>;
    // fn trade_diagram_conventions_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_trade_diagram_conventions(&mut self, value: Option<&'a str>);

    fn trade_message_diagram_template_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn trade_message_diagram_template_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_trade_message_diagram_template_url(&mut self, value: Option<&'a uri>);

    fn trade_messages_overview_note<'a>(&'a self) -> Option<&'a str>;
    // fn trade_messages_overview_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_trade_messages_overview_note(&mut self, value: Option<&'a str>);

    fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeMessageEntry>>;
    // fn messages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeMessageEntry>>;
    // fn set_messages<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeMessageEntry>;

    fn trade_components_overview_note<'a>(&'a self) -> Option<&'a str>;
    // fn trade_components_overview_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_trade_components_overview_note(&mut self, value: Option<&'a str>);

    fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeComponentEntry>>;
    // fn components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeComponentEntry>>;
    // fn set_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeComponentEntry>;

    fn trade_common_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCommonComponentName>>;
    // fn trade_common_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeCommonComponentName>>;
    // fn set_trade_common_components(&mut self, value: Option<&Vec<TradeCommonComponentName>>);

    fn trade_common_component_details<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCommonComponentDetail>>;
    // fn trade_common_component_details_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeCommonComponentDetail>>;
    // fn set_trade_common_component_details<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeCommonComponentDetail>;

    fn trade_footnotes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeComponentTableFootnote>>;
    // fn trade_footnotes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeComponentTableFootnote>>;
    // fn set_trade_footnotes<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeComponentTableFootnote>;

    fn trade_category_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCategorySection>>;
    // fn trade_category_sections_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeCategorySection>>;
    // fn set_trade_category_sections<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeCategorySection>;

    fn referenced_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn referenced_global_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_referenced_global_components<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;


}

impl TradeBusinessArea for crate::TradeBusinessArea {
        fn trade_area<'a>(&'a self) -> &'a crate::BusinessAreaEnum {
        return &self.trade_area;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn published_version<'a>(&'a self) -> Option<&'a str> {
        return self.published_version.as_deref();
    }
        fn publisher<'a>(&'a self) -> Option<&'a str> {
        return self.publisher.as_deref();
    }
        fn trade_introduction<'a>(&'a self) -> Option<&'a str> {
        return self.trade_introduction.as_deref();
    }
        fn trade_diagram_conventions<'a>(&'a self) -> Option<&'a str> {
        return self.trade_diagram_conventions.as_deref();
    }
        fn trade_message_diagram_template_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.trade_message_diagram_template_url.as_ref();
    }
        fn trade_messages_overview_note<'a>(&'a self) -> Option<&'a str> {
        return self.trade_messages_overview_note.as_deref();
    }
        fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeMessageEntry>> {
        return self.messages.as_ref();
    }
        fn trade_components_overview_note<'a>(&'a self) -> Option<&'a str> {
        return self.trade_components_overview_note.as_deref();
    }
        fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeComponentEntry>> {
        return self.components.as_ref();
    }
        fn trade_common_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCommonComponentName>> {
        return self.trade_common_components.as_ref();
    }
        fn trade_common_component_details<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCommonComponentDetail>> {
        return self.trade_common_component_details.as_ref();
    }
        fn trade_footnotes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeComponentTableFootnote>> {
        return self.trade_footnotes.as_ref();
    }
        fn trade_category_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCategorySection>> {
        return self.trade_category_sections.as_ref();
    }
        fn referenced_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.referenced_global_components.as_ref();
    }
}


pub trait TradeMessageEntry   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn category<'a>(&'a self) -> &'a crate::TradeCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::TradeCategoryEnum;
    // fn set_category(&mut self, value: TradeCategoryEnum);


}

impl TradeMessageEntry for crate::TradeMessageEntry {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn category<'a>(&'a self) -> &'a crate::TradeCategoryEnum {
        return &self.category;
    }
}


pub trait TradeComponentEntry   {

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn trade_repetition<'a>(&'a self) -> &'a crate::TradeComponentRepetition;
    // fn trade_repetition_mut(&mut self) -> &mut &'a crate::TradeComponentRepetition;
    // fn set_trade_repetition(&mut self, value: TradeComponentRepetition);

    fn category<'a>(&'a self) -> &'a str;
    // fn category_mut(&mut self) -> &mut &'a str;
    // fn set_category(&mut self, value: String);

    fn trade_is_common(&self) -> Option<bool>;
    // fn trade_is_common_mut(&mut self) -> &mut Option<bool>;
    // fn set_trade_is_common(&mut self, value: Option<bool>);

    fn trade_footnote_number(&self) -> Option<isize>;
    // fn trade_footnote_number_mut(&mut self) -> &mut Option<isize>;
    // fn set_trade_footnote_number(&mut self, value: Option<isize>);


}

impl TradeComponentEntry for crate::TradeComponentEntry {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn trade_repetition<'a>(&'a self) -> &'a crate::TradeComponentRepetition {
        return &self.trade_repetition;
    }
        fn category<'a>(&'a self) -> &'a str {
        return &self.category[..];
    }
        fn trade_is_common(&self) -> Option<bool> {
        return self.trade_is_common;
    }
        fn trade_footnote_number(&self) -> Option<isize> {
        return self.trade_footnote_number;
    }
}


pub trait TradeComponentTableFootnote   {

    fn trade_footnote_number(&self) -> isize;
    // fn trade_footnote_number_mut(&mut self) -> &mut isize;
    // fn set_trade_footnote_number(&mut self, value: isize);

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn trade_introduced_in<'a>(&'a self) -> &'a str;
    // fn trade_introduced_in_mut(&mut self) -> &mut &'a str;
    // fn set_trade_introduced_in(&mut self, value: String);

    fn trade_sole_category<'a>(&'a self) -> &'a crate::TradeCategoryEnum;
    // fn trade_sole_category_mut(&mut self) -> &mut &'a crate::TradeCategoryEnum;
    // fn set_trade_sole_category(&mut self, value: TradeCategoryEnum);

    fn trade_footnote_text<'a>(&'a self) -> Option<&'a str>;
    // fn trade_footnote_text_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_trade_footnote_text(&mut self, value: Option<&'a str>);


}

impl TradeComponentTableFootnote for crate::TradeComponentTableFootnote {
        fn trade_footnote_number(&self) -> isize {
        return self.trade_footnote_number;
    }
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn trade_introduced_in<'a>(&'a self) -> &'a str {
        return &self.trade_introduced_in[..];
    }
        fn trade_sole_category<'a>(&'a self) -> &'a crate::TradeCategoryEnum {
        return &self.trade_sole_category;
    }
        fn trade_footnote_text<'a>(&'a self) -> Option<&'a str> {
        return self.trade_footnote_text.as_deref();
    }
}


pub trait TradeCategorySection   {

    fn category<'a>(&'a self) -> &'a crate::TradeCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::TradeCategoryEnum;
    // fn set_category(&mut self, value: TradeCategoryEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn trade_category_background<'a>(&'a self) -> Option<&'a str>;
    // fn trade_category_background_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_trade_category_background(&mut self, value: Option<&'a str>);

    fn trade_message_groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeMessageGroup>>;
    // fn trade_message_groups_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeMessageGroup>>;
    // fn set_trade_message_groups<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeMessageGroup>;

    fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeMessageDetail>>;
    // fn messages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeMessageDetail>>;
    // fn set_messages<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeMessageDetail>;

    fn trade_category_components_note<'a>(&'a self) -> Option<&'a str>;
    // fn trade_category_components_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_trade_category_components_note(&mut self, value: Option<&'a str>);

    fn trade_category_specific_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeComponentDetail>>;
    // fn trade_category_specific_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeComponentDetail>>;
    // fn set_trade_category_specific_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeComponentDetail>;

    fn trade_fragmentation_entries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeFragmentationEntry>>;
    // fn trade_fragmentation_entries_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeFragmentationEntry>>;
    // fn set_trade_fragmentation_entries<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeFragmentationEntry>;


}

impl TradeCategorySection for crate::TradeCategorySection {
        fn category<'a>(&'a self) -> &'a crate::TradeCategoryEnum {
        return &self.category;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn trade_category_background<'a>(&'a self) -> Option<&'a str> {
        return self.trade_category_background.as_deref();
    }
        fn trade_message_groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeMessageGroup>> {
        return self.trade_message_groups.as_ref();
    }
        fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeMessageDetail>> {
        return self.messages.as_ref();
    }
        fn trade_category_components_note<'a>(&'a self) -> Option<&'a str> {
        return self.trade_category_components_note.as_deref();
    }
        fn trade_category_specific_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeComponentDetail>> {
        return self.trade_category_specific_components.as_ref();
    }
        fn trade_fragmentation_entries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeFragmentationEntry>> {
        return self.trade_fragmentation_entries.as_ref();
    }
}


pub trait TradeMessageDetail   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn trade_layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn trade_layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_trade_layout_url(&mut self, value: Option<&'a uri>);

    fn trade_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeLayoutRow>>;
    // fn trade_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeLayoutRow>>;
    // fn set_trade_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeLayoutRow>;


}

impl TradeMessageDetail for crate::TradeMessageDetail {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn trade_layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.trade_layout_url.as_ref();
    }
        fn trade_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeLayoutRow>> {
        return self.trade_layout_rows.as_ref();
    }
}


pub trait TradeComponentDetail   {

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn trade_repetition<'a>(&'a self) -> Option<&'a crate::TradeComponentRepetition>;
    // fn trade_repetition_mut(&mut self) -> &mut Option<&'a crate::TradeComponentRepetition>;
    // fn set_trade_repetition(&mut self, value: Option<&'a TradeComponentRepetition>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn trade_layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn trade_layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_trade_layout_url(&mut self, value: Option<&'a uri>);

    fn trade_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeLayoutRow>>;
    // fn trade_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeLayoutRow>>;
    // fn set_trade_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeLayoutRow>;


}

impl TradeComponentDetail for crate::TradeComponentDetail {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn trade_repetition<'a>(&'a self) -> Option<&'a crate::TradeComponentRepetition> {
        return self.trade_repetition.as_ref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn trade_layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.trade_layout_url.as_ref();
    }
        fn trade_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeLayoutRow>> {
        return self.trade_layout_rows.as_ref();
    }
}


pub trait TradeMessageGroup   {

    fn trade_group_title<'a>(&'a self) -> &'a str;
    // fn trade_group_title_mut(&mut self) -> &mut &'a str;
    // fn set_trade_group_title(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::TradeMessageDetail>;
    // fn messages_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::TradeMessageDetail>;
    // fn set_messages<E>(&mut self, value: &Vec<E>) where E: Into<TradeMessageDetail>;

    fn trade_ord_status_precedence_entries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeOrdStatusPrecedenceEntry>>;
    // fn trade_ord_status_precedence_entries_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeOrdStatusPrecedenceEntry>>;
    // fn set_trade_ord_status_precedence_entries<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeOrdStatusPrecedenceEntry>;


}

impl TradeMessageGroup for crate::TradeMessageGroup {
        fn trade_group_title<'a>(&'a self) -> &'a str {
        return &self.trade_group_title[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::TradeMessageDetail> {
        return &self.messages;
    }
        fn trade_ord_status_precedence_entries<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeOrdStatusPrecedenceEntry>> {
        return self.trade_ord_status_precedence_entries.as_ref();
    }
}


pub trait TradeCommonComponentDetail   {

    fn component_name<'a>(&'a self) -> &'a crate::TradeCommonComponentName;
    // fn component_name_mut(&mut self) -> &mut &'a crate::TradeCommonComponentName;
    // fn set_component_name(&mut self, value: TradeCommonComponentName);

    fn trade_repetition<'a>(&'a self) -> Option<&'a crate::TradeComponentRepetition>;
    // fn trade_repetition_mut(&mut self) -> &mut Option<&'a crate::TradeComponentRepetition>;
    // fn set_trade_repetition(&mut self, value: Option<&'a TradeComponentRepetition>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn trade_layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn trade_layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_trade_layout_url(&mut self, value: Option<&'a uri>);

    fn trade_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeLayoutRow>>;
    // fn trade_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeLayoutRow>>;
    // fn set_trade_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeLayoutRow>;


}

impl TradeCommonComponentDetail for crate::TradeCommonComponentDetail {
        fn component_name<'a>(&'a self) -> &'a crate::TradeCommonComponentName {
        return &self.component_name;
    }
        fn trade_repetition<'a>(&'a self) -> Option<&'a crate::TradeComponentRepetition> {
        return self.trade_repetition.as_ref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn trade_layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.trade_layout_url.as_ref();
    }
        fn trade_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeLayoutRow>> {
        return self.trade_layout_rows.as_ref();
    }
}


pub trait TradeLayoutRow   {

    fn trade_layout_kind<'a>(&'a self) -> &'a crate::TradeLayoutRowKindEnum;
    // fn trade_layout_kind_mut(&mut self) -> &mut &'a crate::TradeLayoutRowKindEnum;
    // fn set_trade_layout_kind(&mut self, value: TradeLayoutRowKindEnum);

    fn trade_layout_field_tag(&self) -> Option<isize>;
    // fn trade_layout_field_tag_mut(&mut self) -> &mut Option<isize>;
    // fn set_trade_layout_field_tag(&mut self, value: Option<isize>);

    fn trade_layout_element_name<'a>(&'a self) -> &'a str;
    // fn trade_layout_element_name_mut(&mut self) -> &mut &'a str;
    // fn set_trade_layout_element_name(&mut self, value: String);

    fn trade_layout_required(&self) -> Option<bool>;
    // fn trade_layout_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_trade_layout_required(&mut self, value: Option<bool>);

    fn trade_layout_description<'a>(&'a self) -> Option<&'a str>;
    // fn trade_layout_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_trade_layout_description(&mut self, value: Option<&'a str>);

    fn trade_layout_nested(&self) -> Option<bool>;
    // fn trade_layout_nested_mut(&mut self) -> &mut Option<bool>;
    // fn set_trade_layout_nested(&mut self, value: Option<bool>);


}

impl TradeLayoutRow for crate::TradeLayoutRow {
        fn trade_layout_kind<'a>(&'a self) -> &'a crate::TradeLayoutRowKindEnum {
        return &self.trade_layout_kind;
    }
        fn trade_layout_field_tag(&self) -> Option<isize> {
        return self.trade_layout_field_tag;
    }
        fn trade_layout_element_name<'a>(&'a self) -> &'a str {
        return &self.trade_layout_element_name[..];
    }
        fn trade_layout_required(&self) -> Option<bool> {
        return self.trade_layout_required;
    }
        fn trade_layout_description<'a>(&'a self) -> Option<&'a str> {
        return self.trade_layout_description.as_deref();
    }
        fn trade_layout_nested(&self) -> Option<bool> {
        return self.trade_layout_nested;
    }
}


pub trait TradeOrdStatusPrecedenceEntry   {

    fn trade_ord_status_precedence(&self) -> isize;
    // fn trade_ord_status_precedence_mut(&mut self) -> &mut isize;
    // fn set_trade_ord_status_precedence(&mut self, value: isize);

    fn trade_ord_status_label<'a>(&'a self) -> &'a str;
    // fn trade_ord_status_label_mut(&mut self) -> &mut &'a str;
    // fn set_trade_ord_status_label(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);


}

impl TradeOrdStatusPrecedenceEntry for crate::TradeOrdStatusPrecedenceEntry {
        fn trade_ord_status_precedence(&self) -> isize {
        return self.trade_ord_status_precedence;
    }
        fn trade_ord_status_label<'a>(&'a self) -> &'a str {
        return &self.trade_ord_status_label[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}


pub trait TradeFragmentationEntry   {

    fn trade_fragmentation_message<'a>(&'a self) -> &'a str;
    // fn trade_fragmentation_message_mut(&mut self) -> &mut &'a str;
    // fn set_trade_fragmentation_message(&mut self, value: String);

    fn trade_fragmentation_total_entries_field<'a>(&'a self) -> &'a str;
    // fn trade_fragmentation_total_entries_field_mut(&mut self) -> &mut &'a str;
    // fn set_trade_fragmentation_total_entries_field(&mut self, value: String);

    fn trade_fragmentation_repeating_group<'a>(&'a self) -> &'a str;
    // fn trade_fragmentation_repeating_group_mut(&mut self) -> &mut &'a str;
    // fn set_trade_fragmentation_repeating_group(&mut self, value: String);


}

impl TradeFragmentationEntry for crate::TradeFragmentationEntry {
        fn trade_fragmentation_message<'a>(&'a self) -> &'a str {
        return &self.trade_fragmentation_message[..];
    }
        fn trade_fragmentation_total_entries_field<'a>(&'a self) -> &'a str {
        return &self.trade_fragmentation_total_entries_field[..];
    }
        fn trade_fragmentation_repeating_group<'a>(&'a self) -> &'a str {
        return &self.trade_fragmentation_repeating_group[..];
    }
}


pub trait TradeAppendix   {

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn published_version<'a>(&'a self) -> Option<&'a str>;
    // fn published_version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_published_version(&mut self, value: Option<&'a str>);

    fn publisher<'a>(&'a self) -> Option<&'a str>;
    // fn publisher_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_publisher(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn trade_appendix_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeAppendixSection>>;
    // fn trade_appendix_sections_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeAppendixSection>>;
    // fn set_trade_appendix_sections<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeAppendixSection>;


}

impl TradeAppendix for crate::TradeAppendix {
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn published_version<'a>(&'a self) -> Option<&'a str> {
        return self.published_version.as_deref();
    }
        fn publisher<'a>(&'a self) -> Option<&'a str> {
        return self.publisher.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn trade_appendix_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeAppendixSection>> {
        return self.trade_appendix_sections.as_ref();
    }
}


pub trait TradeAppendixSection   {

    fn trade_appendix_category<'a>(&'a self) -> &'a str;
    // fn trade_appendix_category_mut(&mut self) -> &mut &'a str;
    // fn set_trade_appendix_category(&mut self, value: String);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeMessageDetail>>;
    // fn messages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeMessageDetail>>;
    // fn set_messages<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeMessageDetail>;

    fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_components<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;


}

impl TradeAppendixSection for crate::TradeAppendixSection {
        fn trade_appendix_category<'a>(&'a self) -> &'a str {
        return &self.trade_appendix_category[..];
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeMessageDetail>> {
        return self.messages.as_ref();
    }
        fn components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.components.as_ref();
    }
}


pub trait PostTradeBusinessArea   {

    fn area<'a>(&'a self) -> &'a crate::BusinessAreaEnum;
    // fn area_mut(&mut self) -> &mut &'a crate::BusinessAreaEnum;
    // fn set_area(&mut self, value: BusinessAreaEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn published_version<'a>(&'a self) -> Option<&'a str>;
    // fn published_version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_published_version(&mut self, value: Option<&'a str>);

    fn publisher<'a>(&'a self) -> Option<&'a str>;
    // fn publisher_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_publisher(&mut self, value: Option<&'a str>);

    fn post_introduction<'a>(&'a self) -> Option<&'a str>;
    // fn post_introduction_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_post_introduction(&mut self, value: Option<&'a str>);

    fn diagram_conventions<'a>(&'a self) -> Option<&'a str>;
    // fn diagram_conventions_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_diagram_conventions(&mut self, value: Option<&'a str>);

    fn post_common_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeCommonComponentName>>;
    // fn post_common_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeCommonComponentName>>;
    // fn set_post_common_components(&mut self, value: Option<&Vec<PostTradeCommonComponentName>>);

    fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PostTradeMessageEntry>;
    // fn messages_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::PostTradeMessageEntry>;
    // fn set_messages<E>(&mut self, value: &Vec<E>) where E: Into<PostTradeMessageEntry>;

    fn components<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PostTradeComponentEntry>;
    // fn components_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::PostTradeComponentEntry>;
    // fn set_components<E>(&mut self, value: &Vec<E>) where E: Into<PostTradeComponentEntry>;

    fn post_footnotes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeComponentTableFootnote>>;
    // fn post_footnotes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeComponentTableFootnote>>;
    // fn set_post_footnotes<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PostTradeComponentTableFootnote>;

    fn post_category_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeCategorySection>>;
    // fn post_category_sections_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeCategorySection>>;
    // fn set_post_category_sections<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PostTradeCategorySection>;

    fn post_common_component_details<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeCommonComponentDetail>>;
    // fn post_common_component_details_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeCommonComponentDetail>>;
    // fn set_post_common_component_details<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PostTradeCommonComponentDetail>;

    fn messages_overview_note<'a>(&'a self) -> Option<&'a str>;
    // fn messages_overview_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_messages_overview_note(&mut self, value: Option<&'a str>);

    fn components_overview_note<'a>(&'a self) -> Option<&'a str>;
    // fn components_overview_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_components_overview_note(&mut self, value: Option<&'a str>);

    fn referenced_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn referenced_global_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_referenced_global_components<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;


}

impl PostTradeBusinessArea for crate::PostTradeBusinessArea {
        fn area<'a>(&'a self) -> &'a crate::BusinessAreaEnum {
        return &self.area;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn published_version<'a>(&'a self) -> Option<&'a str> {
        return self.published_version.as_deref();
    }
        fn publisher<'a>(&'a self) -> Option<&'a str> {
        return self.publisher.as_deref();
    }
        fn post_introduction<'a>(&'a self) -> Option<&'a str> {
        return self.post_introduction.as_deref();
    }
        fn diagram_conventions<'a>(&'a self) -> Option<&'a str> {
        return self.diagram_conventions.as_deref();
    }
        fn post_common_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeCommonComponentName>> {
        return self.post_common_components.as_ref();
    }
        fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PostTradeMessageEntry> {
        return &self.messages;
    }
        fn components<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PostTradeComponentEntry> {
        return &self.components;
    }
        fn post_footnotes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeComponentTableFootnote>> {
        return self.post_footnotes.as_ref();
    }
        fn post_category_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeCategorySection>> {
        return self.post_category_sections.as_ref();
    }
        fn post_common_component_details<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeCommonComponentDetail>> {
        return self.post_common_component_details.as_ref();
    }
        fn messages_overview_note<'a>(&'a self) -> Option<&'a str> {
        return self.messages_overview_note.as_deref();
    }
        fn components_overview_note<'a>(&'a self) -> Option<&'a str> {
        return self.components_overview_note.as_deref();
    }
        fn referenced_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.referenced_global_components.as_ref();
    }
}


pub trait PostTradeMessageEntry   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn category<'a>(&'a self) -> &'a crate::PostTradeCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::PostTradeCategoryEnum;
    // fn set_category(&mut self, value: PostTradeCategoryEnum);


}

impl PostTradeMessageEntry for crate::PostTradeMessageEntry {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn category<'a>(&'a self) -> &'a crate::PostTradeCategoryEnum {
        return &self.category;
    }
}


pub trait PostTradeComponentEntry   {

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn repetition<'a>(&'a self) -> &'a crate::ComponentRepetition;
    // fn repetition_mut(&mut self) -> &mut &'a crate::ComponentRepetition;
    // fn set_repetition(&mut self, value: ComponentRepetition);

    fn category<'a>(&'a self) -> &'a str;
    // fn category_mut(&mut self) -> &mut &'a str;
    // fn set_category(&mut self, value: String);

    fn is_common(&self) -> Option<bool>;
    // fn is_common_mut(&mut self) -> &mut Option<bool>;
    // fn set_is_common(&mut self, value: Option<bool>);

    fn footnote_number(&self) -> Option<isize>;
    // fn footnote_number_mut(&mut self) -> &mut Option<isize>;
    // fn set_footnote_number(&mut self, value: Option<isize>);


}

impl PostTradeComponentEntry for crate::PostTradeComponentEntry {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn repetition<'a>(&'a self) -> &'a crate::ComponentRepetition {
        return &self.repetition;
    }
        fn category<'a>(&'a self) -> &'a str {
        return &self.category[..];
    }
        fn is_common(&self) -> Option<bool> {
        return self.is_common;
    }
        fn footnote_number(&self) -> Option<isize> {
        return self.footnote_number;
    }
}


pub trait PostTradeComponentTableFootnote   {

    fn footnote_number(&self) -> isize;
    // fn footnote_number_mut(&mut self) -> &mut isize;
    // fn set_footnote_number(&mut self, value: isize);

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn introduced_in<'a>(&'a self) -> &'a str;
    // fn introduced_in_mut(&mut self) -> &mut &'a str;
    // fn set_introduced_in(&mut self, value: String);

    fn post_sole_category<'a>(&'a self) -> &'a crate::PostTradeCategoryEnum;
    // fn post_sole_category_mut(&mut self) -> &mut &'a crate::PostTradeCategoryEnum;
    // fn set_post_sole_category(&mut self, value: PostTradeCategoryEnum);

    fn text<'a>(&'a self) -> Option<&'a str>;
    // fn text_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_text(&mut self, value: Option<&'a str>);


}

impl PostTradeComponentTableFootnote for crate::PostTradeComponentTableFootnote {
        fn footnote_number(&self) -> isize {
        return self.footnote_number;
    }
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn introduced_in<'a>(&'a self) -> &'a str {
        return &self.introduced_in[..];
    }
        fn post_sole_category<'a>(&'a self) -> &'a crate::PostTradeCategoryEnum {
        return &self.post_sole_category;
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        return self.text.as_deref();
    }
}


pub trait PostTradeCategorySection   {

    fn category<'a>(&'a self) -> &'a crate::PostTradeCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::PostTradeCategoryEnum;
    // fn set_category(&mut self, value: PostTradeCategoryEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn category_components_note<'a>(&'a self) -> Option<&'a str>;
    // fn category_components_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_category_components_note(&mut self, value: Option<&'a str>);

    fn post_message_groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeMessageGroup>>;
    // fn post_message_groups_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeMessageGroup>>;
    // fn set_post_message_groups<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PostTradeMessageGroup>;

    fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeMessageDetail>>;
    // fn messages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeMessageDetail>>;
    // fn set_messages<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PostTradeMessageDetail>;

    fn post_category_specific_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeComponentDetail>>;
    // fn post_category_specific_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeComponentDetail>>;
    // fn set_post_category_specific_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PostTradeComponentDetail>;

    fn allocation_scenarios<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AllocationScenarioEnum>>;
    // fn allocation_scenarios_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AllocationScenarioEnum>>;
    // fn set_allocation_scenarios(&mut self, value: Option<&Vec<AllocationScenarioEnum>>);

    fn allocation_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AllocationRoleEnum>>;
    // fn allocation_roles_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AllocationRoleEnum>>;
    // fn set_allocation_roles(&mut self, value: Option<&Vec<AllocationRoleEnum>>);

    fn post_trade_allocation_pricing_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeAllocationPricingMethodEnum>>;
    // fn post_trade_allocation_pricing_methods_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeAllocationPricingMethodEnum>>;
    // fn set_post_trade_allocation_pricing_methods(&mut self, value: Option<&Vec<PostTradeAllocationPricingMethodEnum>>);

    fn allocation_status_descriptions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AllocationStatusDescription>>;
    // fn allocation_status_descriptions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AllocationStatusDescription>>;
    // fn set_allocation_status_descriptions<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AllocationStatusDescription>;

    fn fragmentation_field_map<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AllocationFragmentationFieldMap>>;
    // fn fragmentation_field_map_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::AllocationFragmentationFieldMap>>;
    // fn set_fragmentation_field_map<E>(&mut self, value: Option<&Vec<E>>) where E: Into<AllocationFragmentationFieldMap>;

    fn trade_capture_report_usages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCaptureReportUsage>>;
    // fn trade_capture_report_usages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeCaptureReportUsage>>;
    // fn set_trade_capture_report_usages<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeCaptureReportUsage>;

    fn trade_capture_report_identifier_rules<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCaptureReportIdentifierRule>>;
    // fn trade_capture_report_identifier_rules_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::TradeCaptureReportIdentifierRule>>;
    // fn set_trade_capture_report_identifier_rules<E>(&mut self, value: Option<&Vec<E>>) where E: Into<TradeCaptureReportIdentifierRule>;

    fn registration_status_descriptions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RegistrationStatusDescription>>;
    // fn registration_status_descriptions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::RegistrationStatusDescription>>;
    // fn set_registration_status_descriptions<E>(&mut self, value: Option<&Vec<E>>) where E: Into<RegistrationStatusDescription>;

    fn clearing_services_for_position_management<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ClearingServiceForPositionManagementEnum>>;
    // fn clearing_services_for_position_management_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ClearingServiceForPositionManagementEnum>>;
    // fn set_clearing_services_for_position_management(&mut self, value: Option<&Vec<ClearingServiceForPositionManagementEnum>>);

    fn clearing_services_for_post_trade_processing<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ClearingServicePostTradeProcessingFormat>>;
    // fn clearing_services_for_post_trade_processing_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ClearingServicePostTradeProcessingFormat>>;
    // fn set_clearing_services_for_post_trade_processing<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ClearingServicePostTradeProcessingFormat>;

    fn collateral_management_usages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CollateralManagementUsageEnum>>;
    // fn collateral_management_usages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::CollateralManagementUsageEnum>>;
    // fn set_collateral_management_usages(&mut self, value: Option<&Vec<CollateralManagementUsageEnum>>);

    fn collateral_assignment_purposes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CollateralAssignmentPurposeEnum>>;
    // fn collateral_assignment_purposes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::CollateralAssignmentPurposeEnum>>;
    // fn set_collateral_assignment_purposes(&mut self, value: Option<&Vec<CollateralAssignmentPurposeEnum>>);


}

impl PostTradeCategorySection for crate::PostTradeCategorySection {
        fn category<'a>(&'a self) -> &'a crate::PostTradeCategoryEnum {
        return &self.category;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn category_components_note<'a>(&'a self) -> Option<&'a str> {
        return self.category_components_note.as_deref();
    }
        fn post_message_groups<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeMessageGroup>> {
        return self.post_message_groups.as_ref();
    }
        fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeMessageDetail>> {
        return self.messages.as_ref();
    }
        fn post_category_specific_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeComponentDetail>> {
        return self.post_category_specific_components.as_ref();
    }
        fn allocation_scenarios<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AllocationScenarioEnum>> {
        return self.allocation_scenarios.as_ref();
    }
        fn allocation_roles<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AllocationRoleEnum>> {
        return self.allocation_roles.as_ref();
    }
        fn post_trade_allocation_pricing_methods<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeAllocationPricingMethodEnum>> {
        return self.post_trade_allocation_pricing_methods.as_ref();
    }
        fn allocation_status_descriptions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AllocationStatusDescription>> {
        return self.allocation_status_descriptions.as_ref();
    }
        fn fragmentation_field_map<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::AllocationFragmentationFieldMap>> {
        return self.fragmentation_field_map.as_ref();
    }
        fn trade_capture_report_usages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCaptureReportUsage>> {
        return self.trade_capture_report_usages.as_ref();
    }
        fn trade_capture_report_identifier_rules<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::TradeCaptureReportIdentifierRule>> {
        return self.trade_capture_report_identifier_rules.as_ref();
    }
        fn registration_status_descriptions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::RegistrationStatusDescription>> {
        return self.registration_status_descriptions.as_ref();
    }
        fn clearing_services_for_position_management<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ClearingServiceForPositionManagementEnum>> {
        return self.clearing_services_for_position_management.as_ref();
    }
        fn clearing_services_for_post_trade_processing<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ClearingServicePostTradeProcessingFormat>> {
        return self.clearing_services_for_post_trade_processing.as_ref();
    }
        fn collateral_management_usages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CollateralManagementUsageEnum>> {
        return self.collateral_management_usages.as_ref();
    }
        fn collateral_assignment_purposes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::CollateralAssignmentPurposeEnum>> {
        return self.collateral_assignment_purposes.as_ref();
    }
}


pub trait PostTradeMessageGroup   {

    fn group_title<'a>(&'a self) -> &'a str;
    // fn group_title_mut(&mut self) -> &mut &'a str;
    // fn set_group_title(&mut self, value: String);

    fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PostTradeMessageDetail>;
    // fn messages_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::PostTradeMessageDetail>;
    // fn set_messages<E>(&mut self, value: &Vec<E>) where E: Into<PostTradeMessageDetail>;


}

impl PostTradeMessageGroup for crate::PostTradeMessageGroup {
        fn group_title<'a>(&'a self) -> &'a str {
        return &self.group_title[..];
    }
        fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::PostTradeMessageDetail> {
        return &self.messages;
    }
}


pub trait PostTradeMessageDetail   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_layout_url(&mut self, value: Option<&'a uri>);

    fn post_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeLayoutRow>>;
    // fn post_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeLayoutRow>>;
    // fn set_post_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PostTradeLayoutRow>;


}

impl PostTradeMessageDetail for crate::PostTradeMessageDetail {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.layout_url.as_ref();
    }
        fn post_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeLayoutRow>> {
        return self.post_layout_rows.as_ref();
    }
}


pub trait PostTradeComponentDetail   {

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition>;
    // fn repetition_mut(&mut self) -> &mut Option<&'a crate::ComponentRepetition>;
    // fn set_repetition(&mut self, value: Option<&'a ComponentRepetition>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_layout_url(&mut self, value: Option<&'a uri>);

    fn post_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeLayoutRow>>;
    // fn post_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeLayoutRow>>;
    // fn set_post_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PostTradeLayoutRow>;


}

impl PostTradeComponentDetail for crate::PostTradeComponentDetail {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition> {
        return self.repetition.as_ref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.layout_url.as_ref();
    }
        fn post_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeLayoutRow>> {
        return self.post_layout_rows.as_ref();
    }
}


pub trait PostTradeCommonComponentDetail   {

    fn component_name<'a>(&'a self) -> &'a crate::PostTradeCommonComponentName;
    // fn component_name_mut(&mut self) -> &mut &'a crate::PostTradeCommonComponentName;
    // fn set_component_name(&mut self, value: PostTradeCommonComponentName);

    fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition>;
    // fn repetition_mut(&mut self) -> &mut Option<&'a crate::ComponentRepetition>;
    // fn set_repetition(&mut self, value: Option<&'a ComponentRepetition>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_layout_url(&mut self, value: Option<&'a uri>);

    fn post_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeLayoutRow>>;
    // fn post_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::PostTradeLayoutRow>>;
    // fn set_post_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<PostTradeLayoutRow>;


}

impl PostTradeCommonComponentDetail for crate::PostTradeCommonComponentDetail {
        fn component_name<'a>(&'a self) -> &'a crate::PostTradeCommonComponentName {
        return &self.component_name;
    }
        fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition> {
        return self.repetition.as_ref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.layout_url.as_ref();
    }
        fn post_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::PostTradeLayoutRow>> {
        return self.post_layout_rows.as_ref();
    }
}


pub trait AllocationStatusDescription   {

    fn status_code<'a>(&'a self) -> &'a str;
    // fn status_code_mut(&mut self) -> &mut &'a str;
    // fn set_status_code(&mut self, value: String);

    fn status_label<'a>(&'a self) -> &'a str;
    // fn status_label_mut(&mut self) -> &mut &'a str;
    // fn set_status_label(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);


}

impl AllocationStatusDescription for crate::AllocationStatusDescription {
        fn status_code<'a>(&'a self) -> &'a str {
        return &self.status_code[..];
    }
        fn status_label<'a>(&'a self) -> &'a str {
        return &self.status_label[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}


pub trait AllocationFragmentationFieldMap   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn total_count_field<'a>(&'a self) -> &'a str;
    // fn total_count_field_mut(&mut self) -> &mut &'a str;
    // fn set_total_count_field(&mut self, value: String);

    fn fragment_count_field<'a>(&'a self) -> &'a str;
    // fn fragment_count_field_mut(&mut self) -> &mut &'a str;
    // fn set_fragment_count_field(&mut self, value: String);

    fn principal_message_reference<'a>(&'a self) -> &'a str;
    // fn principal_message_reference_mut(&mut self) -> &mut &'a str;
    // fn set_principal_message_reference(&mut self, value: String);


}

impl AllocationFragmentationFieldMap for crate::AllocationFragmentationFieldMap {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn total_count_field<'a>(&'a self) -> &'a str {
        return &self.total_count_field[..];
    }
        fn fragment_count_field<'a>(&'a self) -> &'a str {
        return &self.fragment_count_field[..];
    }
        fn principal_message_reference<'a>(&'a self) -> &'a str {
        return &self.principal_message_reference[..];
    }
}


pub trait TradeCaptureReportUsage   {

    fn status_label<'a>(&'a self) -> &'a str;
    // fn status_label_mut(&mut self) -> &mut &'a str;
    // fn set_status_label(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn identifier_role<'a>(&'a self) -> Option<&'a crate::TradeCaptureReportIdentifierRoleEnum>;
    // fn identifier_role_mut(&mut self) -> &mut Option<&'a crate::TradeCaptureReportIdentifierRoleEnum>;
    // fn set_identifier_role(&mut self, value: Option<&'a TradeCaptureReportIdentifierRoleEnum>);


}

impl TradeCaptureReportUsage for crate::TradeCaptureReportUsage {
        fn status_label<'a>(&'a self) -> &'a str {
        return &self.status_label[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn identifier_role<'a>(&'a self) -> Option<&'a crate::TradeCaptureReportIdentifierRoleEnum> {
        return self.identifier_role.as_ref();
    }
}


pub trait TradeCaptureReportIdentifierRule   {

    fn identifier_role<'a>(&'a self) -> &'a crate::TradeCaptureReportIdentifierRoleEnum;
    // fn identifier_role_mut(&mut self) -> &mut &'a crate::TradeCaptureReportIdentifierRoleEnum;
    // fn set_identifier_role(&mut self, value: TradeCaptureReportIdentifierRoleEnum);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);


}

impl TradeCaptureReportIdentifierRule for crate::TradeCaptureReportIdentifierRule {
        fn identifier_role<'a>(&'a self) -> &'a crate::TradeCaptureReportIdentifierRoleEnum {
        return &self.identifier_role;
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}


pub trait RegistrationStatusDescription   {

    fn status_code<'a>(&'a self) -> &'a str;
    // fn status_code_mut(&mut self) -> &mut &'a str;
    // fn set_status_code(&mut self, value: String);

    fn status_label<'a>(&'a self) -> &'a str;
    // fn status_label_mut(&mut self) -> &mut &'a str;
    // fn set_status_label(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);


}

impl RegistrationStatusDescription for crate::RegistrationStatusDescription {
        fn status_code<'a>(&'a self) -> &'a str {
        return &self.status_code[..];
    }
        fn status_label<'a>(&'a self) -> &'a str {
        return &self.status_label[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
}


pub trait ClearingServicePostTradeProcessingFormat   {

    fn message_format<'a>(&'a self) -> &'a crate::ClearingServiceForPostTradeProcessingEnum;
    // fn message_format_mut(&mut self) -> &mut &'a crate::ClearingServiceForPostTradeProcessingEnum;
    // fn set_message_format(&mut self, value: ClearingServiceForPostTradeProcessingEnum);

    fn supported_actions<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String>;
    // fn supported_actions_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, String>;
    // fn set_supported_actions(&mut self, value: &Vec<String>);


}

impl ClearingServicePostTradeProcessingFormat for crate::ClearingServicePostTradeProcessingFormat {
        fn message_format<'a>(&'a self) -> &'a crate::ClearingServiceForPostTradeProcessingEnum {
        return &self.message_format;
    }
        fn supported_actions<'a>(&'a self) -> impl poly_containers::SeqRef<'a, String> {
        return &self.supported_actions;
    }
}


pub trait PostTradeLayoutRow   {

    fn post_layout_kind<'a>(&'a self) -> &'a crate::PostTradeLayoutRowKindEnum;
    // fn post_layout_kind_mut(&mut self) -> &mut &'a crate::PostTradeLayoutRowKindEnum;
    // fn set_post_layout_kind(&mut self, value: PostTradeLayoutRowKindEnum);

    fn post_layout_field_tag(&self) -> Option<isize>;
    // fn post_layout_field_tag_mut(&mut self) -> &mut Option<isize>;
    // fn set_post_layout_field_tag(&mut self, value: Option<isize>);

    fn post_layout_element_name<'a>(&'a self) -> &'a str;
    // fn post_layout_element_name_mut(&mut self) -> &mut &'a str;
    // fn set_post_layout_element_name(&mut self, value: String);

    fn post_layout_required(&self) -> Option<bool>;
    // fn post_layout_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_post_layout_required(&mut self, value: Option<bool>);

    fn post_layout_description<'a>(&'a self) -> Option<&'a str>;
    // fn post_layout_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_post_layout_description(&mut self, value: Option<&'a str>);

    fn post_layout_nested(&self) -> Option<bool>;
    // fn post_layout_nested_mut(&mut self) -> &mut Option<bool>;
    // fn set_post_layout_nested(&mut self, value: Option<bool>);


}

impl PostTradeLayoutRow for crate::PostTradeLayoutRow {
        fn post_layout_kind<'a>(&'a self) -> &'a crate::PostTradeLayoutRowKindEnum {
        return &self.post_layout_kind;
    }
        fn post_layout_field_tag(&self) -> Option<isize> {
        return self.post_layout_field_tag;
    }
        fn post_layout_element_name<'a>(&'a self) -> &'a str {
        return &self.post_layout_element_name[..];
    }
        fn post_layout_required(&self) -> Option<bool> {
        return self.post_layout_required;
    }
        fn post_layout_description<'a>(&'a self) -> Option<&'a str> {
        return self.post_layout_description.as_deref();
    }
        fn post_layout_nested(&self) -> Option<bool> {
        return self.post_layout_nested;
    }
}


pub trait InfrastructureBusinessArea   {

    fn area<'a>(&'a self) -> &'a crate::BusinessAreaEnum;
    // fn area_mut(&mut self) -> &mut &'a crate::BusinessAreaEnum;
    // fn set_area(&mut self, value: BusinessAreaEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn published_version<'a>(&'a self) -> Option<&'a str>;
    // fn published_version_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_published_version(&mut self, value: Option<&'a str>);

    fn publisher<'a>(&'a self) -> Option<&'a str>;
    // fn publisher_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_publisher(&mut self, value: Option<&'a str>);

    fn infra_introduction<'a>(&'a self) -> Option<&'a str>;
    // fn infra_introduction_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_infra_introduction(&mut self, value: Option<&'a str>);

    fn diagram_conventions<'a>(&'a self) -> Option<&'a str>;
    // fn diagram_conventions_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_diagram_conventions(&mut self, value: Option<&'a str>);

    fn infra_common_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureComponentName>>;
    // fn infra_common_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InfrastructureComponentName>>;
    // fn set_infra_common_components(&mut self, value: Option<&Vec<InfrastructureComponentName>>);

    fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::InfrastructureMessageEntry>;
    // fn messages_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::InfrastructureMessageEntry>;
    // fn set_messages<E>(&mut self, value: &Vec<E>) where E: Into<InfrastructureMessageEntry>;

    fn messages_overview_note<'a>(&'a self) -> Option<&'a str>;
    // fn messages_overview_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_messages_overview_note(&mut self, value: Option<&'a str>);

    fn components<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::InfrastructureComponentEntry>;
    // fn components_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::InfrastructureComponentEntry>;
    // fn set_components<E>(&mut self, value: &Vec<E>) where E: Into<InfrastructureComponentEntry>;

    fn components_overview_note<'a>(&'a self) -> Option<&'a str>;
    // fn components_overview_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_components_overview_note(&mut self, value: Option<&'a str>);

    fn infra_footnotes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureComponentTableFootnote>>;
    // fn infra_footnotes_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InfrastructureComponentTableFootnote>>;
    // fn set_infra_footnotes<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InfrastructureComponentTableFootnote>;

    fn infra_category_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureCategorySection>>;
    // fn infra_category_sections_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InfrastructureCategorySection>>;
    // fn set_infra_category_sections<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InfrastructureCategorySection>;

    fn standard_responses_pre_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::StandardResponseMapping>>;
    // fn standard_responses_pre_trade_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::StandardResponseMapping>>;
    // fn set_standard_responses_pre_trade<E>(&mut self, value: Option<&Vec<E>>) where E: Into<StandardResponseMapping>;

    fn standard_responses_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::StandardResponseMapping>>;
    // fn standard_responses_trade_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::StandardResponseMapping>>;
    // fn set_standard_responses_trade<E>(&mut self, value: Option<&Vec<E>>) where E: Into<StandardResponseMapping>;

    fn standard_responses_post_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::StandardResponseMapping>>;
    // fn standard_responses_post_trade_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::StandardResponseMapping>>;
    // fn set_standard_responses_post_trade<E>(&mut self, value: Option<&Vec<E>>) where E: Into<StandardResponseMapping>;

    fn key_fields_pre_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReferenceKey>>;
    // fn key_fields_pre_trade_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReferenceKey>>;
    // fn set_key_fields_pre_trade<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ApplicationMessageReferenceKey>;

    fn key_fields_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReferenceKey>>;
    // fn key_fields_trade_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReferenceKey>>;
    // fn set_key_fields_trade<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ApplicationMessageReferenceKey>;

    fn key_fields_post_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReferenceKey>>;
    // fn key_fields_post_trade_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReferenceKey>>;
    // fn set_key_fields_post_trade<E>(&mut self, value: Option<&Vec<E>>) where E: Into<ApplicationMessageReferenceKey>;

    fn business_reject_reason_descriptions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::BusinessRejectReasonDescription>>;
    // fn business_reject_reason_descriptions_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::BusinessRejectReasonDescription>>;
    // fn set_business_reject_reason_descriptions<E>(&mut self, value: Option<&Vec<E>>) where E: Into<BusinessRejectReasonDescription>;

    fn infra_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureGlobalComponentReference>>;
    // fn infra_global_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InfrastructureGlobalComponentReference>>;
    // fn set_infra_global_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InfrastructureGlobalComponentReference>;

    fn referenced_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn referenced_global_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_referenced_global_components<E>(&mut self, value: Option<&Vec<String>>) where E: Into<String>;


}

impl InfrastructureBusinessArea for crate::InfrastructureBusinessArea {
        fn area<'a>(&'a self) -> &'a crate::BusinessAreaEnum {
        return &self.area;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn published_version<'a>(&'a self) -> Option<&'a str> {
        return self.published_version.as_deref();
    }
        fn publisher<'a>(&'a self) -> Option<&'a str> {
        return self.publisher.as_deref();
    }
        fn infra_introduction<'a>(&'a self) -> Option<&'a str> {
        return self.infra_introduction.as_deref();
    }
        fn diagram_conventions<'a>(&'a self) -> Option<&'a str> {
        return self.diagram_conventions.as_deref();
    }
        fn infra_common_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureComponentName>> {
        return self.infra_common_components.as_ref();
    }
        fn messages<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::InfrastructureMessageEntry> {
        return &self.messages;
    }
        fn messages_overview_note<'a>(&'a self) -> Option<&'a str> {
        return self.messages_overview_note.as_deref();
    }
        fn components<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::InfrastructureComponentEntry> {
        return &self.components;
    }
        fn components_overview_note<'a>(&'a self) -> Option<&'a str> {
        return self.components_overview_note.as_deref();
    }
        fn infra_footnotes<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureComponentTableFootnote>> {
        return self.infra_footnotes.as_ref();
    }
        fn infra_category_sections<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureCategorySection>> {
        return self.infra_category_sections.as_ref();
    }
        fn standard_responses_pre_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::StandardResponseMapping>> {
        return self.standard_responses_pre_trade.as_ref();
    }
        fn standard_responses_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::StandardResponseMapping>> {
        return self.standard_responses_trade.as_ref();
    }
        fn standard_responses_post_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::StandardResponseMapping>> {
        return self.standard_responses_post_trade.as_ref();
    }
        fn key_fields_pre_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReferenceKey>> {
        return self.key_fields_pre_trade.as_ref();
    }
        fn key_fields_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReferenceKey>> {
        return self.key_fields_trade.as_ref();
    }
        fn key_fields_post_trade<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReferenceKey>> {
        return self.key_fields_post_trade.as_ref();
    }
        fn business_reject_reason_descriptions<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::BusinessRejectReasonDescription>> {
        return self.business_reject_reason_descriptions.as_ref();
    }
        fn infra_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureGlobalComponentReference>> {
        return self.infra_global_components.as_ref();
    }
        fn referenced_global_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.referenced_global_components.as_ref();
    }
}


pub trait InfrastructureMessageEntry   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn category<'a>(&'a self) -> &'a crate::InfrastructureCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::InfrastructureCategoryEnum;
    // fn set_category(&mut self, value: InfrastructureCategoryEnum);


}

impl InfrastructureMessageEntry for crate::InfrastructureMessageEntry {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn category<'a>(&'a self) -> &'a crate::InfrastructureCategoryEnum {
        return &self.category;
    }
}


pub trait InfrastructureComponentEntry   {

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn repetition<'a>(&'a self) -> &'a crate::ComponentRepetition;
    // fn repetition_mut(&mut self) -> &mut &'a crate::ComponentRepetition;
    // fn set_repetition(&mut self, value: ComponentRepetition);

    fn category<'a>(&'a self) -> &'a crate::InfrastructureCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::InfrastructureCategoryEnum;
    // fn set_category(&mut self, value: InfrastructureCategoryEnum);

    fn footnote_number(&self) -> Option<isize>;
    // fn footnote_number_mut(&mut self) -> &mut Option<isize>;
    // fn set_footnote_number(&mut self, value: Option<isize>);


}

impl InfrastructureComponentEntry for crate::InfrastructureComponentEntry {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn repetition<'a>(&'a self) -> &'a crate::ComponentRepetition {
        return &self.repetition;
    }
        fn category<'a>(&'a self) -> &'a crate::InfrastructureCategoryEnum {
        return &self.category;
    }
        fn footnote_number(&self) -> Option<isize> {
        return self.footnote_number;
    }
}


pub trait InfrastructureComponentTableFootnote   {

    fn footnote_number(&self) -> isize;
    // fn footnote_number_mut(&mut self) -> &mut isize;
    // fn set_footnote_number(&mut self, value: isize);

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn introduced_in<'a>(&'a self) -> &'a str;
    // fn introduced_in_mut(&mut self) -> &mut &'a str;
    // fn set_introduced_in(&mut self, value: String);

    fn infra_sole_category<'a>(&'a self) -> &'a crate::InfrastructureCategoryEnum;
    // fn infra_sole_category_mut(&mut self) -> &mut &'a crate::InfrastructureCategoryEnum;
    // fn set_infra_sole_category(&mut self, value: InfrastructureCategoryEnum);

    fn text<'a>(&'a self) -> Option<&'a str>;
    // fn text_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_text(&mut self, value: Option<&'a str>);


}

impl InfrastructureComponentTableFootnote for crate::InfrastructureComponentTableFootnote {
        fn footnote_number(&self) -> isize {
        return self.footnote_number;
    }
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn introduced_in<'a>(&'a self) -> &'a str {
        return &self.introduced_in[..];
    }
        fn infra_sole_category<'a>(&'a self) -> &'a crate::InfrastructureCategoryEnum {
        return &self.infra_sole_category;
    }
        fn text<'a>(&'a self) -> Option<&'a str> {
        return self.text.as_deref();
    }
}


pub trait InfrastructureCategorySection   {

    fn category<'a>(&'a self) -> &'a crate::InfrastructureCategoryEnum;
    // fn category_mut(&mut self) -> &mut &'a crate::InfrastructureCategoryEnum;
    // fn set_category(&mut self, value: InfrastructureCategoryEnum);

    fn title<'a>(&'a self) -> Option<&'a str>;
    // fn title_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_title(&mut self, value: Option<&'a str>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn category_components_note<'a>(&'a self) -> Option<&'a str>;
    // fn category_components_note_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_category_components_note(&mut self, value: Option<&'a str>);

    fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureMessageDetail>>;
    // fn messages_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InfrastructureMessageDetail>>;
    // fn set_messages<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InfrastructureMessageDetail>;

    fn infra_category_specific_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureComponentDetail>>;
    // fn infra_category_specific_components_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InfrastructureComponentDetail>>;
    // fn set_infra_category_specific_components<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InfrastructureComponentDetail>;

    fn network_status_scenarios<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::NetworkStatusScenarioEnum>>;
    // fn network_status_scenarios_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::NetworkStatusScenarioEnum>>;
    // fn set_network_status_scenarios(&mut self, value: Option<&Vec<NetworkStatusScenarioEnum>>);

    fn network_request_types_referenced<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::NetworkRequestTypeEnum>>;
    // fn network_request_types_referenced_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::NetworkRequestTypeEnum>>;
    // fn set_network_request_types_referenced(&mut self, value: Option<&Vec<NetworkRequestTypeEnum>>);

    fn application_message_report_uses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReportTypeEnum>>;
    // fn application_message_report_uses_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReportTypeEnum>>;
    // fn set_application_message_report_uses(&mut self, value: Option<&Vec<ApplicationMessageReportTypeEnum>>);


}

impl InfrastructureCategorySection for crate::InfrastructureCategorySection {
        fn category<'a>(&'a self) -> &'a crate::InfrastructureCategoryEnum {
        return &self.category;
    }
        fn title<'a>(&'a self) -> Option<&'a str> {
        return self.title.as_deref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn category_components_note<'a>(&'a self) -> Option<&'a str> {
        return self.category_components_note.as_deref();
    }
        fn messages<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureMessageDetail>> {
        return self.messages.as_ref();
    }
        fn infra_category_specific_components<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureComponentDetail>> {
        return self.infra_category_specific_components.as_ref();
    }
        fn network_status_scenarios<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::NetworkStatusScenarioEnum>> {
        return self.network_status_scenarios.as_ref();
    }
        fn network_request_types_referenced<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::NetworkRequestTypeEnum>> {
        return self.network_request_types_referenced.as_ref();
    }
        fn application_message_report_uses<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::ApplicationMessageReportTypeEnum>> {
        return self.application_message_report_uses.as_ref();
    }
}


pub trait InfrastructureMessageDetail   {

    fn msg_type<'a>(&'a self) -> &'a str;
    // fn msg_type_mut(&mut self) -> &mut &'a str;
    // fn set_msg_type(&mut self, value: String);

    fn message_name<'a>(&'a self) -> &'a str;
    // fn message_name_mut(&mut self) -> &mut &'a str;
    // fn set_message_name(&mut self, value: String);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_layout_url(&mut self, value: Option<&'a uri>);

    fn infra_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureLayoutRow>>;
    // fn infra_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InfrastructureLayoutRow>>;
    // fn set_infra_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InfrastructureLayoutRow>;


}

impl InfrastructureMessageDetail for crate::InfrastructureMessageDetail {
        fn msg_type<'a>(&'a self) -> &'a str {
        return &self.msg_type[..];
    }
        fn message_name<'a>(&'a self) -> &'a str {
        return &self.message_name[..];
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.layout_url.as_ref();
    }
        fn infra_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureLayoutRow>> {
        return self.infra_layout_rows.as_ref();
    }
}


pub trait InfrastructureComponentDetail   {

    fn component_name<'a>(&'a self) -> &'a str;
    // fn component_name_mut(&mut self) -> &mut &'a str;
    // fn set_component_name(&mut self, value: String);

    fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition>;
    // fn repetition_mut(&mut self) -> &mut Option<&'a crate::ComponentRepetition>;
    // fn set_repetition(&mut self, value: Option<&'a ComponentRepetition>);

    fn description<'a>(&'a self) -> Option<&'a str>;
    // fn description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_description(&mut self, value: Option<&'a str>);

    fn layout_url<'a>(&'a self) -> Option<&'a crate::uri>;
    // fn layout_url_mut(&mut self) -> &mut Option<&'a crate::uri>;
    // fn set_layout_url(&mut self, value: Option<&'a uri>);

    fn infra_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureLayoutRow>>;
    // fn infra_layout_rows_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, crate::InfrastructureLayoutRow>>;
    // fn set_infra_layout_rows<E>(&mut self, value: Option<&Vec<E>>) where E: Into<InfrastructureLayoutRow>;


}

impl InfrastructureComponentDetail for crate::InfrastructureComponentDetail {
        fn component_name<'a>(&'a self) -> &'a str {
        return &self.component_name[..];
    }
        fn repetition<'a>(&'a self) -> Option<&'a crate::ComponentRepetition> {
        return self.repetition.as_ref();
    }
        fn description<'a>(&'a self) -> Option<&'a str> {
        return self.description.as_deref();
    }
        fn layout_url<'a>(&'a self) -> Option<&'a crate::uri> {
        return self.layout_url.as_ref();
    }
        fn infra_layout_rows<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, crate::InfrastructureLayoutRow>> {
        return self.infra_layout_rows.as_ref();
    }
}


pub trait InfrastructureLayoutRow   {

    fn infra_layout_kind<'a>(&'a self) -> &'a crate::InfrastructureLayoutRowKindEnum;
    // fn infra_layout_kind_mut(&mut self) -> &mut &'a crate::InfrastructureLayoutRowKindEnum;
    // fn set_infra_layout_kind(&mut self, value: InfrastructureLayoutRowKindEnum);

    fn infra_layout_field_tag(&self) -> Option<isize>;
    // fn infra_layout_field_tag_mut(&mut self) -> &mut Option<isize>;
    // fn set_infra_layout_field_tag(&mut self, value: Option<isize>);

    fn infra_layout_element_name<'a>(&'a self) -> &'a str;
    // fn infra_layout_element_name_mut(&mut self) -> &mut &'a str;
    // fn set_infra_layout_element_name(&mut self, value: String);

    fn infra_layout_required(&self) -> Option<bool>;
    // fn infra_layout_required_mut(&mut self) -> &mut Option<bool>;
    // fn set_infra_layout_required(&mut self, value: Option<bool>);

    fn infra_layout_description<'a>(&'a self) -> Option<&'a str>;
    // fn infra_layout_description_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_infra_layout_description(&mut self, value: Option<&'a str>);

    fn infra_layout_nested(&self) -> Option<bool>;
    // fn infra_layout_nested_mut(&mut self) -> &mut Option<bool>;
    // fn set_infra_layout_nested(&mut self, value: Option<bool>);


}

impl InfrastructureLayoutRow for crate::InfrastructureLayoutRow {
        fn infra_layout_kind<'a>(&'a self) -> &'a crate::InfrastructureLayoutRowKindEnum {
        return &self.infra_layout_kind;
    }
        fn infra_layout_field_tag(&self) -> Option<isize> {
        return self.infra_layout_field_tag;
    }
        fn infra_layout_element_name<'a>(&'a self) -> &'a str {
        return &self.infra_layout_element_name[..];
    }
        fn infra_layout_required(&self) -> Option<bool> {
        return self.infra_layout_required;
    }
        fn infra_layout_description<'a>(&'a self) -> Option<&'a str> {
        return self.infra_layout_description.as_deref();
    }
        fn infra_layout_nested(&self) -> Option<bool> {
        return self.infra_layout_nested;
    }
}


pub trait StandardResponseMapping   {

    fn category_label<'a>(&'a self) -> &'a str;
    // fn category_label_mut(&mut self) -> &mut &'a str;
    // fn set_category_label(&mut self, value: String);

    fn fix_message<'a>(&'a self) -> &'a str;
    // fn fix_message_mut(&mut self) -> &mut &'a str;
    // fn set_fix_message(&mut self, value: String);

    fn appropriate_responses<'a>(&'a self) -> &'a str;
    // fn appropriate_responses_mut(&mut self) -> &mut &'a str;
    // fn set_appropriate_responses(&mut self, value: String);


}

impl StandardResponseMapping for crate::StandardResponseMapping {
        fn category_label<'a>(&'a self) -> &'a str {
        return &self.category_label[..];
    }
        fn fix_message<'a>(&'a self) -> &'a str {
        return &self.fix_message[..];
    }
        fn appropriate_responses<'a>(&'a self) -> &'a str {
        return &self.appropriate_responses[..];
    }
}


pub trait ApplicationMessageReferenceKey   {

    fn category_label<'a>(&'a self) -> &'a str;
    // fn category_label_mut(&mut self) -> &mut &'a str;
    // fn set_category_label(&mut self, value: String);

    fn fix_message<'a>(&'a self) -> &'a str;
    // fn fix_message_mut(&mut self) -> &mut &'a str;
    // fn set_fix_message(&mut self, value: String);

    fn business_reject_ref_id_value<'a>(&'a self) -> &'a str;
    // fn business_reject_ref_id_value_mut(&mut self) -> &mut &'a str;
    // fn set_business_reject_ref_id_value(&mut self, value: String);


}

impl ApplicationMessageReferenceKey for crate::ApplicationMessageReferenceKey {
        fn category_label<'a>(&'a self) -> &'a str {
        return &self.category_label[..];
    }
        fn fix_message<'a>(&'a self) -> &'a str {
        return &self.fix_message[..];
    }
        fn business_reject_ref_id_value<'a>(&'a self) -> &'a str {
        return &self.business_reject_ref_id_value[..];
    }
}


pub trait BusinessRejectReasonDescription   {

    fn reject_reason_code(&self) -> isize;
    // fn reject_reason_code_mut(&mut self) -> &mut isize;
    // fn set_reject_reason_code(&mut self, value: isize);

    fn reject_reason_label<'a>(&'a self) -> &'a str;
    // fn reject_reason_label_mut(&mut self) -> &mut &'a str;
    // fn set_reject_reason_label(&mut self, value: String);


}

impl BusinessRejectReasonDescription for crate::BusinessRejectReasonDescription {
        fn reject_reason_code(&self) -> isize {
        return self.reject_reason_code;
    }
        fn reject_reason_label<'a>(&'a self) -> &'a str {
        return &self.reject_reason_label[..];
    }
}


pub trait InfrastructureGlobalComponentReference   {

    fn infra_global_component_name<'a>(&'a self) -> &'a crate::InfrastructureGlobalComponentName;
    // fn infra_global_component_name_mut(&mut self) -> &mut &'a crate::InfrastructureGlobalComponentName;
    // fn set_infra_global_component_name(&mut self, value: InfrastructureGlobalComponentName);

    fn infra_global_component_repetition<'a>(&'a self) -> Option<&'a str>;
    // fn infra_global_component_repetition_mut(&mut self) -> &mut Option<&'a str>;
    // fn set_infra_global_component_repetition(&mut self, value: Option<&'a str>);

    fn infra_global_component_field_tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, isize>>;
    // fn infra_global_component_field_tags_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, isize>>;
    // fn set_infra_global_component_field_tags(&mut self, value: Option<&Vec<isize>>);

    fn infra_global_component_field_names<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn infra_global_component_field_names_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_infra_global_component_field_names(&mut self, value: Option<&Vec<String>>);

    fn infra_global_component_used_in<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::InfrastructureCategoryEnum>;
    // fn infra_global_component_used_in_mut(&mut self) -> &mut impl poly_containers::SeqRef<'a, crate::InfrastructureCategoryEnum>;
    // fn set_infra_global_component_used_in(&mut self, value: &Vec<InfrastructureCategoryEnum>);

    fn infra_global_component_msg_types<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>>;
    // fn infra_global_component_msg_types_mut(&mut self) -> &mut Option<impl poly_containers::SeqRef<'a, String>>;
    // fn set_infra_global_component_msg_types(&mut self, value: Option<&Vec<String>>);


}

impl InfrastructureGlobalComponentReference for crate::InfrastructureGlobalComponentReference {
        fn infra_global_component_name<'a>(&'a self) -> &'a crate::InfrastructureGlobalComponentName {
        return &self.infra_global_component_name;
    }
        fn infra_global_component_repetition<'a>(&'a self) -> Option<&'a str> {
        return self.infra_global_component_repetition.as_deref();
    }
        fn infra_global_component_field_tags<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, isize>> {
        return self.infra_global_component_field_tags.as_ref();
    }
        fn infra_global_component_field_names<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.infra_global_component_field_names.as_ref();
    }
        fn infra_global_component_used_in<'a>(&'a self) -> impl poly_containers::SeqRef<'a, crate::InfrastructureCategoryEnum> {
        return &self.infra_global_component_used_in;
    }
        fn infra_global_component_msg_types<'a>(&'a self) -> Option<impl poly_containers::SeqRef<'a, String>> {
        return self.infra_global_component_msg_types.as_ref();
    }
}
