# Scramblies => https://www.codewars.com/kata/55c04b4cc56a697bb0000048

from collections import Counter


def scramble(str1: str, str2: str) -> bool:
    string1_counter, string2_counter = Counter(str1), Counter(str2)
    for chr in string2_counter:
        if string2_counter[chr] > string1_counter[chr]:
            return False
    return True
