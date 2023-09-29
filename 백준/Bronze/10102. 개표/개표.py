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
arr = list(input())

counter = collections.Counter(arr)
a = counter['A']
b = counter['B']

if (a > b):
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
