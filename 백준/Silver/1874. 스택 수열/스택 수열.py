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
arr = []
stack = []

for _ in range(N):
    arr.append(int(input()))
    
nowIdx = 0
nowNum = 1
ans = []
insertNum = 0

while nowIdx < N:
    target = arr[nowIdx]
    flag = True
    if target >= nowNum:
        while target >= nowNum:
            stack.append(nowNum)
            insertNum = nowNum
            nowNum+=1
            ans.append('+')
            
    else:
        if(target != stack[-1]):
            flag = False
            print('NO')
            break
        
        while stack and target == stack[-1]:
            stack.pop()
            ans.append("-")
            nowIdx += 1
    
        
if flag:
    for x in ans:
        print(x)