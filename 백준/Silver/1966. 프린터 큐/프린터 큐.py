from collections import deque
import copy

T = int(input())

def isMostImportant(queue):
    tmp = copy.deepcopy(queue)
    [myNum, myPower] = tmp.popleft()
    for v in tmp:
        [num, power] = v
        if power > myPower:
            return False
    return True

for _ in range(T):
    [N, M] = list(map(int, input().split()))
    important = list(map(int, input().split()))
    stack = deque()
    arr = []
    for i in range(N):
        stack.append((i, important[i]))
    while (len(stack)):
        if isMostImportant(stack) == True:
            arr.append(stack.popleft())
        else:
            stack.append(stack.popleft())

    for i in range(len(arr)):
        [num, power] = arr[i]
        if num == M:
            print(i+1)
            break
