import math
n,m = map(int,input().split())

six = math.inf
one = math.inf
for i in range(m):
    a,b = map(int,input().split())
    if a<six:
        six = a
    if b<one:
        one = b
six = six if six<6*one else 6*one
remain = min(six,(n%6)*one)
if a==0 or b==0:
    print(0)
else:
    print((n//6)*six + remain)