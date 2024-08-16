import time

def naive_search(S, W):
    n = len(S)
    m = len(W)
    occurrences = 0
    comparisons = 0
    i = 0

    while i <= n - m:
        match = True
        for j in range(m):
            comparisons += 1
            if S[i + j] != W[j]:
                match = False
                break
        if match:
            occurrences += 1
        i += 1

    return occurrences, comparisons


with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()

S = ' '.join(text).lower()
W = "time."


t_start = time.perf_counter()
occurrences, comparisons = naive_search(S, W)
t_stop = time.perf_counter()

print(occurrences)
print(comparisons)
print( "{:.7f}".format(t_stop - t_start))

def hash(word, d, q, N):
    hw = 0
    for i in range(N):
        hw = (hw * d + ord(word[i])) % q
    return hw

def rabin_karp(S, W, d=256, q=101):
    n = len(S)
    m = len(W)
    hW = hash(W, d, q, m)
    occurrences = 0
    comparisons = 0
    collisions = 0
    

    h = 1
    for i in range(m - 1):
        h = (h * d) % q

    hS = hash(S[:m], d, q, m)
    for i in range(n - m + 1):
        comparisons += 1
        if hS == hW:
            if S[i:i + m] == W:
                occurrences += 1
            else:
                collisions += 1
        
        if i < n - m:
            hS = (d * (hS - ord(S[i]) * h) + ord(S[i + m])) % q
            if hS < 0:
                hS += q

    return occurrences, comparisons, collisions


t_start = time.perf_counter()
occurrences, comparisons, collisions = rabin_karp(S, W)
t_stop = time.perf_counter()

print('\n')
print(occurrences)
print(comparisons)
print(collisions)
print( "{:.7f}".format(t_stop - t_start))

