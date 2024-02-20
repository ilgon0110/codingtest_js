import sys
import math
input = sys.stdin.readline

N = int(input())
K = 0
tmp = 0
while tmp != N:
    tmp = (2**K)*3
    K += 1
K -= 1

arr = ['  *  ', ' * * ', '*****']


def printStar(arr):
    for v in arr:
        print(v)


def DFS(L, before):
    if L == K:
        printStar(before)
        return
    else:
        tmp = []
        long = math.ceil(len(before[-1])/2)
        tt = ''
        for _ in range(long):
            tt += " "
        for v in before:
            tmp.append(v+" "+v)
        for i in range(len(before)):
            before[i] = tt+before[i]+tt
        for v in tmp:
            before.append(v)
        DFS(L+1, before)

DFS(0, arr)
