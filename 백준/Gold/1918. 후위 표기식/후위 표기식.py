import sys
from collections import deque

input = sys.stdin.readline

text = str(input())
N = len(text)
stack = deque()
prefix = ''

for char in text:
    if char.isalpha():
        prefix += char
    else:
        if char == '(':
            stack.append(char)
        elif char in ('+', '-'):
            while stack and stack[-1] != '(':
                prefix += stack.pop()
            stack.append(char)
        elif char in ('/', '*'):
            while stack and stack[-1] in ('/', '*'):
                prefix += stack.pop()
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                prefix += stack.pop()
            stack.pop()

while stack:
    prefix += stack.pop()

print(prefix)
