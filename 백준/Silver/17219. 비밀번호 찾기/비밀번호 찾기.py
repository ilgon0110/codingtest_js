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

N,M = map(int,input().split())
my_dict = dict()

for _ in range(N):
    address, password = map(str,input().split())
    my_dict[address] = password

for _ in range(M):
    print(my_dict[str(input().rstrip())])