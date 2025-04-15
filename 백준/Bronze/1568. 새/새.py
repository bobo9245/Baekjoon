k=int(input())

while k>0:
    n=1
    count=0
    while True:
        if n<=k:
            k-=n
            #print(f"n : {n}, k : {k}")
            n+=1
            count+=1
        else:
            n=1
        if k==0:
            break
print(count)