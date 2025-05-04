import bisect

# 피보나치 수 미리 생성
fib = [1, 2]
while True:
    next_fib = fib[-1] + fib[-2]
    if len(str(next_fib)) > 100:
        break
    fib.append(next_fib)

# 입력 처리
while True:
    try:
        line = input().strip()
        if line == "":
            continue
        a, b = line.split()
        if a == "0" and b == "0":
            break

        # 문자열을 정수로 변환
        a = int(a)
        b = int(b)

        # 이진 탐색으로 범위 내 피보나치 수 개수 찾기
        left = bisect.bisect_left(fib, a)
        right = bisect.bisect_right(fib, b)

        print(right - left)

    except EOFError:
        break
