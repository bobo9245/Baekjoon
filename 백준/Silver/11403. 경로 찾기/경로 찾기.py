n=int(input())
ar = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if (ar[j][i] and ar[i][k]):
                ar[j][k]=1 
for a in ar:
    print(*a)