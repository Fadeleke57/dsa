from collections import deque

def bfs(adj, start):
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                q.append(neighbor)
    return visited


visited = set()
def dfs(node):
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    

