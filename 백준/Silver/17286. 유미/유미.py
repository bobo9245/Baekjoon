import math
from itertools import permutations

yumi = list(map(int, input().split()))
people = [list(map(int, input().split())) for _ in range(3)]

min_dist = float('inf')

for p in permutations(people):
    dist = math.sqrt((yumi[0] - p[0][0])**2 + (yumi[1] - p[0][1])**2)
    dist += math.sqrt((p[0][0] - p[1][0])**2 + (p[0][1] - p[1][1])**2)
    dist += math.sqrt((p[1][0] - p[2][0])**2 + (p[1][1] - p[2][1])**2)
    
    if dist < min_dist:
        min_dist = dist

print(int(min_dist))