import sys; input=sys.stdin.readline
n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arrsum=[]
for _ in range(m):
    summ=0
    for i in range(n):
        summ+=arr[i][_]
    arrsum.append(summ)
maxx=0
A=int(input())
if A==1:
    maxx=max(arrsum)
else:
    for _ in range(len(arrsum)-A+1):
        temp=sum(arrsum[_:_+A])
        if temp>maxx:
            maxx=temp
print(maxx)