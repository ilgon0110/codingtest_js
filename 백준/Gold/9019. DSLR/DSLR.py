import sys
from collections import deque

T = int(input())

def D(n):
    return (n*2) % 10000


def S(n):
    return (n-1) % 10000


def L(n):
    return (((n % 1000) // 100)*1000) + (((n % 100) // 10) * 100) + ((n % 10) * 10) + n // 1000


def R(n):
    return (n % 10) * 1000 + (n // 1000) * 100 + ((n % 1000) // 100) * 10 + ((n % 100) // 10)


for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    queue = deque()
    queue.append((A, ''))
    checked = [False for _ in range(10001)]

    while (queue):
        (N, text) = queue.popleft()
        if (N == B):
            print(text)
            break
        d = D(N)
        if not checked[d]:
            checked[d] = True
            queue.append((d, text+'D'))
        s = S(N)
        if not checked[s]:
            checked[s] = True
            queue.append((s, text+'S'))
        l = L(N)
        if not checked[l]:
            checked[l] = True
            queue.append((l, text+'L'))
        r = R(N)
        if not checked[r]:
            checked[r] = True
            queue.append((r, text+'R'))
