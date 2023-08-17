# Sort the odd => https://www.codewars.com/kata/578aa45ee9fd15ff4600090d


def sort_array(numbers: list[int]) -> list[int]:
    odd_nums = iter(sorted([i for i in numbers if i % 2]))
    return [next(odd_nums) if i % 2 else i for i in numbers]
