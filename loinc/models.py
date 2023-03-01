from django.db import models
from django.utils.translation import gettext as _


class Loinc(models.Model):
    """
    LOINC Main / Core Table
    """

    loinc_num = models.CharField(
        _("LOINC Number"),
        max_length=10,
        help_text=_(
            "The unique LOINC Code is a string in the format of nnnnnnnn-n."
        ),
    )
    component = models.CharField(
        _("Component"),
        max_length=255,
        help_text=_("First major axis-component or analyte"),
    )
    loinc_property = models.CharField(
        _("Property (LOINC)"),
        max_length=255,
        help_text=_(
            "Second major axis-property observed (e.g., mass vs. substance)"
        ),
    )
    time_aspct = models.CharField(
        _("Time Aspect"),
        max_length=255,
        help_text=_(
            "Third major axis-timing of the measurement (e.g., point in time "
            "vs 24 hours)"
        ),
    )
    system = models.CharField(
        _("System"),
        max_length=255,
        help_text=_(
            "Fourth major axis-type of specimen or system (e.g., serum vs "
            "urine)"
        ),
    )
    scale_typ = models.CharField(
        _("Scale Type"),
        max_length=255,
        help_text=_(
            "Fifth major axis-scale of measurement (e.g., qualitative vs. "
            "quantitative)"
        ),
    )
    method_typ = models.CharField(
        _("Method Type"),
        max_length=255,
        help_text=_("Sixth major axis-method of measurement"),
    )
    loinc_class = models.CharField(
        _("Class"),
        max_length=255,
        help_text=_(
            "An arbitrary classification of the terms for grouping related "
            "observations together. The current classifications are listed "
            "in Appendix B. We present the database sorted by the class "
            "field within class type (see field 23). Users of the "
            "database should feel free to re-sort the database in any way "
            "they find useful, and/or to add their own classifying fields to "
            "the database. The content of the laboratory test subclasses "
            "should be obvious from the subclass name."
        ),
    )
    version_last_changed = models.CharField(
        _("Version Last Changed"),
        max_length=255,
        help_text=_(
            "Fifth major axis-scale of measurement (e.g., qualitative vs. "
            "quantitative)"
        ),
    )
    chng_type = models.CharField(
        _("Chaneg Type"), max_length=255, help_text=_("Change Type Code")
    )
    definition_description = models.TextField(
        _("Definition Description"),
        help_text=_(
            "Narrative text that describes the LOINC term taken as a whole "
            "(i.e., taking all of the parts of the term together) or relays "
            "information specific to the term, such as the context in which "
            "the term was requested or its clinical utility."
        ),
    )
    status = models.CharField(
        _("Status"),
        max_length=255,
        help_text=_(
            "Status of the LOINC Code (Active / Trial / Discouraged / "
            "Deprecated)"
        ),
    )
    consumer_name = models.CharField(
        _("Consumer Name"),
        max_length=255,
        help_text=_(
            "An experimental (beta) consumer friendly name for this item. "
            "The intent is to provide a test name that health care "
            "consumers will recognize."
        ),
    )
    class_type = models.PositiveSmallIntegerField(
        _("Class Type"),
        choices=(
            (1, _("Laboratory Class")),
            (2, _("Clinical class")),
            (3, _("Claims attatchments")),
            (4, _("Surveys")),
        ),
    )
    formula = models.TextField(
        _("Formula"),
        help_text=_(
            "Contains the formula in human readable form, for calculating "
            "the value of any measure that is based on an algebraic or "
            "other formula except those for which the component expresses "
            "the formula. So Sodium/creatinine does not need a formula, "
            "but Free T3 index does."
        ),
    )
    exmpl_answers = models.TextField(
        _("Formula"),
        help_text=_(
            "For some tests and measurements, we have supplied examples of "
            "valid answers, such as “1:64”, “negative @ 1:16”, or “55”."
        ),
    )
    survey_quest_text = models.TextField(
        _("Survey Quest Text"),
        help_text=_("Verbatim question from the survey instrument"),
    )
    survey_quest_src = models.CharField(
        _("Survey Quest Source"),
        max_length=50,
        help_text=_(
            "Exact name of the survey instrument and the item/question number"
        ),
    )
    units_required = models.BooleanField(
        _("Units Required"),
        default=None,
        help_text=_(
            "Y/N field that indicates that units are required when this "
            "LOINC is included as an OBX segment in a HIPAA attachment"
        ),
    )
    related_names_2 = models.TextField(
        _("Formula"),
        help_text=_(
            "This field was introduced in version 2.05. It contains synonyms "
            "for each of the parts of the fully specified LOINC name "
            "(component, property, time, system, scale, method)."
        ),
    )
    short_name = models.CharField(
        _("Short Name"),
        max_length=255,
        help_text=_(
            "Introduced in version 2.07, this field contains the short form "
            "of the LOINC name and is created via a table-driven algorithmic "
            "process. The short name often includes abbreviations and "
            "acronyms."
        ),
    )
    order_obs = models.CharField(
        _("Order Obs"),
        max_length=15,
        help_text=_(
            "Defines term as order only, observation only, or both. A "
            "fourth category, Subset, is used for terms that are subsets of "
            "a panel but do not represent a package that is known to be "
            "orderable. We have defined them only to make it easier to "
            "maintain panels or other sets within the LOINC construct. "
            "This field reflects our best approximation of the terms "
            "intended use; it is not to be considered normative or a "
            "binding resolution."
        ),
    )
    hl7_field_subfield_id = models.CharField(
        _("HL7 Field Subfield ID"),
        max_length=50,
        help_text=_(
            "A value in this field means that the content should be "
            "delivered in the named field/subfield of the HL7 message. "
            "When NULL, the data for this data element should be sent in "
            "an OBX segment with this LOINC code stored in OBX-3 and with "
            "the value in the OBX-5."
        ),
    )
    external_copyright_notice = models.TextField(
        _("External Copyright Notice"),
        blank=True,
        null=True,
        help_text=_(
            "External copyright holders copyright notice for this LOINC code."
        ),
    )
    long_common_name = models.CharField(
        _("Long Common Name"),
        max_length=255,
        help_text=_(
            "This field contains the LOINC name in a more readable format than "
            "the fully specified name. The long common names have been created "
            "via a tabledriven algorithmic process. Most abbreviations and "
            "acronyms that are used in the LOINC database have been fully "
            "spelled out in English."
        ),
    )
    example_ucum_units = models.CharField(
        _("Example UCUM Units"),
        max_length=255,
        help_text=_(
            "The Unified Code for Units of Measure (UCUM) is a code system "
            "intended to include all units of measures being contemporarily "
            "used in international science, engineering, and business. "
            "(www.unitsofmeasure.org) This field contains example units of "
            "measures for this term expressed as UCUM units."
        ),
    )
    example_units = models.CharField(
        _("Example Units"),
        max_length=255,
        help_text=_(
            "This field is populated with a combination of submitters units "
            "and units that people have sent us. Its purpose is to "
            "show users representative, but not necessarily recommended, "
            "units in which data could be sent for this term."
        ),
    )
    status_reason = models.CharField(
        _("Status Reason"),
        max_length=9,
        blank=True,
        null=True,
        help_text=_(
            "Classification of the reason for concept status. This field "
            "will be Null for ACTIVE concepts, and optionally populated "
            "for terms in other status where the reason is clear. "
            "DEPRECATED or DISCOURAGED terms may take values of: "
            "AMBIGUOUS, DUPLICATE, or ERRONEOUS."
        ),
    )
    status_text = models.TextField(
        _("Status Text"),
        blank=True,
        null=True,
        help_text=_(
            "Explanation of concept status in narrative text. This field "
            "will be Null for ACTIVE concepts, and optionally populated "
            "for terms in other status."
        ),
    )
    change_reason_public = models.TextField(
        _("Change Reason Public"),
        max_length=9,
        blank=True,
        null=True,
        help_text=_(
            "Detailed explanation about special changes to the term over time."
        ),
    )
    common_test_rank = models.PositiveSmallIntegerField(
        _("Common Test Rank"),
        blank=True,
        null=True,
        help_text=_(
            "Ranking by frequency of usage of approximately 20,000 LOINCs "
            "codes as reported in the U.S."
        ),
    )
    common_order_rank = models.PositiveSmallIntegerField(
        _("Common Order Rank"),
        blank=True,
        null=True,
        help_text=_(
            "Ranking of approximately 300 common orders performed by "
            "laboratories in USA."
        ),
    )
    common_si_test_rank = models.PositiveSmallIntegerField(
        _("Common SI Test Rank"),
        blank=True,
        null=True,
        help_text=_("SI ranks no longer provided within LOINC database."),
    )
    hl7_attachment_structure = models.CharField(
        _("Example Units"),
        max_length=15,
        blank=True,
        null=True,
        help_text=_(
            "This field will be populated in collaboration with the HL7 "
            "Attachments Work Group as described in the HL7. Attachment "
            "Specification: Supplement to Consolidated CDA Templated Guide. "
            'As of Version 2.58, the text will either be "IG exists" '
            '(previously STRUCTURED) or "No IG exists" (previously '
            'UNSTRUCTURED) for relevant terms. The "IG exists" terms '
            "are those that have clinically-relevant HL7 implementation "
            'guides that use the U.S. Realm Header. The "No IG exists" '
            "terms are those approved by the HL7 Attachments WG for "
            "transmission using the Unstructured Document template of "
            "the C-CDA."
        ),
    )
    external_copyright_link = models.CharField(
        _("External Copyright Link"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_(
            "For terms that have a third party copyright, this field is "
            "populated with the COPYRIGHT_ID from the Source Organization "
            "table (see below). It links an external copyright statement "
            "to a term."
        ),
    )
    panel_type = models.CharField(
        _("Panel Type"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_(
            'Describes a panel as a "Convenience group", "Organizer", or '
            'Panel". A "Panel" is an enumerated set of terms that are '
            "used together in direct clinical care. The package would "
            "typically be thought of as a single orderable item that "
            'contains a set of reported observations. A "Convenience '
            'group" is an enumerated set of terms used for a common '
            "purpose, but not typically orderable as a single unit. "
            'An "Organizer" is a subpanel (i.e., a child) within another '
            "panel that is only used to group together a set of terms, "
            "but is not an independently used entity. They often represent "
            "a header in a form, or serve as a navigation concept."
        ),
    )
    ask_at_order_entry = models.CharField(
        _("Panel Type"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_(
            "A multi-valued, semicolon delimited list of LOINC codes that "
            "represent optional associated observation(s) for a clinical "
            "observation or laboratory test. A LOINC term in this field "
            "may represent a single associated observation or panel "
            "containing several associated observations."
        ),
    )
    associated_observations = models.CharField(
        _("Associated Observations"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_(
            "A multi-valued, semicolon delimited list of LOINC codes that "
            "represent optional associated observation(s) for a clinical "
            "observation or laboratory test. A LOINC term in this field "
            "may represent a single associated observation or panel "
            "containing several associated observations."
        ),
    )
    version_first_released = models.CharField(
        _("Version First Released"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_(
            "The LOINC version number in which the record was first "
            "released. For oldest records where the version released number "
            "is known, this field will be null."
        ),
    )
    valid_hl7_attachment_request = models.CharField(
        _("Valid HL7 Attachment Request"),
        max_length=50,
        blank=True,
        null=True,
        help_text=_(
            "A value of 'Y' in this field indicates that this LOINC code can "
            "be sent by a payer as part of an HL7 attachment request for "
            "additional information."
        ),
    )
    display_name = models.CharField(
        _("Display Name"),
        max_length=255,
        blank=True,
        null=True,
        help_text=_(
            'This field contains a name that is more "clinician-friendly" '
            "compared to the current LOINC Short Name, Long Common Name, "
            "and Fully Specified Name. It is created algorithmically from "
            "the manually crafted display text for each Part and is generally "
            "more concise than the Long Common Name."
        ),
    )

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")

    def __str__(self):  # pragma: no cover
        return f"{self.loinc_num} [{self.display_name}]"
