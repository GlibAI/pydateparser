"""
core date patterns generator class
"""

import re
import copy


class CoreDatePatternGenerator:

    def __init__(self, formats, start_year=1900, end_year=2100):
        self.formats = formats
        self.start_year = start_year
        self.end_year = end_year
        self.values = self.get_values()
        self.patterns = self.get_patterns()

    def get_values(self):
        values = {
            "%b": ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],
            "%d": self.get_dates(n_digits=2),
            "%-d": self.get_dates(),
            "%Y": self.get_year_value(start_year=self.start_year, end_year=self.end_year),
            "%B": ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"],
            "%m": self.get_months(),
            "%-m": self.get_months(n_digits=1),
            "%y": self.get_year_value(start_year=self.start_year, end_year=self.end_year, n_digits=2),
            "%o": self.get_ordinals()
        }
        return values

    def get_patterns(self):
        final_patterns = {}
        for fmat in self.formats:
            patterns = []
            present_sub_formats = []
            for v in self.values:
                if v in fmat:
                    present_sub_formats.append(v)
            i = 0
            while(i < len(present_sub_formats)):
                v = present_sub_formats[i]
                if len(patterns) == 0:
                    for val in self.values[v]:
                        patterns.append(fmat.replace(v, val))
                else:
                    new_patterns = []
                    for p in patterns:
                        for val in self.values[v]:
                            new_patterns.append(p.replace(v, val))
                    patterns = copy.deepcopy(new_patterns)
                i += 1
            final_patterns[fmat] = {k: None for k in sorted(patterns)}
        return final_patterns

    def get_ordinals(self):
        return ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th",
                "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]

    def get_year_value(self, start_year, end_year, n_digits=4):
        if n_digits == 4:
            return [str(d) for d in range(start_year, end_year+1)]
        else:
            if end_year - start_year >= 100:
                return ["{:02d}".format(d) for d in range(0, 100)]
            else:
                return ["{:02d}".format(int(str(d)[2:])) for d in range(start_year, end_year+1)]

    def get_dates(self, n_digits=1):
        if n_digits == 1:
            return [str(d) for d in range(1, 32)]
        else:
            return ["{:02d}".format(d) for d in range(1, 32)]

    def get_months(self, n_digits=2):
        if n_digits == 2:
            return ["{:02d}".format(d) for d in range(1, 13)]
        else:
            return [str(d) for d in range(1, 13)]
