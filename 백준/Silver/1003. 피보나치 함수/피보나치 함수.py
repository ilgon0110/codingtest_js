T = int(input())

dp = [(0, 0) for _ in range(41)]
dp[0] = (1, 0)
dp[1] = (0, 1)


def fibonacci(L):
    dp[L] = (dp[L-1][0] + dp[L-2][0], dp[L-1][1] + dp[L-2][1])


for i in range(2, 41):
    fibonacci(i)


for _ in range(T):
    N = int(input())
    print(str(dp[N][0]) + ' ' + str(dp[N][1]))
