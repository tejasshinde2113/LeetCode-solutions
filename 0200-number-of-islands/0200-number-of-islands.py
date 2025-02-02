class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visit = [[0 for a in range(n)] for b in range(m)]

        def exploreIsland(row,col):
            q = deque([(row,col)])

            while q:
                r,c = q.popleft()

                for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                    tempr = r+i
                    tempc= c+j

                    if 0<=tempr < m and 0<= tempc < n and grid[tempr][tempc] == '1' and visit[tempr][tempc] == 0:
                        q.append((tempr,tempc))
                        visit[tempr][tempc] = 1




        cnt = 0
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col == '1' and visit[i][j] == 0:
                    visit[i][j] = 1
                    exploreIsland(i,j)

                    cnt+=1
        
        return cnt