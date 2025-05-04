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

def getSafeArea(board):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                queue = deque()
                queue.append((i,j))
                visited[i][j] = 1
                
                while queue:
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if nx<0 or nx>=N or ny<0 or ny>=M:
                            continue
                        if visited[nx][ny] == 1 or board[nx][ny] == 1:
                            continue
                        visited[nx][ny] = 1
                        board[nx][ny] = 2
                        queue.append((nx,ny))
    
    cnt = 0              
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt+=1
    return cnt

ans = 0

def dfs(L,board):
    global ans
    if L == 3:
        #안전 영역 계산
        diff_board = copy.deepcopy(board)
        safeScore = getSafeArea(diff_board)
        ans = max(ans,safeScore)
        return
    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    dfs(L+1,board)
                    board[i][j] = 0

dfs(0,board)
print(ans)