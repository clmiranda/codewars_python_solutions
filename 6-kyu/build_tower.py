# Build Tower -> https://www.codewars.com/kata/576757b1df89ecf5bd00073b

def tower_builder(n_floors: int) -> list[str]:
    if n_floors == 0:
        return []
    lst = []
    for i in range(n_floors):
        stars = '*' * (2 * i + 1)
        spaces = ' ' * (n_floors - i - 1)
        lst.append(spaces + stars + spaces)
    return lst