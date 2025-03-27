expr = input().split('-')
result = sum(map(int, expr[0].split('+')))
for part in expr[1:]:
    result -= sum(map(int, part.split('+')))
print(result)
