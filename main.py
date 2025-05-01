import heapq
from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """

    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    edge_count = {node: float('inf') for node in graph}
    edge_count[source] = 0
    pq = [(0, 0, source)]
    while pq:
        current_dist, current_edges, current_node = heapq.heappop(pq)


        if current_dist > dist[current_node]:
            continue


        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            new_edges = current_edges + 1


            if new_dist < dist[neighbor] or (new_dist == dist[neighbor] and new_edges < edge_count[neighbor]):
                dist[neighbor] = new_dist
                edge_count[neighbor] = new_edges
                heapq.heappush(pq, (new_dist, new_edges, neighbor))


    result = {node: (dist[node], edge_count[node]) for node in graph}

    return result







    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parent = {source: None}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    return parent


def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    current_node = destination
    while current_node is not None:
        path.append(current_node)
        current_node = parents.get(current_node)
    if not path or path[-1] != next((node for node, parent in parents.items() if parent is None), None):
        return []
    result = ""
    for item in  path[::-1]:
        result +=item
    result = result[:-1]
    return result





graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)},
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
