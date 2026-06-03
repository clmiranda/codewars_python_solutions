# Does my number look big in this? => https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic(value) -> bool:
    value_len = len(str(value))
    return value == sum(int(x) ** value_len for x in str(value))