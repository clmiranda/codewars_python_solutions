# Valid Braces => https://www.codewars.com/kata/5277c8a221e209d3f6000b56

def valid_braces(string: str) -> bool:
  braces = {')': '(', ']': '[', '}': '{'}
  stack = []

  for c in string:
        if c in braces.values():
            stack.append(c)
        elif c in braces:
            if not stack or stack.pop() != braces[c]:
                return False
  return not stack