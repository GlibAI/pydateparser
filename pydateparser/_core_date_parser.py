import re
import copy


class CoreDateParser:
    def __init__(self, formats, start_year=1900, end_year=2100):
        self.formats = formats
        self.start_year = start_year
        self.end_year = end_year
        self.values = self.get_values()
        self.patterns = self.get_patterns()

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

    def get_ordinals(self):
        return ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th", 
        "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]
        
    def get_year_value(self, start_year=1900, end_year=2100, n_digits=4):
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

    def find_repeat_matches(self, query_string, sub_string, pattern):
        qs = copy.deepcopy(query_string)
        ret_list = []
        while True:
            orig_string = copy.deepcopy(qs)
            flag = False
            if sub_string in orig_string:
                ret_list.append((sub_string, orig_string.index(
                    sub_string), orig_string.index(sub_string) + len(sub_string), pattern))
                qs = copy.deepcopy(orig_string[:orig_string.index(sub_string)] + " "*len(
                    sub_string) + orig_string[orig_string.index(sub_string) + len(sub_string):])
                flag = True
            if not flag:
                break
        return ret_list

    def parse_string(self, query_string):
        query_string = query_string.lower()
        matches = {}
        for k in self.patterns:
            for v in self.patterns[k]:
                if v in query_string:
                    if k not in matches:
                        matches[k] = []
                    matches[k] += self.find_repeat_matches(query_string, v, k)
        priority_matches = self.priority_matches(matches)
        if len(priority_matches.keys()) > 0:
            token_spans = self.get_token_spans(query_string)
            match_tokens = self.get_match_tokens(priority_matches, token_spans)
            return match_tokens
        return None

    def get_match_tokens(self, priority_matches, token_spans):
        ret_list = []
        for key in priority_matches:
            for pm in priority_matches[key]:
                char_start = pm[1]
                char_end = pm[2]
                start_token = 1000
                end_token = -1
                for idx in token_spans:
                    if (char_start > token_spans[idx][1] and char_start < token_spans[idx][2]) or (char_end > token_spans[idx][1] and char_end < token_spans[idx][2]):
                        start_token = min(start_token, token_spans[idx][3])
                        end_token = max(end_token, token_spans[idx][3])
                ret_list.append(list(pm) + [start_token, end_token])
        ret_list = sorted(ret_list, key=lambda x: x[2]-x[1], reverse=True)
        final_ret_list = []
        for rl in ret_list:
            flag = False
            for frl in final_ret_list:
                if (frl[1] <= rl[1] and frl[2] > rl[2]) or (frl[1] < rl[1] and frl[2] >= rl[2]):
                    flag = True
                    break
            if not flag:
                final_ret_list.append(rl)
        return final_ret_list

    def priority_matches(self, matches):
        unique_found_formats = []
        found_formats = matches.keys()
        found_formats = sorted(
            found_formats, key=lambda x: len(x), reverse=True)
        for f in found_formats:
            flag = False
            for uf in unique_found_formats:
                if f in uf:
                    flag = True
                    break
            if not flag:
                unique_found_formats.append(f)
        return {k: matches[k] for k in unique_found_formats}

    def get_token_spans(self, query_string):
        query_string = query_string.lower()
        tokens = query_string.split()
        ret_obj = {}
        for idx, k in enumerate(tokens):
            ret_obj[idx] = (k, query_string.index(
                k), query_string.index(k) + len(k), idx)
            query_string = query_string[:query_string.index(
                k)] + " "*len(k) + query_string[query_string.index(k) + len(k):]
        return ret_obj
