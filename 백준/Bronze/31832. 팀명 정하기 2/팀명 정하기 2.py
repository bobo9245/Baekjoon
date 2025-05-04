def isGoodName(name):
    isGood=True
    if len(name)>10:
        isGood=False
    if name.isdigit():
        isGood=False
    uppercasecount=sum(1 for n in name if n.isupper())
    lowercasecount=sum(1 for n in name if n.islower())
    if uppercasecount>lowercasecount:
        isGood=False
    if isGood==True:
        print(name) 
    return 

n=int(input())
for _ in range(n):
    isGoodName(input())