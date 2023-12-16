import sys
import math
[K, N] = list(map(int, input().split()))
arr = []
for _ in range(K):
    arr.append(int(input()))

lt = 0
rt = sys.maxsize
answer = 0

while (lt <= rt):
    mid = (lt+rt)//2
    tmp = 0
    for v in arr:
        tmp += math.floor(v//mid)
    if tmp < N:
        rt = mid-1
    else:
        lt = mid+1
        answer = mid
print(answer)
