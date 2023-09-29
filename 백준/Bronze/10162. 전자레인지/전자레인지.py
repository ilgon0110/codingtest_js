import sys

# sys.stdin = open("input.txt", "r")

N = int(input())

arr = [5*60, 60, 10]
if (N % 10 != 0):
    print(-1)
else:
    for i in range(3):
        count = N//arr[i]
        N = N - arr[i]*count
        print(count)
