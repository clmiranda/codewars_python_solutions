# Arithmetic progression => https://www.codewars.com/kata/55caf1fd8063ddfa8e000018


def arithmetic_sequence_elements(a, d, n):
    result = []
    for _ in range(n):
        result.append(str(a))
        a += d
    return ", ".join(result)
