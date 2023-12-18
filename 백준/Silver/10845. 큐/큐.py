import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    v = input().split()
    order = ''
    if v[0] == 'push':
        order = v[0]
        target = v[1]
        queue.append(target)
    else:
        order = v[0]
    if order == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
