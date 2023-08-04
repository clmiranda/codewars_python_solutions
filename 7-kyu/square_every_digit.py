# Square Every Digit => https://www.codewars.com/kata/546e2562b03326a88e000020


def square_digits(number):
    return int("".join([str(i**2) for i in list(map(int, str(number)))]))
