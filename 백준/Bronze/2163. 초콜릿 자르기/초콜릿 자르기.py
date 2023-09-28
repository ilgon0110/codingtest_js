import sys
# sys.stdin = open("input.txt", "r")

[n, m] = list(map(int, input().split()))

print((m-1)*n + n-1)