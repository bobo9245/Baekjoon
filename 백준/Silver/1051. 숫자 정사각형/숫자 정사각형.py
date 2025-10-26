n,m=map(int,input().split())
arr=[[int(i) for i in input()] for _ in range(n)]

max_area = 1

max_side_diff = min(n, m) - 1

for r in range(n):
    for c in range(m):
        for s in range(1, max_side_diff + 1):
            
            if r + s < n and c + s < m:
                
                if arr[r][c] == arr[r][c + s] and \
                   arr[r][c] == arr[r + s][c] and \
                   arr[r][c] == arr[r + s][c + s]:
                    
                    current_area = (s + 1) ** 2
                    
                    if current_area > max_area:
                        max_area = current_area

print(max_area)