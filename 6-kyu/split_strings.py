# Split Strings => https://www.codewars.com/kata/515de9ae9dcfc28eb6000001


def solution(string):
    result = [string[i : i + 2] for i in range(0, len(string), 2)]
    if len(string) % 2 == 1:
        result[-1] += "_"
    return result
