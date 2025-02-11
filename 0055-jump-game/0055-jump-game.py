class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums)-1
        

        for n in range(len(nums)-1,-1,-1):
            if nums[n] + n >= goal:
                goal = n
        
        return True if goal == 0 else False