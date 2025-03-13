import sys
import collections
import math
from collections import deque
import copy
import bisect
import itertools
import heapq

#sys.stdin = open("input.txt", "r")

N,M,V = map(int,input().split())
board = [[] for _ in range(N+1)]
ansDfs = []
ansBfs = []
for _ in range(M):
    x,y = map(int,input().split())
    board[x].append(y)
    board[y].append(x)

for i in range(1,N+1):
    board[i].sort()

def dfs(node, visited):
    visited[node] = 1
    ansDfs.append(node)
    
    for nextNode in board[node]:
        if visited[nextNode] == 1:
            continue
        visited[nextNode] = 1
        dfs(nextNode, visited)

def bfs(node, visited):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    
    while queue:
        node = queue.popleft()
        ansBfs.append(node)
        
        for nextNode in board[node]:
            if visited[nextNode] == 1:
                continue
            visited[nextNode] = 1
            queue.append(nextNode)

dfs(V,[0 for _ in range(N+1)])
bfs(V, [0 for _ in range(N+1)])

print(*ansDfs)
print(*ansBfs)