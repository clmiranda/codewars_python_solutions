# Vowel one => https://www.codewars.com/kata/580751a40b5a777a200000a1


def vowel_one(string):
    return "".join("1" if i in "aeiou" else "0" for i in string.lower())
