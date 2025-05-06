import sys
import collections
import math
from collections import deque
import copy
import bisect
import itertools
import heapq

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

lt = 0
rt = 0
plus = []
minus = []

for num in arr:
    if num >= 0:
        plus.append(num)
    else:
        minus.append(num)

if len(plus) == 0:
    minus.sort(reverse=True)
    print(minus[1],minus[0])
    exit()
elif len(minus) == 0:
    print(plus[0],plus[1])
    exit()

plus.sort(reverse=True)

ans = sys.maxsize
result = [0,0]

while lt < len(plus) and rt < len(minus):
    tmp = plus[lt]+minus[rt]
    
    if abs(tmp) == 0:
        result[0] = plus[lt]
        result[1] = minus[rt]
        break
    
    if ans > abs(tmp):
        ans = abs(tmp)
        result[0] = plus[lt]
        result[1] = minus[rt]
        
    if tmp < 0:
        rt+=1
    elif tmp > 0:
        lt+=1

if lt < len(plus):
    for lt in range(len(plus)-1):
        tmp = plus[lt]+plus[lt+1]
        if ans > abs(tmp):
            result[0] = plus[lt]
            result[1] = plus[lt+1]
elif rt < len(minus):
    for rt in range(len(minus)-1):
        tmp = minus[rt]+minus[rt+1]
        if ans > abs(tmp):
            result[0] = minus[rt]
            result[1] = minus[rt+1]

result.sort()
print(*result)