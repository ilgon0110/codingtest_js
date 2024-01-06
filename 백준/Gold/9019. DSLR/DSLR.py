import sys
from collections import deque

T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    queue = deque()
    queue.append([A, ''])
    visited = [False for i in range(10001)]
    visited[A] = True

    while queue:
        num, text = queue.popleft()
        if (num == B):
            print(text)
            break
        d = (num*2)%10000
        if not visited[d]:
            visited[d] = True
            queue.append([d, text+'D'])
        s = (num-1)%10000
        if not visited[s]:
            visited[s] = True
            queue.append([s, text+'S'])
        l = num // 1000 + (num % 1000)*10
        if not visited[l]:
            visited[l] = True
            queue.append([l, text+'L'])
        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            queue.append([r, text+'R'])
