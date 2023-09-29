import sys
import collections

# sys.stdin = open("input.txt", "r")

N = int(input())
arr = list(int(input()) for _ in range(N))

counter = collections.Counter(arr)

if (counter[1] > counter[0]):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
