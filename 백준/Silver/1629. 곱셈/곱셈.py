import sys

[A, B, C] = list(map(int, input().split()))

def dac(a, b, c):
    if a == 1:
        return a
    elif b <= 1:
        return a % c
    else:
        if b % 2 == 0:
            return (dac(a, b//2, c)**2) % c
        elif b % 2 == 1:
            return ((dac(a, b//2, c)**2)*a) % c

print(dac(A, B, C))
