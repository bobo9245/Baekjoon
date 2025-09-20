n=int(input())
arr=['PROBRAIN','GROW','ARGOS','ADMIN','ANT','MOTION','SPG','COMON','ALMIGHTY']
m=0
count=0
for i in range(9):
    mm=max(list(map(int,input().split())))
    if mm>m:
        m=mm
        count=i
print(arr[count])