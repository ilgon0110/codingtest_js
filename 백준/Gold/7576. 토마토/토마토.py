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

M,N = map(int,input().split())
board = []
visited = [[-1 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(int,input().split())))

queue = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            queue.append([i,j,0])
            visited[i][j] = 0
            
dx = [-1,0,1,0]
dy = [0,-1,0,1]

while queue:
    [x,y,day] = queue.popleft()

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if nx < 0 or nx >= N or ny<0 or ny>=M:
            continue
        if board[nx][ny] == 0 and visited[nx][ny] == -1:
            visited[nx][ny] = day+1
            queue.append([nx,ny,day+1])
            
Flag = True  
ans = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == -1:
            continue
        if visited[i][j] == -1:
            print(-1)
            Flag = False
            exit()
        else:
            ans = max(ans,visited[i][j])

if Flag == True:
    print(ans)