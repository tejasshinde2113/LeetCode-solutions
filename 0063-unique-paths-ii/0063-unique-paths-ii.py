class Solution:
    def uniquePathsWithObstacles(self, ob: List[List[int]]) -> int:
        
        m=len(ob)
        n = len(ob[0])

        if ob[m-1][n-1]==1:
            return 0
        
        grid =[[0 for i in range(n) ] for j in range(m)]
        grid[m-1][n-1]=1
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if ob[row][col] ==1:
                    grid[row][col]=0
                elif row == m-1 and col == n-1:
                    continue  
                else:
                    down = grid[row+1][col] if row+1 < m else 0
                    right = grid[row][col+1] if col+1 < n else 0
                    grid[row][col] = down + right
        return grid[0][0]