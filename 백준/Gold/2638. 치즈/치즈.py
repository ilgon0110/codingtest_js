import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for _ in range(N):
    board.append(list(map(int, input().split())))


def isOutSide(board):
    queue = deque()
    queue.append((0, 0))
    board[0][0] = 2

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                queue.append((nx, ny))
    return board


flag = True
answer = 0
while (flag):
    flag = False
    board = isOutSide(board)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 2:
                        cnt += 1
                if cnt >= 2:
                    board[i][j] = 0
                    flag = True
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                board[i][j] = 0
    if flag == False:
        break
    answer += 1

print(answer)
