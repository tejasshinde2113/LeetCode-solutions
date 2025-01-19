class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        q=deque()
        oneCnt =0


        visit = [[0 for a in range(n)] for b in range(m) ]

        
        def bfs(q):
            nonlocal oneCnt
            cnt =0
        

            while q and oneCnt>0:
                cnt+=1
                for a in range(len(q)):
                    row,col = q.popleft()

                    visit[row][col]=1

                    for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                        tempr = row+x
                        tempc = col+y
                        if   0<=tempr<m and 0<=tempc<n and not visit[tempr][tempc] and grid[tempr][tempc] ==1:
                            visit[tempr][tempc]=1
                            grid[tempr][tempc] =2
                            oneCnt -=1
                            q.append((tempr,tempc))
                
            return cnt



        for i, row in enumerate(grid):
            for j,col in enumerate(row):
                if col == 2 :
                    q.append((i,j))
                elif col ==1:
                    oneCnt+=1
        
        
        maxall=bfs(q)
        
        if oneCnt>0:
            return -1
        return maxall if maxall >-1 else 0 

        

        # m = len(grid)
        # n = len(grid[0])
        # maxall = 0


        # visit = [[0 for a in range(n)] for b in range(m) ]

        
        # cnt= [0]
        # def dfs(r,c,itera):


        #     nonlocal maxall
        #     maxall = max(maxall, itera)
        #     visit[r][c]=1

        #     for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
        #         tempr = r+x
        #         tempc = c+y
        #         if   0<=tempr<m and 0<=tempc<n and not visit[tempr][tempc] and grid[tempr][tempc] ==1:
        #             visit[tempr][tempc]=1
        #             grid[tempr][tempc] =2
                    
                    
        #             dfs(tempr,tempc,itera+1)
                    
                    
        # for i, row in enumerate(grid):
        #     for j,col in enumerate(row):
        #         if col == 2 and not visit[i][j]:
        #             dfs(i,j,0)
        

        

        # for i,row in enumerate(visit):
        #     for j,col in enumerate(row):
        #         if grid[i][j] ==1:
        #             return -1

        # return maxall
        

        