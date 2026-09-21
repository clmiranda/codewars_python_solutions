# N-th Fibonacci => https://www.codewars.com/kata/522551eee9abb932420004a0

def nth_fib(n: int) -> int:
    x, y = 0, 1
    for _ in range(n - 1):
        x, y = y, x + y
    return x