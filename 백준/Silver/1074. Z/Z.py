N, r, c = map(int, input().split())

def sol(N, r, c):
    if N == 0:
        return 0
    else:
        return 2*(r % 2)+(c % 2) + 4*sol(N-1, r//2, c//2)

print(sol(N, r, c))
