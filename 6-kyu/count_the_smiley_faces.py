# Count the smiley faces => https://www.codewars.com/kata/583203e6eb35d7980400002a


def count_smileys(arr: list):
    return len(
        [
            i
            for i in arr
            if (i[0] in [":", ";"] and i[-1] in [")", "D"])
            if (len(i) == 2) or (len(i) == 3 and i[1] in ["-", "~"])
        ]
    )
