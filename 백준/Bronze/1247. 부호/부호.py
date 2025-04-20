import sys
input = sys.stdin.read

def main():
    data = input().split()
    idx = 0
    for _ in range(3):
        N = int(data[idx])
        idx += 1
        total = 0
        for _ in range(N):
            total += int(data[idx])
            idx += 1
        if total > 0:
            print("+")
        elif total < 0:
            print("-")
        else:
            print("0")

if __name__ == "__main__":
    main()
