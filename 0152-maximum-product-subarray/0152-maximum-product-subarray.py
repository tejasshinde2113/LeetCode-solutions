class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax,currmin =1,1
        res =max(nums)
        for n in nums:
            if n==0:
                currmax,currmin = 1,1
            
            temp = currmax
            currmax = max(currmax*n,currmin*n,n)
            currmin = min(currmin*n,temp*n,n)

            res = max(res,currmax)
        return res
        