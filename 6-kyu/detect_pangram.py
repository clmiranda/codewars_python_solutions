# Detect Pangram => https://www.codewars.com/kata/545cedaa9943f7fe7b000048


def is_pangram(string):
    string = "".join(x for x in string if x.isalpha())
    return False if len(set(string.lower())) < 26 else True
