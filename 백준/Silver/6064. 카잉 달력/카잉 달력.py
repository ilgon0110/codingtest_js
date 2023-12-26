import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    cnt = x
    front = x
    back = 0

    for i in range(x):
        if back < N:
            back += 1
        else:
            back = 1
    flag = False

    for _ in range(N):
        if back == y:
            print(cnt)
            flag = True
            break
        back += M
        cnt += M
        while (back > N):
            back -= N
    if flag == False:
        print(-1)
