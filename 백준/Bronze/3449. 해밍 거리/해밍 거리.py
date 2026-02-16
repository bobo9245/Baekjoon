t = int(input())
for i in range(t):
    cnt = 0
    a = input()
    b = input()
    for j in range(len(a)):
        if a[j] != b[j]:
            cnt += 1
    print('Hamming distance is {}.'.format(cnt))