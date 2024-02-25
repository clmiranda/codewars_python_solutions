# Clever split => https://www.codewars.com/kata/5992e11d6ca73b38d50000f0


def clever_split(s: str) -> list[str]:
    r, lst, flag = "", [], False
    for i in s.split():
        if i.startswith("[") or flag:
            r += f"{i} "
            flag = True
            if i.endswith("]"):
                lst.append(r[:-1])
                r, flag = "", False
        else:
            lst.append(i)
    return lst
