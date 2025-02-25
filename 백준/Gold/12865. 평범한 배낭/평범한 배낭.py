n,m = map(int,input().split())
arr=[]
for _ in range(n):
    w,v = map(int,input().split())
    arr.append([w,v])
    arr.sort()
values=[0]*(m+1)
for a in arr:
    w,v = a
    for i in range(m,w-1,-1):
        values[i]=max(values[i],values[i-w]+v)
print(values[-1])