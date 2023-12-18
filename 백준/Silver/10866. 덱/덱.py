import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    v = input().split()
    order = v[0]
    if order == 'push_front':
        queue.appendleft(int(v[1]))
    elif order == 'push_back':
        queue.append(int(v[1]))
    elif order == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'pop_back':
        if queue:
            print(queue.pop())
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
