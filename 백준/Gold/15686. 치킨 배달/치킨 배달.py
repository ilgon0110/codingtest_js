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
N,M = map(int,input().split())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
board = [[0 for _ in range(N+1)]]
for _ in range(N):
    board.append([0]+list(map(int,input().split())))

chickenStores = []
homes = []
for i in range(N+1):
    for j in range(N+1):
        if board[i][j] == 2:
            chickenStores.append((i,j))
        if board[i][j] == 1:
            homes.append((i,j))

def chickenDistance(x,y,cx,cy):
    return abs(x-cx)+abs(y-cy)

def findChickenStore(x,y):
    visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    
    while queue:
        x,y = queue.popleft()
        if board[x][y] == 2:
            return (x,y)
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<1 or nx>=N+1 or ny<1 or ny>=N+1:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

ans = sys.maxsize
def dfs(L,s,track):
    if L == M:
        global ans
        chickens = track
        total = 0
        for x,y in homes:
            minDist = sys.maxsize
            for cx,cy in chickens:
                minDist = min(chickenDistance(x,y,cx,cy), minDist)
            total += minDist
        ans = min(ans,total)
        return
    else:
        for i in range(s,len(chickenStores)):
            track.append(chickenStores[i])
            dfs(L+1,i+1,track)
            track.pop()


dfs(0,0,[])
print(ans)