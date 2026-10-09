# No ifs no buts => https://www.codewars.com/kata/592915cc1fad49252f000006

def no_ifs_no_buts(a: int, b: int) -> str:
    words = {-1: 'smaller than', 0: 'equal to', 1: 'greater than'}
    return f'{a} is {words[(a > b) - (a < b)]} {b}'