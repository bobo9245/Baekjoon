n,l = map(int,input().split())
isTrue=False
for i in range(l,101):
    numerator = n-(i*(i-1)//2)

    if numerator<0:
        break
    if numerator%i==0:
        x=numerator//i
        result = [x+i for i in range(i)]
        print(" ".join(map(str,result)))
        isTrue=True
        break
if not isTrue:
    print(-1)