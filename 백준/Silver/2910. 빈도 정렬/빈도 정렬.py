import sys

[N, C] = list(map(int, input().split()))

arr = list(map(int, input().split()))

dict = dict()

for v in arr:
    if v in dict:
        dict[v] += 1
    else:
        dict[v] = 1

tmp = []

for v in dict:
    tmp.append((v, dict[v]))
tmp.sort(key=lambda x: -x[1])
ans = []

for v in tmp:
    [x, y] = v
    for i in range(y):
        ans.append(x)
print(*ans)
