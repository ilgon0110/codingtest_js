import sys
# sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for v in arr:
    maxNum = 0
    ans = 0
    for j in v:
        count = 0
        for k in v:
            if j == k:
                count += 1
        if (count >= maxNum):
            ans = max(ans, j)
            maxNum = count
    tmp = 0
    if maxNum == 3:
        tmp = 10000+ans*1000
    elif maxNum == 2:
        tmp = 1000 + ans*100
    else:
        tmp = ans*100
    answer = max(answer, tmp)

print(answer)
