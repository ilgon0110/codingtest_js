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

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    queue = deque()
    for i in range(N):
        if i == M:
            queue.append((arr[i],True))
        else:
            queue.append((arr[i], False))

    cnt = 0
    while queue:
        (node, target) = queue.popleft()
        flag = False
        for (x,_) in queue:
            if node < x:
                flag = True
                queue.append((node,target))
                break
        
        if flag == False:
            cnt+=1
            if target == True:
                print(cnt)
                break
        #print(queue)

    #print(ans.index())        

