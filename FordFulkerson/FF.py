class Edge:
    def __init__(self, from_node, to_node, capacity, is_residual=False):
        self.from_node = from_node
        self.to_node = to_node
        self.capacity = capacity
        self.flow = 0
        self.is_residual = is_residual
        self.residual = capacity if not is_residual else 0

    def __repr__(self):
        return f"{self.from_node}->{self.to_node} cap: {self.capacity} flow: {self.flow} res: {self.residual} res_type: {self.is_residual}"

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, from_node, to_node, capacity):
        if from_node not in self.adj_list:
            self.adj_list[from_node] = []
        if to_node not in self.adj_list:
            self.adj_list[to_node] = []
        
        real_edge = Edge(from_node, to_node, capacity)
        residual_edge = Edge(to_node, from_node, 0, is_residual=True)
        
        self.adj_list[from_node].append(real_edge)
        self.adj_list[to_node].append(residual_edge)

    def print_graph(self):
        for node, edges in self.adj_list.items():
            print(f"{node}:")
            for edge in edges:
                print(f"    {edge}")

def bfs(graph, source, sink):
    queue = [source]
    visited = {source}
    parent = {source: None}
    
    while queue:
        current = queue.pop(0)
        
        for edge in graph.adj_list[current]:
            if edge.to_node not in visited and edge.residual > 0:
                visited.add(edge.to_node)
                parent[edge.to_node] = (current, edge)
                if edge.to_node == sink:
                    return parent
                queue.append(edge.to_node)
    return None

def augment_flow(graph, path, source, sink):
    min_capacity = float('Inf')
    node = sink
    
    while node != source:
        parent, edge = path[node]
        min_capacity = min(min_capacity, edge.residual)
        node = parent
    
    node = sink
    while node != source:
        parent, edge = path[node]
        edge.residual -= min_capacity
        edge.flow += min_capacity
        
        for rev_edge in graph.adj_list[edge.to_node]:
            if rev_edge.to_node == edge.from_node and rev_edge.is_residual:
                rev_edge.residual += min_capacity
        
        node = parent
    
    return min_capacity

def edmonds_karp(graph, source, sink):
    max_flow = 0
    path = bfs(graph, source, sink)
    
    while path:
        flow = augment_flow(graph, path, source, sink)
        max_flow += flow
        path = bfs(graph, source, sink)
    
    return max_flow

def main():
    graphs = [
        ('graph_0', [('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]),
        ('graph_1', [('s', 'a', 16), ('s', 'c', 13), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]),
        ('graph_2', [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)])
    ]

    for name, edges in graphs:
        graph = Graph()
        for from_node, to_node, capacity in edges:
            graph.add_edge(from_node, to_node, capacity)
        
        max_flow = edmonds_karp(graph, 's', 't')
        print(f"{name} - found max flow: {max_flow}")
        graph.print_graph()

if __name__ == "__main__":
    main()
