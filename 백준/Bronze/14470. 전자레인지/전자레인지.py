a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

if a<0:
    print(c*abs(a)+d+e*b)
elif a==0:
    print(d+e*b)
else:
    print(e*(b-a))