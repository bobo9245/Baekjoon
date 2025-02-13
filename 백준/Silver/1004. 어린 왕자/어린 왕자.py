import sys

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input().strip())
        count = 0
        for _ in range(n):
            cx, cy, r = map(int, input().split())
            r2 = r * r
            inside_start = (x1 - cx)**2 + (y1 - cy)**2 < r2
            inside_end = (x2 - cx)**2 + (y2 - cy)**2 < r2
            if inside_start != inside_end:
                count += 1
        print(count)

if __name__ == '__main__':
    main()
