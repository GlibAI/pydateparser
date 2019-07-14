""""
Date Parser Adapter.

"""

import attr
from ._loggers import logger
from collections import namedtuple
from .date_formats import DateFormats
from ._errors import DateParserException
from ._utils import _date_format_handler
from ._core_date_parser import CoreDateParser
from ._validators import _positive_integer_validator
from ._validators import _date_format_type_validator, _end_year_validator


_attributes = {'text': attr.ib(validator=attr.validators.instance_of(str)),
               'start_year': attr.ib(validator=[attr.validators.instance_of(int),
                                                _positive_integer_validator]),
               'end_year': attr.ib(validator=[attr.validators.instance_of(int),
                                              _end_year_validator,
                                              _positive_integer_validator]),
               'locale': attr.ib(default=None,
                                 validator=_date_format_type_validator,
                                 converter=_date_format_handler)}


@attr.s(slots=True, these=_attributes)
class DateParser:
    """
    CoreDateParser Adapter class.

    Parameters
    ----------

    text: str
        a string/text document from which we can extract dates.

    start_year: int
        define the start year from which to look for the date.

    end_year: int
        define the end year from which to look for the date.

    locale: None, str, list
        define the type of dateformat(currently supports 'USA', 'EU'), default is None.
        or pass your own list of patterns.

    Returns
    -------
    list
        list of `DATE` objects.

    Note
    ----
        DATE is a namedtuple, which gives out the actual extracted `date`, 
        `token_span`, `token_index` and `format` (matched format) items.

    """
    @staticmethod
    def _format_date(date_object):
        _date = namedtuple(
            "DATE", ["date", "token_span", "token_index", "format"])
        return _date(date_object[0], (date_object[1], date_object[2]),
                     (date_object[4], date_object[5]), date_object[3])

    @staticmethod
    def _parser(text, start_year, end_year, locale, formatter):
        DP = CoreDateParser(locale, start_year=start_year, end_year=end_year)
        try:
            logger.info('Extracting dates from the text.')
            dt = DP.parse_string(text)
            _dt = [formatter(i) for i in dt]
            return _dt
        except Exception:
            return None

    @property
    def date(self):
        return self._parser(self.text, self.start_year, self.end_year, self.locale, self._format_date)
