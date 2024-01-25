import sys

N = int(sys.stdin.readline())
cost = []
for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, len(cost)):
    bridge = cost[i]
    bridge[0] = bridge[0] + min(cost[i-1][1], cost[i-1][2])
    bridge[1] = bridge[1] + min(cost[i-1][0], cost[i-1][2])
    bridge[2] = bridge[2] + min(cost[i-1][0], cost[i-1][1])

print(min(cost[len(cost)-1]))
