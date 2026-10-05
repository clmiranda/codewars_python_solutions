# Maximum subarray sum => https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr: list[int]) -> int:
    x = 0
    y = 0
    for i in arr:
        x = max(0, x + i)
        y = max(y, x)
    return y