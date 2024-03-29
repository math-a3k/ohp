# Generated by Django 4.1.7 on 2023-03-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Loinc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "loinc_num",
                    models.CharField(
                        help_text="The unique LOINC Code is a string in the format of nnnnnnnn-n.",
                        max_length=10,
                        verbose_name="LOINC Number",
                    ),
                ),
                (
                    "component",
                    models.CharField(
                        help_text="First major axis-component or analyte",
                        max_length=255,
                        verbose_name="Component",
                    ),
                ),
                (
                    "loinc_property",
                    models.CharField(
                        help_text="Second major axis-property observed (e.g., mass vs. substance)",
                        max_length=255,
                        verbose_name="Property (LOINC)",
                    ),
                ),
                (
                    "time_aspct",
                    models.CharField(
                        help_text="Third major axis-timing of the measurement (e.g., point in time vs 24 hours)",
                        max_length=255,
                        verbose_name="Time Aspect",
                    ),
                ),
                (
                    "system",
                    models.CharField(
                        help_text="Fourth major axis-type of specimen or system (e.g., serum vs urine)",
                        max_length=255,
                        verbose_name="System",
                    ),
                ),
                (
                    "scale_typ",
                    models.CharField(
                        help_text="Fifth major axis-scale of measurement (e.g., qualitative vs. quantitative)",
                        max_length=255,
                        verbose_name="Scale Type",
                    ),
                ),
                (
                    "method_typ",
                    models.CharField(
                        help_text="Sixth major axis-method of measurement",
                        max_length=255,
                        verbose_name="Method Type",
                    ),
                ),
                (
                    "loinc_class",
                    models.CharField(
                        help_text="An arbitrary classification of the terms for grouping related observations together. The current classifications are listed in Appendix B. We present the database sorted by the class field within class type (see field 23). Users of the database should feel free to re-sort the database in any way they find useful, and/or to add their own classifying fields to the database. The content of the laboratory test subclasses should be obvious from the subclass name.",
                        max_length=255,
                        verbose_name="Class",
                    ),
                ),
                (
                    "version_last_changed",
                    models.CharField(
                        help_text="Fifth major axis-scale of measurement (e.g., qualitative vs. quantitative)",
                        max_length=255,
                        verbose_name="Version Last Changed",
                    ),
                ),
                (
                    "chng_type",
                    models.CharField(
                        help_text="Change Type Code",
                        max_length=255,
                        verbose_name="Chaneg Type",
                    ),
                ),
                (
                    "definition_description",
                    models.TextField(
                        help_text="Narrative text that describes the LOINC term taken as a whole (i.e., taking all of the parts of the term together) or relays information specific to the term, such as the context in which the term was requested or its clinical utility.",
                        verbose_name="Definition Description",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        help_text="Status of the LOINC Code (Active / Trial / Discouraged / Deprecated)",
                        max_length=255,
                        verbose_name="Status",
                    ),
                ),
                (
                    "consumer_name",
                    models.CharField(
                        help_text="An experimental (beta) consumer friendly name for this item. The intent is to provide a test name that health care consumers will recognize.",
                        max_length=255,
                        verbose_name="Consumer Name",
                    ),
                ),
                (
                    "class_type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Laboratory Class"),
                            (2, "Clinical class"),
                            (3, "Claims attatchments"),
                            (4, "Surveys"),
                        ],
                        verbose_name="Class Type",
                    ),
                ),
                (
                    "formula",
                    models.TextField(
                        help_text="Contains the formula in human readable form, for calculating the value of any measure that is based on an algebraic or other formula except those for which the component expresses the formula. So Sodium/creatinine does not need a formula, but Free T3 index does.",
                        verbose_name="Formula",
                    ),
                ),
                (
                    "exmpl_answers",
                    models.TextField(
                        help_text="For some tests and measurements, we have supplied examples of valid answers, such as “1:64”, “negative @ 1:16”, or “55”.",
                        verbose_name="Formula",
                    ),
                ),
                (
                    "survey_quest_text",
                    models.TextField(
                        help_text="Verbatim question from the survey instrument",
                        verbose_name="Survey Quest Text",
                    ),
                ),
                (
                    "survey_quest_src",
                    models.CharField(
                        help_text="Exact name of the survey instrument and the item/question number",
                        max_length=50,
                        verbose_name="Survey Quest Source",
                    ),
                ),
                (
                    "units_required",
                    models.BooleanField(
                        default=None,
                        help_text="Y/N field that indicates that units are required when this LOINC is included as an OBX segment in a HIPAA attachment",
                        verbose_name="Units Required",
                    ),
                ),
                (
                    "related_names_2",
                    models.TextField(
                        help_text="This field was introduced in version 2.05. It contains synonyms for each of the parts of the fully specified LOINC name (component, property, time, system, scale, method).",
                        verbose_name="Formula",
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        help_text="Introduced in version 2.07, this field contains the short form of the LOINC name and is created via a table-driven algorithmic process. The short name often includes abbreviations and acronyms.",
                        max_length=255,
                        verbose_name="Short Name",
                    ),
                ),
                (
                    "order_obs",
                    models.CharField(
                        help_text="Defines term as order only, observation only, or both. A fourth category, Subset, is used for terms that are subsets of a panel but do not represent a package that is known to be orderable. We have defined them only to make it easier to maintain panels or other sets within the LOINC construct. This field reflects our best approximation of the terms intended use; it is not to be considered normative or a binding resolution.",
                        max_length=15,
                        verbose_name="Order Obs",
                    ),
                ),
                (
                    "hl7_field_subfield_id",
                    models.CharField(
                        help_text="A value in this field means that the content should be delivered in the named field/subfield of the HL7 message. When NULL, the data for this data element should be sent in an OBX segment with this LOINC code stored in OBX-3 and with the value in the OBX-5.",
                        max_length=50,
                        verbose_name="HL7 Field Subfield ID",
                    ),
                ),
                (
                    "external_copyright_notice",
                    models.TextField(
                        blank=True,
                        help_text="External copyright holders copyright notice for this LOINC code.",
                        null=True,
                        verbose_name="External Copyright Notice",
                    ),
                ),
                (
                    "long_common_name",
                    models.CharField(
                        help_text="This field contains the LOINC name in a more readable format than the fully specified name. The long common names have been created via a tabledriven algorithmic process. Most abbreviations and acronyms that are used in the LOINC database have been fully spelled out in English.",
                        max_length=255,
                        verbose_name="Long Common Name",
                    ),
                ),
                (
                    "example_ucum_units",
                    models.CharField(
                        help_text="The Unified Code for Units of Measure (UCUM) is a code system intended to include all units of measures being contemporarily used in international science, engineering, and business. (www.unitsofmeasure.org) This field contains example units of measures for this term expressed as UCUM units.",
                        max_length=255,
                        verbose_name="Example UCUM Units",
                    ),
                ),
                (
                    "example_units",
                    models.CharField(
                        help_text="This field is populated with a combination of submitters units and units that people have sent us. Its purpose is to show users representative, but not necessarily recommended, units in which data could be sent for this term.",
                        max_length=255,
                        verbose_name="Example Units",
                    ),
                ),
                (
                    "status_reason",
                    models.CharField(
                        blank=True,
                        help_text="Classification of the reason for concept status. This field will be Null for ACTIVE concepts, and optionally populated for terms in other status where the reason is clear. DEPRECATED or DISCOURAGED terms may take values of: AMBIGUOUS, DUPLICATE, or ERRONEOUS.",
                        max_length=9,
                        null=True,
                        verbose_name="Status Reason",
                    ),
                ),
                (
                    "status_text",
                    models.TextField(
                        blank=True,
                        help_text="Explanation of concept status in narrative text. This field will be Null for ACTIVE concepts, and optionally populated for terms in other status.",
                        null=True,
                        verbose_name="Status Text",
                    ),
                ),
                (
                    "change_reason_public",
                    models.TextField(
                        blank=True,
                        help_text="Detailed explanation about special changes to the term over time.",
                        max_length=9,
                        null=True,
                        verbose_name="Change Reason Public",
                    ),
                ),
                (
                    "common_test_rank",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Ranking by frequency of usage of approximately 20,000 LOINCs codes as reported in the U.S.",
                        null=True,
                        verbose_name="Common Test Rank",
                    ),
                ),
                (
                    "common_order_rank",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Ranking of approximately 300 common orders performed by laboratories in USA.",
                        null=True,
                        verbose_name="Common Order Rank",
                    ),
                ),
                (
                    "common_si_test_rank",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="SI ranks no longer provided within LOINC database.",
                        null=True,
                        verbose_name="Common SI Test Rank",
                    ),
                ),
                (
                    "hl7_attachment_structure",
                    models.CharField(
                        blank=True,
                        help_text='This field will be populated in collaboration with the HL7 Attachments Work Group as described in the HL7. Attachment Specification: Supplement to Consolidated CDA Templated Guide. As of Version 2.58, the text will either be "IG exists" (previously STRUCTURED) or "No IG exists" (previously UNSTRUCTURED) for relevant terms. The "IG exists" terms are those that have clinically-relevant HL7 implementation guides that use the U.S. Realm Header. The "No IG exists" terms are those approved by the HL7 Attachments WG for transmission using the Unstructured Document template of the C-CDA.',
                        max_length=15,
                        null=True,
                        verbose_name="Example Units",
                    ),
                ),
                (
                    "external_copyright_link",
                    models.CharField(
                        blank=True,
                        help_text="For terms that have a third party copyright, this field is populated with the COPYRIGHT_ID from the Source Organization table (see below). It links an external copyright statement to a term.",
                        max_length=255,
                        null=True,
                        verbose_name="External Copyright Link",
                    ),
                ),
                (
                    "panel_type",
                    models.CharField(
                        blank=True,
                        help_text='Describes a panel as a "Convenience group", "Organizer", or Panel". A "Panel" is an enumerated set of terms that are used together in direct clinical care. The package would typically be thought of as a single orderable item that contains a set of reported observations. A "Convenience group" is an enumerated set of terms used for a common purpose, but not typically orderable as a single unit. An "Organizer" is a subpanel (i.e., a child) within another panel that is only used to group together a set of terms, but is not an independently used entity. They often represent a header in a form, or serve as a navigation concept.',
                        max_length=50,
                        null=True,
                        verbose_name="Panel Type",
                    ),
                ),
                (
                    "ask_at_order_entry",
                    models.CharField(
                        blank=True,
                        help_text="A multi-valued, semicolon delimited list of LOINC codes that represent optional associated observation(s) for a clinical observation or laboratory test. A LOINC term in this field may represent a single associated observation or panel containing several associated observations.",
                        max_length=255,
                        null=True,
                        verbose_name="Panel Type",
                    ),
                ),
                (
                    "associated_observations",
                    models.CharField(
                        blank=True,
                        help_text="A multi-valued, semicolon delimited list of LOINC codes that represent optional associated observation(s) for a clinical observation or laboratory test. A LOINC term in this field may represent a single associated observation or panel containing several associated observations.",
                        max_length=255,
                        null=True,
                        verbose_name="Associated Observations",
                    ),
                ),
                (
                    "version_first_released",
                    models.CharField(
                        blank=True,
                        help_text="The LOINC version number in which the record was first released. For oldest records where the version released number is known, this field will be null.",
                        max_length=255,
                        null=True,
                        verbose_name="Version First Released",
                    ),
                ),
                (
                    "valid_hl7_attachment_request",
                    models.CharField(
                        blank=True,
                        help_text="A value of 'Y' in this field indicates that this LOINC code can be sent by a payer as part of an HL7 attachment request for additional information.",
                        max_length=50,
                        null=True,
                        verbose_name="Valid HL7 Attachment Request",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        blank=True,
                        help_text='This field contains a name that is more "clinician-friendly" compared to the current LOINC Short Name, Long Common Name, and Fully Specified Name. It is created algorithmically from the manually crafted display text for each Part and is generally more concise than the Long Common Name.',
                        max_length=255,
                        null=True,
                        verbose_name="Display Name",
                    ),
                ),
            ],
            options={
                "verbose_name": "Unit",
                "verbose_name_plural": "Units",
            },
        ),
    ]
