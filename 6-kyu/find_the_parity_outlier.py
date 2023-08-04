# Find The Parity Outlier => https://www.codewars.com/kata/5526fc09a1bbd946250002dc


def find_outlier(integers):
    even_number, odd_number = [], []
    for i in integers:
        even_number.append(i) if i % 2 == 0 else odd_number.append(i)
    return even_number[0] if len(even_number) < len(odd_number) else odd_number[0]
