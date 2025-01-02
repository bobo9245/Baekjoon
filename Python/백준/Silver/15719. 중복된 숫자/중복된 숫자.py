import sys

def get_range_sum(final_number):
    return final_number * (final_number - 1) // 2
    

def duplicate_number(N, numbers): 
    sum_numbers = 0
    temp = ""
    for num in numbers:
        if num.isdigit():
            temp += num
        elif num == " ":
            sum_numbers += int(temp)
            temp = ""
            
    sum_numbers += int(temp)
    
    return sum_numbers - get_range_sum(N)

if __name__ == "__main__":
    N = int(input())
    numbers = sys.stdin.read()
    print(duplicate_number(N, numbers))