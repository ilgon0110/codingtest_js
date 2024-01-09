import sys

T = int(input())

for _ in range(T):
    n = int(input())
    my_dict = dict()
    for _ in range(n):
        value, key = map(str, sys.stdin.readline().rstrip().split())
        if key not in my_dict:
            my_dict[key] = [value]
        else:
            my_dict[key].append(value)
    items = my_dict.items()
    cnt = 1
    for [key, value] in items:
        cnt *= len(value)+1
    print(cnt-1)
