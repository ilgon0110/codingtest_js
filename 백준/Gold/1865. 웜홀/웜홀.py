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

def floid(dist):
    newDist = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            newDist[i][j] = dist[i][j]
            
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if newDist[i][j] > newDist[i][k]+newDist[k][j]:
                    newDist[i][j] = newDist[i][k]+newDist[k][j]
        
    return newDist

def vellman(start):
    dist = [sys.maxsize for _ in range(N+1)]
    dist[start] = 0
    
    for k in range(N):
        for i in range(1,N+1):
            for cost,to in graph[i]:
                if dist[to] > dist[i] + cost:
                    if k == N-1:
                        return True
                    dist[to] = dist[i]+cost
    return False
                    

TC = int(input())
for _ in range(TC):
    N,M,W = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s,e,t = map(int,input().split())
        graph[s].append((t,e))
        graph[e].append((t,s))
    for _ in range(W):
        s,e,t = map(int,input().split())
        graph[s].append((-t,e))
    
    flag = vellman(1)
    
    if flag:
        print('YES')
    else:
        print('NO')