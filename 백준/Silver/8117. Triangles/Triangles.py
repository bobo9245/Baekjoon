import sys

numbers = []
while True:
    try:
        num = int(sys.stdin.readline())
        if num == 0:
            break
        numbers.append(num)
    except ValueError:
        break

numbers.sort()

found = False
for k in range(len(numbers) - 1, 1, -1):
    c = numbers[k]
    b = numbers[k - 1]
    a = numbers[k - 2]
    
    if a + b > c:
        print(f"{a} {b} {c}")
        found = True
        break

if not found:
    print("NIE")
