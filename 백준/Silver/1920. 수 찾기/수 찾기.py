N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
M = int(input())
arr2 = list(map(int, input().split()))


def find(n):
    lt = 0
    rt = N-1
    while (lt <= rt):
        mid = (lt+rt)//2
        if (n == arr1[mid]):
            return True
        elif n < arr1[mid]:
            rt = mid-1
        else:
            lt = mid+1
    return False

for v in arr2:
    if find(v) == True:
        print(1)
    else:
        print(0)
