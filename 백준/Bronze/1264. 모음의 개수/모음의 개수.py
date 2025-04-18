moeum=['a','e','i','o','u','A','E','I','O','U']
while True:
    arr=list(input())
    if arr==['#']:
        break
    count=0
    for a in arr:
        if a in moeum:
            count+=1
    print(count)
        