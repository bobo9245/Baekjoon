def find_next_number(sequence):
    n = len(sequence)
    
    if n == 1:
        return "A"
    elif n == 2:
        return sequence[0] if sequence[0] == sequence[1] else "A"
    
    # a와 b를 구하기 위해 첫 두 항을 사용
    if sequence[1] - sequence[0] == 0:
        a = 1
        b = 0
    else:
        a = (sequence[2] - sequence[1]) // (sequence[1] - sequence[0]) if (sequence[1] - sequence[0]) != 0 else None
        b = sequence[1] - sequence[0] * a if a is not None else None
    
    # 검증: 모든 항이 해당 규칙을 만족하는지 확인
    if a is not None and b is not None:
        for i in range(n - 1):
            if sequence[i] * a + b != sequence[i + 1]:
                return "B"
        return sequence[-1] * a + b
    
    return "B"

# 입력 처리
n = int(input())
sequence = list(map(int, input().split()))

# 결과 출력
print(find_next_number(sequence))
