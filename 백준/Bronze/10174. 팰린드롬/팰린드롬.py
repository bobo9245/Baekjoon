n=int(input())
for _ in range(n):
    s=list(input().lower().strip())
    isPal=True
    for i in range(len(s)//2):
        if s[i]!=s[-(i+1)]:
            isPal=False
    print('Yes' if isPal else 'No')