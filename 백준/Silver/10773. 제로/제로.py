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

K = int(input())
stack = []

for _ in range(K):
    N = int(input())
    
    if N == 0:
        stack.pop()
    else:
        stack.append(N)

print(sum(stack))    