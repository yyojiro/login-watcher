# -*- coding: utf-8 -*-

import re
import dateutil.parser

auth_login_pattern = r'([(\w)]+[\s]+[\d]+ [\d]{2}:[\d]{2}:[\d]{2}) ' \
                     r'([\S]+) ([\S]+) ([\S]+) session opened for user ([\S]+) by ([\S]+)'
auth_logout_pattern = r'([(\w)]+[\s]+[\d]+ [\d]{2}:[\d]{2}:[\d]{2}) ' \
                      r'([\S]+) ([\S]+) ([\S]+) session closed for user ([\S]+)'

pattern_list = []
pattern_list.append({
    'event_type': 'login',
    'regexp': re.compile(auth_login_pattern)
})
pattern_list.append({
    'event_type': 'logout',
    'regexp': re.compile(auth_logout_pattern)
})


def text2data(raw_text):
    for pattern in pattern_list:
        match_obj = pattern['regexp'].search(raw_text)
        if match_obj:
            datetime = dateutil.parser.parse(match_obj.group(1))
            return {'timestamp': datetime,
                    'host': match_obj.group(2),
                    'user': match_obj.group(5),
                    'event_type':pattern['event_type']}
    return None
