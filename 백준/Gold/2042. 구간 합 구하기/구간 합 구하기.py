class SegTree:
    def __init__(self,arr):
        self.n=len(arr)
        self.arr=arr
        self.tree=[0]*(4*(self.n))
        self._init(1,0,self.n-1)
    def _init(self, node, start, end):
        if start==end:
            self.tree[node]=self.arr[start]
            return self.tree[node]
        mid=(start+end)//2
        self.tree[node]=self._init(node*2,start,mid)+self._init(node*2+1, mid+1, end)
        return self.tree[node]

    def _query(self,node,start,end,left,right):
        if left>end or right<start:
            return 0
        if left<=start and end<=right:
            return self.tree[node]
        mid=(start+end)//2
        return self._query(node*2, start,mid,left,right)+self._query(node*2+1,mid+1,end,left,right)

    def _update(self,node,start,end,index,value):
        if index<start or index>end:
            return
        if start==end:
            self.tree[node]=value
            return
        mid=(start+end)//2
        self._update(node*2,start,mid,index,value)
        self._update(node*2+1,mid+1,end,index,value)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]

    def query(self,left,right):
        return self._query(1,0,self.n-1,left,right)
    def update(self,index,value):
        self._update(1,0,self.n-1,index,value)
        self.arr[index]=value

import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
arr=[int(input())for _ in range(n)]
segtree=SegTree(arr)
for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        segtree.update(b-1,c)
    else:
        print(segtree.query(b-1,c-1))