import sys,math
input=sys.stdin.readline

n=int(input())
road=list(map(int,input().split()))
oil=list(map(int,input().split()))
arr=[]
#min price라는 뜻
mp=math.inf
for o in oil:
    mp=min(mp,o)
    arr.append(mp)
arr.pop()
ans=0
for i in range(n-1):
    ans+=road[i]*arr[i]
print(ans)