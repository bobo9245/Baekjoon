def count_total_operations(N, M):
    count = N 

    while N >= M:
        N = N // M 
        count += N 

    return count
n,m=map(int,input().split())
print(count_total_operations(n,m))