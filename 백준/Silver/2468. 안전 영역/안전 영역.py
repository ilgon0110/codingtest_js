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
maxHeight = 0
for _ in range(N):
    board.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(N):
    for j in range(N):
        maxHeight = max(maxHeight,board[i][j])
        
answer = 0
for height in range(maxHeight+1):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    ans = 0
    
    for i in range(N):
        for j in range(N):
            if board[i][j] > height and visited[i][j] == 0:
                ans+=1
                queue = deque()
                visited[i][j] = 1
                queue.append((i,j))
                
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if nx<0 or nx>=N or ny<0 or ny>=N:
                            continue
                        if visited[nx][ny] or board[nx][ny] <= height:
                            continue
                        visited[nx][ny] = 1
                        queue.append((nx,ny))
    
    answer = max(answer,ans)

print(answer)
                