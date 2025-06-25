# Partial Word Searching => https://www.codewars.com/kata/54b81566cd7f51408300022d

def word_search(query: str, seq: list[str]) -> list[str]:
    query = query.lower()
    op = [c for c in seq if query in c.lower()]
    return op if len(op) > 0 else ["None"]