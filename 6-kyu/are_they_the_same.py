# Are they the "same"? => https://www.codewars.com/kata/550498447451fbbd7600041c


def comp(array1: list[int], array2: list[int]) -> bool:
    if array1 and array2 or array1 == array2:
        array1 = [i * i for i in array1]
        return sorted(array1) == sorted(array2)
    return False
