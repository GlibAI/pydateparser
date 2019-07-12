""""
Defines various supported locale/types
"""


class DateFormats:
    '''
    standard dateformats, according to the various locales.
    '''
    locale = {'USA': [
        '%b %d %Y',
        '%b %-d %Y',
        '%b %d, %Y',
        '%b %-d, %Y',
        '%B %d, %Y',
        '%B %-d, %Y',
        '%B %d %Y',
        '%B %-d %Y',
        '%m/%d/%Y',
        '%m/%-d/%Y',
        '%m/%d/%y',
        '%m/%-d/%y'
    ],
        'EU': [
        '%b %d %Y',
        '%b %-d %Y',
        '%b %d, %Y',
        '%b %-d, %Y',
        '%B %d, %Y',
        '%B %-d, %Y',
        '%B %d %Y',
        '%B %-d %Y',
        '%d/%m/%Y',
        '%-d/%m/%Y',
        '%d/%m/%y',
        '%-d/%m/%y'
    ]}
