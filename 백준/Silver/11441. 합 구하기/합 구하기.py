import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
s = 0
sarr = []
for a in arr:
    s = s+a
    sarr.append(s)
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    print(sarr[b-1]) if a==1 else print(sarr[b-1]-sarr[a-2])
