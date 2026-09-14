# Backspaces in string => https://www.codewars.com/kata/5727bb0fe81185ae62000ae3

def clean_string(s: str) -> str:
    lst = []
    for char in s:
        if char == '#':
            if lst:
                lst.pop()
        else:
            lst.append(char)
    return ''.join(lst)