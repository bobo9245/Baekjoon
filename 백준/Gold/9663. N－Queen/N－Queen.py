n = int(input())
# 열 점유 여부
used_c = [False]*n
# y = x 선상 점유 여부
used_up = [False]*(2*(n-1)+1)
# y = -x 선상 점유 여부
used_down = [False]*(2*(n-1)+1)

def dfs(k):
    global n,cnt

    # 모든 Queen을 놨을 경우
    if k==n:
        cnt+=1
        return

    # i를 점유할 열 번호로 활용
    for i in range(n):
        if not used_c[i] and not used_up[k+i] and not used_down[(n-1)+k-i]:
            used_c[i]=True
            used_up[k+i]=True
            used_down[(n-1)+k-i]=True
            dfs(k+1)
            used_c[i]=False
            used_up[k+i]=False
            used_down[(n-1)+k-i]=False

cnt=0
dfs(0)
print(cnt)