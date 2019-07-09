from collections import namedtuple
from .errors import DateParserException
from .core_datetime_formats import DateTimeFormats


class DateTimeParser:
    """
    DateTime Adaptor class for DateParser
    """

    def __init__(self, text, start_year, end_year, datetime_format=None):
        self.text = text
        self.start_year = start_year
        self.end_year = end_year
        self._datetime_format = datetime_format
        if self._datetime_format == None:
            self._datetime_format = DateTimeFormats.FORMATS
        self._dateparser_formatter = self._format_datetime
        self.datetime = self._parser(self.text, self.start_year, self.end_year,
                                     self._datetime_format, self._dateparser_formatter)

    def __repr__(self):
        return f"DateTimeParser(start={self.start_year}, end={self.end_year}, format={self._datetime_format})"

    @staticmethod
    def _parser(text, start_year, end_year, datetime_format, formatter):
        DP = DateParser(datetime_format, start_year=start_year,
                        end_year=end_year)
        try:
            dt = DP.parse_string(text)
            _dt = [formatter(i) for i in dt]
            return _dt
        except DateParserException:
            return None

    @staticmethod
    def _format_datetime(datetime_object):
        _datetime = namedtuple(
            "datetime", ["date", "token_span", "token_index", "format"])
        return _datetime(datetime_object[0],
                         (datetime_object[1], datetime_object[2]),
                         (datetime_object[4], datetime_object[5]), datetime_object[3])
