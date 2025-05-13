def solve():
    n, k, a, b = map(int, input().split())

    water_levels = [k] * n
    day = 0
    
    num_groups = n // a

    while True:
        day += 1
        
        # 1. 물주기
        # 오늘 물을 줄 그룹의 인덱스 (0-indexed)
        group_to_water_idx = (day - 1) % num_groups
        
        # 물을 줄 첫 번째 화분의 인덱스
        start_plant_idx = group_to_water_idx * a
        
        for i in range(a):
            water_levels[start_plant_idx + i] += b
            
        # 2. 모든 화분 수분 1 감소 및 죽음 확인
        plant_died_today = False
        for i in range(n):
            water_levels[i] -= 1
            if water_levels[i] == 0:
                plant_died_today = True
        
        # 3. 캣닢이 죽었는지 확인
        if plant_died_today:
            print(day)
            return

# # 로컬 테스트용 예제 입력 처리 (제출 시 주석 처리)
# # 예시 1: N=4, K=3, A=2, B=1  => 예상 출력: 5
# # input = lambda: "4 3 2 1" 
# # 예시 2: N=4, K=1, A=2, B=1  => 예상 출력: 1
# # input = lambda: "4 1 2 1"
# # 예시 3: N=2, K=5, A=1, B=1  => 예상 출력: 9
# # input = lambda: "2 5 1 1"

solve()