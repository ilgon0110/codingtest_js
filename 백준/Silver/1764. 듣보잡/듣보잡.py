import sys
input = sys.stdin.readline

N, M = map(int, input().split())

my_dict = dict()

for _ in range(N):
    my_dict[str(input()).rstrip()] = 1
ans = []
for _ in range(M):
    tmp = str(input().rstrip())
    if my_dict.get(tmp) == 1:
        ans.append(tmp)

print(len(ans))
ans.sort()
for v in ans:
    print(v)
