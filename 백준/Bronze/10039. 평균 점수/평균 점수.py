import sys
import math
# sys.stdin = open("input.txt", "r")

arr = [int(input()) for _ in range(5)]

for i in range(len(arr)):
    if arr[i] < 40:
        arr[i] = 40

print(math.floor(sum(arr)/len(arr)))
