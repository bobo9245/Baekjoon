# 1. 입력 받기
n, k = map(int, input().split())
lights = []
for _ in range(k):
    lights.append(list(map(int, input().split())))

# 2. 신호등을 위치(x) 기준으로 정렬
lights.sort()

current_time = 0
current_pos = 0

# 3. 정렬된 신호등 순회
for x, t, s in lights:
    
    # 3-1. 현재 신호등까지 이동
    travel_time = x - current_pos
    arrival_time = current_time + travel_time
    
    # 3-2. 대기 시간 계산
    wait_time = 0
    if arrival_time < s:
        # Case 1: 첫 초록불 켜지기 전
        wait_time = s - arrival_time
    else:
        # Case 2: 첫 초록불 켜진 후
        time_in_cycle = (arrival_time - s) % (2 * t)
        
        if time_in_cycle >= t:
            # 빨간불 구간 [t, 2*t) 에 도착
            wait_time = (2 * t) - time_in_cycle
            
    # 3-3. 현재 시간 및 위치 갱신
    current_time = arrival_time + wait_time
    current_pos = x

# 4. 마지막 신호등에서 목적지(n)까지 이동
final_travel_time = n - current_pos
total_time = current_time + final_travel_time

# 5. 출력
print(total_time)