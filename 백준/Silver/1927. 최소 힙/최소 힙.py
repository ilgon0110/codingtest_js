import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for v in range(N):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
        pass
    else:
        heapq.heappush(heap, num)
