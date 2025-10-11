n=int(input())
rm=601
for _ in range(n):
    temp=sum(list(map(int,input().split())))
    if temp>=512 and temp<rm:
        rm=temp
print(-1 if rm==601 else rm)