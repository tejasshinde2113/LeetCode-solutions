class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        curr=0
        res =0
        for n in nums:
            if n==0:
                curr=0
            curr+=n
            res = max(curr,res)
        
        return res
        