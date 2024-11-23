from collections import defaultdict
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        #if we do a dfs om each node until the connected component is consumed then repeat until every node is consumed then we get the number of connected components
        #maybe build an adj list first then do a dfs/bfs on that
        adj = {} #represents graph
        for node in range(n):
            adj[node] = set()
        for edge in edges:
            start, end = edge[0], edge[1]
            adj[start].add(end)
            adj[end].add(start)
        
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        res = 0
        #for each node in the graph, run a dfs, and making sure to keep track of visited nodes. If that new node isn't in the visited set, it means it's part of a new connected component
        for node in list(adj.keys()):
            if node not in visited:
                res += 1
                dfs(node)
        return res