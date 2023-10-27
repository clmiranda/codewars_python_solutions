def solution(arr: list[str], string: str = "") -> bool:
    if not arr:
        return True
    res = []
    for i in range(len(arr)):
        word = arr[i]
        sliced = arr[:i] + arr[i + 1 :]
        if string == "":
            res.append(solution(sliced, word))
        if string and word and word[-1] == string[0]:
            res.append(solution(sliced, word + string))
        elif word and string and word[0] == string[-1]:
            res.append(solution(sliced, string + word))
        else:
            res.append(False)
    return any(res)
