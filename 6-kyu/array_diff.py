# Array.diff => https://www.codewars.com/kata/523f5d21c841566fde000009


def array_diff(arr_a, arr_b):
    if arr_a == [] or arr_b == []:
        return arr_a
    else:
        return [value for value in arr_a if value not in arr_b]
