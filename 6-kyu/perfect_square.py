# Perfect Square. => https://www.codewars.com/kata/584e93a70f60247eb8000132


def perfect_square(square):
    result = [i.count(".") for i in square.split("\n") if len(set(i.split("."))) == 1]
    return len(set(result)) == 1 and result[0] == len(result)
