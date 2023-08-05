# Counting Duplicates => https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1


def duplicate_count(text: str) -> int:
    text = text.lower()
    return len([i for i in set(text) if text.count(i) > 1])
