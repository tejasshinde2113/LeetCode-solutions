class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)+1
        nums = set(nums)
        
        for i in range(1,l):
            
            if i in nums:
                nums.remove(i)
            else:
                nums.add(i)
        return list(nums)