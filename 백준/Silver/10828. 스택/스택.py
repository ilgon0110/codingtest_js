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
stack = []

for _ in range(N):
    N = input().rstrip()
    command = ''
    num = 0
    if 'push' in N:
        [x,y] = list(map(str,N.split()))
        command = x
        num = int(y)
    else:
        command = N
        
    if command == 'push':
        stack.append(num)
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)