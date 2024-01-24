import sys

answer = sys.maxsize

N = int(sys.stdin.readline())

dp = [0 for i in range(50001)]
dp[1] = 1

for i in range(2, N+1):
    j = 1
    min_value = sys.maxsize
    while j**2 <= i:
        min_value = min(min_value, dp[i - (j**2)] + 1)
        j += 1
    dp[i] = min_value

print(dp[N])
