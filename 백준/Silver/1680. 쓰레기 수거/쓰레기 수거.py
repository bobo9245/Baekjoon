t = int(input()) # 테스트 케이스 수

for _ in range(t):
    w, n = map(int,input().split())
    cnt = 0
    li = [] # 각 지점 쓰레기 갯수
    for i in range(n):
        x_i, w_i = map(int,input().split()) # 거리, 쓰레기 양
        li.append([x_i, w_i])
    
    idx = 0
    w_tmp = w
    while idx < n:
        if li[idx][1] < w_tmp: # 쓰레기를 담고도 남으면 더 뒤로 가기 
            w_tmp,li[idx][1] = max(0,w_tmp- li[idx][1]), max(0,li[idx][1]-w_tmp)
            idx += 1
            if idx == n:
                 cnt += li[idx-1][0] * 2
        elif li[idx][1] == w_tmp: # 다 담았으면 0으로 만들고 다시 돌아가기, 그리고 다시뒤로가기 
                li[idx][1] = 0
                w_tmp = w
                cnt += li[idx][0] * 2
                idx += 1

        else: # 다 못담으면 돌아가기 
            cnt += li[idx][0] * 2
            w_tmp = w
        
    print(cnt)