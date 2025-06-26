# Ones and Zeros => https://www.codewars.com/kata/578553c3a1b8d5c40300037c

def binary_array_to_number(arr: list[int]) -> int:
    return int(''.join([str(x) for x in arr]), 2)