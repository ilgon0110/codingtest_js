

N = list(map(int, input().split()))

SUM = 0

for v in N:
    SUM += v*v

print(SUM % 10)
