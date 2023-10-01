import sys
import heapq

[N, M] = list(map(int, input().split()))

cards = list(map(int, input().split()))

pqueue = []

for i in cards:
    heapq.heappush(pqueue, i)

for _ in range(M):
    a = heapq.heappop(pqueue)
    b = heapq.heappop(pqueue)
    heapq.heappush(pqueue, a+b)
    heapq.heappush(pqueue, a+b)

print(sum(pqueue))
