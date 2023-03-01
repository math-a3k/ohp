from io import StringIO

from django.core.management import call_command
from django.test import SimpleTestCase

from .models import Loinc


class TestLoinc(SimpleTestCase):
    databases = "__all__"

    def test_import_ucum_units_command(self):
        out = StringIO()
        # -> Test --create
        with self.settings(
            LOINC_ZIP_FILE="/loinc/fixtures/Loinc_2.73_ohp_test.zip"
        ):
            call_command("import_loinc_codes", stdout=out)
            self.assertIn("Successfully processed", out.getvalue())
            self.assertEqual(Loinc.objects.all().count(), 3)
        # -> Test --remove
        call_command("import_loinc_codes", "--remove", stdout=out)
        self.assertIn("Successfully removed", out.getvalue())
        self.assertEqual(Loinc.objects.all().count(), 0)
