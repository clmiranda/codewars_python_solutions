# Simple Pig Latin => https://www.codewars.com/kata/520b9d2ad5c005041100000f


def pig_it(text: str) -> str:
    return " ".join(f"{i[1:]}{i[0]}ay" if i.isalpha() else i for i in text.split())
