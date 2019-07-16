"""
utility functions and helpers are defined here.
"""

from .date_formats import DateFormats


def _date_format_handler(locale):
    if locale == None:
        return DateFormats.locale.get('USA')
    elif locale != None and isinstance(locale, str) and locale in DateFormats.locale.keys():
        return DateFormats.locale.get(locale)
    else:
        return locale
