from collections import deque

def solve():
    N, K = input().split()
    K = int(K)
    M = len(N)
    
    queue = deque([(N, 0)])
    visited = set([(N, 0)])
    
    ans = -1
    
    while queue:
        curr, count = queue.popleft()
        
        if count == K:
            ans = max(ans, int(curr))
            continue
        
        curr_list = list(curr)
        
        for i in range(M - 1):
            for j in range(i + 1, M):
                if i == 0 and curr_list[j] == '0':
                    continue
                
                curr_list[i], curr_list[j] = curr_list[j], curr_list[i]
                nxt = "".join(curr_list)
                
                if (nxt, count + 1) not in visited:
                    visited.add((nxt, count + 1))
                    queue.append((nxt, count + 1))
                
                curr_list[i], curr_list[j] = curr_list[j], curr_list[i]

    print(ans)

solve()