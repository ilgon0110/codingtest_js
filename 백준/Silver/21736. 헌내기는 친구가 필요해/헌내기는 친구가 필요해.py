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
dx = [-1,0,1,0]
dy = [0,-1,0,1]
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(str,input().rstrip())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y)) 
    visited[x][y] = 1
    total = 0
    
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or nx >= N or ny<0 or ny >=M:
                continue
            if board[nx][ny] == 'O':
                board[nx][ny] = 'X'
                queue.append((nx,ny))
            elif board[nx][ny] == 'P':
                board[nx][ny] = 'X'
                total+=1
                queue.append((nx,ny))
    return total
            
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            ans = bfs(i,j)

if ans == 0:
    print("TT")
else:
    print(ans)