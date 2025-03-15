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

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(N+1)]

def dfs(node):
    visited[node] = 1
    for nextNode in graph[node]:
        if visited[nextNode] == 1:
            continue
        visited[nextNode] = 1
        dfs(nextNode)

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        node = queue.popleft()
        for nextNode in graph[node]:
            if visited[nextNode] == 1:
                continue
            visited[nextNode] = 1
            queue.append(nextNode)
ans = 0
for i in range(1,N+1):
    if visited[i] == 0:
        ans += 1
        bfs(i)
        
print(ans)