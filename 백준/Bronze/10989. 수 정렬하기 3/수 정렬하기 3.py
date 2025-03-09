import sys

#sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(10001)]

for i in range(N):
    num = int(input())
    arr[num]+=1

for i in range(len(arr)):
    if arr[i] == 0:
        continue
    
    for _ in range(arr[i]):
        print(i)