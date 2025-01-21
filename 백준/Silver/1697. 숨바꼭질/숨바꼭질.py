import sys
#sys.stdin=open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs():
    visited =[0]*100001
    q=deque()
    q.append([N,0])
    visited[N]=1
    while q:
        X , cnt = q.popleft()
        if X==K: #동생위치로 오면 return
            return cnt
        for next in [X*2,X+1,X-1]:
            if next > 100000 or next < 0:
                continue
            if visited[next]:
                continue
            visited[next]=1
            q.append([next,cnt+1])
    return 0
N,K = map(int,input().strip().split())
result=bfs()
print(result)