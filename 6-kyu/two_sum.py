# Two Sum => https://www.codewars.com/kata/52c31f8e6605bcc646000082

def two_sum(numbers, target):
    seen = {}
    for index, num in enumerate(numbers):
        c = target - num
        if c in seen:
            return tuple([seen[c], index])
        seen[num] = index