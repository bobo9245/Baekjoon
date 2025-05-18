import sys

def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

# Store all courses with their group ID
# Format: (credit, day, start_min, end_min, group_id)
all_courses = []

N = int(sys.stdin.readline())

for group_id in range(N):
    Ai = int(sys.stdin.readline())
    for course_idx_in_group in range(Ai):
        C, D, S, E = sys.stdin.readline().split()
        all_courses.append((int(C), int(D), time_to_minutes(S), time_to_minutes(E), group_id))

total_courses_count = len(all_courses) # This is sum(Ai)

count = 0

# Iterate through all possible subsets of courses using a bitmask
# A bitmask of length total_courses_count represents the subset
for i in range(1 << total_courses_count):
    current_credits = 0
    selected_courses_info = [] # List of (credit, day, start_min, end_min, group_id) for selected courses
    
    # Check group constraint while iterating through the subset
    is_valid_subset = True
    selected_groups = set() # To track which groups have a selected course
    
    for j in range(total_courses_count):
        if (i >> j) & 1: # If the j-th bit is set, course j is selected
            course_info = all_courses[j]
            group_id = course_info[4]
            
            if group_id in selected_groups:
                is_valid_subset = False
                break # More than one course from this group
            selected_groups.add(group_id)
            
            selected_courses_info.append(course_info)
            current_credits += course_info[0] # Add credit

    if not is_valid_subset:
        continue

    # Check total credits
    if current_credits != 22:
        continue

    # Check for overlaps among selected courses
    has_overlap = False
    selected_intervals_by_day = {d: [] for d in range(1, 8)}
    
    for course_info in selected_courses_info:
        credit, day, start_min, end_min, group_id = course_info
        selected_intervals_by_day[day].append((start_min, end_min))
    
    for day in range(1, 8):
        intervals_on_day = selected_intervals_by_day[day]
        if not intervals_on_day:
            continue
            
        # Sort intervals by start time to easily check for overlaps
        intervals_on_day.sort()
        
        # Check for overlap between adjacent intervals after sorting
        for k in range(len(intervals_on_day) - 1):
            if intervals_on_day[k][1] > intervals_on_day[k+1][0]: # Overlap condition: end time of previous > start time of next
                has_overlap = True
                break
        if has_overlap:
            break # Overlap found on some day

    # If the subset is valid (satisfies group constraint, credit target, and no overlap)
    if not has_overlap:
        count += 1

print(count)