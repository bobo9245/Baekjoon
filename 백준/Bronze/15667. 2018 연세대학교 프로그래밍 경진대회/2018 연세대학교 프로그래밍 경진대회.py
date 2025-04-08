import math

n = int(input())
discriminant = 4 * n - 3
sqrt_d = int(math.isqrt(discriminant))

if sqrt_d * sqrt_d == discriminant:
    k = (-1 + sqrt_d) // 2
    print(k)