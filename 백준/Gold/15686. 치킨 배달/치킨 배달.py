import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())

arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

#---기본설정끝---
# N<50이기 때문에 브루트포스 때려도됨
# combination으로 m짜리 combination 때리기
house=[]
chick=[]
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            house.append([i,j])
        elif arr[i][j]==2:
            chick.append([i,j])

def min_dis(house, chick):
    chickdis=0
    for h in house:
        mindis=9999
        for c in chick:
            mindis=min(mindis, abs(c[0]-h[0])+abs(c[1]-h[1]))
        chickdis+=mindis
    return chickdis
final_min_dis=9999
for i in combinations(chick,m):
    # print(i)
    # print(min_dis(house,i))
    final_min_dis=min(min_dis(house,i),final_min_dis)
print(final_min_dis)