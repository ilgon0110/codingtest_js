import sys

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

ans = 0

def DFS(L, x, y, direction):
    if x == N-1 and y == N-1:
        global ans
        ans += 1
        return
    else:
        if direction == 'row':
            if 0 <= x < N and 0 <= y+1 < N:
                if board[x][y+1] == 0:
                    DFS(L+1, x, y+1, 'row')
            if 0 <= x+1 < N and 0 <= y+1 < N:
                if board[x+1][y] == 0 and board[x+1][y+1] == 0 and board[x][y+1] == 0:
                    DFS(L+1, x+1, y+1, 'dia')
        if direction == 'col':
            if 0 <= x+1 < N and 0 <= y < N:
                if board[x+1][y] == 0:
                    DFS(L+1, x+1, y, 'col')
            if 0 <= x+1 < N and 0 <= y+1 < N:
                if board[x+1][y] == 0 and board[x+1][y+1] == 0 and board[x][y+1] == 0:
                    DFS(L+1, x+1, y+1, 'dia')
        if direction == 'dia':
            if 0 <= x < N and 0 <= y+1 < N:
                if board[x][y+1] == 0:
                    DFS(L+1, x, y+1, 'row')
            if 0 <= x+1 < N and 0 <= y < N:
                if board[x+1][y] == 0:
                    DFS(L+1, x+1, y, 'col')
            if 0 <= x+1 < N and 0 <= y+1 < N:
                if board[x+1][y] == 0 and board[x+1][y+1] == 0 and board[x][y+1] == 0:
                    DFS(L+1, x+1, y+1, 'dia')


DFS(0, 0, 1, 'row')
print(ans)
