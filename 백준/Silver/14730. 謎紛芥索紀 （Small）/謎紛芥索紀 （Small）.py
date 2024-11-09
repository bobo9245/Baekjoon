n=int(input())
f1 = 0
for i in range(n):
    a,b = map(int,input().split())
    f1 = f1 + (a*b)
print(f1)