import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
arr = [[0, 0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in range(1, K+1):
    for j in range(1, N+1):
        weight, value = arr[j]
        if i < weight:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i-weight][j-1]+value, dp[i][j-1])

print(dp[K][N])
