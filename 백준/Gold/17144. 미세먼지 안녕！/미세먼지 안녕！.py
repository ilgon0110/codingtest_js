import sys
import math

input = sys.stdin.readline

R, C, T = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))


def airFreshUp(x1):
    arr = []
    for j in range(1, C):
        arr.append(board[x1][j])
    for i in range(x1-1, -1, -1):
        arr.append(board[i][C-1])
    for j in range(C-2, -1, -1):
        arr.append(board[0][j])
    for i in range(1, x1-1):
        arr.append(board[i][0])
    board[x1][1] = 0
    idx = 0
    for j in range(2, C):
        board[x1][j] = arr[idx]
        idx += 1
    for i in range(x1-1, -1, -1):
        board[i][C-1] = arr[idx]
        idx += 1
    for j in range(C-2, -1, -1):
        board[0][j] = arr[idx]
        idx += 1
    for i in range(1, x1):
        board[i][0] = arr[idx]
        idx += 1


def airFreshDown(x2):
    arr = []
    for j in range(1, C):
        arr.append(board[x2][j])
    for i in range(x2+1, R):
        arr.append(board[i][C-1])
    for j in range(C-2, -1, -1):
        arr.append(board[R-1][j])
    for i in range(R-2, x2+1, -1):
        arr.append(board[i][0])
    idx = 0
    board[x2][1] = 0
    for j in range(2, C):
        board[x2][j] = arr[idx]
        idx += 1
    for i in range(x2+1, R):
        board[i][C-1] = arr[idx]
        idx += 1
    for j in range(C-2, -1, -1):
        board[R-1][j] = arr[idx]
        idx += 1
    for i in range(R-2, x2, -1):
        board[i][0] = arr[idx]
        idx += 1


airBox = []
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            airBox.append(i)
for _ in range(T):
    visited = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if board[nx][ny] == -1:
                            continue
                        visited[nx][ny] += math.floor(board[i][j]/5)
                        cnt += 1
                board[i][j] -= (math.floor(board[i][j]/5))*cnt
    for i in range(R):
        for j in range(C):
            board[i][j] += visited[i][j]
    airFreshUp(airBox[0])
    airFreshDown(airBox[1])


ans = 0
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            continue
        ans += board[i][j]

print(ans)
