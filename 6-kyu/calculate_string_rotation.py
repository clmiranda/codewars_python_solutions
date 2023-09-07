# Calculate String Rotation => https://www.codewars.com/kata/5596f6e9529e9ab6fb000014


def shifted_diff(first: str, second: str) -> int:
    if first == second:
        return 0
    elif (
        first[::-1] == second
        or first.endswith(second[-3:])
        or len(first) != len(second)
    ):
        return -1
    else:
        try:
            return second.index(first[0])
        except:
            return -1
