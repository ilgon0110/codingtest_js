import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

lt = 0
rt = max(trees)
ans = 0
while (lt <= rt):
    mid = (lt+rt)//2
    take_tree = 0
    for tree in trees:
        if tree > mid:
            take_tree += tree-mid
    if take_tree >= M:
        lt = mid+1
        ans = mid
    else:
        rt = mid-1

print(ans)
