# Which are in? => https://www.codewars.com/kata/550554fd08b86f84fe000a58

def in_array(array1: list[str], array2:list[str]) -> list[str]:
    return sorted(set(i for i in array1 if any(i in j for j in array2)))