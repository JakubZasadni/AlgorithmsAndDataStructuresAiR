class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union_sets(self, s1, s2):
        root1 = self.find(s1)
        root2 = self.find(s2)

        if root1 != root2:
            if self.size[root1] < self.size[root2]:
                root1, root2 = root2, root1
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]

    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)


if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union_sets(0, 1)
    uf.union_sets(3, 4)
    print(uf.same_component(0, 1))  
    print(uf.same_component(1, 2))  
    print(uf.same_component(3, 4))  
    uf.union_sets(2, 0)
    print(uf.same_component(2, 1))  

class Vertex:
    def __init__(self, key, brightness=None):
        self.id = key
        self.brightness = brightness
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    def getBrightness(self):
        return self.brightness
    
    def setBrightness(self, brightness):
        self.brightness = brightness

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self, key, brightness=None):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key, brightness)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    
    def addEdge(self, fromVert, toVert, cost=0):
        if fromVert not in self.vertList:
            self.addVertex(fromVert)
        if toVert not in self.vertList:
            self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], cost)
        self.vertList[toVert].addNeighbor(self.vertList[fromVert], cost)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def getEdges(self):
        edges = []
        for v in self.vertList.values():
            for nbr in v.getConnections():
                edges.append((v.getId(), nbr.getId(), v.getWeight(nbr)))
        return edges
    
    def __iter__(self):
        return iter(self.vertList.values())

import sys

def kruskalMST(graph):
    edges = graph.getEdges()
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(len(graph.getVertices()))
    mst = Graph()
    
    for edge in edges:
        fromVert, toVert, weight = edge
        fromIdx = ord(fromVert) - ord('A')
        toIdx = ord(toVert) - ord('A')
        
        if not uf.same_component(fromIdx, toIdx):
            uf.union_sets(fromIdx, toIdx)
            mst.addEdge(fromVert, toVert, weight)
    
    return mst

def printGraph(g):
    print("------GRAPH------")
    for v in g.getVertices():
        print(v, end=" -> ")
        for n in g.getVertex(v).getConnections():
            print(f"{n.getId()} {g.getVertex(v).getWeight(n)}", end="; ")
        print()
    print("-------------------")

def loadGraphFromList(graph_list):
    graph = Graph()
    for edge in graph_list:
        fromVert, toVert, weight = edge
        graph.addEdge(fromVert, toVert, weight)
    return graph

if __name__ == "__main__":
    graf = [
        ('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
        ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
        ('C', 'G', 9), ('C', 'D', 3),
        ('D', 'G', 10), ('D', 'J', 18),
        ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
        ('F', 'H', 2), ('F', 'G', 8),
        ('G', 'H', 9), ('G', 'J', 8),
        ('H', 'I', 3), ('H', 'J', 9),
        ('I', 'J', 9)
    ]

    graph = loadGraphFromList(graf)
    mst_kruskal = kruskalMST(graph)
    printGraph(mst_kruskal)
