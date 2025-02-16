class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ones =0

        q=deque([])

        visit = [[0 for i in range(n)] for j in range(m)]

        for i,row in enumerate(grid):
            for j,col in enumerate(row):

                if col ==2:
                    visit[i][j]=1
                    q.append((i,j))
                elif col ==1:
                    ones+=1
        

        cnt=0
        while q and ones:
            for _ in range(len(q)):
                row,col = q.popleft()

                visit[row][col]=1


                for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:


                    tr = row+x
                    tc = col+y
                
                    if 0<=tr<m and 0<=tc<n and visit[tr][tc]==0 and grid[tr][tc]==1:
                        ones-=1
                        grid[tr][tc]=2
                        visit[tr][tc]=1
                        q.append((tr,tc))
            cnt+=1

        return cnt if not ones else -1