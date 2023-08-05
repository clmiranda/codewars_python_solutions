# Replace With Alphabet Position => https://www.codewars.com/kata/546f922b54af40e1e90001da


def alphabet_position(text: str) -> str:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    return " ".join(str(ALPHABET.index(i) + 1) for i in text.lower() if i.isalpha())
