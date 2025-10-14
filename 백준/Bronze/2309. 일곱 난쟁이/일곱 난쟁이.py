arr = []
for _ in range(9):
    arr.append(int(input()))

arr = sorted(arr)
s = sum(arr)
found = False

for i in range(9):
    for j in range(i + 1, 9):
        if arr[i] + arr[j] == s - 100:
            arr.pop(j)
            arr.pop(i)
            found = True
            break
    
    if found:
        break

for a in arr:
    print(a)