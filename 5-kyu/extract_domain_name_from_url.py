# Extract the domain name from a URL => https://www.codewars.com/kata/514a024011ea4fb54200004b


def domain_name(url: str) -> str:
    for separator in ["//", "www", "."]:
        url = " ".join(url.split(separator))
    splitted = url.split()
    return splitted[1] if splitted[0].startswith("http") else splitted[0]
