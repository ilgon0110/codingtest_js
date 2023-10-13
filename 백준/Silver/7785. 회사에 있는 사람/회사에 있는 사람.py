import sys

N = int(input())

myMap = dict()

for [name, log] in [list(input().split()) for _ in range(N)]:
    if log == 'enter':
        myMap[name] = log
    else:
        myMap.pop(name)

ans = []


for i in myMap:
    ans.append(i)

ans.sort(reverse=True)
for i in ans:
    print(i)
