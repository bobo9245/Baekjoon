n=int(input())
for i in range(n):
    inp=list(map(int,input().split()))
    print(inp[0]*(inp[2]-1)+inp[1])