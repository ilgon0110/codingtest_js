import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(input())


cnt = 0
bf = -1
flag = 0
for i in range(M):
    if S[i] == 'I':
        continue
    if i > 0 and i < M-1 and S[i] == 'O' and S[i-1] == 'I' and S[i+1] == 'I':
        flag += 1
        if i-2 != bf:
            flag = 1
        if flag >= N:
            cnt += 1
        bf = i


print(cnt)
