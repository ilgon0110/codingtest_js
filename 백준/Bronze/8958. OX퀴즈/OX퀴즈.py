import sys

# sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(input()) for _ in range(N)]

for v in arr:
    count = 0
    answer = 0
    for target in v:
        if target == 'O':
            answer += 1 + count
            count += 1
        else:
            count = 0
    print(answer)
