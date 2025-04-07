def is_palindrome(s):
    return s == s[::-1]

def count_palindromes(n):
    n = int(n)
    count = 0
    i = 1

    while True:
        # 짝수 길이 회문
        s = str(i)
        p_even = int(s + s[::-1])
        if p_even > n:
            break
        count += 1

        # 홀수 길이 회문
        for mid in '0123456789':
            p_odd = int(s + mid + s[::-1])
            if p_odd > n:
                continue
            count += 1

        i += 1

    # 한 자리 수 (1~9)
    count += min(n, 9)

    return count

n = int(input())
print(count_palindromes(n))
