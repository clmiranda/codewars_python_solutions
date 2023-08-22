# Sums of Part => https://www.codewars.com/kata/5ce399e0047a45001c853c2b


def parts_sums(lst: list[int]) -> list[int]:
    total = sum(lst)
    arr_new = [total]
    for num in lst:
        total -= num
        arr_new.append(total)
    return arr_new
