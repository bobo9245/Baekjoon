import math
import sys
input = sys.stdin.readline

R = int(input())

euclidean_area = math.pi * R**2

taxi_area = 2 * R**2

print(f"{euclidean_area:.6f}")
print(f"{taxi_area:.6f}")