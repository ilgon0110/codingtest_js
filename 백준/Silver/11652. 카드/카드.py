import sys

N = int(input())

arr = list(input() for _ in range(N))
dict = {}

for v in arr:
    if v in dict:
        dict[v] += 1
    else:
        dict[v] = 1

tmp = []

for v in dict:
    tmp.append((v, dict[v]))


tmp.sort(key=lambda x: (-x[1], int(x[0])))
print(tmp[0][0])
