import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline
n,m = map(int,input().split())
arr=list(range(n+1))
def find_parent(x):
    if arr[x]!=x:
        arr[x]=find_parent(arr[x])
    return arr[x]
def union(a,b):
    a=find_parent(a)
    b=find_parent(b)
    if a<b:
        arr[b]=a
    else:
        arr[a]=b
for _ in range(m):
    a,b,c = map(int,input().split())
    if a==1:
        print('YES' if find_parent(b)==find_parent(c) else 'NO')
    elif a==0:
        union(b,c)