n,m = map(int,input().split())
a=[]
for i in range(n):
    a.append(list(input()))
garo = [0]*m
sero = [0]*n

for i in range(n):
    for j in range(m):
        if a[i][j]=='X':
            garo[j]=1

for i in range(m):
    for j in range(n):
        if a[j][i]=='X':
            sero[j]=1
print(max(garo.count(0),sero.count(0)))