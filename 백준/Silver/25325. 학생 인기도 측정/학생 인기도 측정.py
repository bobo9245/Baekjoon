n = int(input())
student = input().split()
result = {string : 0 for string in student}	# 딕셔너리 변환
 
for _ in range(n) :
    a = list(input().split())
    for i in a :
        result[i] += 1

sort_dict = sorted(result.items(), key=lambda x: x[1], reverse=True)
 
for key, value in sort_dict :	# 출력
    print(key, value)