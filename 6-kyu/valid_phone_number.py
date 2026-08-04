# Valid Phone Number => https://www.codewars.com/kata/525f47c79f2f25a4db000025

def valid_phone_number(n: str) -> bool:
    return len(n) == 14 and n[0] == '(' and n[4] == ')' and n[5] == ' ' and n[9] == '-' and n[1:4].isdigit() and n[6:9].isdigit() and n[10:14].isdigit()