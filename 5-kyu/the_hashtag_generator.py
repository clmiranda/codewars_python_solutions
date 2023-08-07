# The Hashtag Generator => https://www.codewars.com/kata/52449b062fb80683ec000024


def generate_hashtag(text: str) -> str | bool:
    return (
        "#" + "".join(word.capitalize() for word in text.split())
        if 0 < len(text) <= 140
        else False
    )
