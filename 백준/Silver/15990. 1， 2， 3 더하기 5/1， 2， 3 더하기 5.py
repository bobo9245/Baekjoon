import sys
input = sys.stdin.readline
T = int(input())
ar = [[0]*100001 for i in range(3)]
ar[0][1]=1
ar[0][3]=1
ar[1][2]=1
ar[1][3]=1
ar[2][3]=1
for i in range(4,100001):
    ar[0][i]=(ar[1][i-1]+ar[2][i-1])%1000000009
    ar[1][i]=(ar[0][i-2]+ar[2][i-2])%1000000009
    ar[2][i]=(ar[0][i-3]+ar[1][i-3])%1000000009
for _ in range(T):
    n = int(input())
    sum=0 
    for i in range(3):
        sum+=ar[i][n]
    print(sum%1000000009)