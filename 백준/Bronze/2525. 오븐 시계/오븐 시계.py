import sys
# sys.stdin = open("input.txt", "r")

[time, minute] = list(map(int, input().split()))
spendTime = int(input())

a = time*60 + minute + spendTime

if a // 60 >= 24:
    print(a//60 - 24, a % 60)
else:
    print(a//60, a % 60)
