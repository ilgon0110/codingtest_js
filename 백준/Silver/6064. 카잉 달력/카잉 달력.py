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
    M,N,x,y = map(int,input().split())
    ans = x
    ny = x%N
    if ny == 0:
        ny = N
    flag = ny == y
    
    while ny != y and ans <= (M*N):
            ans += M
            ny = (ny+M)%N
            if ny == 0:
                ny = N
            if ny == y:
                flag = True

    if flag:
        print(ans)
    else:
        print(-1)
    