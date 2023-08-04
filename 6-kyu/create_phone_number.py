# Create Phone Number => https://www.codewars.com/kata/525f50e3b73515a6db000b83


def create_phone_number(n):
    string = "".join(str(i) for i in n)
    return f"({string[0:3]}) {string[3:6]}-{string[6:]}"
