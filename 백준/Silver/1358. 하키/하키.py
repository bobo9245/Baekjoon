import math
W, H, X, Y, P = map(int, input().split())

arr = [W, H, X, Y]

def isInLink(x, y, arr):
    W, H, X, Y = arr[0], arr[1], arr[2], arr[3]
    R = H / 2

    if X <= x and x <= X + W and Y <= y and y <= Y + H:
        return True

    X_L = X
    Y_L = Y + R
    distance_sq_left = (x - X_L)**2 + (y - Y_L)**2
    if distance_sq_left <= R**2:
        return True

    X_R = X + W
    Y_R = Y + R
    distance_sq_right = (x - X_R)**2 + (y - Y_R)**2
    if distance_sq_right <= R**2:
        return True

    return False

count = 0
for _ in range(P):
    x, y = map(int, input().split())
    if isInLink(x, y, arr):
        count += 1
        
print(count)