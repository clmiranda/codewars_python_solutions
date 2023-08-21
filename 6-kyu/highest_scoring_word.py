# Highest Scoring Word => https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

import string

def high(phrase: str) -> str:
    list_values = []
    for word in phrase.split():
        acum = 0
        for chr in word:
            acum += string.ascii_lowercase.index(chr) + 1
        list_values.append(acum)
    return phrase.split()[list_values.index(max(list_values))]
