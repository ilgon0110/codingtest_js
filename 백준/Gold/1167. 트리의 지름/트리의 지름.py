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

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    tmp = list(map(int,input().split()))
    x = tmp[0]
    for i in range(1,len(tmp),2):
        if tmp[i] == -1:
            break
        graph[x].append((tmp[i+1],tmp[i]))

def dijkstra(start):
    dist = [sys.maxsize for _ in range(V+1)]
    queue=deque()
    queue.append(start)
    dist[start] = 0
    
    while queue:
        node = queue.popleft()
        for (nextCost,nextNode) in graph[node]:
            allCost = nextCost+dist[node]
            if dist[nextNode] > allCost:
                dist[nextNode] = allCost
                queue.append(nextNode)
    
    tmp = dist[1:len(dist)]
    targetIndex = tmp.index(max(tmp))
    return [targetIndex+1 , dist]

[mostFar, _] = dijkstra(1)
[mostFar2, _] = dijkstra(mostFar)
[_, dist] = dijkstra(mostFar)

print(dist[mostFar2])