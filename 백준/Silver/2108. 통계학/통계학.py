import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

print(round(sum(arr)/N))
print(sorted(arr)[len(arr)//2])

tmp = sorted(Counter(arr).items(), key=lambda x: (-x[1], x[0]))

if len(tmp) > 1 and tmp[0][1] == tmp[1][1]:
    print(tmp[1][0])
else:
    print(tmp[0][0])

print(max(arr) - min(arr))
