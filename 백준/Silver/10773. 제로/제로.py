import sys
from collections import deque

K = int(input())
arr = [int(input()) for _ in range(K)]

stack = deque()

for v in arr:
    if v == 0:
        stack.pop()
    else:
        stack.append(v)

print(sum(stack))
