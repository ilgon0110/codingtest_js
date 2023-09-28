import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    print(f"Case #{i+1}: {arr[i][0] + arr[i][1]}")
