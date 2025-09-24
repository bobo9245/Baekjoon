import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

if not s1 or not s2:
    print(0)
    sys.exit()

arr = [[0] * len(s2) for _ in range(len(s1))]
sarr = [[""] * len(s2) for _ in range(len(s1))]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            if i > 0 and j > 0:
                arr[i][j] = arr[i - 1][j - 1] + 1
                sarr[i][j] = sarr[i - 1][j - 1] + s1[i]
            else:
                arr[i][j] = 1
                sarr[i][j] = s1[i]
        else:
            top_len = arr[i - 1][j] if i > 0 else 0
            left_len = arr[i][j - 1] if j > 0 else 0

            if top_len > left_len:
                arr[i][j] = top_len
                sarr[i][j] = sarr[i - 1][j] if i > 0 else ""
            else:
                arr[i][j] = left_len
                sarr[i][j] = sarr[i][j - 1] if j > 0 else ""

final_length = arr[len(s1) - 1][len(s2) - 1]
final_string = sarr[len(s1) - 1][len(s2) - 1]

print(final_length)
if final_length > 0:
    print(final_string)
