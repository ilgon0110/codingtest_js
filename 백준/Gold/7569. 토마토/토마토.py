import sys
from collections import deque

[M, N, H] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

tomatoNone = True

dist = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
queue = deque()
for i in range(H):
    arr = board[i]
    for j in range(N):
        for m in range(M):
            if arr[j][m] == 1:
                queue.append([j, m, i])
                dist[i][j][m] = 1
            elif arr[j][m] == 0:
                tomatoNone = False
            elif arr[j][m] == -1:
                dist[i][j][m] = -1

if tomatoNone == True:
    print(0)
else:
    while queue:
        [x, y, idx] = queue.popleft()
        # 동서남북
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and board[idx][nx][ny] == 0:
                board[idx][nx][ny] = 1
                dist[idx][nx][ny] = dist[idx][x][y] + 1
                queue.append([nx, ny, idx])

        # 앞뒤
        if idx == 0 and H > 1:
            if board[idx+1][x][y] == 0:
                board[idx+1][x][y] = 1
                queue.append([x, y, idx+1])
                dist[idx+1][x][y] = dist[idx][x][y] + 1
        elif idx == H-1 and H > 1:
            if board[idx-1][x][y] == 0:
                board[idx-1][x][y] = 1
                queue.append([x, y, idx-1])
                dist[idx-1][x][y] = dist[idx][x][y] + 1
        elif 0 < idx < H-1:
            if board[idx-1][x][y] == 0:
                board[idx-1][x][y] = 1
                queue.append([x, y, idx-1])
                dist[idx-1][x][y] = dist[idx][x][y] + 1
            if board[idx+1][x][y] == 0:
                board[idx+1][x][y] = 1
                queue.append([x, y, idx+1])
                dist[idx+1][x][y] = dist[idx][x][y] + 1

    def ans(arr):
        answer = 0
        for i in range(H):
            for j in range(N):
                for m in range(M):
                    if arr[i][j][m] == 0:
                        return -1
                    answer = max(arr[i][j][m], answer)
        return answer-1
    print(ans(dist))
