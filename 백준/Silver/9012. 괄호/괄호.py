from collections import deque

T = int(input())

for _ in range(T):
    text = str(input())
    stack = deque()
    for v in text:
        if v == '(':
            stack.append(v)
        else:
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(v)
    if stack:
        print('NO')
    else:
        print('YES')
