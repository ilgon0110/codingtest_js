import sys
from collections import deque

[R, C] = list(map(int, input().split()))

board = [list(input()) for _ in range(R)]


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

jihunVisited = [list(0 for _ in range(C)) for _ in range(R)]
fireVisited = [list(0 for _ in range(C)) for _ in range(R)]
jihunQueue = deque()
fireQueue = deque()

for i in range(0, R):
    for j in range(0, C):
        if (board[i][j] == 'J'):
            jihunQueue.append((i, j))
            jihunVisited[i][j] = 1
        if (board[i][j] == 'F'):
            fireQueue.append((i, j))
            fireVisited[i][j] = 1

# fire
while fireQueue:
    x, y = fireQueue.popleft()
    for k in range(0, 4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if not fireVisited[nx][ny] and board[nx][ny] != "#":
                fireVisited[nx][ny] = fireVisited[x][y] + 1
                fireQueue.append((nx, ny))

# jihun
flag = 0
while jihunQueue and flag == 0:
    x, y = jihunQueue.popleft()
    for k in range(0, 4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] != "#" and not jihunVisited[nx][ny]:
                if not fireVisited[nx][ny] or fireVisited[nx][ny] > jihunVisited[x][y] + 1:
                    jihunVisited[nx][ny] = jihunVisited[x][y] + 1
                    jihunQueue.append((nx, ny))
        else:
            print(jihunVisited[x][y])
            flag = 1
            break

if flag == 0:
    print('IMPOSSIBLE')
