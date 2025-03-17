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
ans = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for _ in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            board[i][j] = 0
            queue = deque()
            queue.append([i,j,0])
            
            while queue:
                [x,y,dist] = queue.popleft()
                ans[x][y] = dist
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    
                    if nx<0 or nx >=N or ny<0 or ny>=M:
                        continue
                    if board[nx][ny] == 1:
                        board[nx][ny] = 0
                        queue.append((nx,ny,dist+1))

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and ans[i][j] == 0:
            ans[i][j] = -1

for x in ans:
    print(*x)