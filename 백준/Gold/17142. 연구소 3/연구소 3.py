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
board = []
for _ in range(N):
    board.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(virus,visited):
    queue = deque()
    for x,y in virus:
        queue.append((x,y))
        visited[x][y] = 0
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny<0 or ny>=N:
                continue
            if board[nx][ny] != 1 and visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
                
    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 1 and board[i][j] != 2:
                result = max(visited[i][j],result)
    
    return result

allVirus = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            allVirus.append((i,j))
            
ans = sys.maxsize
def dfs(L, s, track):
    if L == M:
        global ans
        ans = min(ans, bfs(track,[[sys.maxsize for _ in range(N)] for _ in range(N)]))
        #print(track, ans)
        return
    else:
        for i in range(s,len(allVirus)):
            track.append(allVirus[i])
            dfs(L+1,i+1,track)
            track.pop()

dfs(0,0,[])
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)