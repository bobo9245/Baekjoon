n,m= map(list,input().split())
l = len(m)-len(n)+1
if l==0:
    count=0
    for i in range(len(m)):
        if n[i]!=m[i]:
            count+=1
    print(count)
else:
    count=999
    for i in range(l):
        temp=0
        for j in range(len(n)):
            # print(m[i+j], n[j])
            if m[i+j]!=n[j]:
                temp+=1
        count = min(count,temp)
    print(count)