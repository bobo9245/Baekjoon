from collections import deque
N,M=map(int,input().split())
deck=deque([i for i in range(1,N+1)])
arr=list(map(int,input().split()))

count = 0
for num in arr:
    while 1:
        if deck[0] == num:
            deck.popleft()
            break
        else:
            if deck.index(num) <= len(deck)//2:
                deck.rotate(-1)
                count += 1
            else:
                deck.rotate(1)
                count += 1

print(count)