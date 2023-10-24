my_dict = dict()

[N, M] = list(map(int, input().split()))

for v in range(N):
    [key, value] = list(map(str,input().split()))
    my_dict[key] = value

for v in range(M):
    key = str(input())
    print(my_dict[key])
