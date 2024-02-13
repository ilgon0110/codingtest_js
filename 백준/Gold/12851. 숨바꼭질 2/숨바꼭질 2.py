import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
INF = sys.maxsize
dist = [INF for _ in range(100001)]
check = 0

def BFS(start):
    dist[start] = 0
    queue = deque()
    queue.append(start)

    while queue:
        pos = queue.popleft()
        if pos == K:
            global check
            check += 1
        for nPos in [pos+1, pos-1, pos*2]:
            cost = dist[pos] + 1
            if 0 <= nPos <= 100000:
                if dist[nPos] >= cost:
                    dist[nPos] = cost
                    queue.append(nPos)

BFS(N)
print(dist[K])
print(check)
