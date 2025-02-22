class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def exploreisland(row,col):

            q = deque([(row,col)])
            grid[row][col] = 0

            while q:
                row,col = q.popleft()

                for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                    trow = row+i
                    tcol =col+j
                    if 0<=trow<m and 0<=tcol<n and grid[trow][tcol]=='1':
                        q.append((trow,tcol))
                        grid[trow][tcol]=0
                
        island =0
        for i,row in enumerate(grid):
            for j, col in enumerate(row):
                if col == '1':
                    exploreisland(i,j)
                    island+=1
        
        return island
        