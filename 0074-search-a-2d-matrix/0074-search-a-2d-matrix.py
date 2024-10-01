class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r1 =len(matrix) - 1
        c1=0
        while r1>=0 and c1< len(matrix[0]):

            if( matrix[r1][c1] == target ):
                return True
            if(matrix[r1][c1] > target):
                r1=r1-1
                c1=0
            else:
                c1=c1+1
        return False
        