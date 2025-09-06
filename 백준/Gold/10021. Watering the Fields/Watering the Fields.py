import sys
import heapq

#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N,C = map(int,input().split())

nodes = []
parent = [i for i in range(N+1)]

for i in range(1,N+1):
    x1,y1 = map(int,input().split())
    nodes.append([i,(x1,y1)])

def getCost(x,y):
    x1,y1 = nodes[x][1]
    x2,y2 = nodes[y][1]
    return abs(x1-x2)**2 + abs(y1-y2)**2

# root Return
def find(node):
    if parent[node] == node:
        return node
    else:
        parent[node] = find(parent[node])
        return parent[node]

def union(x,y):
    root1,root2 = find(x),find(y)
    if root1 == root2:
        return False
    else:
        parent[root2] = root1
        return True
    
pq = []
for i in range(len(nodes)):
    for j in range(i+1,len(nodes)):
        cost = getCost(i,j)
        if cost >= C:
            heapq.heappush(pq, [cost,i,j])

cnt = 0
total = 0
while pq:
    cost,x,y = heapq.heappop(pq)
    
    if union(x,y):
        cnt+=1
        total+=cost
        if cnt == N-1:
            break
        
if cnt == N-1:
    print(total)
else:
    print(-1)
