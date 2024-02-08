import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

arr2 = list(reversed(arr))
dp2 = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr2[j] < arr2[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

tmp = list(reversed(dp2))

ans = [0 for _ in range(N)]

for i in range(N):
    ans[i] = dp[i] + tmp[i] - 1

print(max(ans))
