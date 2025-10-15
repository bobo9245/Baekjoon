n,a,b=map(int,input().split())

if a<b:
    print("Bus")
else:
    print("Anything" if a==b else "Subway")