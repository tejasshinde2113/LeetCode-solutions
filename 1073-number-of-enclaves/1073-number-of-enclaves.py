class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m= len(grid)
        n = len(grid[0])
        visit = [[0 for a in range(n)] for b in range(m)]


        def bfs(row,col):
            inside = True
            

            q = deque([(row,col)])
            cnt=0
            while q:
                row,col = q.popleft()
                visit[row][col]=1
                cnt+=1
                if row==0 or row==m-1 or col==0 or col==n-1:
                            inside = False

                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr = row+x
                    nc = col+y

                    if 0<=nr<m and 0<=nc<n and not visit[nr][nc] and grid[nr][nc]==1:


                        q.append((nr,nc))
                        visit[nr][nc]=1
            return cnt if inside else 0

        final = 0
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col ==1 and not visit[i][j]:
                    final +=bfs(i,j)
                
        return final 


                
