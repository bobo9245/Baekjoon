x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# CCW 계산: (x2 - x1)(y3 - y1) - (y2 - y1)(x3 - x1)
# P1에서 P2로 가는 벡터에 대해 P3가 왼쪽(+), 오른쪽(-), 일직선(0)인지 판단
ccw = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

if ccw > 0:
    print(1)    # 반시계 방향 (왼쪽)
elif ccw < 0:
    print(-1)   # 시계 방향 (오른쪽)
else:
    print(0)    # 일직선 위