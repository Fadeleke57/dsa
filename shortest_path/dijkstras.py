import heapq
from collections import defaultdict

infinity = float("inf")

def make_graph():
    # identical graph as the YouTube video: https://youtu.be/_lHSawdgXpI
    # tuple = (cost, to_node)
    return {
        'A': [(4, 'B'), (2, 'C')],
        'B': [(3, 'C'), (3, 'E'), (2, 'D')],
        'C': [(1, 'B'), (4, 'D'), (5, 'E')],
        'D': [],
        'E': [(1, 'D')],
    }

def dijkstras(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance < distances[current_node]:
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

    return distances

def dijkstras(graph, start):
    # Initialize distances with infinity and set the start node distance to 0.
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Priority queue of (distance, node)
    q = [(0, start)]
    
    while q:
        current_distance, node = heapq.heappop(q)
        
        # If the current distance is not up-to-date, skip processing.
        if current_distance > distances[node]:
            continue
        
        for neighbor, weight in graph[node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(q, (new_distance, neighbor))
                
    return distances

# Example usage
graph = defaultdict(dict)
graph['A']['B'] = 3
graph['A']['C'] = 1
graph['B']['C'] = 7
graph['C']['B'] = 2
graph['C']['D'] = 6
graph['D']['B'] = 2
distances = dijkstra(graph, 'A')
print(distances)


def main():
    G = make_graph()
    start = 'A'
    shortest_paths = dijkstras(G, start)
    print(f'Shortest path from {start}: {shortest_paths}')

main()
