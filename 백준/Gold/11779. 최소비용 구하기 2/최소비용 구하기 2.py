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

start,end = map(int,input().split())

def dijkstra(start,end):
    dist = [sys.maxsize for _ in range(N+1)]
    dist[start] = 0
    queue = []
    heapq.heappush(queue,(0,start,[start]))
    
    while queue:
        cost,node,track = heapq.heappop(queue)
        if node == end:
            return (dist[node],track)
        for weight,to in graph[node]:
            if dist[to] > cost+weight:
                dist[to] = cost+weight
                heapq.heappush(queue,(cost+weight,to,track+[to]))

time, track = dijkstra(start,end)
print(time)
print(len(track))
print(*track)