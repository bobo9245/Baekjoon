import sys

s = sys.stdin.readline().strip()

mp = {
    'F': 'Foundation',
    'C': 'Claves',
    'V': 'Veritas',
    'E': 'Exploration'
}

print(mp[s[0]])
