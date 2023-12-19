import sys
input = sys.stdin.readline

[N, M, B] = list(map(int, input().split()))
blocks = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    blocks += tmp
ans = sys.maxsize
targetHeight = 0
allBlocks = sum(blocks)
for height in range(max(blocks), min(blocks) - 1, -1):
    if allBlocks + B >= height * N * M:
        time = 0
        for b in blocks:
            diff = b - height
            if diff > 0:
                time += diff*2
            else:
                time -= diff
        if time < ans:
            ans = time
            targetHeight = height
print(ans, targetHeight)
