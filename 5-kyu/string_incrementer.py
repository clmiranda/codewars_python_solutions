# String incrementer => https://www.codewars.com/kata/54a91a4883a7de5d7800009c

import re


def increment_string(string: str) -> str:
    searched = re.search(r"\d+$", string)
    if searched:
        length = len(searched.group())
        string = string[0:-length]
        return string + f"{int(searched.group()) + 1:0{length}d}"
    else:
        return f"{string}1"
