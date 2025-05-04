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

N,M,R = map(int,input().split())
items = list(map(int,input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(R):
    a,b,l = map(int,input().split())
    graph[a].append((l,b))
    graph[b].append((l,a))

dist = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    dist[i][i] = 0
    for cost,to in graph[i]:
        dist[i][to] = min(dist[i][to], cost)

def floid():
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

floid()
ans = 0
for i in range(1,N+1):
    start = i
    cnt = 0
    for j in range(len(dist[i])):
        if dist[i][j] <= M:
            cnt+=items[j-1]
    ans = max(ans,cnt)

print(ans)
        
