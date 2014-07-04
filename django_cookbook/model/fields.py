import pickle
from django.core.exceptions import ValidationError
from django.db.models import TextField, SubfieldBase
from six import with_metaclass


class IterField(with_metaclass(SubfieldBase, TextField)):
    """
    Stores an iterable object in the the database. All the values given to the field must be serializable by the "pickle" package.
    """

    def to_python(self, value):
        if isinstance(value, list) or isinstance(value, dict) or value is None:
            return value

        if not isinstance(value, bytes):
            raise ValidationError("Invalid input for a IterField instance")

        if not value:
            return []

        # We could store the data as a string representation of the iterable which we then "eval" but this would allow
        # for malicious data to be stores in the field so we need to do some sanity checking on the string. We let the
        # pickle library handle this.
        return pickle.loads(value)

    def get_prep_value(self, value):
        return pickle.dumps(value)


