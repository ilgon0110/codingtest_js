import sys

input = sys.stdin.readline

N = int(input())

arr = [0]*N
ans = 0

def is_possible(row):
    for i in range(row):
        if arr[row] == arr[i]:
            return False
        if abs(row - i) == abs(arr[row] - arr[i]):
            return False
    return True

def DFS(row):
    if row == N:
        global ans
        ans += 1
        return
    else:
        for i in range(N):
            arr[row] = i
            if is_possible(row):
                DFS(row+1)

DFS(0)
print(ans)
