import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
results = []
current_index = 1

days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(T):
    digits_in_id = [int(data[current_index + i]) for i in range(10)]
    current_index += 10
    
    allowed_digits = set()
    for i in range(10):
        if digits_in_id[i] == 0:
            allowed_digits.add(i)
            
    count = 0
    
    for m in range(1, 13):
        for d in range(1, days_in_month[m] + 1):
            
            month_digits = set()
            if m >= 10:
                month_digits.add(m // 10)
            month_digits.add(m % 10)
            
            day_digits = set()
            if d >= 10:
                day_digits.add(d // 10)
            day_digits.add(d % 10)
            
            all_digits_in_birthday = month_digits.union(day_digits)
            
            is_valid_birthday = True
            for digit in all_digits_in_birthday:
                if digit not in allowed_digits:
                    is_valid_birthday = False
                    break
            
            if is_valid_birthday:
                count += 1
                
    results.append(str(count))

print('\n'.join(results))