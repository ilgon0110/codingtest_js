import sys
from collections import deque

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

flag = True
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0

def isAround(i, j):
    queue = deque()
    queue.append((i, j))
    board[i][j] = 2

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx, ny))

flag = True
while flag:
    flag = False
    isAround(0, 0)
    for i in range(N):
        for j in range(M):
            count = 0
            if board[i][j] == 1:
                flag = True
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 2:
                        count += 1
            if count >= 2:
                board[i][j] = 'C'
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'C' or board[i][j] == 2:
                board[i][j] = 0
    if flag == False:
        break
    ans += 1

print(ans)
