import sys

# sys.stdin = open("input.txt", "r")

while True:
    [a, b] = list(map(int, input().split()))
    if (a == 0):
        break
    print(a+b)
