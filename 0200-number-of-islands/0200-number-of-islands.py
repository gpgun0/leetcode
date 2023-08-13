class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        result = 0

        def dfs(x, y):
            grid[x][y] = "0"

            for dx, dy in move:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n \
                    and grid[nx][ny] == "1":
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1
        
        return result