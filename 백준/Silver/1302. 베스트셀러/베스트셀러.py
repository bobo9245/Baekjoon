import sys
input=sys.stdin.readline
n=int(input())
dic={}
for _ in range(n):
    str=input().strip()
    if str in dic:
        dic[str]+=1
    else:
        dic[str]=1

book_list=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
print(book_list[0][0])