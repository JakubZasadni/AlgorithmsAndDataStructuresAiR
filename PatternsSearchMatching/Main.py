def string_compare_recursive(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    
    cost_substitute = string_compare_recursive(P, T, i-1, j-1) + (P[i] != T[j])
    cost_insert = string_compare_recursive(P, T, i, j-1) + 1
    cost_delete = string_compare_recursive(P, T, i-1, j) + 1
    
    return min(cost_substitute, cost_insert, cost_delete)

P = ' kot'
T = ' pies'

cost = string_compare_recursive(P, T, len(P) - 1, len(T) - 1)
print(cost)

import numpy as np

def string_compare_pd(P, T):
    len_p = len(P)
    len_t = len(T)
    
    D = np.zeros((len_p, len_t), dtype=int)
    for i in range(len_p):
        D[i][0] = i
    for j in range(len_t):
        D[0][j] = j
    
    for i in range(1, len_p):
        for j in range(1, len_t):
            cost_substitute = D[i-1][j-1] + (P[i] != T[j])
            cost_insert = D[i][j-1] + 1
            cost_delete = D[i-1][j] + 1
            D[i][j] = min(cost_substitute, cost_insert, cost_delete)
    
    return D[len_p - 1][len_t - 1]

P = ' biały autobus'
T = ' czarny autokar'

cost = string_compare_pd(P, T)
print(cost)

def string_compare_pd_with_path(P, T):
    len_p = len(P)
    len_t = len(T)
    
    D = np.zeros((len_p, len_t), dtype=int)
    parents = np.full((len_p, len_t), 'X', dtype=str)
    
    for i in range(len_p):
        D[i][0] = i
        parents[i][0] = 'D'
    for j in range(len_t):
        D[0][j] = j
        parents[0][j] = 'I'
    
    for i in range(1, len_p):
        for j in range(1, len_t):
            cost_substitute = D[i-1][j-1] + (P[i] != T[j])
            cost_insert = D[i][j-1] + 1
            cost_delete = D[i-1][j] + 1
            min_cost = min(cost_substitute, cost_insert, cost_delete)
            D[i][j] = min_cost
            
            if min_cost == cost_substitute:
                parents[i][j] = 'S' if P[i] != T[j] else 'M'
            elif min_cost == cost_insert:
                parents[i][j] = 'I'
            else:
                parents[i][j] = 'D'
    
    i, j = len_p - 1, len_t - 1
    path = []
    
    while not (i == 0 and j == 0):
        operation = parents[i][j]
        path.append(operation)
        if operation == 'M' or operation == 'S':
            i -= 1
            j -= 1
        elif operation == 'I':
            j -= 1
        elif operation == 'D':
            i -= 1
    
    path.reverse()
    return ''.join(path)

P = ' thou shalt not'
T = ' you should not'

path = string_compare_pd_with_path(P, T)
print(path)

def string_compare_substring(P, T):
    len_p = len(P)
    len_t = len(T)
    
    D = np.zeros((len_p, len_t), dtype=int)
    for j in range(len_t):
        D[0][j] = 0
    
    for i in range(1, len_p):
        for j in range(1, len_t):
            cost_substitute = D[i-1][j-1] + (P[i] != T[j])
            cost_insert = D[i][j-1] + 1
            cost_delete = D[i-1][j] + 1
            D[i][j] = min(cost_substitute, cost_insert, cost_delete)
    
    min_cost = min(D[len_p-1])
    end_index = np.argmin(D[len_p-1])
    
    return min_cost, end_index

P = ' ban'
T = ' mokeyssbanana'

cost, index = string_compare_substring(P, T)
print(index)

def longest_common_subsequence(P, T):
    len_p = len(P)
    len_t = len(T)
    
    D = np.zeros((len_p, len_t), dtype=int)
    for i in range(len_p):
        D[i][0] = i
    for j in range(len_t):
        D[0][j] = j
    
    for i in range(1, len_p):
        for j in range(1, len_t):
            cost_substitute = D[i-1][j-1] + (P[i] != T[j])
            if P[i] != T[j]:
                cost_substitute += len(P) + len(T)
            cost_insert = D[i][j-1] + 1
            cost_delete = D[i-1][j] + 1
            D[i][j] = min(cost_substitute, cost_insert, cost_delete)
    
    i, j = len_p - 1, len_t - 1
    lcs = []
    
    while i > 0 and j > 0:
        if P[i] == T[j]:
            lcs.append(P[i])
            i -= 1
            j -= 1
        elif D[i-1][j] < D[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    lcs.reverse()
    return ''.join(lcs)

P = ' democrat'
T = ' republican'

lcs = longest_common_subsequence(P, T)
print(lcs)

def longest_monotonic_subsequence(T):
    P = ' ' + ''.join(sorted(T.strip()))
    return longest_common_subsequence(P, T)

T = ' 243517698'
lms = longest_monotonic_subsequence(T)
print(lms)

