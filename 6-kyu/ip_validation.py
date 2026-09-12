# IP Validation => https://www.codewars.com/kata/515decfd9dcfc23bb6000006

def is_valid_IP(s: str) -> bool:
    return all(x.isdigit() and (x == '0' or not x.startswith('0')) and 0 <= int(x) <= 255 for x in s.split('.')) and len(s.split('.')) == 4