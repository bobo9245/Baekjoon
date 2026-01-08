import sys
input=sys.stdin.readline
n=int(input())
ans=0
m=n
for _ in range(n):
    ans+=(n/m)
    m-=1
print(ans)