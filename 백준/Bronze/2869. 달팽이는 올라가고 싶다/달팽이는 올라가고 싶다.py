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

A,B,V = map(int,input().split())

print(math.ceil((V-A)/(A-B))+1)