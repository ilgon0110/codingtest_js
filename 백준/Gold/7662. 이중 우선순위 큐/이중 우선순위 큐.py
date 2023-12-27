import sys
import heapq
input = sys.stdin.readline


T = int(input())


def sync(heap):
    while heap and arr[heap[0][1]] == 1:
        heapq.heappop(heap)


for _ in range(T):
    min_queue = []
    max_queue = []
    K = int(input())
    arr = [0 for _ in range(K)]

    for i in range(K):
        [order, n] = list(input().split())
        N = int(n)
        if order == 'I':
            heapq.heappush(min_queue, (N, i))
            heapq.heappush(max_queue, (-N, i))
        elif order == 'D':
            if N == -1 and min_queue:
                [_, idx] = heapq.heappop(min_queue)
                arr[idx] = 1
            elif N == 1 and max_queue:
                [_, idx] = heapq.heappop(max_queue)
                arr[idx] = 1
        sync(max_queue)
        sync(min_queue)
    if min_queue == []:
        print('EMPTY')
    else:
        print(-max_queue[0][0], min_queue[0][0])
