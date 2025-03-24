import sys
input = sys.stdin.readline

n = int(input())
w,b=0,0
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

def jg(x1,y1,x2,y2):
    global w,b
    isSame=True
    for x in range(x1,x2):
        for y in range(y1,y2):
            if arr[x][y]!=arr[x1][y1]:
                isSame=False 
    if isSame:
        if arr[x1][y1]==1:
            b+=1
        else:
            w+=1
    else:
        xmid,ymid=int((x1+x2)/2),int((y1+y2)/2)
        jg(x1,y1,xmid,ymid)
        jg(xmid,y1,x2,ymid)
        jg(x1,ymid,xmid,y2)
        jg(xmid,ymid,x2,y2)
jg(0,0,n,n)
print(w)
print(b)