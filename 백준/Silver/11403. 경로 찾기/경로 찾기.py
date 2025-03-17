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
graph = [[] for _ in range(N)]

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j] == 1:
            graph[i].append(j)

ans = []

def bfs(x):
    queue = deque()
    queue.append(x)
    visited = [0 for _ in range(N)]
    
    while queue:
        node = queue.popleft()
        for nextNode in graph[node]:
            if visited[nextNode] == 1:
                continue
            visited[nextNode] = 1
            queue.append(nextNode)
    
    return visited

for i in range(N):
    ans.append(bfs(i))

for x in ans:
    print(*x)
    