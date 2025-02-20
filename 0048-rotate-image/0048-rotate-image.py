class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left=0
        right=len(matrix)-1

        while left<right:

            for i in range(right-left):

                top=left
                bottom = right


                topleft = matrix[top][left+i]

                matrix[top][left+i] = matrix[bottom-i][left]

                matrix[bottom-i][left] = matrix[bottom][right-i]

                matrix[bottom][right-i] = matrix[top+i][right]

                matrix[top+i][right] = topleft
            
            left+=1
            right-=1
        














        # m = len(matrix)
        # left = 0
        # right = m-1
        
        

        # while left<right:

        #     for i in range(right-left):
        #         top = left
        #         bottom = right

        #         topleft = matrix[top][left+i]


        #         matrix[top][left+i] = matrix[bottom-i][left]

        #         matrix[bottom-i][left] = matrix[bottom][right-i]

        #         matrix[bottom][right-i] = matrix[top+i][right]

        #         matrix[top+i][right] = topleft

        #     left+=1
        #     right-=1

            
        


