arr=[]
i=1
while len(arr)<1000:
    for j in range(i):
        arr.append(i)
    i+=1
sum=0
a,b=map(int,input().split())
for i in range(a-1,b):
    sum+=arr[i]
print(sum)