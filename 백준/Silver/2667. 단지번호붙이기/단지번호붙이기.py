import sys
from collections import deque

N = int(input())
board = [list(map(int, input())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

Sum = 0
count = []

for i in range(0, N):
    for j in range(0, N):
        pos = board[i][j]
        if (pos == 1):
            queue = deque()
            queue.append([i, j])
            board[i][j] = 0
            cnt = 1
            Sum += 1
            while queue:
                [x, y] = queue.popleft()
                for k in range(0, 4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if (nx < 0 or nx >= N or ny < 0 or ny >= N):
                        continue
                    if (board[nx][ny] == 1):
                        cnt += 1
                        board[nx][ny] = 0
                        queue.append([nx, ny])
            count.append(cnt)
print(Sum)
count.sort()
for i in count:
    print(i)
