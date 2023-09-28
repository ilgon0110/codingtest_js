import sys
# sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(input().split()) for _ in range(N)]

for i in range(N):
    tmp = float(arr[i][0])
    for j in range(1, len(arr[i])):
        if arr[i][j] == '@':
            tmp *= 3
        elif arr[i][j] == '%':
            tmp += 5
        elif arr[i][j] == '#':
            tmp -= 7
    print("{:.2f}".format(tmp))
