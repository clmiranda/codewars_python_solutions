# Pete, the baker => https://www.codewars.com/kata/525c65e51bf619685c000059


def cakes(recipe: dict, available: dict):
    if set(recipe) <= set(available):
        counter = 0
        while True:
            for key, value in recipe.items():
                if available[key] >= value:
                    available[key] -= value
                else:
                    return counter
            counter += 1
    return 0
