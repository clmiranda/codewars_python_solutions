# Populate hash with array keys and default value => https://www.codewars.com/kata/51c38e14ea1c97ffaf000003


def populate_dict(keys: list, default) -> dict:
    return {x: default for x in keys}
