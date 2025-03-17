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

N = int(input())

board = []
redBoard = [[' ' for _ in range(N)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(str,input().rstrip())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 'G':
            redBoard[i][j] = 'R'
        else:
            redBoard[i][j] = board[i][j]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y,board,visited):
    queue = deque()
    queue.append((x,y))
    
    visited[x][y] = 1
    
    while queue:
        x,y, = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == 0 and board[nx][ny] == board[x][y]:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                
visited = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j,board, visited)
            cnt+=1
            
visited = [[0 for _ in range(N)] for _ in range(N)]
cnt2 = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j,redBoard,visited)
            cnt2+=1

print(cnt,cnt2)