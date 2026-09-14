# +1 Array => https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9

def up_array(arr: list[int]) -> list[int] | None:
    return (
        None
        if not arr or any(i < 0 or i > 9 for i in arr)
        else [int(d) for d in str(int("".join(map(str, arr))) + 1).zfill(len(arr))]
    )