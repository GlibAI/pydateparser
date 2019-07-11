import attr
from .loggers import logger
from collections import namedtuple
from .errors import DateParserException
from .core_date_parser import DateParser
from .core_datetime_formats import DateTimeFormats
from ._validators import _datetime_format_type_validator, _end_year_validator, _mode_type_validator


@attr.s(slots=True)
class DateTimeParser:
    """
    Adaptor class for CoreDateParser
    """
    text = attr.ib(validator=attr.validators.instance_of(str))
    start_year = attr.ib(validator=attr.validators.instance_of(int))
    end_year = attr.ib(validator=attr.validators.instance_of(int))
    mode = attr.ib(default="date", validator=[
                   _mode_type_validator, attr.validators.instance_of(str)])
    datetime_format = attr.ib(
        default=None, validator=_datetime_format_type_validator)    

    def __attrs_post_init__(self):
        object.__setattr__(self, "datetime_format",
                           self.datetime_format_handler(self.datetime_format))

    @staticmethod
    def datetime_format_handler(datetime_format):
        if datetime_format == None:
            return DateTimeFormats.FORMATS
        else:
            return DateTimeFormats.FORMATS+datetime_format

    @staticmethod
    def _format_datetime(datetime_object):
        _datetime = namedtuple(
            "datetime", ["date", "token_span", "token_index", "format"])
        return _datetime(datetime_object[0], (datetime_object[1], datetime_object[2]),
                         (datetime_object[4], datetime_object[5]), datetime_object[3])

    @staticmethod
    def _parser(text, start_year, end_year, datetime_format, formatter):
        DP = DateParser(datetime_format, start_year=start_year,
                        end_year=end_year)
        try:
            logger.info('Extracting dates from the text.')
            dt = DP.parse_string(text)
            _dt = [formatter(i) for i in dt]
            return _dt
        except DateParserException:
            return None

    @property
    def datetime(self):
        return self._parser(self.text, self.start_year, self.end_year, self.datetime_format, self._format_datetime)
