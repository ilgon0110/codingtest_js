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

N,K,R = map(int,input().split())
roads = [[[] for _ in range(N)] for _ in range(N)]
board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(R):
    a,b,c,d = map(int,input().split())
    roads[a-1][b-1].append((c-1,d-1))
    roads[c-1][d-1].append((a-1,b-1))

cows = []
for i in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1] = i+1
    cows.append((a-1,b-1))

dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = 0

for i,(x,y) in enumerate(cows):
    #print(i,x,y)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    tmp = [1 for _ in range(K+1)]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    tmp[i+1] = 0
    
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=N or visited[nx][ny]:
                continue
            if (x,y) in roads[nx][ny]:
                continue
            visited[nx][ny] = 1
            queue.append((nx,ny))
            if board[nx][ny] > 0:
                tmp[board[nx][ny]] = 0
    
    ans += (sum(tmp) - 1)
    
print(ans //2 )