class Solution:
    def countElements(self, nums: List[int]) -> int:

        nums.sort()
        
        if(len(nums)<3):
            return 0
        while( len(nums)>1 and nums[0]==nums[1]):
            del nums[0]
        while( len(nums)>1 and nums[-1]==nums[-2]):
            del nums[-1]
        if(len(nums)<3):
            return 0
        
        return len(nums)-2
        