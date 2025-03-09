[N, M] = list(map(int, input().split()))
ans = 0
for i in range(1, 10001):
    if N % i == 0 and M % i == 0:
        ans = max(i, ans)

print(ans)
print(ans * N // ans * M // ans)
