from typing import List
class UnionFind: # so useful
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
                
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        T = UnionFind(len(edges) + 1)
        for u, v in edges:
            if T.find(u) != T.find(v):
                T.union(u, v)
            else:
                return [u, v]
        return []
                