# Moving Zeros To The End => https://www.codewars.com/kata/52597aa56021e91c93000cb0


def move_zeros(num_lst: list[int]) -> list[int]:
    new_lst = [num for num in num_lst if 0 != num]
    [new_lst.append(0) for _ in range(num_lst.count(0))]
    return new_lst
