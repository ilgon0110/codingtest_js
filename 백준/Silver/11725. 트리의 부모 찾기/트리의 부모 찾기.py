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
for _ in range(N-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
parents = [1 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

def dfs(node):
    global parents, visited
    visited[node] = 1
    for nextNode in graph[node]:
        if visited[nextNode] == 1:
            continue
        parents[nextNode] = node
        dfs(nextNode)

def bfs(node):
    global parents, visited
    queue = deque()
    visited[node] = 1
    queue.append(node)
    
    while queue:
        node = queue.popleft()
        for nextNode in graph[node]:
            if visited[nextNode] == 1:
                continue
            parents[nextNode] = node
            visited[nextNode] = 1
            queue.append(nextNode)

for i in range(1,N+1):
    if visited[i] == 0:
        bfs(i)

for i in range(2,N+1):
    print(parents[i])