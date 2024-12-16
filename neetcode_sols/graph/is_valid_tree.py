# also a good sol for detecting cycles in an undirected graph
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = {} #build hash set rep graph
        for node in range(n):
            adj[node] = set()
        for edge in edges:
            start = edge[0]
            end = edge[1]
            adj[start].add(end)
            adj[end].add(start)

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for child in adj[node]:
                if child == parent: # edge case for bi-directional edges in undirected graph
                    continue
                if not dfs(child, node):
                    return False # loop detected
            return True
        
        noCycles = dfs(0, -1)
        for node in list(adj.keys()):
            if node not in visited: # graph is disconnected
                return False
        return noCycles