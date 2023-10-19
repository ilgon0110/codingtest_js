import sys
input = sys.stdin.readline

[K, L] = list(map(int, input().split()))

my_dict = dict()

for i in range(1, L+1):
    my_dict[input().rstrip()] = i

arr = []
for (a, b) in my_dict.items():
    arr.append((a, b))

arr.sort(key=lambda x: x[1])
M = len(arr)
if K > M:
    for i in range(M):
        print(arr[i][0])
else:
    for i in range(K):
        print(arr[i][0])

