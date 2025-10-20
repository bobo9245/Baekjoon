T=int(input())
for _ in range(T):
    L,R,S=map(int,input().split())
    print(min(2*(S-L)+1,2*(R-S)))