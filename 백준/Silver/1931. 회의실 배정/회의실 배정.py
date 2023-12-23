import sys
input = sys.stdin.readline

N = int(input())

table = []

for _ in range(N):
    start, end = map(int, input().split())
    table.append([start, end])


table.sort(key=lambda x: (x[1], x[0]))

time = 0
cnt = 0
for v in table:
    [start, end] = v
    if time <= start:
        time = end
        cnt += 1

print(cnt)
