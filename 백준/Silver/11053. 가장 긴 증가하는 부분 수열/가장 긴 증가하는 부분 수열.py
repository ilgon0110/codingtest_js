import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = 1

for i in range(1, N):
    tmp = 0
    for j in range(i):
        if arr[j] >= arr[i]:
            continue
        tmp = max(tmp, dp[j])
    dp[i] = tmp+1

print(max(dp))
