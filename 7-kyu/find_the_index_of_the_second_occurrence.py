# Find the index of the second occurrence of a letter in a string =>
# https://www.codewars.com/kata/63f96036b15a210058300ca9


def second_symbol(s, letter):
    return s.find(letter, s.find(letter) + 1)
