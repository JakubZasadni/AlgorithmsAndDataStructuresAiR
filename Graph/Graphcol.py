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
    
    def __iter__(self):
        return iter(self.vertList.values())

import sys

def primMST(graph):
    intree = {v: False for v in graph.getVertices()}
    distance = {v: sys.maxsize for v in graph.getVertices()}
    parent = {v: None for v in graph.getVertices()}
    
    startVertex = next(iter(graph.getVertices()))
    distance[startVertex] = 0
    
    while not all(intree.values()):
        u = min((v for v in graph.getVertices() if not intree[v]), key=lambda v: distance[v])
        intree[u] = True
        

        for v in graph.getVertex(u).getConnections():
            if not intree[v.getId()] and graph.getVertex(u).getWeight(v) < distance[v.getId()]:
                distance[v.getId()] = graph.getVertex(u).getWeight(v)
                parent[v.getId()] = u
    

    mst = Graph()
    for v in graph.getVertices():
        if parent[v] is not None:
            mst.addEdge(parent[v], v, distance[v])
    
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
    mst = primMST(graph)
    printGraph(mst)
