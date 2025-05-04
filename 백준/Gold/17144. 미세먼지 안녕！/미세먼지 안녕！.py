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

R,C,T = map(int,input().split())
board = []
for _ in range(R):
    board.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(T):
    tmp = [[0 for _ in range(C)] for _ in range(R)]
    targets = []
    cleaner  = []
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                targets.append((i,j))
            if board[i][j] == -1:
                cleaner.append((i,j))
    
    for x,y in targets:
        cnt = 0
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or nx>=R or ny<0 or ny>=C:
                continue
            if board[nx][ny] == -1:
                continue
            tmp[nx][ny] += board[x][y]//5
            cnt+=1
        board[x][y] = board[x][y] - ((board[x][y]//5)*cnt)
    
    for i in range(R):
        for j in range(C):
            board[i][j] += tmp[i][j]
    
    # 공기청청기 작동
    x1,y1 = cleaner[0]
    queue1 = deque()
    for i in range(1,C):
        queue1.append(board[x1][i])
    tmp1 = queue1.pop()
    queue1.appendleft(0)

    for i in range(1,C):
        board[x1][i] = queue1[i-1]
    
    queue2 = deque()
    for i in range(x1-1,-1,-1):
        queue2.append(board[i][C-1])
    queue2.appendleft(tmp1)
    tmp2 = queue2.pop()

    tmpIdx = 0
    for i in range(x1-1,-1,-1):
        board[i][C-1] = queue2[tmpIdx]
        tmpIdx+=1
        
    
    queue3 = deque()
    for i in range(C-2,-1,-1):
        queue3.append(board[0][i])
    queue3.appendleft(tmp2)
    tmp3 = queue3.pop()
    tmpIdx = 0
    for i in range(C-2,-1,-1):
        board[0][i] = queue3[tmpIdx]
        tmpIdx+=1
    
    queue4 = deque()
    for i in range(1,x1):
        queue4.append(board[i][0])
    queue4.appendleft(tmp3)
    queue4.pop()
    for i in range(1,x1):
        board[i][0] = queue4[i-1]
    
    x2,y2 = cleaner[1]
    queue = deque()
    for i in range(1,C):
       queue.append(board[x2][i])
    tmp = queue.pop()
    queue.appendleft(0)
    tmpIdx = 0
    for i in range(1,C):
        board[x2][i] = queue[tmpIdx]
        tmpIdx +=1

    queue=deque()
    for i in range(x2+1,R):
        queue.append(board[i][C-1])
    queue.appendleft(tmp)
    tmp = queue.pop()
    tmpIdx = 0
    for i in range(x2+1,R):
        board[i][C-1] = queue[tmpIdx]
        tmpIdx+=1
    
    queue=deque()
    for i in range(C-2,-1,-1):
        queue.append(board[R-1][i])
    queue.appendleft(tmp)
    tmp = queue.pop()
    tmpIdx = 0
    for i in range(C-2,-1,-1):
        board[R-1][i] = queue[tmpIdx]
        tmpIdx+=1
    
    queue = deque()
    for i in range(R-2,x2,-1):
        queue.append(board[i][0])
    queue.appendleft(tmp)
    queue.pop()
    tmpIdx = 0
    for i in range(R-2,x2,-1):
        board[i][0] = queue[tmpIdx]   
        tmpIdx+=1
    
ans = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            ans += board[i][j]

print(ans)