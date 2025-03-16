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

N,K = map(int,input().split())
dist = [sys.maxsize for _ in range(100001)]
def bfs(x):
    dist[x] = 0
    queue = deque()
    queue.append((x,0))
    
    while queue:
        node,cost = queue.popleft()
        move = [node-1,node+1,2*node]
        
        for m in move:
            if m < 0 or m > 100000:
                continue
            nextCost = cost+1
            if nextCost < dist[m]:
                dist[m] = nextCost
                queue.append((m,nextCost))

    return dist[K]

print(bfs(N))
        