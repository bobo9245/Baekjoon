import sys
input=sys.stdin.readline

def modify(node,start,end,index,value):
    if index<start or index>end:
        return

    if start==end:
        tree[node]=value
        return

    mid=(start+end)//2
    modify(node*2,start,mid,index,value)
    modify(node*2+1,mid+1,end,index,value)

    tree[node]=tree[node*2]+tree[node*2+1]

def sum_range(node,start,end,left,right):
    if left>end or right<start:
        return 0

    if left<=start and right>=end:
        return tree[node]

    mid=(start+end)//2
    return sum_range(node*2,start,mid,left,right)+sum_range(node*2+1,mid+1,end,left,right)

N,M=map(int,input().split())
tree=[0]*(4*N)

for i in range(M):
    try:
        data=list(map(int,input().split()))
    except:
        continue

    if not data:
        continue

    Q,A,B=data[0],data[1],data[2]

    if Q==0:
        if A>B:
            A,B=B,A
        print(sum_range(1,0,N-1,A-1,B-1))
    else:
        modify(1,0,N-1,A-1,B)