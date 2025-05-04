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
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

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

for i in range(1,N+1):
    tmp = dist[i][1:]
    for j in range(len(tmp)):
        if tmp[j] == sys.maxsize:
            tmp[j] = 0
    print(*tmp)