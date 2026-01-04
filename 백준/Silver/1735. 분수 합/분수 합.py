import sys
input=sys.stdin.readline

a1,b1=map(int,input().split())
a2,b2=map(int,input().split())

def GCD(b1,b2):
    while b1 > 0:
        b2, b1 = b1, b2 % b1
    return b2

lcm=(b1*b2)//GCD(b1,b2)
#print(lcm)

a3,b3=((a1*(lcm//b1))+(a2*(lcm//b2))),lcm

gcd=GCD(a3,b3)
print(a3//gcd,b3//gcd)