a,b = map(int,input().split())
sg = a*b
ar = list(map(int,input().split()))
for a in ar:
    print(a-sg, end=' ')