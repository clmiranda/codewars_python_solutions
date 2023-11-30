# What's A Name In? => https://www.codewars.com/kata/59daf400beec9780a9000045


def name_in_str(strng: str, name: str) -> bool:
    j, c = 0, 0
    for i in strng.lower():
        if j == len(name):
            break
        if name.lower()[j] == i:
            c += 1
            j += 1
    return True if c == len(name) else False
