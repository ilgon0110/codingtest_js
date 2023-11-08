N = int(input())

dp = [0 for _ in range(46)]

dp[1] = 1
dp[2] = 1

if N > 2:
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N])
