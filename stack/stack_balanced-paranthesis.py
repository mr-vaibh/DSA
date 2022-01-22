from collections import deque

def is_balanced(string):
    stack = deque()

    match = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
    }

    for char in string:
        if char in ('(', '[', '{'):
            stack.append(char)
        elif char in (')', ']', '}'):
            if len(stack) == 0:
                return False
            
            if match[char] == stack[-1]:
                stack.pop()
            else:
                return False

    return len(stack) == 0

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))