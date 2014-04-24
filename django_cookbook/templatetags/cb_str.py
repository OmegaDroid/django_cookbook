"""
A set of useful string manipulation template tags
"""
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def nbsp(value):
    """
    Converts spaces in a string into non breaking spaces

    :param value: The String to convert
    :return: The converted string
    """
    return mark_safe("&nbsp;".join(value.split(' ')))

@register.filter()
def concat(left, right):
    """
    Concatenates the arguments as strings

    :param left: The left hand side of the concatenation
    :param right: The right hand side of the concatenation
    :return: The concatenated string (ie str(left)+str(right))
    """
    return str(left)+str(right)