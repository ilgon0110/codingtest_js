import sys

input = sys.stdin.readline

[N, M] = list(map(int, input().rstrip().split()))

arr = [input().rstrip() for _ in range(N)]
my_dict = dict()
for i in range(1, len(arr)+1):
    my_dict[arr[i-1]] = i
    my_dict[str(i)] = arr[i-1]


for v in range(M):
    target = input().rstrip()
    print(my_dict[target])
