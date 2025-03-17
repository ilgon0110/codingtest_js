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

M,N,H = map(int,input().split())
board = [[[] for _ in range(M)] for _ in range(N)]
for z in range(H):
    for i in range(N):
        tmp = list(map(int,input().split()))
        for j in range(M):
            board[i][j].append(tmp[j])
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs():
    queue=deque()
    visited = [[[-1 for _ in range(H)] for _ in range(M)] for _ in range(N)]
    ans = 0
    
    for i in range(N):
        for j in range(M):
            for z in range(H):
                if board[i][j][z] == 1:
                    queue.append([i,j,z,0])
                    visited[i][j][z] = 0
                
    while queue:
        [x,y,z,day] = queue.popleft()
        
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if visited[nx][ny][z] == -1 and board[nx][ny][z] == 0:
                visited[nx][ny][z] = day+1
                queue.append([nx,ny,z,day+1])
            if z+1 < H:
                if visited[x][y][z+1] == -1 and board[x][y][z+1] == 0:
                    visited[x][y][z+1] = day+1
                    queue.append([x,y,z+1,day+1])
            if z-1 >= 0:
                if visited[x][y][z-1] == -1 and board[x][y][z-1] == 0:
                    visited[x][y][z-1] = day+1
                    queue.append([x,y,z-1,day+1])
    
    for i in range(N):
        for j in range(M):
            for z in range(H):
                if board[i][j][z] == -1:
                    continue
                if visited[i][j][z] == -1:
                    ans = -1
                    return ans
                else:
                    ans = max(visited[i][j][z], ans)
    
    return ans                
    
    

print(bfs())
