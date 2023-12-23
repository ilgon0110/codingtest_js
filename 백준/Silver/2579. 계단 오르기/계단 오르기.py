N = int(input())
stair = [0]
for _ in range(N):
    stair.append(int(input()))

dp = [[0]*3 for _ in range(N+1)]

if N == 1:
    print(stair[1])
    exit()
elif N == 2:
    print(stair[1] + stair[2])
    exit()

dp[1][1] = stair[1]
dp[2][1], dp[2][2] = stair[2], stair[1]+stair[2]

for i in range(3, N+1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stair[i]
    dp[i][2] = dp[i-1][1] + stair[i]

print(max(dp[N]))
