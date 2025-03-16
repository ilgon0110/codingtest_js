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
ans = sys.maxsize
person = sys.maxsize
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(x):
    dist = [sys.maxsize for _ in range(N+1)]
    dist[x] = 0
    queue = deque()
    queue.append((x,0))

    while queue:
        node, cost = queue.popleft()
        allCost = cost+1
        for nextNode in graph[node]:            
            if allCost < dist[nextNode]:
                queue.append((nextNode,allCost))
                dist[nextNode] = allCost
    return sum(dist[1:N+1])

for i in range(N,0,-1):
    result = dijkstra(i)
    if result <= ans:
        ans  = result
        person = i

print(person)
