import sys

def to_int(char):
    if '0' <= char <= '9':
        return int(char)
    else:
        return ord(char) - ord('A') + 10

def to_char(num):
    if 0 <= num <= 9:
        return str(num)
    else:
        return chr(num - 10 + ord('A'))

n = int(sys.stdin.readline())
numbers = [sys.stdin.readline().strip() for _ in range(n)]
k = int(sys.stdin.readline())

gains = {to_char(i): 0 for i in range(36)}
initial_sum = 0

for num_str in numbers:
    place_value = 1
    for char in reversed(num_str):
        val = to_int(char)
        initial_sum += val * place_value
        gains[char] += (35 - val) * place_value
        place_value *= 36

sorted_gains = sorted(gains.values(), reverse=True)

final_sum = initial_sum
for i in range(k):
    final_sum += sorted_gains[i]

if final_sum == 0:
    print("0")
else:
    result = ""
    temp_sum = final_sum
    while temp_sum > 0:
        remainder = temp_sum % 36
        result += to_char(remainder)
        temp_sum //= 36
    print(result[::-1])