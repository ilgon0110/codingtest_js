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

T = int(input())
for _ in range(T):
    w,h = map(int,input().split())
    f_board = []
    for _ in range(h):
        f_board.append(list(input().rstrip()))
        
    f_time = [[-1 for _ in range(w)] for _ in range(h)]
    p_time = [[-1 for _ in range(w)] for _ in range(h)]
    
    f_queue = deque()
    p_queue = deque()
    
    for i in range(h):
        for j in range(w):
            if f_board[i][j] == '*':
                f_queue.append((i,j,0))
                f_time[i][j] = 0
            elif f_board[i][j] == '@':
                p_queue.append((i,j,0))
                p_time[i][j] = 0
    
    #불먼저 bfs 시작
    ans = 0
    while f_queue:
        x,y,time = f_queue.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            
            if nx<0 or nx>=h or ny<0 or ny>=w or f_time[nx][ny] >= 0:
                continue
            if f_board[nx][ny] == '.' or f_board[nx][ny] == '@':
                f_time[nx][ny] = time+1
                f_board[nx][ny] = '*'
                f_queue.append((nx,ny, time+1))

    # 불이 bfs 다 하고 난 결과로 상근이 bfs
    while p_queue:
        x,y,time = p_queue.popleft()
        flag = False
        
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if nx<0 or nx>=h or ny<0 or ny>=w:
                ans = time+1
                flag = True
                break
            if p_time[nx][ny] >= 0:
                continue
            if f_board[nx][ny] == '#':
                continue
            if f_board[nx][ny] == '*' and f_time[nx][ny] <= time+1:
                continue
            p_time[nx][ny] = time+1
            p_queue.append((nx,ny,time+1))
                
        
        if flag:
            break

    if ans == 0:
        print('IMPOSSIBLE')
    else:
        print(ans)

        
        