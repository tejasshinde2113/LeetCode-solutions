class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start =0
        end = len(nums)-1
        N = len(nums)

        if N == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[N - 1] > nums[N - 2]:
            return N - 1

        while start<=end:
            mid = start + (end - start)//2
            if(nums[(mid+N-1)%N]< nums[mid] and nums[mid]> nums[(mid+1)%N]):
                return mid
            if(nums[(mid+N-1)%N]< nums[mid] ):
                start=mid+1
            else:
                end = mid -1
        return 0 if len(nums)==1 else 1