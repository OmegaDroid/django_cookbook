import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_cookbook.test.settings")

from django.test import TestCase
from django_cookbook.model.fields import IterField


class IterField_ToPython(TestCase):
    def test_ValueIsNone_ReturnedValueIsNone(self):
        field = IterField()

        self.assertIsNone(field.to_python(None))

    def test_StringIsEmpty_ReturnedValueIsEmptyList(self):
        field = IterField()

        self.assertEqual([], field.to_python(""))

    def test_ValueIsList_ListIsReturned(self):
        field = IterField()

        self.assertEqual([1, 2, {3: 4}], field.to_python([1, 2, {3: 4}]))

    def test_ValueIsDictionary_DictionaryIsReturned(self):
        field = IterField()

        self.assertEqual({1: 2, 3: [4, 5, 6]}, field.to_python({1: 2, 3: [4, 5, 6]}))

    def test_StringIsEmptyList_ReturnedValueIsEmptyList(self):
        field = IterField()

        self.assertEqual([], field.to_python("[]"))

    def test_StringIsListWithOneField_ReturnedValueIsListWithThatField(self):
        field = IterField()

        self.assertEqual(["foo"], field.to_python('["foo"]'))

    def test_StringIsListWithMultipleField_ReturnedValueIsListWithThoseFields(self):
        field = IterField()

        self.assertEqual(["foo", "bar", "boo"], field.to_python('["foo","bar","boo"]'))

    def test_StringIsListWithMultipleFieldOneOfWhichIsAList_ReturnedValueIsListWithThoseFields(self):
        field = IterField()

        self.assertEqual(["foo", ["bar", "boo"], "moo"], field.to_python('["foo",["bar","boo"],"moo"]'))

    def test_StringIsDictionary_ReturnedValueIsADictionaryWithTheCorrectFields(self):
        field = IterField()

        self.assertEqual({"foo": "bar", "boo": ["moo", "maa"]}, field.to_python('{"foo":"bar", "boo":["moo","maa"]}'))