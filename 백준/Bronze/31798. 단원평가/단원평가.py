import math
a,b,c=map(int,input().split())
if a==0:
    print(c**2-b)
elif b==0:
    print(c**2-a)
else:
    print(int(math.sqrt(a+b)))