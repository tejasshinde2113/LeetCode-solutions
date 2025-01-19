class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        m = len(isWater)
        n = len(isWater[0])
        visit= [[0 for a in range(n)] for b in range(m)]

        q=deque()
        for i,row in enumerate(isWater):
            for j, col in enumerate(row):
                if col == 1:
                    q.append((i,j))
                    isWater[i][j] =0
                    visit[i][j]=1
                


        while q:
            row,col = q.popleft()
            visit[row][col]=1

            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr = row+x
                nc = col+y
                if 0<=nr<m and 0<=nc<n and visit[nr][nc]==0:
                    visit[nr][nc]=1
                    q.append((nr,nc))
                    isWater[nr][nc] = isWater[row][col]+1
            
        return isWater


