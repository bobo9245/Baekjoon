import sys
cows = sys.stdin.readline().strip()
answer = [] # 경로가 만나는 소들의 쌍 리스트
dic = {chr(i): [-1, -1] for i in range(65, 91)} # 각 소들이 나타나는 인덱스를 기록
for i, c in enumerate(cows): 
    if dic[c][0] == -1: # 소가 처음 나타난 경우
        dic[c][0] = i
    else: # 소가 두 번째 나타난 경우
        dic[c][1] = i

for i in range(52):
    for j in range(i+1, 52): # i번째 소와 j번째 소의 인덱스가 서로 엇갈리는지 확인
        if dic[cows[i]][0] < dic[cows[j]][0] < dic[cows[i]][1] < dic[cows[j]][1] or dic[cows[i]][0] > dic[cows[j]][0] > dic[cows[i]][1] > dic[cows[j]][1]:
            if cows[i] != cows[j] and set([cows[i], cows[j]]) not in answer:
                answer.append(set([cows[i], cows[j]])) # 경로가 만나고, 이미 찾은 답이 아니라면 추가
print(len(answer))