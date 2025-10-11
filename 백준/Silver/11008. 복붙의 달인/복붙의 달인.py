n=int(input())
for _ in range(n):
    str1,str2=input().split()
    str1=str1.replace(str2,'@')
    print(len(str1))
        