def _datetime_format_type_validator(instance, attribute, value):
    if value != None and not isinstance(value, list):
        raise ValueError(
            "datetime_format attribute can be of type 'list' or 'None'.")


def _mode_type_validator(instance, attribute, value):
    if value not in ["date", "datetime", "time"]:
        raise ValueError(
            "mode attribute's format can be of type 'date', 'time' or 'datetime'.")


def _end_year_validator(instance, attribute, value):
    if value < instance.start_year:
        raise ValueError(
            "'end_year' has to be greater than or equal to 'start_year'!")
