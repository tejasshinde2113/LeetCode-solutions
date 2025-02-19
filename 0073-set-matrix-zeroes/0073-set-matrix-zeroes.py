class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n= len(matrix[0])
        baseCol = False
        for i in range(len(matrix)):
            for j in range(n):
                
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    
                    if j==0:
                        baseCol = True
                    else:
                        matrix[0][j]=0
        
        for i in range(1,len(matrix)):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] ==0:
                    matrix[i][j]=0


        for i in range(0,n):
            if matrix[0][0]==0:
                matrix[0][i]=0
        
        for i in range(0,m):
            if baseCol:
                matrix[i][0]=0

