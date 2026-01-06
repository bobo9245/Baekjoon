import sys

def solve():
    data = sys.stdin.read().split()
    if not data: return

    idx = 0
    words = []
    while idx < len(data) and data[idx] != '-':
        w = data[idx]
        mask, freq = 0, [0] * 26
        uniques = []
        for c in w:
            i = ord(c) - 65
            if not freq[i]: uniques.append(i)
            freq[i] += 1
            mask |= (1 << i)
        words.append((mask, freq, uniques))
        idx += 1

    idx += 1
    while idx < len(data) and data[idx] != '#':
        p = data[idx]
        p_mask, p_freq = 0, [0] * 26
        p_uniques = []
        for c in p:
            i = ord(c) - 65
            if not p_freq[i]: p_uniques.append(i)
            p_freq[i] += 1
            p_mask |= (1 << i)
        
        p_uniques.sort()
        scores = [0] * 26
        for w_mask, w_freq, w_indices in words:
            if (w_mask & p_mask) != w_mask: continue
            if all(w_freq[i] <= p_freq[i] for i in w_indices):
                for i in w_indices: scores[i] += 1

        p_scores = [scores[i] for i in p_uniques]
        mn, mx = min(p_scores), max(p_scores)
        
        res_min = "".join(chr(i + 65) for i in p_uniques if scores[i] == mn)
        res_max = "".join(chr(i + 65) for i in p_uniques if scores[i] == mx)
        print(f"{res_min} {mn} {res_max} {mx}")
        idx += 1

solve()