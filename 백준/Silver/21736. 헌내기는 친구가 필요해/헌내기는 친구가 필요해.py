import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            queue = deque()
            visited[i][j] = 1
            queue.append([i, j])
            while queue:
                [x, y] = queue.popleft()
                if board[x][y] == 'P':
                    answer += 1
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if nx >= 0 and nx < N and ny >= 0 and ny < M:
                        if (board[nx][ny] == 'O' or board[nx][ny] == 'P') and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            queue.append([nx, ny])

if answer == 0:
    print('TT')
else:
    print(answer)
