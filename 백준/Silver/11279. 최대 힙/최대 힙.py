import sys
import heapq

N = int(sys.stdin.readline())

queue = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(queue) == 0:
            print(0)
        else:
            print(-heapq.heappop(queue))
    else:
        heapq.heappush(queue, -x)
