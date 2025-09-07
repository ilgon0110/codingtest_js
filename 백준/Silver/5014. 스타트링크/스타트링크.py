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

F,S,G,U,D = map(int,input().split())

visited = [0 for _ in range(F+1)]

queue = deque()
queue.append((S,0))
visited[S] = 1
dx = [U,-D]
ans = -1

while queue:
    pos,cost = queue.popleft()
    if pos == G:
        ans = cost
        break
    for k in dx:
        nx = pos+k
        if nx<=0 or nx >F or visited[nx]:
            continue
        visited[nx] = 1
        queue.append((nx,cost+1))

if ans == -1:
    print('use the stairs')
else:
    print(ans)