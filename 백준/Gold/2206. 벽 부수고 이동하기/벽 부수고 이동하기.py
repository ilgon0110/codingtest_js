import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, list(input().rstrip()))))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dist = [[[0]*2 for _ in range(M)] for _ in range(N)]

ans = sys.maxsize

def BFS(i, j):
    queue = deque()
    queue.append((i, j, 0))
    dist[i][j][0] = 1

    while queue:
        [x, y, w] = queue.popleft()
        if x == N-1 and y == M-1:
            return dist[x][y][w]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and dist[nx][ny][w] == 0:
                    dist[nx][ny][w] = dist[x][y][w] + 1
                    queue.append([nx, ny, w])
                if board[nx][ny] == 1 and w == 0:
                    dist[nx][ny][w+1] = dist[x][y][w] + 1
                    queue.append([nx, ny, w+1])
    return -1


print(BFS(0, 0))
