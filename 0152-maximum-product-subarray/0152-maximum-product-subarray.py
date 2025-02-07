class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin,currmax=1,1

        res = max( nums)

        for n in nums:

            if n==0:
                currmin,currmax=1,1
                continue
            
            temp = currmax
            currmax = max(currmax*n,currmin*n,n)
            currmin = min(temp*n,currmin*n,n)

            res = max(res,currmax)
        return res

        