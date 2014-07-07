import os
import pickle

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_cookbook.test.settings")

from django_cookbook.model.fields import IterField
from django.test import TestCase


class IterField_GetPrepValue(TestCase):
    def test_ValueIsAnEmptyList_StringIsEmptyList(self):
        field = IterField()
        value = []

        self.assertEqual(pickle.dumps(value), field.get_prep_value(value))

    def test_ValueIsAnEmptyDictionary_StringIsEmptyDict(self):
        field = IterField()
        value = {}

        self.assertEqual(pickle.dumps(value), field.get_prep_value(value))

    def test_ValueIsATuple_StringIsEmptyDict(self):
        field = IterField()
        value = (1, 2, 3)

        self.assertEqual(pickle.dumps(value), field.get_prep_value(value))

    def test_ValueIsListOfElements_StringIsJsonRepresentationOfThatListWithNoSpaces(self):
        field = IterField()
        value = [1, 2, 3, 4, 5]

        self.assertEqual(pickle.dumps(value), field.get_prep_value(value))

    def test_ValueIsListOfListsAndDictionaries_StringIsJsonRepresentationOfThatListWithNoSpaces(self):
        field = IterField()
        value = [[1, 2, 3], {4: 5}]

        self.assertEqual(pickle.dumps(value), field.get_prep_value(value))

    def test_ValueIsDictionaryOfElements_StringIsJsonRepresentationOfThatListWithNoSpaces(self):
        field = IterField()
        value = {1: 2, 3: 4, 5: 6}

        self.assertEqual(pickle.dumps(value), field.get_prep_value(value))

    def test_ValueIsDictionaryOfListsAndDictionaries_StringIsJsonRepresentationOfThatListWithNoSpaces(self):
        field = IterField()
        value = {1: {2: 3}, 4: [5, 6]}

        self.assertEqual(pickle.dumps(value), field.get_prep_value(value))

    def test_ValueIsTupleOfListsAndDictionaries_StringIsJsonRepresentationOfThatListWithNoSpaces(self):
        field = IterField()
        value = (0, {1: {2: 3}}, [4, 5, 6])

        self.assertEqual(pickle.dumps(value), field.get_prep_value(value))
