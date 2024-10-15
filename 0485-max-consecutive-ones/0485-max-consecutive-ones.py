class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        p1=0
        final = 0
        for p2 in range(len(nums)):
            if(nums[p2]!=1):
                final = max(p2-p1, final)
                p1=p2+1
              
        final = max(p2-p1+1, final)
        return final 
