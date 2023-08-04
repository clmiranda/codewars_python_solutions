# Simple Fun #154: Zero And One => https://www.codewars.com/kata/58ad09d6154165a1c80000d1


def zero_and_one(string: str):
    return len(string.replace("01", "").replace("10", ""))
