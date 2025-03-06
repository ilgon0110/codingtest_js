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

T = int(input())

for _ in range(T):
    A,B = map(int,input().split())
    print(f"Case #{_+1}: {A} + {B} = {A+B}")