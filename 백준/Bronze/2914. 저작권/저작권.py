import sys
# sys.stdin = open("input.txt", "r")

[A, I] = list(map(int, input().split()))

I = I - 1

print(A*I+1)
