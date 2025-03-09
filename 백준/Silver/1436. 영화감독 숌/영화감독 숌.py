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
cnt = 0
for i in range(666,10000000):
    if '666' in str(i):
        cnt+=1
    
    if cnt == N:
        print(i)
        break