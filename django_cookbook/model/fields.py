import json

from django.core.exceptions import ValidationError
from django.db.models import TextField


class IterField(TextField):
    """
    Stores the an iterable object in the the database. The data is stored as JSON and so all the values given to the
    field must be serializable by the "json" module. This includes dict, list, tuple, str, int, float, True, False and
    None
    """

    def to_python(self, value):
        if isinstance(value, list):
            return value

        if not isinstance(value, str):
            raise ValidationError("Invalid input for a IterField instance")

        if not value:
            return []

        # We could store the data as a string representation of the iterable which we then "eval" but this would allow
        # for malicious data to be stores in the field so we need to do some sanity checking on the string. We let the
        # json library handle this.
        return json.loads(value)

    def get_prep_value(self, value):
        return json.dumps(value, separators=(',', ':'))


