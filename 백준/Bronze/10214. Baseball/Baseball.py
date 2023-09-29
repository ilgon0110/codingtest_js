import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

arr = [[list(map(int, input().split())) for _ in range(9)] for _ in range(T)]

for i in arr:
    ysum = 0
    ksum = 0
    for j in i:
        [y, k] = j
        ysum += y
        ksum += k
    if ysum > ksum:
        print('Yonsei')
    elif ysum < ksum:
        print('Korea')
    else:
        print('Draw')
