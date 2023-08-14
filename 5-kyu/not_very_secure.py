# Not very secure => https://www.codewars.com/kata/526dbd6c8c0eb53254000110


def alphanumeric(password: str) -> bool:
    return 0 < len([chr for chr in password if chr.isalnum()]) == len(password)
