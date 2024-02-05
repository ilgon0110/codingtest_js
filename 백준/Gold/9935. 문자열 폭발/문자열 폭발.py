import sys
from collections import deque

input = sys.stdin.readline

text = input().rstrip()
bomb = input().rstrip()
stack = deque()

for char in text:
    stack.append(char)
    if len(stack) < len(bomb):
        continue
    tmp = []
    for i in range(len(stack)-1, len(stack)-len(bomb)-1, -1):
        tmp.append(stack[i])
    tmp = ''.join(reversed(tmp))
    if tmp == bomb:
        for i in range(len(stack)-1, len(stack)-len(bomb)-1, -1):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
