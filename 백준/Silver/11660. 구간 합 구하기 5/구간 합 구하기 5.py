import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
dp = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))

dp[0][0] = board[0][0]

for i in range(N):
    for j in range(N):
        if i == 0 and j > 0:
            dp[i][j] = dp[i][j-1] + board[i][j]
        else:
            tmp = 0
            tmp = dp[i-1][j] + board[i][j]
            if j > 0:
                tmp += dp[i][j-1] - dp[i-1][j-1]
            dp[i][j] = tmp

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    x1 = x1-1
    y1 = y1-1
    x2 = x2-1
    y2 = y2-1
    if y1 > 0:
        ans = dp[x2][y2] - dp[x2][y1-1]
    else:
        ans = dp[x2][y2]
    if x1 > 0 and y1 > 0:
        ans -= (dp[x1-1][y2] - dp[x1-1][y1-1])
    elif x1 > 0:
        ans -= dp[x1-1][y2]
    print(ans)
