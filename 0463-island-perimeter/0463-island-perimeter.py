class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visit = [[0 for i in range(n)] for b in range(m)]
        coor= None
        for i,row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    coor = (i,j)
                    break
        
        if not coor:
            return 0

        final =0
        
        q = deque([coor])
        visit[coor[0]][coor[1]]=1
        while q:
            row,col = q.popleft()
            cnt=0
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                tr = row+i
                tc = col+j

                if 0<=tr<m and 0<=tc<n and grid[tr][tc]==1 and visit[tr][tc]==0 :
                    
                    q.append((tr,tc))
                    visit[tr][tc]=1
                if 0<=tr<m and 0<=tc<n and grid[tr][tc]==1:
                    cnt+=1
            final +=(4-cnt)
        
        return final



        