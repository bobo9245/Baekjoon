s,n,k,r1,r2,c1,c2 = map(int, input().split())
size = n ** s

def recur(t,x,y):
    if t == 1:
        return 0
    tmp = t // n
    if (tmp * (n-k)//2 <= x < tmp * (n+k)//2) and (tmp * (n-k)//2 <= y < tmp * (n+k)//2):
        return 1
    return recur(tmp,x%tmp,y%tmp)

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(recur(size, i,j), end='')
    print()