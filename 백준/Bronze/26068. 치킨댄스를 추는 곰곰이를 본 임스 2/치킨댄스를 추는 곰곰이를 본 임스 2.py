n=int(input())
count=0
for i in range(n):
    if int(input().split('-')[1])<=90:
        count+=1
print(count)