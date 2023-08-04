# Consecutive strings => https://www.codewars.com/kata/56a5d994ac971f1ac500003e


def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""
    new_strarr = ["".join(strarr[index : index + k]) for index in range(len(strarr))]
    return max([string for string in new_strarr], key=lambda string: len(string))
