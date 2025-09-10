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

M,N,K = map(int,input().split())
board = [[0 for _ in range(N)] for _ in range(M)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    
    for i in range(M-y2, M-y1):
        for j in range(x1,x2):
            board[i][j] = 1
ans = 0
sizes = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            ans+=1
            queue = deque()
            queue.append((i,j))
            board[i][j] = 1
            size = 0
            
            while queue:
                x,y = queue.popleft()
                size+=1
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    
                    if nx<0 or nx>=M or ny<0 or ny>=N or board[nx][ny] == 1:
                        continue
                    board[nx][ny] = 1
                    queue.append((nx,ny))
            sizes.append(size)

print(ans)
sizes.sort()
print(*sizes)
            
        