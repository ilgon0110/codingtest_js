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
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
ans = []

def sol(arr1,arr2):
    if len(arr1) == 0 or len(arr2) == 0:
        return
    global ans
    maxArr1 = max(arr1)
    maxArr2 = max(arr2)
    idx1 = arr1.index(maxArr1)
    idx2 = arr2.index(maxArr2)

    if maxArr1 == maxArr2:
        ans.append(maxArr1)
        arr1.pop(idx1)
        arr2.pop(idx2)
        sol(arr1[idx1:len(arr1)],arr2[idx2:len(arr2)])
    elif maxArr1 > maxArr2:
        arr1.pop(idx1)
        sol(arr1,arr2)
    else:
        arr2.pop(idx2)
        sol(arr1,arr2)
        

sol(arr1,arr2)
print(len(ans))
if ans:
    print(*ans)
