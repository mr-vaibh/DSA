from collections import deque

def reverse_string(string):
    stack = deque()

    for char in string:
        stack.append(char)
    
    new_string = ""
    
    while len(stack) != 0:
        new_string += stack.pop()
    
    return new_string


print(reverse_string('We will conquer COVID-19'))