class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if grid[r][c] == 1 or (r, c) in visited:
                return True
            visited.add((r, c))
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            return up and down and left and right

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if dfs(i, j):
                        count += 1

        return count