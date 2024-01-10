import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N+1)]
dp[0] = nums[0]

for i in range(1, N):
    dp[i] = dp[i-1]+nums[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j-1]-dp[i-2])
