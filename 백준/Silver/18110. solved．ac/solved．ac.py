import sys
input = sys.stdin.readline

n = int(input())
arr = []

def my_round(num: float) -> int:
    if num < 0:
        return -my_round(-num)

    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

for _ in range(n):
    arr.append(int(input()))
arr.sort()
out = my_round(n*0.15)
total = 0
M = n-out*2
for i in range(out, n-out):
    total += arr[i]
if n == 0:
    print(0)
else:
    print(my_round(total/M))
