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
scores = list(map(int,input().split()))

M = max(scores)
total = 0
for x in scores:
    total += (x/M)*100

print(total/N)