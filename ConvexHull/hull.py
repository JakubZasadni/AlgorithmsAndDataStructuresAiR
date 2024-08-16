from typing import List, Tuple

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0 
    elif val > 0:
        return 1 
    else:
        return 2 


def jarvis_convex_hull_v1(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    n = len(points)
    if n < 3:
        return [] 


    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
        elif points[i][0] == points[l][0] and points[i][1] < points[l][1]:
            l = i

    hull = []
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break

    return hull


def jarvis_convex_hull_v2(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    n = len(points)
    if n < 3:
        return [] 


    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
        elif points[i][0] == points[l][0] and points[i][1] < points[l][1]:
            l = i

    hull = []
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            o = orientation(points[p], points[i], points[q])
            if o == 2 or (o == 0 and ((points[i][0] - points[p][0]) ** 2 + (points[i][1] - points[p][1]) ** 2 > 
                                      (points[q][0] - points[p][0]) ** 2 + (points[q][1] - points[p][1]) ** 2)):
                q = i
        p = q
        if p == l:
            break

    return hull


points3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]


hull3_v1 = jarvis_convex_hull_v1(points3)
hull3_v2 = jarvis_convex_hull_v2(points3)


print(hull3_v1)
print(hull3_v2)
