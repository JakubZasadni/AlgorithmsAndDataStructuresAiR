import cv2
import numpy as np
from heapq import heappush, heappop
import matplotlib.pyplot as plt

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
    
    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, key):
        return self.vertList.get(key)
    
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

def primMST(graph):
    startVertex = next(iter(graph.getVertices()))
    minHeap = [(0, startVertex, None)]
    inMST = set()
    mst = Graph()
    maxEdge = (None, None, -1)

    while minHeap:
        weight, currentVert, prevVert = heappop(minHeap)
        if currentVert in inMST:
            continue
        inMST.add(currentVert)

        if prevVert is not None:
            mst.addEdge(prevVert, currentVert, weight)
            if weight > maxEdge[2]:
                maxEdge = (prevVert, currentVert, weight)

        for neighbor in graph.getVertex(currentVert).getConnections():
            if neighbor.getId() not in inMST:
                heappush(minHeap, (graph.getVertex(currentVert).getWeight(neighbor), neighbor.getId(), currentVert))

    mst.removeEdge(maxEdge[0], maxEdge[1])
    return mst, maxEdge

def removeEdge(self, fromVert, toVert):
    if fromVert in self.vertList and toVert in self.vertList:
        if toVert in self.vertList[fromVert].connectedTo:
            del self.vertList[fromVert].connectedTo[toVert]
        if fromVert in self.vertList[toVert].connectedTo:
            del self.vertList[toVert].connectedTo[fromVert]

Graph.removeEdge = removeEdge

def traverseAndColor(graph, startVert, color, img, XX):
    stack = [startVert]
    visited = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        y = current // XX
        x = current % XX
        img[y, x] = color
        for neighbor in graph.getVertex(current).getConnections():
            if (neighbor.getId() not in visited) and (img[neighbor.getId() // XX, neighbor.getId() % XX] == 0):
                stack.append(neighbor.getId())

if __name__ == "__main__":

    image_path = 'sample.png'
    I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if I is None:
        print(f"Nie można wczytać obrazu: {image_path}")
        exit(1)
    
    YY, XX = I.shape
    

    plt.imshow(I, cmap='gray')
    plt.title("Oryginalny obraz")
    plt.show()
    
    graph = Graph()
    
    for y in range(YY):
        for x in range(XX):
            currentVert = XX * y + x
            if x < XX - 1:
                rightVert = XX * y + (x + 1)
                graph.addEdge(currentVert, rightVert, abs(int(I[y, x]) - int(I[y, x + 1])))
            if y < YY - 1:
                downVert = XX * (y + 1) + x
                graph.addEdge(currentVert, downVert, abs(int(I[y, x]) - int(I[y + 1, x])))
            if x < XX - 1 and y < YY - 1:
                downRightVert = XX * (y + 1) + (x + 1)
                graph.addEdge(currentVert, downRightVert, abs(int(I[y, x]) - int(I[y + 1, x + 1])))
            if x > 0 and y < YY - 1:
                downLeftVert = XX * (y + 1) + (x - 1)
                graph.addEdge(currentVert, downLeftVert, abs(int(I[y, x]) - int(I[y + 1, x - 1])))
    
    mst, maxEdge = primMST(graph)
    
    IS = np.zeros((YY, XX), dtype='uint8')
    traverseAndColor(mst, maxEdge[0], 100, IS, XX)
    traverseAndColor(mst, maxEdge[1], 200, IS, XX)
    
    plt.imshow(IS, cmap='gray')
    plt.title("Wynik")
    plt.show()
