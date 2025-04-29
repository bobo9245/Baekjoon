import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n = int(input())
    
    queue = deque()
    A = []  # 좋아하는 메뉴를 먹은 학생
    B = []  # 좋아하지 않는 메뉴를 먹은 학생
    
    for _ in range(n):
        data = list(map(int, input().split()))
        if data[0] == 1:
            # "1 a b": 학생 a가 좋아하는 메뉴 b를 들고 줄에 섬
            _, a, b = data
            queue.append((a, b))
        else:
            # "2 b": 메뉴 b 1인분 준비 → 맨 앞 학생 한 명 식사 시작
            _, b = data
            student_id, fav = queue.popleft()
            if fav == b:
                A.append(student_id)
            else:
                B.append(student_id)
    
    # 남은 사람들은 식사 못 함
    C = [student_id for student_id, _ in queue]
    
    # 결과 정렬 및 출력 함수
    def print_list(lst):
        if lst:
            print(' '.join(map(str, sorted(lst))))
        else:
            print('None')
    
    print_list(A)
    print_list(B)
    print_list(C)
main()
