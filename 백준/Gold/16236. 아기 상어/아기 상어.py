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
for _ in range(N):
    board.append(list(map(int,input().split())))

sharkSize = 2
exp = 0
time = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]

def findEatFishes(x,y):
    canEatFishes = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((x,y,0))
    visited[x][y] = 1
    min_Time = sys.maxsize
    
    while queue:
        x,y,cost = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if board[nx][ny] > sharkSize:
                continue
            # 먹을 수 있는 물고기
            elif board[nx][ny] < sharkSize and visited[nx][ny] == 0 and board[nx][ny] > 0:
                if min_Time >= cost+1:
                    min_Time = cost+1
                    canEatFishes.append((nx,ny,cost+1))
            # 이동
            elif board[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny,cost+1))
            elif board[nx][ny] > 0 and board[nx][ny] == sharkSize and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny,cost+1))
    
    return canEatFishes
                

while True:
    shark_x = 0
    shark_y = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                shark_x = i
                shark_y = j
    canEat = findEatFishes(shark_x,shark_y)
    if len(canEat) == 0:
        print(time)
        break
    
    canEat.sort(key=lambda x : (x[0], x[1]))
    target_x = canEat[0][0]
    target_y = canEat[0][1]
    costTime = canEat[0][2]
    exp+=1
    time+=costTime
    if sharkSize == exp:
        sharkSize+=1
        exp=0
    board[shark_x][shark_y] = 0
    board[target_x][target_y] = 9