import sys
input=sys.stdin.readline
num = int(input())

n1 = 4
n2 = 2
h = 3
ans = [0]*num
for i in range(int(num)):
    n = int(input())
    if n < 3:
        ans[i] = n
    else:
        temp = n1 + n2 + 1
        while(temp <= n):
            n2 = n1
            n1 = temp
            h += 1
            temp = n1 + n2 + 1
        ans[i] = h
        h = 3
        n1 = 4
        n2 = 2

for i in range(num):
    print(ans[i])