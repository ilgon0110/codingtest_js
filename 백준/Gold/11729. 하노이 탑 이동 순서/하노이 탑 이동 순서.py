import sys

N = int(input())

board = [list(i for i in range(1, N+1))]
for _ in range(N-1):
    board.append([0 for _ in range(N)])

path = []
answer = 0

def hanoi(L, start, via, end, count):
    global answer
    answer += 1
    if L == 1:
        path.append([start, end])
        return
    else:
        hanoi(L-1, start, end, via, count+1)
        path.append([start, end])
        hanoi(L-1, via, start, end, count+1)


hanoi(N, 1, 2, 3, 0)
print(answer)
for v in path:
    print(*v)
