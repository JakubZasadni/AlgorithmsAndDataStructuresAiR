import numpy as np
import copy

def create_adjacency_matrix(edges, num_vertices):
    matrix = np.zeros((num_vertices, num_vertices))
    for edge in edges:
        i, j, _ = edge
        matrix[i][j] = 1
        matrix[j][i] = 1
    return matrix

graph_G = [('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
graph_P = [('A','B',1), ('B','C',1), ('A','C',1)]

vertex_map_G = {v: idx for idx, v in enumerate(sorted(set(v for edge in graph_G for v in edge[:2])))}
vertex_map_P = {v: idx for idx, v in enumerate(sorted(set(v for edge in graph_P for v in edge[:2])))}

G = create_adjacency_matrix([(vertex_map_G[i], vertex_map_G[j], w) for i, j, w in graph_G], len(vertex_map_G))
P = create_adjacency_matrix([(vertex_map_P[i], vertex_map_P[j], w) for i, j, w in graph_P], len(vertex_map_P))

def ullmann(used_columns, current_row, M, G, P, num_recursive_calls):
    num_recursive_calls[0] += 1
    if current_row == M.shape[0]:
        if np.array_equal(P, M @ G @ M.T):
            return [copy.deepcopy(M)], num_recursive_calls
        return [], num_recursive_calls
    
    valid_isomorphisms = []
    for col in range(M.shape[1]):
        if not used_columns[col]:
            M[current_row] = 0
            M[current_row][col] = 1
            used_columns[col] = True
            isomorphisms, num_recursive_calls = ullmann(used_columns, current_row + 1, M, G, P, num_recursive_calls)
            valid_isomorphisms.extend(isomorphisms)
            used_columns[col] = False
    
    return valid_isomorphisms, num_recursive_calls

M = np.zeros((P.shape[0], G.shape[0]))

isomorphisms, num_recursive_calls = ullmann([False] * G.shape[0], 0, M, G, P, [0])
print(len(isomorphisms))
print(num_recursive_calls[0])

def create_initial_M0(G, P):
    M0 = np.zeros((P.shape[0], G.shape[0]))
    deg_G = np.sum(G, axis=1)
    deg_P = np.sum(P, axis=1)
    for i in range(P.shape[0]):
        for j in range(G.shape[0]):
            if deg_P[i] <= deg_G[j]:
                M0[i][j] = 1
    return M0

M0 = create_initial_M0(G, P)

def ullmann_v2(used_columns, current_row, M, M0, G, P, num_recursive_calls):
    num_recursive_calls[0] += 1
    if current_row == M.shape[0]:
        if np.array_equal(P, M @ G @ M.T):
            return [copy.deepcopy(M)], num_recursive_calls
        return [], num_recursive_calls
    
    valid_isomorphisms = []
    for col in range(M.shape[1]):
        if not used_columns[col] and M0[current_row][col] == 1:
            M[current_row] = 0
            M[current_row][col] = 1
            used_columns[col] = True
            isomorphisms, num_recursive_calls = ullmann_v2(used_columns, current_row + 1, M, M0, G, P, num_recursive_calls)
            valid_isomorphisms.extend(isomorphisms)
            used_columns[col] = False
    
    return valid_isomorphisms, num_recursive_calls

M = M0.copy()

isomorphisms_v2, num_recursive_calls_v2 = ullmann_v2([False] * G.shape[0], 0, M, M0, G, P, [0])
print(len(isomorphisms_v2))
print(num_recursive_calls_v2[0])

def prune(P, G, M):
    change = True
    while change:
        change = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i][j] == 1:
                    neighbors_P = np.where(P[i] == 1)[0]
                    neighbors_G = np.where(G[j] == 1)[0]
                    for neighbor_P in neighbors_P:
                        found = False
                        for neighbor_G in neighbors_G:
                            if M[neighbor_P][neighbor_G] == 1:
                                found = True
                                break
                        if not found:
                            M[i][j] = 0
                            change = True
                            break
    return M





def ullmann_v3(P, G, current_row=0, M=None, using=None, result=0, iterations=0):
    iterations += 1
    if M is None:
        M = np.zeros((P.shape[0], G.shape[0]))
    if using is None:
        using = [False] * M.shape[1]
    
    if current_row == M.shape[0]:
        if np.array_equal(P, M @ G @ M.T):
            result += 1
        return result, iterations
    
    M_copy = copy.deepcopy(M)
    prune(P, G, M_copy)
    for i in range(M.shape[1]):
        if not using[i] and M[current_row][i] != 0:
            using[i] = True
            M_copy[current_row] = 0
            M_copy[current_row][i] = 1
            result, iterations = ullmann_v3(P, G, current_row + 1, M_copy, using, result, iterations)
            using[i] = False
    return result, iterations

graph_G = [('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
graph_P = [('A','B',1), ('B','C',1), ('A','C',1)]

vertex_map_G = {v: idx for idx, v in enumerate(sorted(set(v for edge in graph_G for v in edge[:2])))}
vertex_map_P = {v: idx for idx, v in enumerate(sorted(set(v for edge in graph_P for v in edge[:2])))}

G = create_adjacency_matrix([(vertex_map_G[i], vertex_map_G[j], w) for i, j, w in graph_G], len(vertex_map_G))
P = create_adjacency_matrix([(vertex_map_P[i], vertex_map_P[j], w) for i, j, w in graph_P], len(vertex_map_P))

M0 = np.zeros((P.shape[0], G.shape[0]))
deg_G = np.sum(G, axis=1)
deg_P = np.sum(P, axis=1)
for i in range(M0.shape[0]):
    for j in range(M0.shape[1]):
        if deg_P[i] <= deg_G[j]:
            M0[i][j] = 1

result, iterations = ullmann_v3(P, G, M=M0)
print(result)
print(iterations)