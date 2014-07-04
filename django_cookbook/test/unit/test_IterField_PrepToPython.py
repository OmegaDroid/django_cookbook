import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_cookbook.test.settings")

from django.test import TestCase
from django_cookbook.model.fields import IterField


class IterField_PrepToPython(TestCase):
    def test_ValueIsEmptyList_ResultMatchesInput(self):
        value = []
        field = IterField()

        prepped = field.get_prep_value(value)
        py = field.to_python(prepped)

        self.assertEqual(value, py)

    def test_ValueIsListWithElementsListAndDicts_ResultMatchesInput(self):
        value = [1, 2, 3, [4, 5, 6], {"foo": 8}]
        field = IterField()

        prepped = field.get_prep_value(value)
        py = field.to_python(prepped)

        self.assertEqual(value, py)

    def test_ValueIsEmptyDict_ResultMatchesInput(self):
        value = {}
        field = IterField()

        prepped = field.get_prep_value(value)
        py = field.to_python(prepped)

        self.assertEqual(value, py)

    def test_ValueIsDictWithElementsListAndDicts_ResultMatchesInput(self):
        value = {"foo": 1, "bar": [2, 3, 4], "boo": {"moo": 5}}
        field = IterField()

        prepped = field.get_prep_value(value)
        py = field.to_python(prepped)

        self.assertEqual(value, py)