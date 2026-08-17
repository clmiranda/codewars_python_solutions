# Reverse or rotate? => https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991

def rev_rot(string: str, sz: int) -> str:
    if sz <= 0 or sz > len(string):
        return ""
    
    r = []
    for i in range(0, len(string) - sz + 1, sz):
        chunk = string[i:i + sz]
        if sum(int(x) for x in chunk) % 2 == 0:
            r.append(chunk[::-1])
        else:
            r.append(chunk[1:] + chunk[0])
    return "".join(r)