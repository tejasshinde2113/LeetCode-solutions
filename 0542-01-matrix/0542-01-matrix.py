class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        visit =[[0 for _ in range(n)] for _ in range(m)]


        def dist(q):

            
            while q:
                for a in range(len(q)):
                    row,col = q.popleft()
                    

                    for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:

                        newr= row +x
                        newc = col+y


                        if 0<=newr<m and 0<=newc<n:

                            if mat[newr][newc] == '*':
                                mat[newr][newc] = mat[row][col]+1
                                q.append((newr,newc))




        q=deque()
        for i,row in enumerate(mat):
            for j,col in enumerate(row):
                if col == 1:
                    mat[i][j] = '*'
                else:
                    q.append((i,j))
        dist(q)
        return mat
        