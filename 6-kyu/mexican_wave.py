# Mexican Wave -> https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(w: str) -> list[str]:
    return [w[:i] + w[i].upper() + w[i+1:] for i in range(len(w)) if w[i].isalpha()]