import sys
# sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(input().split()) for _ in range(N)]

for i in range(N):
    [arr[i][0], arr[i][1]] = [int(arr[i][0]), list(arr[i][1])]


for i in range(N):
    ans = []
    count = arr[i][0]
    for j in range(len(arr[i][1])):
        tmp = ''
        tmp += arr[i][1][j] * count
        ans.append(tmp)
    print(''.join(ans))
