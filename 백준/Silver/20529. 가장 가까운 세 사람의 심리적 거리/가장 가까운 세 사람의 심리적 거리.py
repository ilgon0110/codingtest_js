import sys

T = int(sys.stdin.readline())


def DFS(L,  mbti,  visited, tmp):
    if L == 3:
        global answer
        [one, two, three] = tmp
        total = cal_mind(one, two) + cal_mind(one, three) + \
            cal_mind(two, three)
        answer = min(total, answer)
        return
    else:
        for i in range(len(mbti)):
            if visited[i] > 0:
                continue
            tmp.append(mbti[i])
            visited[i] = 1
            DFS(L+1, mbti, visited, tmp)
            tmp.pop()
            visited[i] = 0


def cal_mind(one, two):
    cnt = 4
    for i in range(4):
        if one[i] == two[i]:
            cnt -= 1
    return cnt


for _ in range(T):
    N = int(sys.stdin.readline())
    mbti = list(map(str, sys.stdin.readline().split()))
    visited = [0 for _ in range(N)]
    answer = sys.maxsize
    if(N > 32):
        print(0)
    else:
        DFS(0, mbti, visited, [])
        print(answer)
