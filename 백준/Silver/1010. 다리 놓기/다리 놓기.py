import operator as op
from functools import reduce


def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise ValueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

n=int(input())
for _ in range(n):
    a,b = map(int,input().split())
    print(nCr(b,a))