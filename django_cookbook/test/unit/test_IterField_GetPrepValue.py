import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_cookbook.test.settings")

from django_cookbook.model.fields import IterField
from django.test import TestCase


class IterField_GetPrepValue(TestCase):
    def test_ValueIsAnEmptyList_StringIsEmptyList(self):
        field = IterField()

        self.assertEqual("[]", field.get_prep_value([]))

    def test_ValueIsAnEmptyDictionary_StringIsEmptyDict(self):
        field = IterField()

        self.assertEqual("{}", field.get_prep_value({}))

    def test_ValueIsListOfElements_StringIsJsonRepresentationOfThatListWithNoSpaces(self):
        field = IterField()

        self.assertEqual("[1,2,3,4,5]", field.get_prep_value([1, 2, 3, 4, 5]))

    def test_ValueIsListOfListsAndDictionaries_StringIsJsonRepresentationOfThatListWithNoSpaces(self):
        field = IterField()

        self.assertEqual("[[1,2,3],{\"4\":5}]", field.get_prep_value([[1, 2, 3], {4: 5}]))

    def test_ValueIsDictionaryOfElements_StringIsJsonRepresentationOfThatListWithNoSpaces(self):
        field = IterField()

        self.assertEqual("{\"1\":2,\"3\":4,\"5\":6}", field.get_prep_value({1: 2, 3: 4, 5: 6}))

    def test_ValueIsDictionaryOfListsAndDictionaries_StringIsJsonRepresentationOfThatListWithNoSpaces(self):
        field = IterField()

        self.assertEqual("{\"1\":{\"2\":3},\"4\":[5,6]}", field.get_prep_value({1: {2: 3}, 4: [5, 6]}))
