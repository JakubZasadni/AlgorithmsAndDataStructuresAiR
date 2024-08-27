import polska
class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return str(self.key)

class GraphList:
    def __init__(self):
        self.adjacency_list = {}

    def is_empty(self):
        return len(self.adjacency_list) == 0
    
    def insert_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=1):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1][vertex2] = edge
            self.adjacency_list[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for v, edges in self.adjacency_list.items():
                if vertex in edges:
                    del edges[vertex]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            del self.adjacency_list[vertex1][vertex2]
            del self.adjacency_list[vertex2][vertex1]

    def neighbours(self, vertex):
        if vertex in self.adjacency_list:
            return list(self.adjacency_list[vertex].items())  

    def vertices(self):
        return list(self.adjacency_list.keys())  

    def get_vertex(self, vertex):
        if vertex in self.adjacency_list:
            return vertex

class Graph:
    def __init__(self):
        self.adjacency_matrix = []
        self.vertex_list = []

    def is_empty(self):
        return len(self.vertex_list) == 0
    
    def insert_vertex(self, vertex):
        if vertex not in self.vertex_list:
            self.vertex_list.append(vertex)
            size = len(self.adjacency_matrix)
            for i in range(size):
                self.adjacency_matrix[i].append(0)
            self.adjacency_matrix.append([0] * (size + 1))

    def insert_edge(self, vertex1, vertex2):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            index1 = self.vertex_list.index(vertex1)
            index2 = self.vertex_list.index(vertex2)
            self.adjacency_matrix[index1][index2] = 1
            self.adjacency_matrix[index2][index1] = 1

    def delete_vertex(self, vertex):
        if vertex in self.vertex_list:
            index = self.vertex_list.index(vertex)
            self.vertex_list.remove(vertex)
            del self.adjacency_matrix[index]
            for row in self.adjacency_matrix:
                del row[index]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.vertex_list and vertex2 in self.vertex_list:
            index1 = self.vertex_list.index(vertex1)
            index2 = self.vertex_list.index(vertex2)
            self.adjacency_matrix[index1][index2] = 0
            self.adjacency_matrix[index2][index1] = 0

    def neighbours(self, vertex_id):
        if 0 <= vertex_id < len(self.vertex_list):
            neighbours = []
            for j in range(len(self.adjacency_matrix[vertex_id])):
                if self.adjacency_matrix[vertex_id][j] != 0:
                    neighbours.append((self.vertex_list[j], self.adjacency_matrix[vertex_id][j]))
            return iter(neighbours)

    def vertices(self):
        return self.vertex_list

    def get_vertex(self, vertex_id):
        if 0 <= vertex_id < len(self.vertex_list):
            return self.vertex_list[vertex_id]

def build_graph_from_edges(graph_class, edges):
    graph = graph_class()
    for edge in edges:
        vertex1 = Vertex(edge[0])
        vertex2 = Vertex(edge[1])

        graph.insert_vertex(vertex1)
        graph.insert_vertex(vertex2)
        graph.insert_edge(vertex1, vertex2)

    return graph

def remove_vertex_and_edge(graph, vertex_to_remove, edge_to_remove):
    graph.delete_vertex(vertex_to_remove)
    graph.delete_edge(*edge_to_remove)

def color_graph(graph, method):
    if method == "DFS":
        traversal_order = graph.vertices() 
    elif method == "BFS":
        traversal_order = [graph.vertices()[0]] 

    colors = {} 
    max_color = 0  

    for vertex in traversal_order:
        neighbors_colors = {colors[neighbor]: True for neighbor, _ in graph.neighbours(vertex) if neighbor in colors}

        color = 0
        while color in neighbors_colors:
            color += 1

        colors[vertex] = color
        max_color = max(max_color, color)

    colored_map = [(str(vertex), colors[vertex]) for vertex in colors]

    polska.draw_map(graph, colored_map)

    return max_color + 1  


def main():
    adjacency_list_graph = build_graph_from_edges(GraphList, polska.graf)
    adjacency_matrix_graph = build_graph_from_edges(Graph, polska.graf)

    print("DFS:")
    max_colors_dfs_list = color_graph(adjacency_list_graph, "DFS")
    max_colors_dfs_matrix = color_graph(adjacency_matrix_graph, "DFS")
    print(f"Max colors (DFS) - List: {max_colors_dfs_list}, Matrix: {max_colors_dfs_matrix}")

    print("\nBFS:")
    max_colors_bfs_list = color_graph(adjacency_list_graph, "BFS")
    max_colors_bfs_matrix = color_graph(adjacency_matrix_graph, "BFS")
    print(f"Max colors (BFS) - List: {max_colors_bfs_list}, Matrix: {max_colors_bfs_matrix}")


if __name__ == "__main__":
    main()
