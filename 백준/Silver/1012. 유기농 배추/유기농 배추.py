import sys
import collections
import math
from collections import deque
import copy
import bisect
import itertools
import heapq

#sys.stdin = open("input.txt", "r")

T = int(input())

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(T):
    M,N,K = map(int,input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for __ in range(K):
        x,y = map(int,input().split())
        board[y][x] = 1
    cnt = 0
    
    def dfs(x,y):
        board[x][y] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=N or ny <0 or ny >= M:
                continue
            if board[nx][ny] == 0:
                continue
            board[nx][ny] = 0
            dfs(nx,ny)
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or nx >=N or ny <0 or ny >= M:
                    continue
                if board[nx][ny] == 0:
                    continue
                board[nx][ny] = 0
                queue.append((nx,ny))
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                bfs(i,j)
                cnt+=1
    
    print(cnt)
