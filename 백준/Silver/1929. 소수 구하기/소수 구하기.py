import math

[N, M] = list(map(int, input().split()))
for i in range(N, M+1):
    if i == 1:
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        print(i)
