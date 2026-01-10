import sys



input_data = sys.stdin.read().split()

if input_data:

    T = int(input_data[0])

    for i in range(1, T + 1):

        S = input_data[i]

        n = len(S)

        L = (n + 2) // 3

        

        S_p = S[:L]

        rev = S_p[::-1]

        t_rev = rev[1:]

        t_s = S_p[1:]

        

        c1 = S_p + rev + S_p

        c2 = S_p + t_rev + S_p

        c3 = S_p + rev + t_s

        c4 = S_p + t_rev + t_s

        

        if S == c1 or S == c2 or S == c3 or S == c4:

            print(1)

        else:

            print(0)