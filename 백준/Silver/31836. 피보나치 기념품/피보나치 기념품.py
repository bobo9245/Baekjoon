import sys
input = sys.stdin.readline

def main():
    N = int(input())
    
    # 1) F[1..N+2] 계산
    F = [0] * (N + 3)
    F[1] = F[2] = 1
    for i in range(3, N + 3):
        F[i] = F[i-1] + F[i-2]
    
    # 2) 전체 합 S = sum_{i=1..N} F[i] = F[N+2] - 1
    S = F[N+2] - 1
    
    # 3) S가 홀수면 F[N]을 버리고 M = N-1
    M = N
    if S % 2 != 0:
        S -= F[N]
        M = N - 1
    
    # 4) 목표 합 = S/2
    target = S // 2
    
    # 5) 그리디로 세림(A)에 줄 인덱스 선택
    used = [False] * (N + 1)
    A = []
    for i in range(M, 0, -1):
        if F[i] <= target:
            A.append(i)
            used[i] = True
            target -= F[i]
            if target == 0:
                break
    
    # 6) 성주(B)는 나머지
    B = [i for i in range(1, M+1) if not used[i]]
    
    # 7) 출력
    print(len(A))
    print(*A)
    print(len(B))
    print(*B)
    
main()
