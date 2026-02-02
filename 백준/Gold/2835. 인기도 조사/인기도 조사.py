import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    def to_sec(hms):
        h, m, s = map(int, hms.split(':'))
        return h * 3600 + m * 60 + s

    SIZE = 86400
    diff = [0] * (SIZE + 1)
    
    N = int(data[idx])
    idx += 1
    total_pop = 0
    
    for _ in range(N):
        start = to_sec(data[idx])
        end = to_sec(data[idx + 2])
        idx += 3
        
        if end < start:
            diff[0] += 1
            diff[end + 1] -= 1
            diff[start] += 1
            diff[SIZE] -= 1
            total_pop += (SIZE - start + end + 1)
        else:
            diff[start] += 1
            diff[end + 1] -= 1
            total_pop += (end - start + 1)

    pop_arr = [0] * SIZE
    curr = 0
    for i in range(SIZE):
        curr += diff[i]
        pop_arr[i] = curr
        
    prefix = [0] * (SIZE + 1)
    for i in range(SIZE):
        prefix[i + 1] = prefix[i] + pop_arr[i]

    Q = int(data[idx])
    idx += 1
    output = []
    
    for _ in range(Q):
        start = to_sec(data[idx])
        end = to_sec(data[idx + 2])
        idx += 3
        
        if end < start:
            s_sum = prefix[SIZE] - (prefix[start] - prefix[end + 1])
            length = SIZE - start + end + 1
        else:
            s_sum = prefix[end + 1] - prefix[start]
            length = end - start + 1
            
        output.append(f"{s_sum / length:.10f}")
    
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()