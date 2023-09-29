import sys
#sys.stdin = open("input.txt", "r")

def gencd(num):
    ans = []
    for i in range(1, num):
        if num % i == 0:
            ans.append(i)
    return ans

while True:
    num = int(input())
    if (num == -1):
        break
    ans = gencd(num)
    if num == sum(ans):
        tmp = ''
        for v in ans:
            tmp += str(v) + ' + '
        print(f"{num} = {tmp[:-3]}")
    else:
        print(f"{num} is NOT perfect.")
