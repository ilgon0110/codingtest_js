import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
board = []
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))


def DFS(L, x, y, total):
    if L == 3:
        global ans
        ans = max(ans, total)
        return
    elif L == 1:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                DFS(L+1, x, y, total+board[nx][ny])
                visited[nx][ny] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                DFS(L+1, nx, ny, total+board[nx][ny])
                visited[nx][ny] = 0
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                DFS(L+1, nx, ny, total+board[nx][ny])
                visited[nx][ny] = 0


answer = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        ans = 0
        DFS(0, i, j, board[i][j])
        visited[i][j] = 0
        answer = max(ans, answer)

print(answer)
