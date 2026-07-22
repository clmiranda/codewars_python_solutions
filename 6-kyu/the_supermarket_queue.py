# The Supermarket Queue -> https://www.codewars.com/kata/57b06f90e298a7b53d000a86

def queue_time(customers: list[int], n: int) -> int:
    tills = [0] * n
    for customer in customers:
        i = tills.index(min(tills))
        tills[i] += customer
    return max(tills)