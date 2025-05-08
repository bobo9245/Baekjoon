import sys
input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    
    parent = list(range(n + 1))
    parity = [0] * (n + 1)  
    size = [1] * (n + 1)  
    is_bip = [True] * (n + 1)  
    
    non_bip_count = 0
    
    def find(x):
        if parent[x] != x:
            root, par = find(parent[x])
            parity[x] = parity[x] ^ par 
            parent[x] = root
        return parent[x], parity[x]
    
    def union(a, b):
        nonlocal non_bip_count
        
        root_a, par_a = find(a)
        root_b, par_b = find(b)
        
        if root_a == root_b:
            if par_a == par_b:
                if is_bip[root_a]:
                    is_bip[root_a] = False 
                    non_bip_count += size[root_a]
            return
        
        old_non_bip = 0
        if not is_bip[root_a]:
            old_non_bip += size[root_a]
        if not is_bip[root_b]:
            old_non_bip += size[root_b]
        
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
            par_a, par_b = par_b, par_a
        
        new_par = par_a ^ par_b ^ 1  
        
        parent[root_b] = root_a
        parity[root_b] = new_par
        
        size[root_a] += size[root_b]
        
        is_bip[root_a] = is_bip[root_a] and is_bip[root_b]
        
        new_non_bip = 0
        if not is_bip[root_a]:
            new_non_bip = size[root_a]
        
        non_bip_count = non_bip_count - old_non_bip + new_non_bip
    
    for _ in range(q):
        a, b = map(int, input().split())
        union(a, b)
        print(non_bip_count)

main()