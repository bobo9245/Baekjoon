import sys
input=sys.stdin.readline
B,N,M=map(int,input().split())
dic={}
for _ in range(N):
    item, price=input().split()
    price=int(price)
    dic[item]=price
sum=0
for _ in range(M):
    sum+=dic[input().strip()]

print("acceptable" if sum<=B else "unacceptable")