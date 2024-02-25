# Simple Simple Simple String Expansion => https://www.codewars.com/kata/5ae326342f8cbc72220000d2

import re


def string_expansion(string: str) -> str:
    if not string:
        return ""
    lst = re.findall(r"\d[a-zA-Z]+|\D+", string)
    result = ""
    for value in lst:
        if len(value) == 2:
            if value[0].isdigit():
                result += int(value[0]) * value[1]
            else:
                result += value
        else:
            if value[0].isdigit():
                result += "".join([int(value[0]) * j for j in value[1:]])
            else:
                result += value
    return result
