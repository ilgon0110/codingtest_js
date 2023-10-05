import sys
N = int(input())

arr = list(map(int, input().split()))
dp = [0 for _ in range(len(arr) + 1)]

for v in arr:
    dp[v] = dp[v-1] + 1

print(len(arr) - max(dp))
