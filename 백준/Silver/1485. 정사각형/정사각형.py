import sys, math
input=sys.stdin.readline

T=int(input())
def caldis(a,b):
    return (a[1]-b[1])**2+(a[0]-b[0])**2
for _ in range(T):
    arr=[]
    for i in range(4):
        arr.append(list(map(int,input().split())))
    # print(arr)
    distances=[]
    isSquare=True
    for i in range(4):
        for j in range(i+1,4):
            distances.append(caldis(arr[i],arr[j]))
    distances=sorted(distances)
    # print(distances)
    isSquare = (
        distances[0] > 0 and 
        distances[0] == distances[1] == distances[2] == distances[3] and
        distances[4] == distances[5] and
        distances[4] == 2 * distances[0]
    )
    print(1 if isSquare else 0)