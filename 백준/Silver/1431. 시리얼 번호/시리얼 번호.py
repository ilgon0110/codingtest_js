import sys

N = int(input())

arr = [list(input()) for _ in range(N)]
numArr = []

def customSort(arr):
    arr.sort(key=lambda x: (len(x), sum(int(char)
             for char in x if str(char).isdigit()), x))
    return arr

tmp = customSort(arr)

for v in tmp:
    print(''.join(v))
