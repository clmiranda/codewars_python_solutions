# Ranking System => https://www.codewars.com/kata/58e16de3a312d34d000000bd

def rankings(arr: list[int]) -> list[int]:
    arr2, arr3 = sorted(arr, reverse=True), [0] * len(arr)
    for i in range(1, len(arr) + 1):
        arr3[arr.index(arr2[i - 1])] = i
    return arr3
