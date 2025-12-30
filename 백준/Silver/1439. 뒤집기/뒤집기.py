S = list(input())
temp = S[0]
count = 1

for i in range(1, len(S)):
    if S[i] != temp:
        count += 1 
        temp = S[i] 

print(count // 2)