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
node = 1
cnt = 1

while node < N:
    node += 6*cnt
    cnt+=1

print(cnt)