import sys
from collections import deque
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def move(board):
    newBoard = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if newBoard[i][j] == 2:
                queue = deque()
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M:
                            if newBoard[nx][ny] == 0:
                                newBoard[nx][ny] = 2
                                queue.append((nx, ny))
    return newBoard


ans = 0

def DFS(L, board):
    if L == 3:
        global ans
        total = 0
        result = move(board)
        for i in range(N):
            total += result[i].count(0)
        ans = max(ans, total)
        return
    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    DFS(L+1, board)
                    board[i][j] = 0

DFS(0, board)
print(ans)
