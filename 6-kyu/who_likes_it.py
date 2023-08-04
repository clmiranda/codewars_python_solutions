# Who likes it? => https://www.codewars.com/kata/5266876b8f4bf2da9b000362


def likes(names):
    return (
        "no one likes this"
        if len(names) == 0
        else f"{names[0]} likes this"
        if len(names) == 1
        else f"{names[0]} and {names[1]} like this"
        if len(names) == 2
        else f"{names[0]}, {names[1]} and {names[2]} like this"
        if len(names) == 3
        else f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
    )
