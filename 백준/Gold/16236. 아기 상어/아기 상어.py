import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def findFish(sharkSize):
    ans = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and board[i][j] != 9 and board[i][j] < sharkSize:
                ans.append((i, j))
    return ans

def move(i, j, sharkSize):
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((i, j))
    dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1 and board[nx][ny] <= sharkSize:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist

sharkSize = 2
time = 0
eat = 0
while True:
    fishes = findFish(sharkSize)
    if len(fishes) == 0:
        break
    sharkX = 0
    sharkY = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                sharkX = i
                sharkY = j
    dist = move(sharkX, sharkY, sharkSize)
    distance = sys.maxsize
    go = []
    for fish in fishes:
        x, y = fish
        if dist[x][y] < distance:
            if dist[x][y] == -1:
                continue
            distance = dist[x][y]
            go.append((x, y))
    if len(go) == 0:
        break
    moveX, moveY = go.pop()
    board[moveX][moveY] = 9
    board[sharkX][sharkY] = 0
    time += dist[moveX][moveY]
    eat += 1
    if eat == sharkSize:
        sharkSize += 1
        eat = 0
print(time)
