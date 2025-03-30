def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def make_sequence(n):
    A = list(range(1, n + 1))  # 오름차순 초기화

    # 조건 1: A_2는 2의 배수
    if A[1] % 2 != 0:
        A[1] += 1
        for i in range(2, n):
            A[i] = A[i-1] + 1

    # 조건 2: A_N은 소수
    # 1000 이하의 소수 중, A[N-1]보다 크고 가장 작은 소수로 설정
    candidate = A[-2] + 1
    while candidate <= 1000:
        if is_prime(candidate):
            A[-1] = candidate
            break
        candidate += 1

    return A

# 입력 및 출력 처리
n = int(input())
A = make_sequence(n)

print(n)
print(' '.join(map(str, A)))
