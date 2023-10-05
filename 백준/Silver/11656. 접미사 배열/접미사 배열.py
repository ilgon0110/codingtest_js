import sys

N = list(input())
N.reverse()


arr = []
for i in range(len(N)):
    tmp = []
    for j in range(i+1):
        tmp.append(N[j])
    tmp.reverse()
    arr.append(tmp)


tmp = []
for v in arr:
    tmp.append(''.join(v))

tmp.sort()
for v in tmp:
    print(v)
