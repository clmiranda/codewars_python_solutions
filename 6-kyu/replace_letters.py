# Replace letters => https://www.codewars.com/kata/5a4331b18f27f2b31f000085


def replace_letters(word: str):
    vowels, consonants = ["a", "e", "i", "o", "u"], [
        "bcd",
        "fgh",
        "jklmn",
        "pqrst",
        "vwxyz",
    ]
    new_word = ""
    for character in word:
        for index, value in enumerate(consonants):
            if character in value:
                if index == len(consonants) - 1:
                    new_word += vowels[0]
                else:
                    new_word += vowels[index + 1]
                break
            elif character in vowels[index]:
                new_word += consonants[index - 1][-1]
                break
    return new_word
