import sys
# sys.stdin = open("input.txt", "r")

arr = list(map(int, input().split()))

ans = []

for i in arr:
    tmp = i
    count = 0
    for j in arr:
        if tmp == j:
            count += 1
    ans.append((i, count))

ans = sorted(ans, key=lambda x: (-x[1], -x[0]))

if ans[0][1] == 3:
    print(10000 + (ans[0][0] * 1000))
elif ans[0][1] == 2:
    print(1000 + ans[0][0]*100)
else:
    print(ans[0][0] * 100)
