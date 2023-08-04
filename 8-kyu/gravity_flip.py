# Gravity Flip => https://www.codewars.com/kata/5f70c883e10f9e0001c89673


def flip(direction, array):
    return sorted(array) if direction == "R" else sorted(array, reverse=True)
