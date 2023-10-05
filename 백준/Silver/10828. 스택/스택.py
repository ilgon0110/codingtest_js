import sys
from collections import deque

N = int(input())
orders = [list((input().split())) for _ in range(N)]

stack = deque()

for v in orders:
    if v[0] == 'push':
        stack.append(int(v[1]))
    elif v[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif v[0] == 'size':
        count = 0
        for i in stack:
            if int(i) == i:
                count += 1
        print(count)
    elif v[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif v[0] == 'top':
        if len(stack) > 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
