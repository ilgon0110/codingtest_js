import sys
import copy

[N, M] = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
cctv = []

move = [[],
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]]
        ]
# 북,서,남,동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(N):
    for j in range(M):
        if board[i][j] != '#' and 0 < board[i][j] < 6:
            cctv.append([i, j, board[i][j]])


def fill(board, idx, x, y):
    for i in idx:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = '#'

answer = sys.maxsize

def DFS(L, arr):
    if L == len(cctv):
        global answer
        count = 0
        for i in range(N):
            count += arr[i].count(0)
        answer = min(answer, count)
        return
    else:
        tmp = copy.deepcopy(arr)
        [x, y, num] = cctv[L]
        for i in move[num]:
            fill(tmp, i, x, y)
            DFS(L+1, tmp)
            tmp = copy.deepcopy(arr)

DFS(0, board)
print(answer)
