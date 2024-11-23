from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def bfs(r, c):
            Q = [(r, c)]
            area = 0
            while Q:
                row, col = Q.pop(0)
                if (row, col) not in visited:
                    area += 1
                visited.add((row, col))
                directions = [(0,1),(1,0),(-1,0), (0,-1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == 1:
                        Q.append((nr, nc))
            return area
        maxArea = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    maxArea = max(maxArea, bfs(row, col))
        return maxArea