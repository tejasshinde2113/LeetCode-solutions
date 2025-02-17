class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        p1=0
        res = float('inf')
        curr =0
        for p2 in range(len(nums)):
            curr+=nums[p2]
            
            while curr>target:
                if curr>=target:
                    res = min(res,p2-p1+1)
                curr-=nums[p1]
                p1+=1
                
            

            if curr==target:
                res = min(res,p2-p1+1)
            
        
        
        return res if res != float('inf') else 0
                