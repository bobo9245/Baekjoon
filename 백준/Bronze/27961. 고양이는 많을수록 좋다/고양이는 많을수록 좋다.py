n=int(input())
count=1
m=1
while m<n:
    count+=1
    m*=2
print(count if n>=1 else 0)