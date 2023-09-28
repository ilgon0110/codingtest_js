import sys
# sys.stdin = open("input.txt", "r")

N = int(input())

left = 1
right = N-1
count = 1

while left < right:
    left += 1
    right -= left
    count += 1

print(count)
