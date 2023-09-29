import sys
import itertools
import heapq
import bisect
import collections
from collections import deque
import math
import queue
# sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for v in arr:
    [r, e, c] = v
    if (e - c > r):
        print('advertise')
    elif e - c == r:
        print('does not matter')
    else:
        print('do not advertise')
