import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
INF = sys.maxsize
dist = [INF for _ in range(100001)]

def BFS(start):
    queue = deque()
    queue.append(start)
    dist[start] = 0

    while queue:
        pos = queue.popleft()
        if pos == K:
            break
        nPos = pos*2
        if 0 <= nPos <= 100000 and dist[nPos] > dist[pos]:
            dist[nPos] = dist[pos]
            queue.append(nPos)
        for nPos in [pos+1, pos-1]:
            if 0 <= nPos <= 100000 and dist[nPos] > dist[pos] + 1:
                dist[nPos] = dist[pos]+1
                queue.append(nPos)


BFS(N)
print(dist[K])
