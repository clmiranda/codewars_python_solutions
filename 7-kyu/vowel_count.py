# Vowel Count => https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence: str) -> int:
    return len([i for i in sentence if i in 'aeiou'])