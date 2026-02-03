import math

x, y, d, t = map(int, input().split())
L = math.sqrt(x**2 + y**2)

case1 = L

if L >= d:
    n = L // d
    case2 = min(n * t + (L - n * d), (n + 1) * t + ((n + 1) * d - L))
    case3 = (L // d + 1) * t
else:
    case2 = min(t + (d - L), L)
    case3 = 2.0 * t

print(f"{min(case1, case2, case3):.10f}")