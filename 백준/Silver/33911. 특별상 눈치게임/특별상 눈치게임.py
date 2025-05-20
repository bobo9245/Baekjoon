def solve():
    N = int(input())
    other_freq = [0] * 101

    for _ in range(N):
        a, b, c = map(int, input().split())
        other_freq[a] += 1
        other_freq[b] += 1
        other_freq[c] += 1

    win_count = 0

    for m1_val in range(1, 98 + 1):
        for m2_val in range(m1_val + 1, 99 + 1):
            for m3_val in range(m2_val + 1, 100 + 1):
                
                my_picked_nums_set = {m1_val, m2_val, m3_val}
                
                other_freq[m1_val] += 1
                other_freq[m2_val] += 1
                other_freq[m3_val] += 1
                
                max_remaining_num = -1
                
                for num_to_check in range(100, 0, -1):
                    if other_freq[num_to_check] == 1:
                        max_remaining_num = num_to_check
                        break
                
                if max_remaining_num != -1:
                    if max_remaining_num in my_picked_nums_set:
                        win_count += 1
                
                other_freq[m1_val] -= 1
                other_freq[m2_val] -= 1
                other_freq[m3_val] -= 1
                        
    print(win_count)

solve()