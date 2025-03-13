T = int(input())

dp = [1 for _ in range(101)]

dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i-5] + dp[i-1]

for _ in range(T):
    print(dp[int(input())])
