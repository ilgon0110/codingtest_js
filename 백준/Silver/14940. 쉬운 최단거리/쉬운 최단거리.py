import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dist = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            queue.append([i, j])
            while (queue):
                [x, y] = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and nx < N and ny >= 0 and ny < M and visited[nx][ny] == 0 and board[nx][ny] == 1:
                        dist[nx][ny] = dist[x][y] + 1
                        visited[nx][ny] = 1
                        queue.append([nx, ny])
                        
for i in range(N):
    for j in range(M):
        if dist[i][j] == 0 and board[i][j] == 1:
            dist[i][j] = -1

for v in dist:
    print(' '.join(map(str, v)))
