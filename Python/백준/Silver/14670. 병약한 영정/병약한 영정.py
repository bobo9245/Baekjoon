class HashTable:
    def __init__(self, size=101, prime=23):
        self.size = size
        self.prime = prime
        self.table = [[] for _ in range(size)]

    def get_key(self, key):
        return (key * self.prime) % self.size

    def add(self, data, value):
        key = self.get_key(data)
        self.table[key].append((data, value))

    def contain(self, data):
        key = self.get_key(data)
        for d, v in self.table[key]:
            if d == data:
                return v
        return -1

n = int(input())
hash_table = HashTable()

# 약 정보 입력을 해시 테이블에 저장
for _ in range(n):
    h, y = map(int, input().split())
    hash_table.add(h, y)

m = int(input())
results = []

# 증상 처리
for _ in range(m):
    data = list(map(int, input().split()))
    x = data[0]  # 증상 개수
    symptoms = data[1:]
    ans = []
    flag = False

    for symptom in symptoms:
        effect = hash_table.contain(symptom)
        if effect == -1:
            flag = True
        else:
            ans.append(effect)

    if flag:
        results.append("YOU DIED")
    else:
        results.append(" ".join(map(str, ans)))

# 결과 출력
print("\n".join(results))