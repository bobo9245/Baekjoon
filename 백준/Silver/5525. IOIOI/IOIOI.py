def make_ioi(n):
    return list('IO'*n+'I')
n=int(input())
ioi=make_ioi(n)
m=int(input())
s=list(input())
count=0
for _ in range(0,len(s)-len(ioi)):
    if s[_:_+len(ioi)]==ioi:
        count+=1
if len(s)-len(ioi)==0:
    if s==ioi:
        count+=1
print(count)