class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):

                if row ==m-1 and col == n-1:
                    continue

                right = grid[row][col+1]  if col+1<n else float('inf')
                down = grid[row+1][col]  if row+1<m else float('inf')

                grid[row][col] = grid[row][col] + min(right,down)
        
        return grid[0][0]
        