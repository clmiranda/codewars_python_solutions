# Your order, please => https://www.codewars.com/kata/55c45be3b2079eccff00010f


def order(sentence: str) -> str:
    return " ".join(
        sorted(sentence.split(), key=lambda x: [i for i in x if i.isdigit()])
    )
