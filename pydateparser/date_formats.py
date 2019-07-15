""""
Defines various supported locale/types.

"""

from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class DateFormats:
    '''
    standard dateformats, according to the various locales.
    currently defines most comman formats for 'USA' & 'EU'.

    default formats: 

    {'USA': [
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
        '%m/%-d/%y',
        '%o of %B, %Y',
        '%B %o, %Y'
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
        '%-d/%m/%y',
        '%o of %B, %Y',
        '%B %o, %Y'
    ]}

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
        '%m/%-d/%y',
        '%o of %B, %Y',
        '%B %o, %Y',
        '%b %o, %Y'
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
        '%-d/%m/%y',
        '%o of %B, %Y',
        '%B %o, %Y',
        '%b %o, %Y'
    ]}
