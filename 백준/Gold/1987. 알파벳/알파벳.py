import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = []

for _ in range(R):
    board.append(list(input().rstrip()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

ans = 0

visited = [0 for _ in range(100)]

def dfs(i, j, deps):
    global ans
    ans = max(ans, deps)
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx >= 0 and nx < R and ny >= 0 and ny < C:
            idx = ord(board[nx][ny])
            if visited[idx] == 0:
                visited[idx] = 1
                dfs(nx, ny, deps+1)
                visited[idx] = 0


visited[ord(board[0][0])] = 1
dfs(0, 0, 1)
print(ans)
