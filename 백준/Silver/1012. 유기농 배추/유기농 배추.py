import sys
from collections import deque

T = int(input())

for _ in range(T):
    [M, N, K] = list(map(int, input().split()))

    board = [list(0 for _ in range(M)) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for _ in range(K):
        [m, n] = list(map(int, input().split()))
        board[n][m] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if (board[i][j] == 1):
                count += 1
                queue = deque()
                queue.append([i, j])
                board[i][j] = 0
                while queue:
                    [x, y] = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1):
                            board[nx][ny] = 0
                            queue.append([nx, ny])

    print(count)
