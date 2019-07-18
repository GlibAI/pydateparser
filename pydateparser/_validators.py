"""
Implements various validators.
"""


def _date_format_type_validator(instance, attribute, value):
    if value != None and not isinstance(value, list) and not isinstance(value, str):
        raise ValueError(
            "date_format attribute can be of type 'list' or 'None' or 'str'.")


def _end_year_validator(instance, attribute, value):
    if value < instance.start_year:
        raise ValueError(
            "'end_year' has to be greater than or equal to 'start_year'!")


def _positive_integer_validator(isinstance, attribute, value):
    if value < 0:
        raise ValueError("'year' should be positive integer.")
