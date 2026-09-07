# Write Number in Expanded Form => https://www.codewars.com/kata/5842df8ccbd22792a4000245

def expanded_form(num: int) -> str:
    s = str(num)
    return ' + '.join(
        str(int(digit) * 10 ** (len(s) - i - 1))
        for i, digit in enumerate(s)
        if digit != '0'
    )