import sys

T = int(input())

for _ in range(0, T):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    a = sorted(arr, key=lambda x: -int(x[1]))
    print(a[0][0])
