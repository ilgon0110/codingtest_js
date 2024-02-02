import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
front = []
while True:
    N = input()
    if N == '':
        break
    front.append(int(N))

def postorder(rootIdx, endIdx):
    if rootIdx > endIdx:
        return
    global front
    right_start = endIdx + 1
    
    for i in range(rootIdx+1, endIdx + 1):
        if front[rootIdx] < front[i]:
            right_start = i
            break

    postorder(rootIdx+1, right_start-1)
    postorder(right_start, endIdx)
    print(front[rootIdx])

postorder(0, len(front) - 1)
