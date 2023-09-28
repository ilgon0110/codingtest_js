import sys
import math
# sys.stdin = open("input.txt", "r")

N = int(input())


def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True


if N == 1:
    exit()
ans = []
while (isPrime(N) == False):
    for i in range(2, N):
        if N % i == 0:
            ans.append(i)
            N = N // i
            break
        elif isPrime(N) == True:
            ans.append(i)
            break
ans.append(N)
ans.sort()

for i in ans:
    print(i)
