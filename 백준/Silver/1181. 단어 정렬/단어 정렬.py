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
my_set = set()

for _ in range(N):
    text = str(input()).rstrip()
    my_set.add(text)

arr = list(my_set)
arr.sort()
newArr = sorted(arr, key=lambda x : len(x))

for x in newArr:
    print(x)