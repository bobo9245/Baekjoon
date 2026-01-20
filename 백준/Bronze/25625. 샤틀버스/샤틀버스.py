import sys

# x: 편도 소요 시간, y: 제2공학관 도착까지 남은 시간
x, y = map(int, sys.stdin.readline().split())

# 버스가 현재 제2공학관으로 향하는 중 (서울대입구역을 이미 지남)
if y < x:
    print(y + x)
# 버스가 현재 서울대입구역으로 오는 중 (제2공학관에 도착하기 위해 서울대입구역을 거쳐야 함)
else:
    print(y - x)