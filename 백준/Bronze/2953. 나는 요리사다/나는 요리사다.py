king=0
m=0
for _ in range(5):
    score=sum(list(map(int,input().split())))
    if score>m:
        m=score
        king=_

print(king+1, m)
    