import sys

N, X, K = map(int, sys.stdin.readline().split())

cup_list = [0] * (N + 1)
cup_list[X] = 1

for _ in range(K):
    A, B = map(int, sys.stdin.readline().split())

    cup_list[A], cup_list[B] = cup_list[B], cup_list[A]

print(cup_list.index(1))