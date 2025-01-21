from collections import deque
n,m = map(int,input().split())
ar = []
for i in range(n):
    ar.append(list(map(int,input().split())))
distances = [[-1]*m for _ in range(n)]
que = deque([])
for i in range(n):
    for j in range(m):
        if ar[i][j]==0:
            distances[i][j]=0
        if ar[i][j]==2:
            distances[i][j]=0
            que.append((i,j))
            
dd = [(1,0), (-1,0), (0,1), (0,-1)]
# print(que)
while(que):
    x,y = que.popleft()
    for (dx,dy) in dd:
        new_x, new_y = x+dx, y+dy
        if (0<=new_x<n) and (0<=new_y<m) and distances[new_x][new_y]==-1:
            distances[new_x][new_y]=distances[x][y]+1
            # print(f"{new_x},{new_y},distance={distances[new_x][new_y]}")
            que.append((new_x, new_y))
for a in range(n):
    for b in range(m):
        print(distances[a][b], end=' ')
    print('')