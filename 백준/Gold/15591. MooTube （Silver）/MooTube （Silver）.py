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

N,Q = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[p].append((r,q))
    graph[q].append((r,p))
    
    graph[p].sort()
    graph[q].sort()

dp = [[]]

for i in range(1,N+1):
    queue = deque()
    visited = [0 for _ in range(N+1)]
    usados = [sys.maxsize for _ in range(N+1)]
    visited[i] = 1
    queue.append((sys.maxsize,i))
    
    while queue:
        usado, node = queue.popleft()
        for next_usado, nextNode in graph[node]:
            next_usado = min(next_usado,usado)
            if next_usado < usados[nextNode] and not visited[nextNode]:
                usados[nextNode] = next_usado
                queue.append((next_usado, nextNode))
                visited[nextNode] = 1
    
    dp.append(usados)

for _ in range(Q):
    k,v = map(int,input().split())
    cnt = 0
    
    usados = dp[v]
    for usado in usados:
        if usado >= k and usado != sys.maxsize:
            cnt+=1
    
    print(cnt)
    

