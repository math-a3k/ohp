import csv
import tempfile
from zipfile import ZipFile

from django.conf import settings
from django.core.management.base import BaseCommand

from loinc.models import Loinc


class Command(BaseCommand):
    help = "Loads / Removes LOINC codes"

    def add_arguments(self, parser):
        parser.add_argument(
            "--remove",
            action="store_true",
            default=False,
            help="Removes LOINC codes",
        )
        parser.add_argument(
            "--load",
            action="store_true",
            default=True,
            help="Load UCUM units",
        )

    def handle(self, *args, **options):
        if options["remove"]:
            options["load"] = False
            data = Loinc.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully removed Loinc codes ({} units)".format(
                        data[0]
                    )
                )
            )

        if options["load"]:
            loinc_zip = f"{settings.BASE_DIR}{settings.LOINC_ZIP_FILE}"
            temp_dir = tempfile.gettempdir()
            with ZipFile(loinc_zip) as zObject:
                zObject.extract(
                    "LoincTable/Loinc.csv",
                    path=temp_dir,
                )

            codes_created, codes_processed = 0, 0
            with open(temp_dir + "/LoincTable/Loinc.csv") as loinc_csv:
                csv_reader = csv.DictReader(loinc_csv)
                for row in csv_reader:
                    l, created = Loinc.objects.update_or_create(
                        loinc_num=row["LOINC_NUM"],
                        defaults={
                            "loinc_num": row["LOINC_NUM"],
                            "component": row["COMPONENT"],
                            "loinc_property": row["PROPERTY"],
                            "time_aspct": row["TIME_ASPCT"],
                            "system": row["SYSTEM"],
                            "scale_typ": row["SCALE_TYP"],
                            "method_typ": row["METHOD_TYP"],
                            "loinc_class": row["CLASS"],
                            "version_last_changed": row["VersionLastChanged"],
                            "chng_type": row["CHNG_TYPE"],
                            "definition_description": row[
                                "DefinitionDescription"
                            ],
                            "status": row["STATUS"],
                            "consumer_name": row["CONSUMER_NAME"],
                            "class_type": row["CLASSTYPE"],
                            "formula": row["FORMULA"],
                            "exmpl_answers": row["EXMPL_ANSWERS"],
                            "survey_quest_text": row["SURVEY_QUEST_TEXT"],
                            "survey_quest_src": row["SURVEY_QUEST_SRC"],
                            "units_required": row["UNITSREQUIRED"] == "Y",
                            "related_names_2": row["RELATEDNAMES2"],
                            "short_name": row["SHORTNAME"],
                            "order_obs": row["ORDER_OBS"],
                            "hl7_attachment_structure": row[
                                "HL7_FIELD_SUBFIELD_ID"
                            ],
                            "external_copyright_notice": row[
                                "EXTERNAL_COPYRIGHT_NOTICE"
                            ],
                            "example_units": row["EXAMPLE_UNITS"],
                            "long_common_name": row["LONG_COMMON_NAME"],
                            "example_ucum_units": row["EXAMPLE_UCUM_UNITS"],
                            "status_reason": row["STATUS_REASON"],
                            "status_text": row["STATUS_TEXT"],
                            "change_reason_public": row[
                                "CHANGE_REASON_PUBLIC"
                            ],
                            "common_test_rank": row["COMMON_TEST_RANK"],
                            "common_order_rank": row["COMMON_ORDER_RANK"],
                            "common_si_test_rank": row["COMMON_SI_TEST_RANK"],
                            "hl7_attachment_structure": row[
                                "HL7_ATTACHMENT_STRUCTURE"
                            ],
                            "external_copyright_link": row[
                                "EXTERNAL_COPYRIGHT_LINK"
                            ],
                            "panel_type": row["PanelType"],
                            "ask_at_order_entry": row["AskAtOrderEntry"],
                            "associated_observations": row[
                                "AssociatedObservations"
                            ],
                            "version_first_released": row[
                                "VersionFirstReleased"
                            ],
                            "valid_hl7_attachment_request": row[
                                "ValidHL7AttachmentRequest"
                            ],
                            "display_name": row["DisplayName"],
                        },
                    )
                    codes_processed += 1
                    if created:
                        codes_created += 1
            self.stdout.write(
                self.style.SUCCESS(
                    (
                        f"Successfully processed {codes_processed} LOINC codes "
                        f"({codes_created} created)"
                    )
                )
            )
