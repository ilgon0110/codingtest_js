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
tree = dict()

for _ in range(N):
    node,left,right = map(str,input().split())
    tree[node] = [left,right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def midorder(root):
    if root != '.':
        midorder(tree[root][0])
        print(root,end='')
        midorder(tree[root][1])
        
def back_order(root):
    if root != '.':
        back_order(tree[root][0])
        back_order(tree[root][1])
        print(root,end='')

preorder('A')
print()
midorder('A')
print()
back_order('A')
print()
