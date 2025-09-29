import sys
from collections import deque

input=sys.stdin.readline

T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    d=list(map(int,input().strip().split()))
    graph=[[] for _ in range(N+1)]
    inDegree=[0 for _ in range(N+1)]
    dp=[0 for _ in range(N+1)]
    queue=deque()

    # 위상정렬을 위한 Graph와, 들어가는 차수 계산
    for i in range(K):
        a,b=map(int,input().strip().split())
        graph[a].append(b)
        inDegree[b]+=1

    # 어디 건물을 기준으로 할건지에 대한 설정
    w=int(input().strip())

    # DP
    for i in range(1,N+1):
        # 위상정렬 : inDegree가 0인 애들은 시작점이라 가정하고 queue에 넣고 시작한다.
        if inDegree[i]==0:
            queue.append(i)
            dp[i]=d[i-1]

    # 위상정렬
    while queue:
        tmp=queue.popleft()
        for i in graph[tmp]:
            inDegree[i]-=1
            # 기존 위상정렬과 다른 점은, 여기에서 dp를 추가적으로 이용한다는 점이지 않을까?
            dp[i]=max(dp[i],dp[tmp]+d[i-1])
            # 그렇게 해서 입력차수가 0이 되면 다시 queue에 append해준다.
            if inDegree[i]==0:
                queue.append(i)
    # 최소값을 뽑아야 하니까, 이렇게 완료된 애를 기반으로 DP 뽑기
    print(dp[w])