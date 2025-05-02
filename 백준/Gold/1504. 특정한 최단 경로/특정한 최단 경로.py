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

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
v1,v2 = map(int,input().split())

def dijkstra(start,target):
    queue = []
    dist = [sys.maxsize for _ in range(N+1)]
    dist[start] = 0
    heapq.heappush(queue,(0,start,[start]))

    while queue:
        cost,node, track = heapq.heappop(queue)
        if node == target:
            flag = False
            for trackNode in track:
                if target == v1 and trackNode == v2:
                    flag = True
                elif target == v2 and trackNode == v1:
                    flag = True
            return (dist[node],flag)
        for weight,to in graph[node]:
            if dist[to] > weight+cost:
                dist[to] = weight+cost
                heapq.heappush(queue,(weight+cost,to, track+[to]))
    
    return (dist[target],False)
        
a,flagA = dijkstra(1,v1)
b,_ =dijkstra(v1,v2)
c,_ = dijkstra(v2,N)

one = 0
if flagA:
    tmp,_ = dijkstra(v1,N)
    one = a+tmp
else:
    one = a+b+c

d,flagD = dijkstra(1,v2)
e,_ = dijkstra(v2,v1)
f,_ = dijkstra(v1,N)
two = 0
if flagD:
    tmp,_ = dijkstra(v2,N)
    two = d+tmp
else:
    two = d+e+f

ans = min(one,two)
if ans >= sys.maxsize:
    print(-1)
else:
    print(ans)