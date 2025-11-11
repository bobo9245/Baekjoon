# 연두의 영어 이름
name = input().upper()
# 팀 이름 후보 수
n = int(input())
# 팀 이름을 저장할 배열
team_list = []

for _ in range(n):
	team_name = input().upper()
	team_list.append(team_name)
team_list.sort() # 사전 순 정렬
# 확률값을 저장할 배열
result = []
for i in range(n):
	# L O V E의 각각의 개수를 찾자.
	L = name.count("L") + team_list[i].count("L")
	O = name.count("O") + team_list[i].count("O")
	V = name.count("V") + team_list[i].count("V")
	E = name.count("E") + team_list[i].count("E")
	# 공식
	p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
	result.append(p)

# 우승 확률이 가장 높은 팀 이름 출력
print(team_list[result.index(max(result))].upper())