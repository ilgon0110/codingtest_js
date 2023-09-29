import sys
#sys.stdin = open("input.txt", "r")

arr = [list(map(int, input().split())) for _ in range(3)]

x = 0
y = 0
for v in arr:
    [x1, y1] = v
    xCount = 0
    yCount = 0
    for j in arr:
        [x2, y2] = j
        if (x1 == x2):
            xCount += 1
        if (y1 == y2):
            yCount += 1
    if (xCount == 1):
        x = x1
    if (yCount == 1):
        y = y1

print(x, y)
