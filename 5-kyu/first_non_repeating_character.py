# First non-repeating character => https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

def first_non_repeating_letter(s: str) -> str:
    return [i for i in s if s.lower().count(i.lower()) == 1][0] if any(s.lower().count(i.lower()) == 1 for i in s) else ''