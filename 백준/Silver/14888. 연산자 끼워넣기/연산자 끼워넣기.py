import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int , input().split()))
cals = list(map(int,input().split()))
operators = []
tmp = ['+','-','*','/']

for i in range(4):
    for _ in range(cals[i]):
        operators.append(tmp[i])

visited = [0 for _ in range(len(operators))]
all_operators = []


def calculate(one,two,operator):
    if operator == '+':
        return one+two
    if operator == '-':
        return one-two
    if operator == '*':
        return one*two
    if operator == '/':
        if one < 0:
            return -(abs(one)//two)
        else:
            return one//two

answer = []

max_answer = -sys.maxsize
min_answer = sys.maxsize

def recursive(L,tmp):
    if L == N-1:
        before = 0
        final = 0
        global max_answer
        global min_answer
        for i in range(-1,N - 1):
            if i == -1:
                final = arr[i+1]
            else:
                final = calculate(before, arr[i + 1], tmp[i])
            before = final
        max_answer = max(max_answer, final)
        min_answer = min(min_answer ,final)
        return
    else:
        for i in range(N-1):
            if visited[i] == 0:
                visited[i] = 1
                tmp.append(operators[i])
                recursive(L+1,tmp)
                tmp.pop()
                visited[i] = 0

recursive(0,[])

print(max_answer)
print(min_answer)



