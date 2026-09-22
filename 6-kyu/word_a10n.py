# Word a10n (abbreviation) => https://www.codewars.com/kata/5375f921003bf62192000746

import re

def abbreviate(sentence: str) -> str:
    return re.sub(
        r'[A-Za-z]{4,}',
        lambda x: f'{x.group()[0]}{len(x.group()) - 2}{x.group()[-1]}',
        sentence
    )