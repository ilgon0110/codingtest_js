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
ans = 0
my_dict = dict()

for rt in range(N):
    if arr[rt] in my_dict:
        my_dict[arr[rt]]+=1
    else:
        my_dict[arr[rt]] = 1
    
    if lt > 0:
        left = lt-1
        if arr[left] in my_dict:
            my_dict[arr[left]] -= 1
            if my_dict[arr[left]] == 0:
                del my_dict[arr[left]]
    
    if(len(my_dict.keys()) <= 2):
        ans = max(ans,rt-lt+1)
        continue
    else:
        lt+=1

print(ans)