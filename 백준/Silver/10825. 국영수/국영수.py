import sys

N = int(input())

arr = [list(input().split()) for _ in range(N)]

tmp = sorted(arr, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for v in tmp:
    print(v[0])
