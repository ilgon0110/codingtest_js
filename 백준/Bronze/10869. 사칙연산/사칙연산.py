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

A,B = map(int , input().split())

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)