class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s =set(nums)
        res=0
        for a in nums:
            n=a
            if n-1 not in s:
                t=0
                
                while n in s:
                    t+=1
                    n+=1
                res = max(res,t)
        return res
        