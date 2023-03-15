from io import StringIO

import requests_mock
from django.conf import settings
from django.core.management import call_command
from django.test import SimpleTestCase

from .models import Unit

ucum_response_mock = """<?xml version="1.0" encoding="ascii"?>
<root xmlns="http://unitsofmeasure.org/ucum-essence" version="2.1"
      revision="$Revision: 442 $"
      revision-date="$Date: 2017-11-21 19:04:52 -0500 (Tue, 21 Nov 2017) $">
   <base-unit Code="rad" CODE="RAD" dim="A">
      <name>radian</name>
      <printSymbol>rad</printSymbol>
      <property>plane angle</property>
   </base-unit>
   <unit Code="10*" CODE="10*" isMetric="no" class="dimless">
      <name>the number ten for arbitrary powers</name>
      <printSymbol>10</printSymbol>
      <property>number</property>
      <value Unit="1" UNIT="1" value="10">10</value>
   </unit>
   <unit Code="10^" CODE="10^" isMetric="no" class="dimless">
      <name>the number ten for arbitrary powers</name>
      <printSymbol>10</printSymbol>
      <property>number</property>
      <value Unit="1" UNIT="1" value="10">10</value>
   </unit>
   <unit Code="10^" CODE="10^" isMetric="no" class="dimless">
      <name>the number ten for arbitrary powers</name>
      <printSymbol>10</printSymbol>
      <property>number</property>
      <value Unit="1" UNIT="1" value="10">10</value>
   </unit>
   <prefix Code="Ti" CODE="TIB">
      <name>tebi</name>
      <printSymbol>Ti</printSymbol>
      <value value="1099511627776">1099511627776</value>
   </prefix>
</root>
"""


class TestUnit(SimpleTestCase):
    databases = "__all__"

    def test_import_ucum_units_command(self):
        out = StringIO()
        # -> Test --create
        with requests_mock.Mocker() as m:
            m.get(settings.UCUM_UNITS_URL, text=ucum_response_mock)
            call_command("import_ucum_units", stdout=out)
            self.assertIn("Successfully processed", out.getvalue())
            self.assertEqual(Unit.objects.all().count(), 3)
            # Test exceptions
            with self.assertRaises(Exception):
                m.get(settings.UCUM_UNITS_URL, status_code=400)
                call_command("import_ucum_units", stdout=out)
        # -> Test --remove
        call_command("import_ucum_units", "--remove", stdout=out)
        self.assertIn("Successfully removed", out.getvalue())
        self.assertEqual(Unit.objects.all().count(), 0)
