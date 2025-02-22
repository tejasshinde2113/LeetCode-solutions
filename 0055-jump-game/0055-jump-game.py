class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums)-1

        ind = len(nums)-1
        for num in (nums[::-1]):
            if num+ind >=goal:
                goal=ind
            ind-=1
        
        return goal==0
        