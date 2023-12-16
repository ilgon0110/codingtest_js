from collections import deque

stack = deque()

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

now = 0
cnt = 1
answer = []
stack.append(cnt)
answer.append('+')
while (len(stack) and now < len(arr)):
    if stack[len(stack) - 1] > arr[now]:
        break
    while (stack[len(stack)-1] != arr[now]):
        cnt += 1
        stack.append(cnt)
        answer.append('+')
    stack.pop()
    answer.append('-')
    now += 1
    if len(stack) == 0 and now != len(arr):
        cnt += 1
        stack.append(cnt)
        answer.append('+')

if now == N:
    for v in answer:
        print(v)
else:
    print('NO')
