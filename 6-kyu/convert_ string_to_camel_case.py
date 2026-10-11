# Convert string to camel case => https://www.codewars.com/kata/517abf86da9663f1d2000003

import re


def to_camel_case(text):
    lst = re.split("_|-", text)
    return "".join(lst[i].title() if i > 0 else lst[i] for i in range(len(lst)))
