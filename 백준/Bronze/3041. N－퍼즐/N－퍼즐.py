ans=['ABCD','EFGH','IJKL','MNO.']
arr=[]
dic={}

for _ in range(4):
    arr.append(input())
for i in range(4):
    for j in range(4):
        if ans[i][j]!=arr[i][j] and arr[i][j]!='.':
            dic[arr[i][j]]=(i,j)
dis=0
for i in range(4):
    for j in range(4):
        if ans[i][j] in dic.keys():
            dis+=abs(dic[ans[i][j]][0]-i)+abs(dic[ans[i][j]][1]-j)
print(dis)