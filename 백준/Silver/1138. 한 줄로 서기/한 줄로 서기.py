import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
people = [0]*n
for i in range(1,n+1):
    count=0
    h = arr[i-1]
    for j in range(n):
        if h==0:
            if people[j]==0:
                people[j]=i
                break
        elif people[j]!=0:
            pass
        elif count==h:
            people[j]=i
            break        
        else:
            count+=1
print(' '.join(map(str,people)))