import sys

N, M = map(int, sys.stdin.readline().split())

true_num, *true_people = list(map(int, sys.stdin.readline().split()))
answer = M
partys = []
visited = [0 for _ in range(M)]
all_enter = set()
for v in true_people:
    all_enter.add(v)

for _ in range(M):
    partys.append(list(map(int, sys.stdin.readline().split())))


def DFS(L):
    flag = 1
    for v in visited:
        if v == 0:
            flag = 0
            break
    if flag == 1:
        return
    else:
        for i in range(M):
            if visited[i] > 0:
                continue
            _, *party_people = partys[i]
            for people in party_people:
                if people in all_enter:
                    visited[i] = 1
                    for el in party_people:
                        all_enter.add(el)
                    global answer
                    answer -= 1
                    DFS(L+1)
                    break


DFS(0)
print(answer)
