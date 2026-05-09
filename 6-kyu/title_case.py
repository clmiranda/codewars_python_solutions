# Title Case => https://www.codewars.com/kata/5202ef17a402dd033c000009

def title_case(title, minor_words='') -> str:
    minor_words = minor_words.lower().split()
    return ' '.join(i.title() if i.lower() not in minor_words or idx == 0 else i.lower() for idx, i in enumerate(title.split()))

print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))