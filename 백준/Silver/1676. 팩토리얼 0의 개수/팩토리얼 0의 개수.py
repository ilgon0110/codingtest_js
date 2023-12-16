N = int(input())

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

target = str(factorial(N))
arr = []
for v in target:
    arr.append(v)
tmp = list(reversed(arr))

for i in range(len(tmp)):
    if tmp[i] != '0':
        print(i)
        break
