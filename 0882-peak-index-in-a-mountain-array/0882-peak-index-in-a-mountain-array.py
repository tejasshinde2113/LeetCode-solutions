class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        start =0
        end = len(nums)-1
        N = len(nums)

        while start<=end:
            mid = start + (end - start)//2
            if(nums[(mid+N-1)%N]< nums[mid] and nums[mid]> nums[(mid+1)%N]):
                return mid
            if(nums[(mid+N-1)%N]< nums[mid] ):
                start=mid+1
            else:
                end = mid -1
        return 1