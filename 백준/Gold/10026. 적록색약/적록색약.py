import sys
from collections import deque

N = int(input())

board = [list(input()) for _ in range(N)]
diffBoard = []
M = len(board[0])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    tmp = []
    for j in range(len(board[0])):
        if board[i][j] == 'G':
            tmp.append('R')
        else:
            tmp.append(board[i][j])
    diffBoard.append(tmp)

diffQueue = deque()
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            # bfs
            cnt += 1
            target = board[i][j]
            queue = deque()
            queue.append([i, j])
            board[i][j] = 0
            while queue:
                [x, y] = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == target:
                        board[nx][ny] = 0
                        queue.append([nx, ny])
diffCnt = 0
for i in range(N):
    for j in range(M):
        if diffBoard[i][j] != 0:
            # bfs
            diffCnt += 1
            target = diffBoard[i][j]
            queue = deque()
            queue.append([i, j])
            diffBoard[i][j] = 0
            while queue:
                [x, y] = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < N and 0 <= ny < M and diffBoard[nx][ny] == target:
                        diffBoard[nx][ny] = 0
                        queue.append([nx, ny])


print(cnt, diffCnt)
