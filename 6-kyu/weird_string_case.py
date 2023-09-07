# WeIrD StRiNg CaSe => https://www.codewars.com/kata/52b757663a95b11b3d00062d


def to_weird_case(words: str) -> str:
    return " ".join(
        [
            "".join(
                word[i].upper() if i % 2 == 0 else word[i].lower()
                for i in range(len(word))
            )
            for word in words.split()
        ]
    )


print(to_weird_case("THIs iS a TEST"))
