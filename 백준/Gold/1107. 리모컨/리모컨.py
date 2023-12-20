import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = []
if M > 0:
    for v in list(map(int, input().split())):
        broken.append(v)

now = 100
ans = sys.maxsize

nArr = list(str(N))

if abs(N-now) < 3:
    print(abs(N-now))
else:
    for i in range(1000000):
        tmp = list(str(i))
        flag = True
        for v in tmp:
            if int(v) in broken:
                flag = False
                break
        if flag == False:
            continue
        if abs(i-N) + len(str(i)) < ans:
            ans = abs(i-N)+len(str(i))
    print(min(abs(now - N), ans))
