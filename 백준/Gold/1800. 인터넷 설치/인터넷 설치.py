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

N,P,K = map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(P):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

left = 0
right = 1000001

answer = -1

def dijkstra(start,limit):
    # limit를 넘긴 count를 저장함.
    dist = [sys.maxsize for _ in range(N+1)]
    queue = []
    heapq.heappush(queue,(0,start))
    dist[start] = 0
    
    while queue:
        #print(queue)
        cost,node = heapq.heappop(queue)
        if dist[node] < cost:
            continue
        for weight,to in graph[node]:
            if weight > limit:
                if cost+1 < dist[to]:
                    dist[to] = cost+1
                    heapq.heappush(queue,(cost+1,to))
            else:
                if cost < dist[to]:
                    dist[to] = cost
                    heapq.heappush(queue,(cost,to))
    #print('dist[1]',dist[1])
    return dist[1]

while left <= right:
    mid = (left+right)//2
    #print(mid)
    result = dijkstra(N,mid)
    
    # 가능하면 limit를 줄여봄
    if result <= K:
        right = mid-1
        answer = mid
    else:
        left = mid+1

print(answer)