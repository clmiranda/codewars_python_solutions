# Sorting Dictionaries => https://www.codewars.com/kata/53da6a7e112bd15cbc000012


def sort_dict(d: dict):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)
