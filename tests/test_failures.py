import unittest
from collections import namedtuple
from pydateparser import DateParser

_date = namedtuple("DATE", ["date", "token_span", "token_index", "format"])

texts = {'S1': 'Tomorrow is January 01 2019.',
         'S2': 'entries are due by January 04, 2017 at 8:00pm',
         'S3': 'created 01/15/2005 by ACME Inc. and associates.',
         'S4': 'Dec.01.2015 - Dec 31 2015 - Dec,12,2015 - Dec,12,2015 - Dec,12th,2015 '}


class TestDateParserExpectedFailures(unittest.TestCase):

    @unittest.expectedFailure
    def input_failure_1(self):
        d = DateParser(text=texts.get('S1'),
                       start_year=2019.0, end_year=2019.0)
        expected_output = [_date(date='january 01 2019', token_span=(
            12, 27), token_index=(4, 4), format='%B %d %Y')]
        self.assertNotEqual(d.date, expected_output, 'should be equal.')

    @unittest.expectedFailure
    def input_failure_2(self):
        d = DateParser(text=texts.get('S1'),
                       start_year='2019', end_year='2019')
        expected_output = [_date(date='january 01 2019', token_span=(
            12, 27), token_index=(4, 4), format='%B %d %Y')]
        self.assertEqual(d.date, expected_output, 'should be equal.')

    @unittest.expectedFailure
    def input_failure_3(self):
        d = DateParser(text='', start_year=2019, end_year=2019)
        expected_output = [_date(date='january 01 2019', token_span=(
            12, 27), token_index=(4, 4), format='%B %d %Y')]
        self.assertEqual(d.date, expected_output, 'should be equal.')

    @unittest.expectedFailure
    def input_failure_4(self):
        d = DateParser(text=[texts.get('S1'), texts.get(
            'S2')], start_year=2019, end_year=2019)
        expected_output = [_date(date='january 01 2019', token_span=(
            12, 27), token_index=(4, 4), format='%B %d %Y')]
        self.assertEqual(d.date, expected_output, 'should be equal.')

    @unittest.expectedFailure
    def input_failure_5(self):
        d = DateParser(text=texts.get('S1'),
                       start_year=2019, end_year=2019, locale=[])
        expected_output = [_date(date='january 01 2019', token_span=(
            12, 27), token_index=(4, 4), format='%B %d %Y')]
        self.assertEqual(d.date, expected_output, 'should be equal.')

    @unittest.expectedFailure
    def input_failure_6(self):
        d = DateParser(text=texts.get('S1'),
                       start_year=2019, end_year=2019, locale='')
        expected_output = [_date(date='january 01 2019', token_span=(
            12, 27), token_index=(4, 4), format='%B %d %Y')]
        self.assertEqual(d.date, expected_output, 'should be equal.')

    @unittest.expectedFailure
    def input_failure_7(self):
        d = DateParser(text=texts.get('S1'),
                       start_year=2019, end_year=2019, locale='IND')
        expected_output = [_date(date='january 01 2019', token_span=(
            12, 27), token_index=(4, 4), format='%B %d %Y')]
        self.assertEqual(d.date, expected_output, 'should be equal.')

    @unittest.expectedFailure
    def input_failure_8(self):
        d = DateParser(text=texts.get('S1'),
                       start_year=2019, end_year=2019, locale='YMD')
        expected_output = [_date(date='january 01 2019', token_span=(
            12, 27), token_index=(4, 4), format='%B %d %Y')]
        self.assertEqual(d.date, expected_output, 'should be equal.')


if __name__ == '__main__':
    unittest.main(verbosity=4)
