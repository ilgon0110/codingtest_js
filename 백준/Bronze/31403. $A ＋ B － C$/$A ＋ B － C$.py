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

A = int(input())
B = int(input())
C = int(input())

print(A+B-C)
print(int(str(A)+str(B))-C)