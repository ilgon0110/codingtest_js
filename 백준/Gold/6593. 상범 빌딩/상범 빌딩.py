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

dx = [-1,0,1,0]
dy = [0,-1,0,1]

while True:
    L,R,C = map(int,input().split())
    if L == 0:
        break
    
    board = [[] for _ in range(L)]
    for i in range(L):
        for _ in range(R):
            board[i].append(list(input().rstrip()))
        input()
    
    start = []
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    
    queue = deque()
    
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k] == 'S':
                    queue.append((i,j,k,0))
                    visited[i][j][k] = 1
    ans = -1
    while queue:
        l,r,c,dist = queue.popleft()
        if board[l][r][c] == 'E':
            ans = dist
            break
        
        # 같은 층 상하좌우
        for k in range(4):
            nx = r+dx[k]
            ny = c+dy[k]
            if nx<0 or nx >=R or ny<0 or ny>=C or visited[l][nx][ny]:
                continue
            if board[l][nx][ny] == '#':
                continue
            visited[l][nx][ny] = 1
            queue.append((l,nx,ny,dist+1))
        
        #다른 층 상,하
        if l+1 < L and visited[l+1][r][c] == 0 and board[l+1][r][c] != '#':
            visited[l+1][r][c] = 1
            queue.append((l+1,r,c,dist+1))
        if l-1 >= 0 and visited[l-1][r][c] == 0 and board[l-1][r][c] != '#':
            visited[l-1][r][c] = 1
            queue.append((l-1,r,c,dist+1))
    
    if ans == -1:
        print('Trapped!')
    else:
        print('Escaped in',ans, 'minute(s).')
            