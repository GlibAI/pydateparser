import attr
from ._loggers import logger
from collections import namedtuple
from .date_formats import DateFormats
from ._errors import DateParserException
from ._core_date_parser import CoreDateParser
from ._validators import _date_format_type_validator, _end_year_validator


@attr.s(slots=True)
class DateParser:
    """
    CoreDateParser Adapter class.
    """
    text = attr.ib(validator=attr.validators.instance_of(str))
    start_year = attr.ib(validator=attr.validators.instance_of(int))
    end_year = attr.ib(validator=attr.validators.instance_of(int))
    locale = attr.ib(default=None, validator=_date_format_type_validator)

    def __attrs_post_init__(self):
        object.__setattr__(self, "locale", self._date_format_handler(self.locale))

    @staticmethod
    def _date_format_handler(locale):
        if locale == None:
            return DateFormats.locale.get('USA')
        elif locale != None and isinstance(locale, str) and locale in DateFormats.locale.keys():
            return DateFormats.locale.get(locale)
        else:
            return locale

    @staticmethod
    def _format_date(date_object):
        _date = namedtuple("DATE", ["date", "token_span", "token_index", "format"])
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
        except DateParserException:
            return None

    @property
    def date(self):
        return self._parser(self.text, self.start_year, self.end_year, self.locale, self._format_date)