import sys
# sys.stdin = open("input.txt", "r")

N = list(map(int, input().split()))

N.sort()

print(N[1])
