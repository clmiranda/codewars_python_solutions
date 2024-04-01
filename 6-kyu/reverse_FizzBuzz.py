# Reverse FizzBuzz => https://www.codewars.com/kata/5a622f5f85bef7a9e90009e2


def another_validation(string: str):
    if string == "Fizz":
        return [3]
    if string == "Buzz":
        return [5]
    if string == "FizzBuzz":
        return [15]
    if string == "Buzz Fizz":
        return [5, 6]
    if string == "Fizz Buzz":
        return [9, 10]
    else:
        return None


def reverse_fizzbuzz(string: str) -> list[int]:
    valid = another_validation(string)
    if valid:
        return valid
    lst = [int(i) if i.isdigit() else 0 for i in string.split()]
    first = 0
    for i in lst:
        if i != 0:
            first = i
            break
    first = first - lst.index(first) - 1
    return [first := first + 1 if i == 0 else i for i in lst]
