import sys

input = sys.stdin.readline

N = int(input())

def multi(a, b):
    ans = [[0 for _ in range(2)] for _ in range(2)]
    for k in range(2):
        for i in range(2):
            for j in range(2):
                ans[k][i] += a[k][j] * b[j][i] % 1000000007
    return ans

def divide(board, n):
    if n == 1:
        return board
    else:
        tmp = divide(board, n//2)
        if n % 2 == 0:
            return multi(tmp, tmp)
        else:
            return multi(multi(tmp, tmp), board)

matrix = [[1, 1], [1, 0]]
result = divide(matrix, N)
print(result[0][1] % 1000000007)
