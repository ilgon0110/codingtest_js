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
visited=[[0 for _ in range(M)] for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(N):
    board.append(list(map(int,input().rstrip())))

queue = deque()
queue.append([0,0,1])
board[0][0] = 0

while queue:
    [x,y,dist] = queue.popleft()
    if x == N-1 and y == M-1:
        print(dist)
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx>=N or ny<0 or ny>=M:
            continue
        if board[nx][ny] == 1:
            board[nx][ny] = 0
            queue.append([nx,ny,dist+1])
