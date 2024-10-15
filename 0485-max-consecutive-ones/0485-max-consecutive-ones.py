class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        p1=0
        final = 0
        res = 0
        for p2 in range(len(nums)):
            if(nums[p2]==1):
                res+=1
            else:
                final = max(res, final)
                res =0
        final = max(res, final)
        return final 
