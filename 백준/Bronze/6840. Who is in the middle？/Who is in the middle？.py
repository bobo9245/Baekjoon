# 세 개의 무게를 입력
lst = [int(input()) for _ in range(3)]

# 무게를 정렬하고, 중간 무게에 해당하는 Mama Bear의 그릇의 무게를 출력
print(sorted(lst)[1])