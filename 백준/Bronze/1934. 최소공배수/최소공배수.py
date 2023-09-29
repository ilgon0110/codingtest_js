import sys
import math
# sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for x in arr:
    [num1, num2] = x
    print(num1*num2 // math.gcd(num1, num2))
