import sys
import math
input = sys.stdin.readline

D, H, W = map(int, input().split())

hwratio = H**2 + W**2
x = D / math.sqrt(hwratio)

height = H * x
width = W * x

print(int(height),int(width))