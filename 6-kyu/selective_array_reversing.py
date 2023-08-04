# Selective Array Reversing => https://www.codewars.com/kata/58f6000bc0ec6451960000fd


def sel_reverse(array, length):
    return (
        [j for i in range(0, len(array), length) for j in array[i : i + length][::-1]]
        if length != 0
        else array
    )
