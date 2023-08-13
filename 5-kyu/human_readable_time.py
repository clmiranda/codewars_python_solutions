# Human Readable Time => https://www.codewars.com/kata/52685f7382004e774f0001f7


def make_readable(seconds: int) -> str:
    if 0 <= seconds <= 59:
        return f"00:00:{seconds:02d}"
    elif 60 <= seconds <= 3599:
        MM = seconds // 60
        SS = seconds - (MM * 60)
        return f"00:{MM:02d}:{SS:02d}"
    else:
        HH = seconds // 3600
        AUX = seconds - HH * 3600
        MM = AUX // 60
        SS = AUX - MM * 60
        return f"{HH:02d}:{MM:02d}:{SS:02d}"
