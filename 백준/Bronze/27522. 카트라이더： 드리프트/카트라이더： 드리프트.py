import sys
input=sys.stdin.readline

arr=[]
for _ in range(8):
    time,team=input().split()
    time=list(map(int,time.split(':')))
    time=time[0]*100000+time[1]*1000+time[2]
    arr.append([time,team])
arr=sorted(arr)
B=0
R=0
for i in range(8):
    score=[10,8,6,5,4,3,2,1,0]
    if arr[i][1]=='B':
        B+=score[i]
    else:
        R+=score[i]
    # print(arr[i],B,R)
print('Red' if R>B else 'Blue')    