from collections import deque

[N, K] = list(map(int, input().split()))

queue = deque()
ans = []
for i in range(1, N+1):
    queue.append(i)

while (queue):
    for _ in range(K-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

print('<' + ', '.join(map(str, ans)) + '>')
