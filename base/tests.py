from django.test import TestCase


class BaseTestCase(TestCase):
    def test_test(self):
        self.assertTrue(True)
