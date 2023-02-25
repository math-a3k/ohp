from xml.etree.ElementTree import fromstring

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from units.models import Unit


class Command(BaseCommand):
    help = "Loads / Removes UCUM units"

    def add_arguments(self, parser):
        parser.add_argument(
            "--remove",
            action="store_true",
            default=False,
            help="Removes UCUM units",
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
            data = Unit.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully removed UCUM units ({} units)".format(
                        data[0]
                    )
                )
            )

        if options["load"]:
            response = requests.get(settings.UCUM_UNITS_URL)
            if response.status_code == 200:
                et = fromstring(response.content)
            else:
                raise Exception(
                    msg=(
                        f"Unable to obtain the xmlfile from "
                        f"{settings.UCUM_UNITS_URL}: "
                        f"{response.code} - {response.content}"
                    )
                )
            namespace = {"": "http://unitsofmeasure.org/ucum-essence"}
            nodes_base_units = et.findall("base-unit", namespace)
            nodes_units = et.findall("unit", namespace)
            units_created, units_processed = 0, 0
            for unit in [*nodes_base_units, *nodes_units]:
                u_ps = unit.find("printSymbol", namespace)
                print_symbol = (
                    u_ps.text if isinstance(u_ps, type(unit)) else None
                )
                u_value = unit.find("value", namespace)
                unit_unit, unit_value = None, None
                if isinstance(u_value, type(unit)):
                    unit_unit = u_value.attrib["Unit"]
                    unit_value = u_value.text
                u, created = Unit.objects.update_or_create(
                    code=unit.attrib["Code"],
                    unit_class=unit.attrib.get("class", "base-unit"),
                    is_metric=(unit.attrib.get("isMetric", "no") == "yes"),
                    defaults={
                        "name": unit.find("name", namespace).text,
                        "print_symbol": print_symbol,
                        "unit_property": unit.find("property", namespace).text,
                        "unit": unit_unit,
                        "unit_value": unit_value,
                    },
                )
                units_processed += 1
                if created:
                    units_created += 1
            self.stdout.write(
                self.style.SUCCESS(
                    (
                        f"Successfully processed {units_processed} UCUM units "
                        f"({units_created} created)"
                    )
                )
            )
