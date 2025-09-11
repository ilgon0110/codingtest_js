import sys

input = sys.stdin.readline

N, B = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))


def multi(arr1, arr2):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += arr1[i][k] * arr2[k][j]
    for i in range(N):
        for j in range(N):
            result[i][j] = result[i][j] % 1000
    return result


def divide_conquer(arr, n):
    if n == 1:
        return arr
    tmp = multi(arr, arr)
    if n == 2:
        return tmp
    elif n % 2 == 0:
        return divide_conquer(tmp, n//2)
    else:
        return multi(arr, divide_conquer(tmp, n//2))


ans = divide_conquer(arr, B)
for i in range(N):
    for j in range(N):
        ans[i][j] = ans[i][j] % 1000
for i in range(N):
    print(*ans[i])
