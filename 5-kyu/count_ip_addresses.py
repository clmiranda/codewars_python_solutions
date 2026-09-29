# Count IP Addresses => https://www.codewars.com/kata/526989a41034285187000de4

import ipaddress

def ips_between(start: str, end: str) -> int:
    return int(ipaddress.IPv4Address(end)) - int(ipaddress.IPv4Address(start))