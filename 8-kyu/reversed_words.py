# Reversed Words => https://www.codewars.com/kata/51c8991dee245d7ddf00000e


def reverse_words(string):
    return " ".join(word for word in string.split()[::-1])
