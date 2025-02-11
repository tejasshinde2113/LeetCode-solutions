class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        start =0
        end = len(nums)-1
        close = -1
        while start<=end:
            mid = start + (end-start)//2

            if nums[mid]== target:
                return mid
            
            if nums[mid] > target:
                close = mid
                end = mid-1
            else:
                start = mid+1
        return close if close != -1 else len(nums)