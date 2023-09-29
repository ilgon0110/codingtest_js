import sys

# sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans1 = 100
ans2 = 100

for v in arr:
    [a, b] = v
    if (a > b):
        ans2 -= a
    elif a < b:
        ans1 -= b
    else:
        continue

print(ans1)
print(ans2)
