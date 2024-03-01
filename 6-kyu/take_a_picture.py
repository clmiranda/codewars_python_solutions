# Take a picture ! => https://www.codewars.com/kata/56c9f47b0844d85f81000fc2


def sort_photos(pics: list[str]) -> list[str]:
    lst = [(i[0:4], i[5:]) for i in pics]
    lst.sort(key=lambda x: (int(x[0]), int("".join(c for c in x[1] if c.isdigit()))))
    lst = [f"{i[0]}.{i[1]}" for i in lst][-5:]
    number = int("".join([i for i in lst[-1][5:] if i.isdigit()]))
    lst.append(f"{lst[-1][:-len(str(number))]}{number + 1}")
    return lst
