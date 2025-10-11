n=int(input())
dic={}
for _ in range(n):
    low,up=input().split()
    dic[up]=low
s=input()
ans=""
for c in s:
    ans+=dic[c]
a,b=map(int,input().split())
print(ans[a-1:b])