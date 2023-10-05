import sys

T = int(input())

for _ in range(T):
    [N, M] = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    lt = 0
    rt = 0
    cnt = 0
    while lt < len(A) and rt < len(B):
        if A[lt] > B[rt]:
            cnt += len(B) - rt
            lt += 1
        else:
            rt += 1
    print(cnt)
