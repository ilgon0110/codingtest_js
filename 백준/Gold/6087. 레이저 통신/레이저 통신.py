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

W,H = map(int,input().split())
board = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(H):
    board.append(list(input().rstrip()))

razor = []
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            razor.append((i,j))

visited = [[[sys.maxsize,[]] for _ in range(W)] for _ in range(H)]
rx1,ry1 = razor[0]
rx2,ry2 = razor[1]

queue = deque()
queue.append((rx1,ry1,-1,0))
visited[rx1][ry1][0] = 0
visited[rx1][ry1][1].append(-1)
ans = sys.maxsize

while queue:
    x,y,direction,cnt = queue.popleft()
    if x == rx2 and y == ry2:
        ans = min(ans,cnt)
    
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        
        if nx<0 or nx>=H or ny<0 or ny>=W:
            continue
        if board[nx][ny] != '*':
            # 이미 방문했어도 거울 적게 사용해서 방문했으면 다시 방문 가능해야함
            if cnt <= visited[nx][ny][0]:
                if direction != k: # 방향 바뀜(거울추가)
                    if direction == -1:
                        visited[nx][ny][0] = cnt
                        visited[nx][ny][1].append(k)
                        queue.append((nx,ny,k,cnt))
                    else:
                        if k in visited[nx][ny][1]:
                            if cnt+1 < visited[nx][ny][0]:
                                visited[nx][ny][0] = cnt+1
                                visited[nx][ny][1].append(k)
                                queue.append((nx,ny,k,cnt+1))
                        else:
                            visited[nx][ny][0] = cnt+1
                            visited[nx][ny][1].append(k)
                            queue.append((nx,ny,k,cnt+1))                           
                elif direction == k:
                    if k in visited[nx][ny][1]:
                        if cnt < visited[nx][ny][0]:
                            visited[nx][ny][0] = cnt
                            visited[nx][ny][1].append(k)
                            queue.append((nx,ny,k,cnt))
                    else:
                        visited[nx][ny][0] = cnt
                        visited[nx][ny][1].append(k)
                        queue.append((nx,ny,k,cnt))

print(ans)