import sys

input = sys.stdin.readline

N = int(input())

board = []
dp = []

for i in range(N):
    board.append(list(map(int, input().split())))
    dp.append([-1 for _ in range(i+1)])
ans = 0
dp[0][0] = board[0][0]

for i in range(1, N):
    for j in range(len(board[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + board[i][j]
        elif j == len(board[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + board[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + board[i][j]

print(max(dp[N-1]))
