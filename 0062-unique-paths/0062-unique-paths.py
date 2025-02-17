class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if col == n-1 or row==m-1:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row][col+1]+grid[row+1][col]
        
        return grid[0][0]
                