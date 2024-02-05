import sys
import copy

input = sys.stdin.readline

N, B = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def multi(a, b):
    tmp2 = copy.deepcopy(a)
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += a[i][k] * b[k][j]
            tmp2[i][j] = tmp % 1000
    return tmp2

# 분할 정복
def square(a, recursive):
    if recursive == 1:
        return a
    tmp = square(a, recursive//2)
    if recursive % 2 == 0:
        return multi(tmp, tmp)
    else:
        return multi(multi(tmp, tmp), a)

ans = square(board, B)

for i in range(N):
    for j in range(N):
        ans[i][j] = ans[i][j] % 1000

for v in ans:
    print(*v)
