a,b = map(int,input().split())
l = list(map(int,input().split()))
count = 0
ans=0
for n in l:
    count = 0 if count+n<=0 else count+n
    if count>=b:
        ans = ans+1
print(ans)