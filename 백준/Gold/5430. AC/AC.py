from collections import deque
import json
import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    operations = input().strip()
    m = int(input())
    arr = deque(json.loads(input()))
    isError = False
    isReversed = False

    for op in operations:
        if op == 'R':
            isReversed = not isReversed
        elif op == 'D':
            if arr:
                if isReversed:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                isError = True
                break

    if isError:
        print("error")
    else:
        if isReversed:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")
