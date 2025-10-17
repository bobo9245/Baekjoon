n=int(input())
arr=list(map(int,input().split()))

if n==1:
    print(sum(arr)-max(arr))
else:
    min1=min(arr[0],arr[5])
    min2=min(arr[1],arr[4])
    min3=min(arr[2],arr[3])
    
    min1,min2,min3=sorted([min1,min2,min3])
    
    side1=5*(n**2)-16*n+12
    side2=8*n-12
    side3=4

    print(side1*min1 + side2*(min1+min2) + side3*(min1+min2+min3))
    