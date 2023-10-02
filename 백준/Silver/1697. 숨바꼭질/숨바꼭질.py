import sys
from collections import deque

[N, K] = list(map(int, input().split()))
dist = [0 for _ in range(100002)]
queue = deque()

queue.append(N)
flag = 0
if (N == K):
    print(0)
    flag = 1
while queue and flag == 0:
    pos = queue.popleft()
    tmp = [pos-1, pos+1, 2*pos]
    for npos in tmp:
        if (npos < 0 or npos > 100000):
            continue
        if (npos == K):
            print(dist[pos]+1)
            flag = 1
            break
        if (dist[npos]):
            continue
        dist[npos] = dist[pos] + 1
        queue.append(npos)
