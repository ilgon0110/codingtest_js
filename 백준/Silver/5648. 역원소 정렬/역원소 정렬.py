import sys

tmp = list(map(int, input().split()))
N = tmp[0]
rest = []
for i in range(1, len(tmp)):
    rest.append(tmp[i])

while True:
    try:
        tmp = list(map(int, input().split()))
        for i in tmp:
            rest.append(i)
    except:
        break

ans = []
for i in rest:
    a = int(''.join(list(reversed(list(str(i))))))
    ans.append(a)

ans.sort()
for v in ans:
    print(v)
