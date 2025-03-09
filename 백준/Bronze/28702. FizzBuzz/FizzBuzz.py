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

A = str(input()).rstrip()
B = str(input()).rstrip()
C = str(input()).rstrip()
arr = [A,B,C]

if str.isdigit(A):
    target = int(A)+3
    if target%15 == 0 and target >=15:
        print('FizzBuzz')
    elif target % 3 == 0:
        print('Fizz')
    elif target % 5 == 0:
        print('Buzz')
    else:
        print(target)
elif str.isdigit(B):
    target = int(B)+2
    if target%15 == 0 and target >=15:
        print('FizzBuzz')
    elif target % 3 == 0:
        print('Fizz')
    elif target % 5 == 0:
        print('Buzz')
    else:
        print(target)
elif str.isdigit(C):
    target = int(C)+1
    if target%15 == 0 and target >=15:
        print('FizzBuzz')
    elif target % 3 == 0:
        print('Fizz')
    elif target % 5 == 0:
        print('Buzz')
    else:
        print(target)
        