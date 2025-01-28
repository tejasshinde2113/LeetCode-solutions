class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])
        visit = [[0 for a in range(n)] for b in range(m)]


        def bfs(i,j):
            visit[i][j]=1
            fish = 0
            q = deque([(i,j)])

            while q:
                
                row,col = q.popleft()
                fish += grid[row][col]
                visit[row][col]=1

                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    trow = row+x
                    tcol = col+y

                    if 0<=trow<m and 0<=tcol<n and visit[trow][tcol] ==0 and grid[trow][tcol] != 0:
                        q.append((trow,tcol))
                        visit[trow][tcol]=1

            return fish

        for i,row in enumerate(grid):
            for j, col in enumerate(row):
                if  col !=0 and visit[i][j] ==0:
                    res = max(res,bfs(i,j))
        
        return res