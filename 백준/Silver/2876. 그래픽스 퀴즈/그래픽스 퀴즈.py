import sys

data = sys.stdin.read().split()

if not data:
    sys.exit()

N = int(data[0])
desk_data = []

for i in range(N):
    A = int(data[1 + 2*i])
    B = int(data[1 + 2*i + 1])
    desk_data.append((A, B))
        
max_students = 0
best_grade = 0

for G in range(1, 6):
    current_streak = 0
    current_max_students = 0
    
    for A, B in desk_data:
        if A == G or B == G:
            current_streak += 1
        else:
            current_max_students = max(current_max_students, current_streak)
            current_streak = 0
    
    current_max_students = max(current_max_students, current_streak)

    if current_max_students > max_students:
        max_students = current_max_students
        best_grade = G

print(f"{max_students} {best_grade}")