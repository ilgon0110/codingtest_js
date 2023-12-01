
N = int(input())
arr = list(map(int, input().split()))
ans = []

dp = [1 for _ in range(N)]
dp2 = [[arr[_]] for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

target = max(dp)

cnt = target
for i in range(N-1, -1, -1):
    if dp[i] == cnt:
        ans.append(arr[i])
        cnt -= 1
ans.reverse()
print(target)
print(' '.join(map(str, ans)))
