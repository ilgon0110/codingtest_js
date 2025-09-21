import sys
import collections
import math
from collections import deque
import copy
import bisect
import itertools
import heapq

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

while True:
    a,b = map(int,input().split())
    if a == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    dist = [sys.maxsize for _ in range(N+1)]
    queue = []
    heapq.heappush(queue,start)
    dist[start] = 0
    
    while queue:
        node = heapq.heappop(queue)
        
        for nx in graph[node]:
            if dist[node] + 1 < dist[nx]:
                dist[nx] = dist[node]+1
                heapq.heappush(queue,nx)

    return dist[1:]
ans = []
value = sys.maxsize
tmp = []
for i in range(1,N+1):
    cnt = max(dijkstra(i))
    tmp.append((i,cnt))

for (i,cnt) in tmp:
    value = min(value,cnt)

for (i,cnt) in tmp:
    if cnt == value:
        ans.append(i)

print(value, len(ans))
print(*ans)
