import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
m = list(map(int, str(input())))
for i in range(3):
    print(n * m[-1])
    print(n * m[-2])
    print(n * m[-3])
    break
print(n * int(''.join(map(str, m))))
