import sys
input=sys.stdin.readline
n=int(input())
students=[]
for _ in range(n):
    students.append(list(map(int,input().split())))
#print(*students)

m=0
ans=(-1,-1)
for i in range(5):
    for j in range(i+1,5):
        temp=0
        for k in range(n):
            if students[k][i]==1 and students[k][j]==1:
                temp+=1
        if temp>m:
            m=temp
            ans=(i,j)
anss=[0,0,0,0,0]
if ans==(-1,-1):
    anss=[1,1,0,0,0]
else:    
    for a in ans:
        anss[a]=1
print(m)
print(*anss)