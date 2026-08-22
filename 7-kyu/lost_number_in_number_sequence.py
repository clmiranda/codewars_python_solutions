# Lost number in number sequence => https://www.codewars.com/kata/595aa94353e43a8746000120

def find_deleted_number(arr: list[int], mixed_arr: list[int]) -> int:
   return sum(arr) - sum(mixed_arr)