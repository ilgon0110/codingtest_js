import sys

# sys.stdin = open("input.txt", "r")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dict = dict()
dict['Q1'] = 0
dict['Q2'] = 0
dict['Q3'] = 0
dict['Q4'] = 0
dict['AXIS'] = 0


for v in arr:
    [x, y] = v
    if (x == 0 or y == 0):
        dict['AXIS'] += 1
    elif x > 0 and y > 0:
        dict['Q1'] += 1
    elif x > 0 and y < 0:
        dict['Q4'] += 1
    elif x < 0 and y > 0:
        dict['Q2'] += 1
    elif x < 0 and y < 0:
        dict['Q3'] += 1
for i in dict:
    print(f"{i}: {dict[i]}")
