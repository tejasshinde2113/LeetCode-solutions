class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        res =[[0 for i in range(n)] for _ in range(n)]
        

        left =0
        right = n
        top=0
        bottom =n
        cnt=1

        while left <right and top<bottom:

            for i in range(left,right):
                res[top][i] = cnt
                cnt+=1
            top+=1

            for i in range(top,bottom):
                print(top,right-1)
                # print(res)
                res[i][right-1] = cnt
                cnt+=1
            right-=1

            if not(left<right and top<bottom):
                break

            for i in range(right-1,left-1,-1):
                res[bottom-1][i] = cnt
                cnt+=1
            bottom-=1

            for i in range(bottom-1,top-1,-1):
                res[i][left] = cnt
                cnt+=1
            left+=1
        return res