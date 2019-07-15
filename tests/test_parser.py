import unittest
from collections import namedtuple
from pydateparser import DateParser

_date = namedtuple("DATE", ["date", "token_span", "token_index", "format"])

texts = {'S1': 'Tomorrow is January 01 2019.',
         'S2': 'entries are due by January 04, 2017 at 8:00pm',
         'S3': 'created 01/15/2005 by ACME Inc. and associates.',
         'S4': 'Dec.01.2015 - Dec 31 2015 - Dec,12,2015 - Dec,12,2015 - december 12th, 2015 '}


class TestDateParserInputs(unittest.TestCase):

    def test_date_parser(self):
        d1 = DateParser(text=texts.get(
            'S1'), start_year=2019, end_year=2019)
        o1 = [_date(date='january 01 2019', token_span=(
            12, 27), token_index=(4, 4), format='%B %d %Y')]
        self.assertEqual(d1.date, o1, 'should be equal.')

        d2 = DateParser(text=texts.get(
            'S2'), start_year=2019, end_year=2019)
        o2 = None
        self.assertEqual(d2.date, o2, 'should be equal.')

        d3 = DateParser(text=texts.get(
            'S2'), start_year=2016, end_year=2019)
        o3 = [_date(date='january 04, 2017', token_span=(
            19, 35), token_index=(1000, -1), format='%B %d, %Y')]
        self.assertEqual(d3.date, o3, 'should be equal.')

        d4 = DateParser(text=texts.get('S1'), start_year=2019, end_year=2019)
        d5 = DateParser(text=texts.get('S1'), start_year=2019, end_year=2019)
        self.assertEqual(d4, d5, 'should be equal.')

        d6 = DateParser(text=texts.get('S4'), start_year=2015, end_year=2019)
        o4 = [_date(date='december 12th, 2015', token_span=(56, 75), token_index=(1000, -1), format='%B %o, %Y'), 
            _date(date='dec 31 2015', token_span=(14, 25), token_index=(1000, -1), format='%b %-d %Y'), 
            _date(date='dec 31 2015', token_span=(14, 25), token_index=(1000, -1), format='%b %d %Y')]
        self.assertEqual(d6.date, o4, 'should be equal.')


if __name__ == '__main__':
    unittest.main()
