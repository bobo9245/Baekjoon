# 입력 받기
n = int(input().strip())

# 주인이 받은 카드 점수들
juwon_cards = list(map(int, input().split()))

# 사장님이 받은 카드 점수들
owner_cards = list(map(int, input().split()))

# 카드를 오름차순으로 정렬하여 승부를 쉽게 판단
juwon_cards.sort()
owner_cards.sort()

# 주인이 이긴 횟수와 사장님이 이긴 횟수를 추적
juwon_score = 0
owner_score = 0

# 각 라운드에서 승부 진행
i, j = 0, 0
while i < n and j < n:
    if juwon_cards[i] < owner_cards[j]:
        # 주인이 더 작은 카드를 냈으므로 점수 획득
        juwon_score += 1
        i += 1
        j += 1
    else:
        # 사장님이 더 작은 카드이거나 무승부인 경우
        j += 1

# 필요한 최소 승점 계산
needed_score = (n + 1) // 2

# 주인이 필요한 점수를 얻었는지 확인하고 출력
if juwon_score >= needed_score:
    print("YES")
else:
    print("NO")
